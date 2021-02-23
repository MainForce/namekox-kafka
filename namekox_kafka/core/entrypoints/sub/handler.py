#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


import six


from logging import getLogger
from kafka import KafkaConsumer
from namekox_kafka.constants import KAFKA_CONFIG_KEY
from namekox_core.core.service.entrypoint import Entrypoint
from namekox_kafka.core.messaging import get_message_headers


logger = getLogger(__name__)


class KafkaSubHandler(Entrypoint):
    def __init__(self, dbname, *topics, **configs):
        self.gt = None
        self.consumer = None
        self.topics = topics
        self.dbname = dbname
        self.configs = configs
        super(KafkaSubHandler, self).__init__(**configs)

    def setup(self):
        config = self.container.config.get(KAFKA_CONFIG_KEY, {}).get(self.dbname, {}).copy()
        [config.update({k: v}) for k, v in six.iteritems(self.configs) if k in KafkaConsumer.DEFAULT_CONFIG]
        self.configs = config
        self.consumer = KafkaConsumer(*self.topics, **self.configs)

    def start(self):
        self.gt = self.container.spawn_manage_thread(self._run)

    def stop(self):
        self.consumer and self.consumer.close()
        self.gt.kill()

    def _run(self):
        for m in self.consumer:
            msg = '{} receive {}'.format(self.obj_name, m)
            logger.debug(msg)
            args, kwargs = (m.value,), {}
            ctx_data = get_message_headers(m)
            self.container.spawn_worker_thread(self, args, kwargs, ctx_data=ctx_data)
