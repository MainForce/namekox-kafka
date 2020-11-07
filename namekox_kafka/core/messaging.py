#! -*- coding: utf-8 -*-

# author: forcemain@163.com


import six


from namekox_kafka.constants import DEFAULT_KAFKA_H_PREFIX


def gen_message_headers(context):
    headers = {}
    for k, v in six.iteritems(context):
        k = '{}-'.format(DEFAULT_KAFKA_H_PREFIX) + k
        headers.update({k: v})
    return headers


def get_message_headers(message):
    headers = {}
    for k, v in message.headers:
        p = '{}-'.format(DEFAULT_KAFKA_H_PREFIX)
        k.startswith(p) and headers.update({k[len(p):]: v})
    return headers