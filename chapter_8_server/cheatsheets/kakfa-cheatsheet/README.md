**Setup**

Run [landoop/fast-data-dev](https://github.com/Landoop/fast-data-dev) docker image. For example: 

```
docker run --rm -it -p 2181:2181 -p 3030:3030 -p 8081:8081 -p 8082:8082 -p 8083:8083 -p 9092:9092 -p 9581:9581 -p 9582:9582 -p 9583:9583 -p 9584:9584 -e ADV_HOST=127.0.0.1 landoop/fast-data-dev:latest
```
_Note: Follow the instructions on fast-data-dev README to customise the container._

Enter the container bash: 

```
docker run --rm -it --net=host landoop/fast-data-dev bash
```

Kafka utilities are now available:

# Topics

Creating a New Topic
```
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic my-topic
```
Verify the topic
```
kafka-topics --list --zookeeper localhost:2181
```
Adding Partitions
```
kafka-topics --zookeeper localhost:2181 --alter --topic my-topic --partitions 16
```
Deleting a Topic
```
kafka-topics --zookeeper localhost:2181 --delete --topic my-topic
```
Listing All Topics in a Cluster
```
kafka-topics --zookeeper localhost:2181 --list
```
Describing Topic Details
```
kafka-topics --zookeeper localhost:2181/kafka-cluster --describe
```
Show Under-replicated Partitions for topics
```
kafka-topics --zookeeper localhost:2181/kafka-cluster --describe --under-replicated-partitions
```

# Producers
Produce messages standard input
```
kafka-console-producer --broker-list localhost:9092 --topic my-topic
```
Produce messages file
```
kafka-console-producer --broker-list localhost:9092 --topic test < messages.txt
```
Produce Avro messages
```
kafka-avro-console-producer --broker-list localhost:9092 --topic my.Topic --property value.schema='{"type":"record","name":"myrecord","fields":[{"name":"f1","type":"string"}]}' --property schema.registry.url=http://localhost:8081
```
And enter a few values from the console:
```
{"f1": "value1"}
```

# Consumers

## Consume messages

Start a consumer from the beginning of the log
```
kafka-console-consumer --bootstrap-server localhost:9092 --topic my-topic --from-beginning
```
Consume 1 message
```
kafka-console-consumer --bootstrap-server localhost:9092 --topic my-topic  --max-messages 1
```

Consume 1 message from `__consumer_offsets`
```
kafka-console-consumer --bootstrap-server localhost:9092 --topic __consumer_offsets --formatter 'kafka.coordinator.GroupMetadataManager$OffsetsMessageFormatter' --max-messages 1
```

Consume, specify consumer group:
```
kafka-console-consumer --topic my-topic --new-consumer --bootstrap-server localhost:9092 --consumer-property group.id=my-group
```

## Consume Avro messages
```
kafka-avro-console-consumer --topic position-reports --new-consumer --bootstrap-server localhost:9092 --from-beginning --property schema.registry.url=localhost:8081 --max-messages 10
```

```
kafka-avro-console-consumer --topic position-reports --new-consumer --bootstrap-server localhost:9092 --from-beginning --property schema.registry.url=localhost:8081
```

## Consumers admin operations

List Groups
```
kafka-consumer-groups --new-consumer --list --bootstrap-server localhost:9092
```
Describe Groups
```
kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group testgroup
```

# Config
Set the retention for the topic
```
kafka-configs --zookeeper localhost:2181 --alter --entity-type topics --entity-name my-topic --add-config retention.ms=3600000
``` 
Show all configuration overrides for a topic
```
kafka-configs --zookeeper localhost:2181 --describe --entity-type topics --entity-name my-topic
```
Delete a configuration override for retention.ms for a topic 
```
kafka-configs --zookeeper localhost:2181 --alter --entity-type topics --entity-name my-topic --delete-config retention.ms 
```

# Performance

Producer
```
kafka-producer-perf-test --topic position-reports --throughput 10000 --record-size 300 --num-records 20000 --producer-props bootstrap.servers="localhost:9092"
```

# ACLs
```
kafka-acls --authorizer-properties zookeeper.connect=localhost:2181 --add --allow-principal User:Bob --consumer --topic topicA --group groupA
```

```
kafka-acls --authorizer-properties zookeeper.connect=localhost:2181 --add --allow-principal User:Bob --producer --topic topicA
```
List the ACLs
```
 kafka-acls --authorizer-properties zookeeper.connect=localhost:2181 --list --topic topicA
```

# Zookeeper 
Enter zookeepr shell:
```
zookeeper-shell localhost:2182 ls /
```
