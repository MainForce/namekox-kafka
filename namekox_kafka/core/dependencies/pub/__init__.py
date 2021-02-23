#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import six


from namekox_kafka.constants import KAFKA_CONFIG_KEY
from namekox_kafka.core.producer import KafkaProducer
from namekox_core.core.service.dependency import Dependency


class KafkaPubProxy(Dependency):
    def __init__(self, dbname, **configs):
        self.dbname = dbname
        self.producer = None
        self.configs = configs
        super(KafkaPubProxy, self).__init__(**configs)

    def setup(self):
        config = self.container.config.get(KAFKA_CONFIG_KEY, {}).get(self.dbname, {}).copy()
        [config.update({k: v}) for k, v in six.iteritems(self.configs) if k in KafkaProducer.DEFAULT_CONFIG]
        self.configs = config
        self.producer = KafkaProducer(**self.configs)

    def stop(self):
        self.producer and self.producer.close()

    def get_instance(self, context):
        return self.producer(context)
