
RMQ:
TASK-1
=>Install and configure 1 node RMQ cluster version 3.7.9.

Task-2
=>The RMQ cluster should be on TLS and have a username/password.

Task-3
=>Data should be persisted on disk.

Task-4
=>Add 2 more nodes to the cluster without restarting RMQ service on first one.

Task-5
=>Create a vhost and a user with read-write permissions to the vhost.

Task-6
=>Create 2 queues (DATA, DATA_SIDELINE) on the above created vhost.

Task-7
=>Create a publisher and consumer for the DATA queue, the messages which were not consumed by the consumer should move to the DATA_SIDELINE queue after a specific time.

Task-8
=>Stop the consumer.

Task-9
Publish 100 messages to DATA queue.

Task-10
=>The 100 messages should automatically get moved to DATA_SIDELINE queue.

Task-11
=>Stop the publisher.

Task-12
=>Take a dump of the messages in DATA_SIDELINE queue using RMQ API/curl.

Task-13
=>Delete the messages from the DATA_SIDELINE queue using RMQ API/curl.

Task-14
=>Push the messages to DATA queue using RMQ API/curl
