FROM apache/flink:1.18.1-scala_2.12-java17

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip wget && \
    ln -sf /usr/bin/python3 /usr/bin/python

RUN pip3 install apache-flink==1.18.1

# Kafka Connector
RUN wget -P /opt/flink/lib \
https://repo1.maven.org/maven2/org/apache/flink/flink-connector-kafka/3.0.2-1.18/flink-connector-kafka-3.0.2-1.18.jar

# Kafka Client Library
RUN wget -P /opt/flink/lib \
https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.5.1/kafka-clients-3.5.1.jar

WORKDIR /opt/flink/job

COPY . .

USER flink