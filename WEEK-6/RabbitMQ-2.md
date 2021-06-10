# RABBIT-MQ


### STOP THE CONSUMER
```
Stopping the Consumer can be done my stopping the scripts or by Stopping in The RMQ -APP UI 
In the app-UI 
In my cases just stopped the script where consumer code were written.
```

### PUBLISH 100 MESSAGES
```
=>Publish 100 messages to DATA queue

=> In the Script where there was SENDER message and publish message for DATA Queue.
=> In the send1.py  (queue name => DATA)
=> The for loop was implemented where the basic_publish was inside the queue.

=>
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.queue_declare(queue='DATA')
channel.queue_bind(exchange='logs', queue='DATA')

#channel.basic_publish(exchange='logs', routing_key='DATA', body='Hello World!')
#print(" [x] Sent 'Hello World!'")
message = "Hello World";                                                     // basic message "Hello World"   
for i in range(1,101):                                                      // For Loop from 1-101 =>(1,100)
            channel.basic_publish(body=message,                             // body =message (variable) 
                                exchange='logs',
                                routing_key='DATA',                         //  Queue name DATA
                                properties=pika.BasicProperties(delivery_mode=2, ))    // delivery_mode=2 for messages to stay persisted  
            print("[x] Sent '{i}' 'message...'")
connection.close()

=> exchange='logs', ( Type used was 'logs')
=> There are a few exchange types available: direct, topic, headers and fanout. 

```

### 100 MESSAGES TO OTHER QUEUE
```
=> The 100 messages should automatically get moved to DATA_SIDELINE queue

=> For this SHOVEL Concept was used where.
=> First the Consumer for DATA Queue script was stopped.
=> Then the second QUEUES (DATA_SIDELINE) consumer was added.

=> rabbitmqctl set_parameter shovel my-shovel2'{"src-protocol": "amqp091", "src-uri": "amqp://raju:raju@/kanakaraju", "src-queue": "DATA", 
                      "dest-protocol": "amqp091", "dest-uri": "amqp://raju:raju@/kanakaraju", "dest-queue": "DATA_SIDELINE"}'

=> "src-queue": "DATA" (The message is being published in DATA queue)
=> "dest-queue": "DATA_SIDELINE"  (The destination was DATA_SIDELINE queue )
```

### STOP THE PUBLISHER
```
Stop the publisher
This can be done using my stopping the Publisher in the appUI
Click on the queue => publisher => delete publisher
```

### TAKE A DUMP OF THE MESSAGES
```
=>The RabbitMQ Management plugin provides an HTTP-based API for management and monitoring of your RabbitMQ server.
=>Take a dump of the messages in DATA_SIDELINE queue using RMQ API/curl
=> The DUMP was taken using curl.
=>                                                 
curl -u raju:raju -H "content-type:application/json" -XPOST http://192.168.43.102:15672/api/queues/kanakaraju/DATA_SIDELINE/get -d'
      {"count":1,"ackmode":"ack_requeue_true","encoding":"auto","truncate":50000}' -o payload.json

=>  The number of the messages was stored into =>(payload.json) file.
=> Where certain details regarding the Queue was found.
```

### PURGE QUEUE
```=> Delete the messages from the DATA_SIDELINE queue using RMQ API/curl

=> curl -i -u raju:raju -XDELETE http://192.168.43.102:15672/api/queues/kanakaraju/DATASIDELINE/contents                    

=> -XDELETE =>(deletes)
=> contents => contents inside the queue.
```

