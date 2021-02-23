#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import six


from kafka import KafkaProducer
from namekox_kafka.constants import KAFKA_CONFIG_KEY
from namekox_core.core.friendly import AsLazyProperty


class KafkaPubProxy(object):
    def __init__(self, config, **options):
        self.config = config
        self.options = options

    @AsLazyProperty
    def configs(self):
        return self.config.get(KAFKA_CONFIG_KEY, {})

    def __call__(self, dbname, **options):
        self.options.update(options)
        config = self.configs.get(dbname, {}).copy()
        [config.update({k: v}) for k, v in six.iteritems(self.options) if k in KafkaProducer.DEFAULT_CONFIG]
        self.options = config
        return KafkaProducer(**self.options)
