#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


import six


from kafka import KafkaProducer as BaseKafkaProducer
from namekox_kafka.core.messaging import gen_message_headers


class KafkaProducer(BaseKafkaProducer):
    def __init__(self, **configs):
        self.context = None
        super(KafkaProducer, self).__init__(**configs)

    def send(self, topic, value=None, key=None, headers=None, partition=None, timestamp_ms=None):
        headers = headers or []
        _header = gen_message_headers(self.context.data) if self.context else {}
        headers.extend([(k, v) for k, v in six.iteritems(_header) if (k, v) not in headers])
        return super(KafkaProducer, self).send(topic, value=value, key=key, headers=headers, partition=partition, timestamp_ms=timestamp_ms)

    def __call__(self, context=None):
        self.context = context
        return self
