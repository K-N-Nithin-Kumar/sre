import json
import os
os.system("sh script.sh")

from riemann_client.transport import TCPTransport
from riemann_client.client import QueuedClient
with QueuedClient(TCPTransport("192.168.43.173", 5555)) as client:


  with open('payload.json') as json_file:                             // Extracting the data of payload.json_file
    data = json.load(json_file)

  a = data['messages_details']
  client.event(service="message details", metric_f=a,ttl=120)          // It had many key-value pair values like a dictionary.
                                                                       // Certain messages related details were extracted from Json file.            
                                                                      // Such as messages_details,messages_ready_ram,message_bytes_unacknowledged etc
  a = data['messages_ready_ram']
  client.event(service="message_ready_ram", metric_f=a,ttl=120)


  b = data['message_bytes_unacknowledged']
  client.event(service="message_bytes", metric_f=b,ttl=120)

  c = data['message_bytes']
  client.event(service="message_bytes", metric_f=c,ttl=120) 


  client.flush() 
  
  
  // From the requested curl request the other metrics can also be added which can also be used 
  
  
