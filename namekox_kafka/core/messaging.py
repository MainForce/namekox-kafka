#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import six
import anyjson


from namekox_kafka.constants import DEFAULT_KAFKA_H_PREFIX


def gen_message_headers(context):
    headers = {}
    for k, v in six.iteritems(context):
        k = '{}-'.format(DEFAULT_KAFKA_H_PREFIX) + k
        headers.update({k: anyjson.serialize(v)})
    return headers


def get_message_headers(message):
    headers = {}
    for k, v in message.headers:
        p = '{}-'.format(DEFAULT_KAFKA_H_PREFIX)
        if not k.lower().startswith(p):
            continue
        k = k.lower()[len(p):].replace('-', '_')
        headers.update({k: anyjson.deserialize(v)})
    return headers
