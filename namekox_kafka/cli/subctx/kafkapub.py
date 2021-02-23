#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


from namekox_kafka.core.proxy import KafkaPubProxy


class KafkaPub(object):
    def __init__(self, config):
        self.config = config
        self.proxy = KafkaPubProxy(config)

    @classmethod
    def name(cls):
        return 'kafkapub'
