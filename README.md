# Install
```shell script
pip install -U namekox-kafka
```

# Example
```shell script
# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


import time
import json
import random


from logging import getLogger
from namekox_kafka.core.entrypoints import kafka
from namekox_timer.core.entrypoints.timer import timer
from namekox_webserver.core.entrypoints.app import app
from namekox_kafka.core.dependencies.pub import KafkaPubProxy


logger = getLogger(__name__)


def generate_ip():
    return '.'.join([str(random.randint(1, 255)) for _ in range(4)])


class Ping(object):
    name = 'ping'

    kafka_pub = KafkaPubProxy(name, compression_type='gzip', value_serializer=json.dumps)

    @app.api('/api/producer/metrics', methods=['GET'])
    def producer_metrics(self, request):
        return self.kafka_pub.metrics()

    @kafka.sub(name, 'ping', group_id='qa-ping', value_deserializer=json.loads)
    def kafka_sub(self, message):
        print('recv ping channel data', message)

    @timer(5)
    def ip_ping(self):
        ip = generate_ip()
        mapping = {
            int(time.time() * 1000): random.choice([0, 1])
        }
        self.kafka_pub.send('ping', {ip: mapping})
```

# Running
> config.yaml
```yaml
KAFKA:
  ping:
    bootstrap_servers: "*.*.*.*:9092"
    retry_backoff_ms: 100
```
> namekox run ping
```shell script
2020-11-07 22:16:52,955 DEBUG load container class from namekox_core.core.service.container:ServiceContainer
2020-11-07 22:16:52,957 DEBUG starting services ['ping']
2020-11-07 22:16:52,957 DEBUG starting service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:producer_metrics, ping:namekox_timer.core.entrypoints.timer.Timer:ip_ping, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server, ping:namekox_kafka.core.entrypoints.sub.handler.KafkaSubHandler:kafka_sub]
2020-11-07 22:16:52,958 DEBUG Added sensor with name connections-closed
2020-11-07 22:16:52,958 DEBUG Added sensor with name connections-created
2020-11-07 22:16:52,958 DEBUG Added sensor with name select-time
2020-11-07 22:16:52,958 DEBUG Added sensor with name io-time
2020-11-07 22:16:52,959 DEBUG Initiating connection to node bootstrap-0 at *.*.*.*:9092
2020-11-07 22:16:52,959 DEBUG Added sensor with name bytes-sent-received
2020-11-07 22:16:52,959 DEBUG Added sensor with name bytes-sent
2020-11-07 22:16:52,959 DEBUG Added sensor with name bytes-received
2020-11-07 22:16:52,959 DEBUG Added sensor with name request-latency
2020-11-07 22:16:52,959 DEBUG Added sensor with name node-bootstrap-0.bytes-sent
2020-11-07 22:16:52,960 DEBUG Added sensor with name node-bootstrap-0.bytes-received
2020-11-07 22:16:52,960 DEBUG Added sensor with name node-bootstrap-0.latency
2020-11-07 22:16:52,960 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <disconnected> [IPv4 None]>: creating new socket
2020-11-07 22:16:52,960 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <disconnected> [IPv4 ('*.*.*.*', 9092)]>: setting socket option (6, 1, 1)
2020-11-07 22:16:52,961 INFO <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: connecting to *.*.*.*:9092 [('*.*.*.*', 9092) IPv4]
2020-11-07 22:16:52,961 INFO Probing node bootstrap-0 broker version
2020-11-07 22:16:52,970 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: established TCP connection
2020-11-07 22:16:52,971 INFO <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: Connection complete.
2020-11-07 22:16:52,971 DEBUG Node bootstrap-0 connected
2020-11-07 22:16:52,971 DEBUG Sending request ApiVersionRequest_v0()
2020-11-07 22:16:52,971 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 1: ApiVersionRequest_v0()
2020-11-07 22:16:53,074 DEBUG Sending request MetadataRequest_v0(topics=[])
2020-11-07 22:16:53,075 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 2: MetadataRequest_v0(topics=[])
2020-11-07 22:16:53,075 DEBUG Received correlation id: 1
2020-11-07 22:16:53,075 DEBUG Processing response ApiVersionResponse_v0
2020-11-07 22:16:53,076 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 1 (104.804992676 ms): ApiVersionResponse_v0(error_code=0, api_versions=[(api_key=0, min_version=0, max_version=7), (api_key=1, min_version=0, max_version=10), (api_key=2, min_version=0, max_version=4), (api_key=3, min_version=0, max_version=7), (api_key=4, min_version=0, max_version=1), (api_key=5, min_version=0, max_version=0), (api_key=6, min_version=0, max_version=4), (api_key=7, min_version=0, max_version=1), (api_key=8, min_version=0, max_version=6), (api_key=9, min_version=0, max_version=5), (api_key=10, min_version=0, max_version=2), (api_key=11, min_version=0, max_version=3), (api_key=12, min_version=0, max_version=2), (api_key=13, min_version=0, max_version=2), (api_key=14, min_version=0, max_version=2), (api_key=15, min_version=0, max_version=2), (api_key=16, min_version=0, max_version=2), (api_key=17, min_version=0, max_version=1), (api_key=18, min_version=0, max_version=2), (api_key=19, min_version=0, max_version=3), (api_key=20, min_version=0, max_version=3), (api_key=21, min_version=0, max_version=1), (api_key=22, min_version=0, max_version=1), (api_key=23, min_version=0, max_version=2), (api_key=24, min_version=0, max_version=1), (api_key=25, min_version=0, max_version=1), (api_key=26, min_version=0, max_version=1), (api_key=27, min_version=0, max_version=0), (api_key=28, min_version=0, max_version=2), (api_key=29, min_version=0, max_version=1), (api_key=30, min_version=0, max_version=1), (api_key=31, min_version=0, max_version=1), (api_key=32, min_version=0, max_version=2), (api_key=33, min_version=0, max_version=1), (api_key=34, min_version=0, max_version=1), (api_key=35, min_version=0, max_version=1), (api_key=36, min_version=0, max_version=0), (api_key=37, min_version=0, max_version=1), (api_key=38, min_version=0, max_version=1), (api_key=39, min_version=0, max_version=1), (api_key=40, min_version=0, max_version=1), (api_key=41, min_version=0, max_version=1), (api_key=42, min_version=0, max_version=1)])
2020-11-07 22:16:53,082 DEBUG Received correlation id: 2
2020-11-07 22:16:53,083 DEBUG Processing response MetadataResponse_v0
2020-11-07 22:16:53,084 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 2 (8.957862854 ms): MetadataResponse_v0(brokers=[(node_id=1, host=u'*.*.*.*', port=9092)], topics=[(error_code=0, topic=u'dns', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'cloudprint', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'wifiscreen', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_info', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'safe', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'__consumer_offsets', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=10, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=20, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=40, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=30, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=9, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=11, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=31, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=39, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=13, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=18, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=22, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=8, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=32, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=43, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=29, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=34, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=6, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=41, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=27, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=48, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=5, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=15, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=35, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=25, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=46, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=26, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=36, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=44, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=16, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=37, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=17, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=45, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=3, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=24, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=38, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=33, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=23, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=28, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=12, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=19, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=14, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=4, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=47, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=49, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=42, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=7, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=21, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient_info', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'share', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ping', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'menjin', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'webmeeting', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient-info', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'kms', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'telephone', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ad', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_action', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'canonprint', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'device-__assignor-__leader', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'bj_sxflog', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])])])
2020-11-07 22:16:53,087 INFO Broker version identified as 2.1.0
2020-11-07 22:16:53,087 INFO Set configuration api_version=(2, 1, 0) to skip auto check_version requests on startup
2020-11-07 22:16:53,087 DEBUG Added sensor with name bytes-fetched
2020-11-07 22:16:53,088 DEBUG Added sensor with name records-fetched
2020-11-07 22:16:53,088 DEBUG Added sensor with name fetch-latency
2020-11-07 22:16:53,088 DEBUG Added sensor with name records-lag
2020-11-07 22:16:53,088 DEBUG Added sensor with name fetch-throttle-time
2020-11-07 22:16:53,088 DEBUG Added sensor with name heartbeat-latency
2020-11-07 22:16:53,088 DEBUG Added sensor with name join-latency
2020-11-07 22:16:53,089 DEBUG Added sensor with name sync-latency
2020-11-07 22:16:53,089 DEBUG Added sensor with name commit-latency
2020-11-07 22:16:53,089 INFO Updating subscribed topics to: ('ping',)
2020-11-07 22:16:53,089 DEBUG spawn manage thread handle ping:namekox_timer.core.entrypoints.timer:_run(args=(), kwargs={}, tid=_run)
2020-11-07 22:16:53,091 DEBUG spawn manage thread handle ping:namekox_webserver.core.entrypoints.app.server:handle_connect(args=(), kwargs={}, tid=handle_connect)
2020-11-07 22:16:53,091 DEBUG spawn manage thread handle ping:namekox_kafka.core.entrypoints.sub.handler:_run(args=(), kwargs={}, tid=_run)
2020-11-07 22:16:53,091 DEBUG Sending group coordinator request for group qa-ping to broker bootstrap-0
2020-11-07 22:16:53,091 DEBUG Sending request GroupCoordinatorRequest_v0(consumer_group='qa-ping')
2020-11-07 22:16:53,091 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 3: GroupCoordinatorRequest_v0(consumer_group='qa-ping')
2020-11-07 22:16:53,092 DEBUG Sending metadata request MetadataRequest_v1(topics=['ping']) to node bootstrap-0
2020-11-07 22:16:53,092 DEBUG Sending request MetadataRequest_v1(topics=['ping'])
2020-11-07 22:16:53,092 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 4: MetadataRequest_v1(topics=['ping'])
2020-11-07 22:16:53,093 DEBUG service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:producer_metrics, ping:namekox_timer.core.entrypoints.timer.Timer:ip_ping, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server, ping:namekox_kafka.core.entrypoints.sub.handler.KafkaSubHandler:kafka_sub] started
2020-11-07 22:16:53,093 DEBUG starting service ping dependencies [ping:namekox_kafka.core.dependencies.pub.KafkaPubProxy:kafka_pub]
2020-11-07 22:16:53,093 DEBUG Starting the Kafka producer
2020-11-07 22:16:53,094 DEBUG Added sensor with name connections-closed
2020-11-07 22:16:53,095 DEBUG Added sensor with name connections-created
2020-11-07 22:16:53,095 DEBUG Added sensor with name select-time
2020-11-07 22:16:53,095 DEBUG Added sensor with name io-time
2020-11-07 22:16:53,095 DEBUG Initiating connection to node bootstrap-0 at *.*.*.*:9092
2020-11-07 22:16:53,095 DEBUG Added sensor with name bytes-sent-received
2020-11-07 22:16:53,095 DEBUG Added sensor with name bytes-sent
2020-11-07 22:16:53,096 DEBUG Added sensor with name bytes-received
2020-11-07 22:16:53,096 DEBUG Added sensor with name request-latency
2020-11-07 22:16:53,096 DEBUG Added sensor with name node-bootstrap-0.bytes-sent
2020-11-07 22:16:53,096 DEBUG Added sensor with name node-bootstrap-0.bytes-received
2020-11-07 22:16:53,097 DEBUG Added sensor with name node-bootstrap-0.latency
2020-11-07 22:16:53,097 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <disconnected> [IPv4 None]>: creating new socket
2020-11-07 22:16:53,119 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <disconnected> [IPv4 ('*.*.*.*', 9092)]>: setting socket option (6, 1, 1)
2020-11-07 22:16:53,120 INFO <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: connecting to *.*.*.*:9092 [('*.*.*.*', 9092) IPv4]
2020-11-07 22:16:53,120 INFO Probing node bootstrap-0 broker version
2020-11-07 22:16:53,120 DEBUG Received correlation id: 3
2020-11-07 22:16:53,120 DEBUG Processing response GroupCoordinatorResponse_v0
2020-11-07 22:16:53,120 DEBUG Received correlation id: 4
2020-11-07 22:16:53,121 DEBUG Processing response MetadataResponse_v1
2020-11-07 22:16:53,121 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 3 (29.1249752045 ms): GroupCoordinatorResponse_v0(error_code=0, coordinator_id=1, host=u'*.*.*.*', port=9092)
2020-11-07 22:16:53,121 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 4 (28.8791656494 ms): MetadataResponse_v1(brokers=[(node_id=1, host=u'*.*.*.*', port=9092, rack=None)], controller_id=1, topics=[(error_code=0, topic=u'ping', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])])])
2020-11-07 22:16:53,121 DEBUG Received group coordinator response GroupCoordinatorResponse_v0(error_code=0, coordinator_id=1, host=u'*.*.*.*', port=9092)
2020-11-07 22:16:53,121 DEBUG Updating coordinator for qa-ping: GroupCoordinatorResponse_v0(error_code=0, coordinator_id=1, host=u'*.*.*.*', port=9092)
2020-11-07 22:16:53,121 INFO Group coordinator for qa-ping is BrokerMetadata(nodeId='coordinator-1', host=u'*.*.*.*', port=9092, rack=None)
2020-11-07 22:16:53,121 INFO Discovered coordinator coordinator-1 for group qa-ping
2020-11-07 22:16:53,122 DEBUG Updated cluster metadata to ClusterMetadata(brokers: 1, topics: 1, groups: 1)
2020-11-07 22:16:53,122 INFO Starting new heartbeat thread
2020-11-07 22:16:53,122 DEBUG Heartbeat thread started
2020-11-07 22:16:53,122 INFO Revoking previously assigned partitions set([]) for group qa-ping
2020-11-07 22:16:53,122 DEBUG Initiating connection to node coordinator-1 at *.*.*.*:9092
2020-11-07 22:16:53,123 DEBUG Added sensor with name node-coordinator-1.bytes-sent
2020-11-07 22:16:53,123 DEBUG Added sensor with name node-coordinator-1.bytes-received
2020-11-07 22:16:53,123 DEBUG Added sensor with name node-coordinator-1.latency
2020-11-07 22:16:53,123 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <disconnected> [IPv4 None]>: creating new socket
2020-11-07 22:16:53,123 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <disconnected> [IPv4 ('*.*.*.*', 9092)]>: setting socket option (6, 1, 1)
2020-11-07 22:16:53,123 INFO <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: connecting to *.*.*.*:9092 [('*.*.*.*', 9092) IPv4]
2020-11-07 22:16:53,134 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: established TCP connection
2020-11-07 22:16:53,135 INFO <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: Connection complete.
2020-11-07 22:16:53,135 DEBUG Node bootstrap-0 connected
2020-11-07 22:16:53,135 DEBUG Sending request ApiVersionRequest_v0()
2020-11-07 22:16:53,135 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 1: ApiVersionRequest_v0()
2020-11-07 22:16:53,227 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: established TCP connection
2020-11-07 22:16:53,227 INFO <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: Connection complete.
2020-11-07 22:16:53,227 DEBUG Node coordinator-1 connected
2020-11-07 22:16:53,227 INFO <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: Closing connection.
2020-11-07 22:16:53,235 DEBUG Sending request MetadataRequest_v0(topics=[])
2020-11-07 22:16:53,236 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 2: MetadataRequest_v0(topics=[])
2020-11-07 22:16:53,236 DEBUG Received correlation id: 1
2020-11-07 22:16:53,236 DEBUG Processing response ApiVersionResponse_v0
2020-11-07 22:16:53,237 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 1 (101.511001587 ms): ApiVersionResponse_v0(error_code=0, api_versions=[(api_key=0, min_version=0, max_version=7), (api_key=1, min_version=0, max_version=10), (api_key=2, min_version=0, max_version=4), (api_key=3, min_version=0, max_version=7), (api_key=4, min_version=0, max_version=1), (api_key=5, min_version=0, max_version=0), (api_key=6, min_version=0, max_version=4), (api_key=7, min_version=0, max_version=1), (api_key=8, min_version=0, max_version=6), (api_key=9, min_version=0, max_version=5), (api_key=10, min_version=0, max_version=2), (api_key=11, min_version=0, max_version=3), (api_key=12, min_version=0, max_version=2), (api_key=13, min_version=0, max_version=2), (api_key=14, min_version=0, max_version=2), (api_key=15, min_version=0, max_version=2), (api_key=16, min_version=0, max_version=2), (api_key=17, min_version=0, max_version=1), (api_key=18, min_version=0, max_version=2), (api_key=19, min_version=0, max_version=3), (api_key=20, min_version=0, max_version=3), (api_key=21, min_version=0, max_version=1), (api_key=22, min_version=0, max_version=1), (api_key=23, min_version=0, max_version=2), (api_key=24, min_version=0, max_version=1), (api_key=25, min_version=0, max_version=1), (api_key=26, min_version=0, max_version=1), (api_key=27, min_version=0, max_version=0), (api_key=28, min_version=0, max_version=2), (api_key=29, min_version=0, max_version=1), (api_key=30, min_version=0, max_version=1), (api_key=31, min_version=0, max_version=1), (api_key=32, min_version=0, max_version=2), (api_key=33, min_version=0, max_version=1), (api_key=34, min_version=0, max_version=1), (api_key=35, min_version=0, max_version=1), (api_key=36, min_version=0, max_version=0), (api_key=37, min_version=0, max_version=1), (api_key=38, min_version=0, max_version=1), (api_key=39, min_version=0, max_version=1), (api_key=40, min_version=0, max_version=1), (api_key=41, min_version=0, max_version=1), (api_key=42, min_version=0, max_version=1)])
2020-11-07 22:16:53,243 DEBUG Received correlation id: 2
2020-11-07 22:16:53,243 DEBUG Processing response MetadataResponse_v0
2020-11-07 22:16:53,245 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 2 (9.0229511261 ms): MetadataResponse_v0(brokers=[(node_id=1, host=u'*.*.*.*', port=9092)], topics=[(error_code=0, topic=u'dns', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'cloudprint', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'wifiscreen', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_info', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'safe', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'__consumer_offsets', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=10, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=20, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=40, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=30, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=9, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=11, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=31, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=39, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=13, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=18, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=22, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=8, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=32, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=43, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=29, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=34, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=6, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=41, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=27, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=48, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=5, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=15, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=35, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=25, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=46, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=26, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=36, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=44, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=16, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=37, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=17, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=45, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=3, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=24, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=38, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=33, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=23, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=28, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=12, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=19, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=14, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=4, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=47, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=49, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=42, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=7, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=21, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient_info', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'share', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ping', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'menjin', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'webmeeting', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient-info', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'kms', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'telephone', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ad', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_action', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'canonprint', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'device-__assignor-__leader', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'bj_sxflog', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])])])
2020-11-07 22:16:53,246 INFO Broker version identified as 2.1.0
2020-11-07 22:16:53,246 INFO Set configuration api_version=(2, 1, 0) to skip auto check_version requests on startup
2020-11-07 22:16:53,247 DEBUG Added sensor with name bufferpool-wait-time
2020-11-07 22:16:53,248 DEBUG Added sensor with name batch-size
2020-11-07 22:16:53,249 DEBUG Added sensor with name compression-rate
2020-11-07 22:16:53,249 DEBUG Added sensor with name queue-time
2020-11-07 22:16:53,249 DEBUG Added sensor with name produce-throttle-time
2020-11-07 22:16:53,249 DEBUG Added sensor with name records-per-request
2020-11-07 22:16:53,249 DEBUG Added sensor with name bytes
2020-11-07 22:16:53,249 DEBUG Added sensor with name record-retries
2020-11-07 22:16:53,249 DEBUG Added sensor with name errors
2020-11-07 22:16:53,250 DEBUG Added sensor with name record-size-max
2020-11-07 22:16:53,250 DEBUG Starting Kafka producer I/O thread.
2020-11-07 22:16:53,250 DEBUG Sending metadata request MetadataRequest_v1(topics=NULL) to node bootstrap-0
2020-11-07 22:16:53,250 DEBUG Sending request MetadataRequest_v1(topics=NULL)
2020-11-07 22:16:53,250 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 3: MetadataRequest_v1(topics=NULL)
2020-11-07 22:16:53,251 DEBUG Kafka producer started
2020-11-07 22:16:53,252 DEBUG service ping dependencies [ping:namekox_kafka.core.dependencies.pub.KafkaPubProxy:kafka_pub] started
2020-11-07 22:16:53,252 DEBUG services ['ping'] started
2020-11-07 22:16:53,257 DEBUG Received correlation id: 3
2020-11-07 22:16:53,257 DEBUG Processing response MetadataResponse_v1
2020-11-07 22:16:53,259 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 3 (8.15391540527 ms): MetadataResponse_v1(brokers=[(node_id=1, host=u'*.*.*.*', port=9092, rack=None)], controller_id=1, topics=[(error_code=0, topic=u'dns', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'cloudprint', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'wifiscreen', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_info', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'safe', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'__consumer_offsets', is_internal=True, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=10, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=20, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=40, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=30, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=9, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=11, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=31, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=39, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=13, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=18, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=22, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=8, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=32, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=43, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=29, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=34, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=6, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=41, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=27, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=48, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=5, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=15, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=35, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=25, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=46, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=26, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=36, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=44, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=16, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=37, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=17, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=45, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=3, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=24, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=38, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=33, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=23, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=28, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=12, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=19, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=14, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=4, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=47, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=49, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=42, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=7, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=21, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient_info', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'share', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ping', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'menjin', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'webmeeting', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient-info', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'kms', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'telephone', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ad', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_action', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'canonprint', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'device-__assignor-__leader', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'bj_sxflog', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])])])
2020-11-07 22:16:53,262 DEBUG Updated cluster metadata to ClusterMetadata(brokers: 1, topics: 20, groups: 0)
2020-11-07 22:16:53,328 INFO (Re-)joining group qa-ping
2020-11-07 22:16:53,328 DEBUG Sending JoinGroup (JoinGroupRequest_v2(group='qa-ping', session_timeout=10000, rebalance_timeout=300000, member_id='', protocol_type='consumer', group_protocols=[(protocol_name='range', protocol_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x00'), (protocol_name='roundrobin', protocol_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x00')])) to coordinator coordinator-1
2020-11-07 22:16:53,329 DEBUG Sending request JoinGroupRequest_v2(group='qa-ping', session_timeout=10000, rebalance_timeout=300000, member_id='', protocol_type='consumer', group_protocols=[(protocol_name='range', protocol_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x00'), (protocol_name='roundrobin', protocol_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x00')])
2020-11-07 22:16:53,329 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 1: JoinGroupRequest_v2(group='qa-ping', session_timeout=10000, rebalance_timeout=300000, member_id='', protocol_type='consumer', group_protocols=[(protocol_name='range', protocol_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x00'), (protocol_name='roundrobin', protocol_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x00')])
2020-11-07 22:16:53,336 DEBUG Received correlation id: 1
2020-11-07 22:16:53,336 DEBUG Processing response JoinGroupResponse_v2
2020-11-07 22:16:53,337 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 1 (7.4770450592 ms): JoinGroupResponse_v2(throttle_time_ms=0, error_code=0, generation_id=49, group_protocol=u'range', leader_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', members=[(member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', member_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x00')])
2020-11-07 22:16:53,337 DEBUG Received successful JoinGroup response for group qa-ping: JoinGroupResponse_v2(throttle_time_ms=0, error_code=0, generation_id=49, group_protocol=u'range', leader_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', members=[(member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', member_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x00')])
2020-11-07 22:16:53,337 INFO Elected group leader -- performing partition assignments using range
2020-11-07 22:16:53,338 DEBUG Performing assignment for group qa-ping using strategy range with subscriptions {u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6': ConsumerProtocolMemberMetadata(version=0, subscription=[u'ping'], user_data='')}
2020-11-07 22:16:53,338 DEBUG Finished assignment for group qa-ping: {u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6': ConsumerProtocolMemberAssignment(version=0, assignment=[(topic=u'ping', partitions=[0])], user_data='')}
2020-11-07 22:16:53,338 DEBUG Sending leader SyncGroup for group qa-ping to coordinator coordinator-1: SyncGroupRequest_v1(group='qa-ping', generation_id=49, member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', group_assignment=[(member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', member_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00')])
2020-11-07 22:16:53,338 DEBUG Sending request SyncGroupRequest_v1(group='qa-ping', generation_id=49, member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', group_assignment=[(member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', member_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00')])
2020-11-07 22:16:53,339 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 2: SyncGroupRequest_v1(group='qa-ping', generation_id=49, member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', group_assignment=[(member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', member_metadata='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00')])
2020-11-07 22:16:53,339 DEBUG Initializing connection to node 1 for metadata request
2020-11-07 22:16:53,339 DEBUG Initiating connection to node 1 at *.*.*.*:9092
2020-11-07 22:16:53,340 DEBUG Added sensor with name node-1.bytes-sent
2020-11-07 22:16:53,340 DEBUG Added sensor with name node-1.bytes-received
2020-11-07 22:16:53,340 DEBUG Added sensor with name node-1.latency
2020-11-07 22:16:53,340 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <disconnected> [IPv4 None]>: creating new socket
2020-11-07 22:16:53,341 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <disconnected> [IPv4 ('*.*.*.*', 9092)]>: setting socket option (6, 1, 1)
2020-11-07 22:16:53,341 INFO <BrokerConnection node_id=1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: connecting to *.*.*.*:9092 [('*.*.*.*', 9092) IPv4]
2020-11-07 22:16:53,346 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: established TCP connection
2020-11-07 22:16:53,346 INFO <BrokerConnection node_id=1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: Connection complete.
2020-11-07 22:16:53,346 DEBUG Node 1 connected
2020-11-07 22:16:53,346 DEBUG Sending metadata request MetadataRequest_v1(topics=['ping']) to node 1
2020-11-07 22:16:53,346 DEBUG Sending request MetadataRequest_v1(topics=['ping'])
2020-11-07 22:16:53,347 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 1: MetadataRequest_v1(topics=['ping'])
2020-11-07 22:16:53,349 DEBUG Received correlation id: 2
2020-11-07 22:16:53,350 DEBUG Processing response SyncGroupResponse_v1
2020-11-07 22:16:53,350 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 2 (10.8730792999 ms): SyncGroupResponse_v1(throttle_time_ms=0, error_code=0, member_assignment='\x00\x00\x00\x00\x00\x01\x00\x04ping\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00')
2020-11-07 22:16:53,350 INFO Successfully joined group qa-ping with generation 49
2020-11-07 22:16:53,350 INFO Updated partition assignment: [TopicPartition(topic=u'ping', partition=0)]
2020-11-07 22:16:53,350 INFO Setting newly assigned partitions set([TopicPartition(topic=u'ping', partition=0)]) for group qa-ping
2020-11-07 22:16:53,351 DEBUG Node coordinator-1 not ready -- failing offset fetch request
2020-11-07 22:16:53,452 DEBUG Received correlation id: 1
2020-11-07 22:16:53,452 DEBUG Processing response MetadataResponse_v1
2020-11-07 22:16:53,452 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 1 (105.106830597 ms): MetadataResponse_v1(brokers=[(node_id=1, host=u'*.*.*.*', port=9092, rack=None)], controller_id=1, topics=[(error_code=0, topic=u'ping', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])])])
2020-11-07 22:16:53,452 DEBUG Updated cluster metadata to ClusterMetadata(brokers: 1, topics: 1, groups: 1)
2020-11-07 22:16:53,452 DEBUG Group qa-ping fetching committed offsets for partitions: set([TopicPartition(topic=u'ping', partition=0)])
2020-11-07 22:16:53,452 DEBUG Sending request OffsetFetchRequest_v1(consumer_group='qa-ping', topics=[(topic=u'ping', partitions=[0])])
2020-11-07 22:16:53,453 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 3: OffsetFetchRequest_v1(consumer_group='qa-ping', topics=[(topic=u'ping', partitions=[0])])
2020-11-07 22:16:53,460 DEBUG Received correlation id: 3
2020-11-07 22:16:53,460 DEBUG Processing response OffsetFetchResponse_v1
2020-11-07 22:16:53,460 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 3 (7.18092918396 ms): OffsetFetchResponse_v1(topics=[(topic=u'ping', partitions=[(partition=0, offset=262, metadata=u'', error_code=0)])])
2020-11-07 22:16:53,460 DEBUG Resetting offset for partition TopicPartition(topic=u'ping', partition=0) to the committed offset 262
2020-11-07 22:16:53,460 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 262
2020-11-07 22:16:53,460 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:53,460 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=262, max_bytes=1048576)])])
2020-11-07 22:16:53,461 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 2: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=262, max_bytes=1048576)])])
2020-11-07 22:16:53,470 DEBUG Received correlation id: 2
2020-11-07 22:16:53,471 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:53,471 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 2 (9.8340511322 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='\x00\x00\x00\x00\x00\x00\x01\x06\x00\x00\x00_\x00\x00\x00\x00\x02\xc1p\xa5\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x0e`\x0f\x00\x00\x01u\xa3\x0e`\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01Z\x00\x00\x00\x01N{"60.49.168.117": {"1604757857474...')])])
2020-11-07 22:16:53,471 DEBUG Adding fetched record for partition TopicPartition(topic=u'ping', partition=0) with offset 262 to buffered record list
2020-11-07 22:16:53,471 DEBUG Added sensor with name topic.ping.bytes-fetched
2020-11-07 22:16:53,472 DEBUG Added sensor with name topic.ping.records-fetched
2020-11-07 22:16:53,472 DEBUG kafka_sub receive ConsumerRecord(topic=u'ping', partition=0, offset=262, timestamp=1604758429711, timestamp_type=0, key=None, value={u'60.49.168.117': {u'1604757857474': 1}}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=39, serialized_header_size=-1)
2020-11-07 22:16:53,472 DEBUG spawn worker thread handle ping:kafka_sub(args=({u'60.49.168.117': {u'1604757857474': 1}},), kwargs={}, context={})
2020-11-07 22:16:53,472 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:53,472 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:53,472 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:53,472 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 3: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
('recv ping channel data', {u'60.49.168.117': {u'1604757857474': 1}})
2020-11-07 22:16:53,986 DEBUG Received correlation id: 3
2020-11-07 22:16:53,986 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:53,987 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 3 (514.094114304 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:53,987 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:53,988 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:53,988 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:53,988 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 4: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:54,496 DEBUG Received correlation id: 4
2020-11-07 22:16:54,496 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:54,496 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 4 (508.419036865 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:54,497 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:54,498 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:54,498 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:54,498 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 5: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:55,008 DEBUG Received correlation id: 5
2020-11-07 22:16:55,008 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:55,008 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 5 (509.518861771 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:55,009 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:55,009 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:55,009 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:55,010 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 6: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:55,519 DEBUG Received correlation id: 6
2020-11-07 22:16:55,520 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:55,520 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 6 (510.087013245 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:55,520 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:55,521 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:55,521 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:55,521 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 7: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:56,034 DEBUG Received correlation id: 7
2020-11-07 22:16:56,035 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:56,035 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 7 (513.98897171 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:56,037 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:56,037 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:56,038 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:56,038 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 8: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:56,352 DEBUG Heartbeat: qa-ping[49] kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6
2020-11-07 22:16:56,353 DEBUG Sending request HeartbeatRequest_v1(group='qa-ping', generation_id=49, member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6')
2020-11-07 22:16:56,353 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 4: HeartbeatRequest_v1(group='qa-ping', generation_id=49, member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6')
2020-11-07 22:16:56,359 DEBUG Received correlation id: 4
2020-11-07 22:16:56,359 DEBUG Processing response HeartbeatResponse_v1
2020-11-07 22:16:56,359 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 4 (6.49690628052 ms): HeartbeatResponse_v1(throttle_time_ms=0, error_code=0)
2020-11-07 22:16:56,360 DEBUG Received successful heartbeat response for group qa-ping
2020-11-07 22:16:56,544 DEBUG Received correlation id: 8
2020-11-07 22:16:56,545 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:56,545 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 8 (506.130933762 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:56,546 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:56,546 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:56,546 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:56,546 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 9: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:57,056 DEBUG Received correlation id: 9
2020-11-07 22:16:57,056 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:57,056 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 9 (510.158061981 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:57,057 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:57,057 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:57,057 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:57,058 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 10: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:57,569 DEBUG Received correlation id: 10
2020-11-07 22:16:57,569 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:57,569 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 10 (510.963916779 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:57,570 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:57,570 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:57,570 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:57,570 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 11: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:58,082 DEBUG Received correlation id: 11
2020-11-07 22:16:58,082 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:58,083 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 11 (512.013196945 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=263, last_stable_offset=263, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:58,083 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 263
2020-11-07 22:16:58,083 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:58,083 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:58,083 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 12: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=263, max_bytes=1048576)])])
2020-11-07 22:16:58,091 DEBUG spawn worker thread handle ping:ip_ping(args=(), kwargs={}, context=None)
2020-11-07 22:16:58,092 DEBUG Sending (key=None value={'193.53.159.177': {1604758618092: 0}} headers=[]) to TopicPartition(topic='ping', partition=0)
2020-11-07 22:16:58,092 DEBUG Allocating a new 16384 byte message buffer for TopicPartition(topic='ping', partition=0)
2020-11-07 22:16:58,092 DEBUG Waking up the sender since TopicPartition(topic='ping', partition=0) is either full or getting a new batch
2020-11-07 22:16:58,093 DEBUG Node 1 not ready; delaying produce of accumulated batch
2020-11-07 22:16:58,093 DEBUG Initiating connection to node 1 at *.*.*.*:9092
2020-11-07 22:16:58,093 DEBUG Added sensor with name node-1.bytes-sent
2020-11-07 22:16:58,093 DEBUG Added sensor with name node-1.bytes-received
2020-11-07 22:16:58,093 DEBUG Added sensor with name node-1.latency
2020-11-07 22:16:58,094 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <disconnected> [IPv4 None]>: creating new socket
2020-11-07 22:16:58,094 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <disconnected> [IPv4 ('*.*.*.*', 9092)]>: setting socket option (6, 1, 1)
2020-11-07 22:16:58,094 INFO <BrokerConnection node_id=1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: connecting to *.*.*.*:9092 [('*.*.*.*', 9092) IPv4]
2020-11-07 22:16:58,095 DEBUG Node 1 not ready; delaying produce of accumulated batch
2020-11-07 22:16:58,098 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: established TCP connection
2020-11-07 22:16:58,098 INFO <BrokerConnection node_id=1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: Connection complete.
2020-11-07 22:16:58,099 DEBUG Node 1 connected
2020-11-07 22:16:58,099 INFO <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: Closing connection.
2020-11-07 22:16:58,099 DEBUG Node 1 not ready; delaying produce of accumulated batch
2020-11-07 22:16:58,099 DEBUG Sending metadata request MetadataRequest_v1(topics=['ping']) to node 1
2020-11-07 22:16:58,100 DEBUG Sending request MetadataRequest_v1(topics=['ping'])
2020-11-07 22:16:58,100 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 1: MetadataRequest_v1(topics=['ping'])
2020-11-07 22:16:58,101 DEBUG Node 1 not ready; delaying produce of accumulated batch
2020-11-07 22:16:58,107 DEBUG Received correlation id: 1
2020-11-07 22:16:58,107 DEBUG Processing response MetadataResponse_v1
2020-11-07 22:16:58,107 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 1 (7.24005699158 ms): MetadataResponse_v1(brokers=[(node_id=1, host=u'*.*.*.*', port=9092, rack=None)], controller_id=1, topics=[(error_code=0, topic=u'ping', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])])])
2020-11-07 22:16:58,108 DEBUG Updated cluster metadata to ClusterMetadata(brokers: 1, topics: 1, groups: 0)
2020-11-07 22:16:58,108 DEBUG Added sensor with name topic.ping.records-per-batch
2020-11-07 22:16:58,108 DEBUG Added sensor with name topic.ping.bytes
2020-11-07 22:16:58,108 DEBUG Added sensor with name topic.ping.compression-rate
2020-11-07 22:16:58,108 DEBUG Added sensor with name topic.ping.record-retries
2020-11-07 22:16:58,109 DEBUG Added sensor with name topic.ping.record-errors
2020-11-07 22:16:58,109 DEBUG Nodes with data ready to send: set([1])
2020-11-07 22:16:58,109 DEBUG Created 1 produce requests: {1: ProduceRequest_v7(transactional_id=None, required_acks=1, timeout=30000, topics=[(topic='ping', partitions=[(partition=0, messages='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x02\x94bz\x19\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x11?\xec\x00\x00\x01u\xa3\x11?\xec\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01\\\x00\x00\x00\x01P{"193.53.159.177": {"160475861809...')])])}
2020-11-07 22:16:58,109 DEBUG Sending Produce Request: ProduceRequest_v7(transactional_id=None, required_acks=1, timeout=30000, topics=[(topic='ping', partitions=[(partition=0, messages='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x02\x94bz\x19\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x11?\xec\x00\x00\x01u\xa3\x11?\xec\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01\\\x00\x00\x00\x01P{"193.53.159.177": {"160475861809...')])])
2020-11-07 22:16:58,110 DEBUG Sending request ProduceRequest_v7(transactional_id=None, required_acks=1, timeout=30000, topics=[(topic='ping', partitions=[(partition=0, messages='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x02\x94bz\x19\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x11?\xec\x00\x00\x01u\xa3\x11?\xec\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01\\\x00\x00\x00\x01P{"193.53.159.177": {"160475861809...')])])
2020-11-07 22:16:58,110 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 2: ProduceRequest_v7(transactional_id=None, required_acks=1, timeout=30000, topics=[(topic='ping', partitions=[(partition=0, messages='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x02\x94bz\x19\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x11?\xec\x00\x00\x01u\xa3\x11?\xec\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01\\\x00\x00\x00\x01P{"193.53.159.177": {"160475861809...')])])
2020-11-07 22:16:58,120 DEBUG Received correlation id: 12
2020-11-07 22:16:58,120 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:58,120 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 12 (36.4439487457 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=264, last_stable_offset=264, aborted_transactions=NULL, message_set='\x00\x00\x00\x00\x00\x00\x01\x07\x00\x00\x00`\x00\x00\x00\x00\x02\x94bz\x19\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x11?\xec\x00\x00\x01u\xa3\x11?\xec\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01\\\x00\x00\x00\x01P{"193.53.159.177": {"160475861809...')])])
2020-11-07 22:16:58,120 DEBUG Adding fetched record for partition TopicPartition(topic=u'ping', partition=0) with offset 263 to buffered record list
2020-11-07 22:16:58,121 DEBUG kafka_sub receive ConsumerRecord(topic=u'ping', partition=0, offset=263, timestamp=1604758618092, timestamp_type=0, key=None, value={u'193.53.159.177': {u'1604758618092': 0}}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=40, serialized_header_size=-1)
2020-11-07 22:16:58,121 DEBUG spawn worker thread handle ping:kafka_sub(args=({u'193.53.159.177': {u'1604758618092': 0}},), kwargs={}, context={})
2020-11-07 22:16:58,121 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 264
2020-11-07 22:16:58,121 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:58,121 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:16:58,121 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 13: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:16:58,122 DEBUG Received correlation id: 2
2020-11-07 22:16:58,122 DEBUG Processing response ProduceResponse_v7
2020-11-07 22:16:58,122 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 2 (12.1188163757 ms): ProduceResponse_v7(topics=[(topic=u'ping', partitions=[(partition=0, error_code=0, offset=263, timestamp=-1, log_start_offset=0)])], throttle_time_ms=0)
2020-11-07 22:16:58,122 DEBUG Parsing produce response: ProduceResponse_v7(topics=[(topic=u'ping', partitions=[(partition=0, error_code=0, offset=263, timestamp=-1, log_start_offset=0)])], throttle_time_ms=0)
2020-11-07 22:16:58,122 DEBUG Produced messages to topic-partition TopicPartition(topic='ping', partition=0) with base offset 263 log start offset 0 and error None.
('recv ping channel data', {u'193.53.159.177': {u'1604758618092': 0}})
2020-11-07 22:16:58,353 DEBUG Sending offset-commit request with {TopicPartition(topic=u'ping', partition=0): OffsetAndMetadata(offset=264, metadata='')} for group qa-ping to coordinator-1
2020-11-07 22:16:58,353 DEBUG Sending request OffsetCommitRequest_v2(consumer_group='qa-ping', consumer_group_generation_id=49, consumer_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', retention_time=-1, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, metadata='')])])
2020-11-07 22:16:58,353 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 5: OffsetCommitRequest_v2(consumer_group='qa-ping', consumer_group_generation_id=49, consumer_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', retention_time=-1, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, metadata='')])])
2020-11-07 22:16:58,361 DEBUG Received correlation id: 5
2020-11-07 22:16:58,361 DEBUG Processing response OffsetCommitResponse_v2
2020-11-07 22:16:58,361 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 5 (8.28289985657 ms): OffsetCommitResponse_v2(topics=[(topic=u'ping', partitions=[(partition=0, error_code=0)])])
2020-11-07 22:16:58,362 DEBUG Group qa-ping committed offset OffsetAndMetadata(offset=264, metadata='') for partition TopicPartition(topic=u'ping', partition=0)
2020-11-07 22:16:58,362 DEBUG Completed autocommit of offsets {TopicPartition(topic=u'ping', partition=0): OffsetAndMetadata(offset=264, metadata='')} for group qa-ping
2020-11-07 22:16:58,631 DEBUG Received correlation id: 13
2020-11-07 22:16:58,631 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:58,632 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 13 (509.99212265 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=264, last_stable_offset=264, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:58,633 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 264
2020-11-07 22:16:58,633 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:58,633 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:16:58,633 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 14: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:16:59,138 DEBUG Received correlation id: 14
2020-11-07 22:16:59,138 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:59,138 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 14 (504.908084869 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=264, last_stable_offset=264, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:59,139 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 264
2020-11-07 22:16:59,139 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:59,139 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:16:59,139 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 15: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:16:59,354 DEBUG Heartbeat: qa-ping[49] kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6
2020-11-07 22:16:59,355 DEBUG Sending request HeartbeatRequest_v1(group='qa-ping', generation_id=49, member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6')
2020-11-07 22:16:59,355 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 6: HeartbeatRequest_v1(group='qa-ping', generation_id=49, member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6')
2020-11-07 22:16:59,369 DEBUG Received correlation id: 6
2020-11-07 22:16:59,370 DEBUG Processing response HeartbeatResponse_v1
2020-11-07 22:16:59,370 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 6 (14.9340629578 ms): HeartbeatResponse_v1(throttle_time_ms=0, error_code=0)
2020-11-07 22:16:59,370 DEBUG Received successful heartbeat response for group qa-ping
2020-11-07 22:16:59,962 DEBUG Received correlation id: 15
2020-11-07 22:16:59,962 DEBUG Processing response FetchResponse_v4
2020-11-07 22:16:59,962 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 15 (822.746038437 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=264, last_stable_offset=264, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:16:59,963 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 264
2020-11-07 22:16:59,963 DEBUG Sending FetchRequest to node 1
2020-11-07 22:16:59,963 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:16:59,963 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 16: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:17:00,509 DEBUG Received correlation id: 16
2020-11-07 22:17:00,510 DEBUG Processing response FetchResponse_v4
2020-11-07 22:17:00,510 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 16 (546.273946762 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=264, last_stable_offset=264, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:17:00,511 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 264
2020-11-07 22:17:00,511 DEBUG Sending FetchRequest to node 1
2020-11-07 22:17:00,511 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:17:00,511 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 17: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:17:01,017 DEBUG Received correlation id: 17
2020-11-07 22:17:01,017 DEBUG Processing response FetchResponse_v4
2020-11-07 22:17:01,017 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 17 (506.042957306 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=264, last_stable_offset=264, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:17:01,018 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 264
2020-11-07 22:17:01,018 DEBUG Sending FetchRequest to node 1
2020-11-07 22:17:01,019 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:17:01,019 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 18: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
^C2020-11-07 22:17:01,139 DEBUG stopping services ['ping']
2020-11-07 22:17:01,140 DEBUG stopping service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:producer_metrics, ping:namekox_timer.core.entrypoints.timer.Timer:ip_ping, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server, ping:namekox_kafka.core.entrypoints.sub.handler.KafkaSubHandler:kafka_sub]
2020-11-07 22:17:01,140 DEBUG Closing the KafkaConsumer.
2020-11-07 22:17:01,526 DEBUG Sending offset-commit request with {TopicPartition(topic=u'ping', partition=0): OffsetAndMetadata(offset=264, metadata='')} for group qa-ping to coordinator-1
2020-11-07 22:17:01,526 DEBUG Sending request OffsetCommitRequest_v2(consumer_group='qa-ping', consumer_group_generation_id=49, consumer_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', retention_time=-1, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, metadata='')])])
2020-11-07 22:17:01,526 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 7: OffsetCommitRequest_v2(consumer_group='qa-ping', consumer_group_generation_id=49, consumer_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6', retention_time=-1, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, metadata='')])])
2020-11-07 22:17:01,535 DEBUG Received correlation id: 18
2020-11-07 22:17:01,535 DEBUG Processing response FetchResponse_v4
2020-11-07 22:17:01,535 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 18 (516.289949417 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=264, last_stable_offset=264, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:17:01,536 DEBUG Adding fetch request for partition TopicPartition(topic=u'ping', partition=0) at offset 264
2020-11-07 22:17:01,536 DEBUG Sending FetchRequest to node 1
2020-11-07 22:17:01,536 DEBUG Sending request FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:17:01,537 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 19: FetchRequest_v4(replica_id=-1, max_wait_time=500, min_bytes=1, max_bytes=52428800, isolation_level=0, topics=[(topic=u'ping', partitions=[(partition=0, offset=264, max_bytes=1048576)])])
2020-11-07 22:17:01,540 DEBUG Received correlation id: 7
2020-11-07 22:17:01,540 DEBUG Processing response OffsetCommitResponse_v2
2020-11-07 22:17:01,540 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 7 (13.7329101562 ms): OffsetCommitResponse_v2(topics=[(topic=u'ping', partitions=[(partition=0, error_code=0)])])
2020-11-07 22:17:01,540 DEBUG Group qa-ping committed offset OffsetAndMetadata(offset=264, metadata='') for partition TopicPartition(topic=u'ping', partition=0)
2020-11-07 22:17:01,540 INFO Stopping heartbeat thread
2020-11-07 22:17:01,543 DEBUG Heartbeat thread closed
2020-11-07 22:17:02,043 INFO Leaving consumer group (qa-ping).
2020-11-07 22:17:02,043 DEBUG Sending request LeaveGroupRequest_v1(group='qa-ping', member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6')
2020-11-07 22:17:02,044 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 8: LeaveGroupRequest_v1(group='qa-ping', member_id=u'kafka-python-2.0.2-7c455180-554f-48ad-9fa6-039fd0dfd2a6')
2020-11-07 22:17:02,045 DEBUG Received correlation id: 19
2020-11-07 22:17:02,045 DEBUG Processing response FetchResponse_v4
2020-11-07 22:17:02,045 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 19 (508.592844009 ms): FetchResponse_v4(throttle_time_ms=0, topics=[(topics=u'ping', partitions=[(partition=0, error_code=0, highwater_offset=264, last_stable_offset=264, aborted_transactions=NULL, message_set='')])])
2020-11-07 22:17:02,051 DEBUG Received correlation id: 8
2020-11-07 22:17:02,051 DEBUG Processing response LeaveGroupResponse_v1
2020-11-07 22:17:02,051 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 8 (7.21716880798 ms): LeaveGroupResponse_v1(throttle_time_ms=0, error_code=0)
2020-11-07 22:17:02,051 DEBUG LeaveGroup request for group qa-ping returned successfully
2020-11-07 22:17:02,052 INFO <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: Closing connection.
2020-11-07 22:17:02,052 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: reconnect backoff 0.0406080994745 after 1 failures
2020-11-07 22:17:02,052 INFO <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: Closing connection.
2020-11-07 22:17:02,052 DEBUG <BrokerConnection node_id=coordinator-1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: reconnect backoff 0.0477360482422 after 1 failures
2020-11-07 22:17:02,052 DEBUG The KafkaConsumer has closed.
2020-11-07 22:17:02,053 DEBUG wait service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:producer_metrics, ping:namekox_timer.core.entrypoints.timer.Timer:ip_ping, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server, ping:namekox_kafka.core.entrypoints.sub.handler.KafkaSubHandler:kafka_sub] stop
2020-11-07 22:17:02,053 DEBUG service ping entrypoints [ping:namekox_webserver.core.entrypoints.app.handler.ApiServerHandler:producer_metrics, ping:namekox_timer.core.entrypoints.timer.Timer:ip_ping, ping:namekox_webserver.core.entrypoints.app.server.WebServer:server, ping:namekox_kafka.core.entrypoints.sub.handler.KafkaSubHandler:kafka_sub] stopped
2020-11-07 22:17:02,053 DEBUG stopping service ping dependencies [ping:namekox_kafka.core.dependencies.pub.KafkaPubProxy:kafka_pub]
2020-11-07 22:17:02,053 INFO Closing the Kafka producer with inf secs timeout.
2020-11-07 22:17:02,054 DEBUG Beginning shutdown of Kafka producer I/O thread, sending remaining records.
2020-11-07 22:17:02,054 INFO <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: Closing connection.
2020-11-07 22:17:02,054 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: reconnect backoff 0.057582732023 after 1 failures
2020-11-07 22:17:02,054 DEBUG Shutdown of Kafka producer I/O thread has completed.
2020-11-07 22:17:02,055 DEBUG The Kafka producer has closed.
2020-11-07 22:17:02,055 DEBUG service ping dependencies [ping:namekox_kafka.core.dependencies.pub.KafkaPubProxy:kafka_pub] stopped
2020-11-07 22:17:02,055 DEBUG services ['ping'] stopped
2020-11-07 22:17:02,055 DEBUG killing services ['ping']
2020-11-07 22:17:02,055 DEBUG service ping already stopped
2020-11-07 22:17:02,055 DEBUG services ['ping'] killed
```

# Debug
> config.yaml
```yaml
CONTEXT:
  - namekox_kafka.cli.subctx.kafkapub:KafkaPub
KAFKA:
  ping:
    bootstrap_servers: "*.*.*.*:9092"
    retry_backoff_ms: 100
```
> namekox shell
```shell script
In [1]: import json

In [2]: nx.kafkapub.proxy('ping', compression_type='gzip', value_serializer=json.dumps).send('ping', {"60.49.168.117": {"1604757857474": 1}})
2020-11-07 22:13:49,530 DEBUG Starting the Kafka producer
2020-11-07 22:13:49,534 DEBUG Added sensor with name connections-closed
2020-11-07 22:13:49,534 DEBUG Added sensor with name connections-created
2020-11-07 22:13:49,535 DEBUG Added sensor with name select-time
2020-11-07 22:13:49,535 DEBUG Added sensor with name io-time
2020-11-07 22:13:49,536 DEBUG Initiating connection to node bootstrap-0 at *.*.*.*:9092
2020-11-07 22:13:49,537 DEBUG Added sensor with name bytes-sent-received
2020-11-07 22:13:49,537 DEBUG Added sensor with name bytes-sent
2020-11-07 22:13:49,537 DEBUG Added sensor with name bytes-received
2020-11-07 22:13:49,537 DEBUG Added sensor with name request-latency
2020-11-07 22:13:49,538 DEBUG Added sensor with name node-bootstrap-0.bytes-sent
2020-11-07 22:13:49,538 DEBUG Added sensor with name node-bootstrap-0.bytes-received
2020-11-07 22:13:49,538 DEBUG Added sensor with name node-bootstrap-0.latency
2020-11-07 22:13:49,538 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <disconnected> [IPv4 None]>: creating new socket
2020-11-07 22:13:49,539 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <disconnected> [IPv4 ('*.*.*.*', 9092)]>: setting socket option (6, 1, 1)
2020-11-07 22:13:49,540 INFO <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: connecting to *.*.*.*:9092 [('*.*.*.*', 9092) IPv4]
2020-11-07 22:13:49,540 INFO Probing node bootstrap-0 broker version
2020-11-07 22:13:49,545 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: established TCP connection
2020-11-07 22:13:49,545 INFO <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: Connection complete.
2020-11-07 22:13:49,545 DEBUG Node bootstrap-0 connected
2020-11-07 22:13:49,545 DEBUG Sending request ApiVersionRequest_v0()
2020-11-07 22:13:49,546 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 1: ApiVersionRequest_v0()
2020-11-07 22:13:49,649 DEBUG Sending request MetadataRequest_v0(topics=[])
2020-11-07 22:13:49,649 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 2: MetadataRequest_v0(topics=[])
2020-11-07 22:13:49,650 DEBUG Received correlation id: 1
2020-11-07 22:13:49,650 DEBUG Processing response ApiVersionResponse_v0
2020-11-07 22:13:49,650 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 1 (104.593992233 ms): ApiVersionResponse_v0(error_code=0, api_versions=[(api_key=0, min_version=0, max_version=7), (api_key=1, min_version=0, max_version=10), (api_key=2, min_version=0, max_version=4), (api_key=3, min_version=0, max_version=7), (api_key=4, min_version=0, max_version=1), (api_key=5, min_version=0, max_version=0), (api_key=6, min_version=0, max_version=4), (api_key=7, min_version=0, max_version=1), (api_key=8, min_version=0, max_version=6), (api_key=9, min_version=0, max_version=5), (api_key=10, min_version=0, max_version=2), (api_key=11, min_version=0, max_version=3), (api_key=12, min_version=0, max_version=2), (api_key=13, min_version=0, max_version=2), (api_key=14, min_version=0, max_version=2), (api_key=15, min_version=0, max_version=2), (api_key=16, min_version=0, max_version=2), (api_key=17, min_version=0, max_version=1), (api_key=18, min_version=0, max_version=2), (api_key=19, min_version=0, max_version=3), (api_key=20, min_version=0, max_version=3), (api_key=21, min_version=0, max_version=1), (api_key=22, min_version=0, max_version=1), (api_key=23, min_version=0, max_version=2), (api_key=24, min_version=0, max_version=1), (api_key=25, min_version=0, max_version=1), (api_key=26, min_version=0, max_version=1), (api_key=27, min_version=0, max_version=0), (api_key=28, min_version=0, max_version=2), (api_key=29, min_version=0, max_version=1), (api_key=30, min_version=0, max_version=1), (api_key=31, min_version=0, max_version=1), (api_key=32, min_version=0, max_version=2), (api_key=33, min_version=0, max_version=1), (api_key=34, min_version=0, max_version=1), (api_key=35, min_version=0, max_version=1), (api_key=36, min_version=0, max_version=0), (api_key=37, min_version=0, max_version=1), (api_key=38, min_version=0, max_version=1), (api_key=39, min_version=0, max_version=1), (api_key=40, min_version=0, max_version=1), (api_key=41, min_version=0, max_version=1), (api_key=42, min_version=0, max_version=1)])
2020-11-07 22:13:49,659 DEBUG Received correlation id: 2
2020-11-07 22:13:49,659 DEBUG Processing response MetadataResponse_v0
2020-11-07 22:13:49,661 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 2 (11.3220214844 ms): MetadataResponse_v0(brokers=[(node_id=1, host=u'*.*.*.*', port=9092)], topics=[(error_code=0, topic=u'dns', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'cloudprint', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'wifiscreen', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_info', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'safe', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'__consumer_offsets', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=10, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=20, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=40, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=30, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=9, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=11, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=31, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=39, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=13, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=18, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=22, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=8, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=32, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=43, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=29, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=34, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=6, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=41, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=27, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=48, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=5, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=15, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=35, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=25, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=46, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=26, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=36, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=44, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=16, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=37, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=17, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=45, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=3, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=24, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=38, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=33, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=23, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=28, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=12, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=19, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=14, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=4, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=47, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=49, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=42, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=7, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=21, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient_info', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'share', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ping', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'menjin', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'webmeeting', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient-info', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'kms', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'telephone', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ad', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_action', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'canonprint', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'device-__assignor-__leader', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'bj_sxflog', partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])])])
2020-11-07 22:13:49,663 INFO Broker version identified as 2.1.0
2020-11-07 22:13:49,663 INFO Set configuration api_version=(2, 1, 0) to skip auto check_version requests on startup
2020-11-07 22:13:49,664 DEBUG Added sensor with name bufferpool-wait-time
2020-11-07 22:13:49,691 DEBUG Added sensor with name batch-size
2020-11-07 22:13:49,691 DEBUG Added sensor with name compression-rate
2020-11-07 22:13:49,691 DEBUG Added sensor with name queue-time
2020-11-07 22:13:49,691 DEBUG Added sensor with name produce-throttle-time
2020-11-07 22:13:49,691 DEBUG Added sensor with name records-per-request
2020-11-07 22:13:49,691 DEBUG Added sensor with name bytes
2020-11-07 22:13:49,691 DEBUG Added sensor with name record-retries
2020-11-07 22:13:49,692 DEBUG Added sensor with name errors
2020-11-07 22:13:49,692 DEBUG Added sensor with name record-size-max
2020-11-07 22:13:49,692 DEBUG Starting Kafka producer I/O thread.
2020-11-07 22:13:49,692 DEBUG Kafka producer started
2020-11-07 22:13:49,693 DEBUG Sending metadata request MetadataRequest_v1(topics=NULL) to node bootstrap-0
2020-11-07 22:13:49,693 DEBUG Requesting metadata update for topic ping
2020-11-07 22:13:49,693 DEBUG Sending request MetadataRequest_v1(topics=NULL)
2020-11-07 22:13:49,694 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 3: MetadataRequest_v1(topics=NULL)
2020-11-07 22:13:49,702 DEBUG Received correlation id: 3
2020-11-07 22:13:49,702 DEBUG Processing response MetadataResponse_v1
2020-11-07 22:13:49,703 DEBUG <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 3 (9.19795036316 ms): MetadataResponse_v1(brokers=[(node_id=1, host=u'*.*.*.*', port=9092, rack=None)], controller_id=1, topics=[(error_code=0, topic=u'dns', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'cloudprint', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'wifiscreen', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_info', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'safe', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'__consumer_offsets', is_internal=True, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=10, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=20, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=40, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=30, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=9, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=11, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=31, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=39, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=13, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=18, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=22, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=8, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=32, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=43, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=29, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=34, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=6, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=41, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=27, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=48, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=5, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=15, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=35, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=25, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=46, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=26, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=36, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=44, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=16, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=37, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=17, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=45, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=3, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=24, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=38, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=33, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=23, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=28, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=12, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=19, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=14, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=4, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=47, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=49, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=42, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=7, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=21, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient_info', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'share', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ping', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'menjin', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'webmeeting', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcpclient-info', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'kms', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'telephone', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'ad', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'dhcp_action', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'canonprint', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'device-__assignor-__leader', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1])]), (error_code=0, topic=u'bj_sxflog', is_internal=False, partitions=[(error_code=0, partition=0, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=2, leader=1, replicas=[1], isr=[1]), (error_code=0, partition=1, leader=1, replicas=[1], isr=[1])])])
2020-11-07 22:13:49,705 DEBUG Updated cluster metadata to ClusterMetadata(brokers: 1, topics: 20, groups: 0)
2020-11-07 22:13:49,710 DEBUG _wait_on_metadata woke after 0.0168640613556 secs.
2020-11-07 22:13:49,711 DEBUG Sending (key=None value={'60.49.168.117': {'1604757857474': 1}} headers=[]) to TopicPartition(topic='ping', partition=0)
2020-11-07 22:13:49,711 DEBUG Allocating a new 16384 byte message buffer for TopicPartition(topic='ping', partition=0)
2020-11-07 22:13:49,711 DEBUG Waking up the sender since TopicPartition(topic='ping', partition=0) is either full or getting a new batch
2020-11-07 22:13:49,712 DEBUG Beginning shutdown of Kafka producer I/O thread, sending remaining records.
2020-11-07 22:13:49,712 DEBUG Node 1 not ready; delaying produce of accumulated batch
2020-11-07 22:13:49,712 DEBUG Initiating connection to node 1 at *.*.*.*:9092
2020-11-07 22:13:49,712 DEBUG Added sensor with name node-1.bytes-sent
2020-11-07 22:13:49,712 DEBUG Added sensor with name node-1.bytes-received
2020-11-07 22:13:49,712 DEBUG Added sensor with name node-1.latency
2020-11-07 22:13:49,713 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <disconnected> [IPv4 None]>: creating new socket
2020-11-07 22:13:49,713 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <disconnected> [IPv4 ('*.*.*.*', 9092)]>: setting socket option (6, 1, 1)
2020-11-07 22:13:49,713 INFO <BrokerConnection node_id=1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: connecting to *.*.*.*:9092 [('*.*.*.*', 9092) IPv4]
2020-11-07 22:13:49,713 DEBUG Node 1 not ready; delaying produce of accumulated batch
2020-11-07 22:13:49,718 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: established TCP connection
2020-11-07 22:13:49,718 INFO <BrokerConnection node_id=1 host=*.*.*.*:9092 <connecting> [IPv4 ('*.*.*.*', 9092)]>: Connection complete.
2020-11-07 22:13:49,718 DEBUG Node 1 connected
2020-11-07 22:13:49,719 INFO <BrokerConnection node_id=bootstrap-0 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: Closing connection.
2020-11-07 22:13:49,720 DEBUG Added sensor with name topic.ping.records-per-batch
2020-11-07 22:13:49,720 DEBUG Added sensor with name topic.ping.bytes
2020-11-07 22:13:49,721 DEBUG Added sensor with name topic.ping.compression-rate
2020-11-07 22:13:49,721 DEBUG Added sensor with name topic.ping.record-retries
2020-11-07 22:13:49,721 DEBUG Added sensor with name topic.ping.record-errors
2020-11-07 22:13:49,722 DEBUG Nodes with data ready to send: set([1])
2020-11-07 22:13:49,722 DEBUG Created 1 produce requests: {1: ProduceRequest_v7(transactional_id=None, required_acks=1, timeout=30000, topics=[(topic='ping', partitions=[(partition=0, messages='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_\x00\x00\x00\x00\x02\xc1p\xa5\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x0e`\x0f\x00\x00\x01u\xa3\x0e`\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01Z\x00\x00\x00\x01N{"60.49.168.117": {"1604757857474...')])])}
2020-11-07 22:13:49,722 DEBUG Sending Produce Request: ProduceRequest_v7(transactional_id=None, required_acks=1, timeout=30000, topics=[(topic='ping', partitions=[(partition=0, messages='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_\x00\x00\x00\x00\x02\xc1p\xa5\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x0e`\x0f\x00\x00\x01u\xa3\x0e`\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01Z\x00\x00\x00\x01N{"60.49.168.117": {"1604757857474...')])])
2020-11-07 22:13:49,722 DEBUG Sending request ProduceRequest_v7(transactional_id=None, required_acks=1, timeout=30000, topics=[(topic='ping', partitions=[(partition=0, messages='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_\x00\x00\x00\x00\x02\xc1p\xa5\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x0e`\x0f\x00\x00\x01u\xa3\x0e`\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01Z\x00\x00\x00\x01N{"60.49.168.117": {"1604757857474...')])])
2020-11-07 22:13:49,722 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Request 1: ProduceRequest_v7(transactional_id=None, required_acks=1, timeout=30000, topics=[(topic='ping', partitions=[(partition=0, messages='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_\x00\x00\x00\x00\x02\xc1p\xa5\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x01u\xa3\x0e`\x0f\x00\x00\x01u\xa3\x0e`\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x01Z\x00\x00\x00\x01N{"60.49.168.117": {"1604757857474...')])])
2020-11-07 22:13:49,729 DEBUG Received correlation id: 1
2020-11-07 22:13:49,729 DEBUG Processing response ProduceResponse_v7
2020-11-07 22:13:49,730 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]> Response 1 (7.3459148407 ms): ProduceResponse_v7(topics=[(topic=u'ping', partitions=[(partition=0, error_code=0, offset=262, timestamp=-1, log_start_offset=0)])], throttle_time_ms=0)
2020-11-07 22:13:49,730 DEBUG Parsing produce response: ProduceResponse_v7(topics=[(topic=u'ping', partitions=[(partition=0, error_code=0, offset=262, timestamp=-1, log_start_offset=0)])], throttle_time_ms=0)
2020-11-07 22:13:49,731 DEBUG Produced messages to topic-partition TopicPartition(topic='ping', partition=0) with base offset 262 log start offset 0 and error None.
2020-11-07 22:13:49,731 INFO <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: Closing connection.
2020-11-07 22:13:49,731 DEBUG <BrokerConnection node_id=1 host=*.*.*.*:9092 <connected> [IPv4 ('*.*.*.*', 9092)]>: reconnect backoff 0.0476399714485 after 1 failures
2020-11-07 22:13:49,731 DEBUG Shutdown of Kafka producer I/O thread has completed.
Out[2]: <kafka.producer.future.FutureRecordMetadata at 0x111c8ddd0>
```
