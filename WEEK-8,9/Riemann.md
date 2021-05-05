# Riemann 

### SETUP RIEMANN ON A VM
```
The idea behind Riemann is to make monitoring and measuring events an easy default.
A Riemann Server and Riemann Client must be installed.
A Riemann Server is instaled on a new Virtual Machine.
```

### CONFIGURATION
```

=> A new Virtual Machine was installed in order to setup a riemann server.
=> The Vm's Ip was as follows => IP(192.168.43.173)

STEP-1 => From the wget command
        => wget https://github.com/riemann/riemann/releases/download/0.3.6/riemann-0.3.6.tar.bz2        // Dowmloading the tar version.
        => tar xvfj riemann-0.3.6.tar.bz2                                                               // Extracting the tar package installed   
        => cd riemann-0.3.6
        => wget https://github.com/riemann/riemann/releases/download/0.3.6/riemann-0.3.6.tar.bz2.md5    // Check the md5sum to verify the tarball
        => md5sum -c riemann-0.3.6.tar.bz2.md5                                                          // Verify the installed tarball version
        => sudo apt-get -y install default-jre ruby-dev build-essential                                 // Install the server Dependencies
        => bin/riemann etc/riemann.config                                                               // Starting the riemann server.
        => gem install riemann-client riemann-tools riemann-dash                                        // Install the Ruby client, utility package, and dashboard       

                                 


STEP-2 => On the Configuration file.
          => In the directory              => cd /riemann-0.3.6/etc
          => Open the configuration file  => nano riemann.config
          => In the line => (let [host "192.168.43.173"]   (Replace this line)

STEP-3 => Start the dashboard
         => riemann-dash
         => Open the desired browser and point to => http://192.168.43.173:4567/                        // Riemann runs on port 4567
```

### SETUP RIEMANN CLIENT
```
=> Riemann clients speak Protocol Buffers over TCP and UDP
=> Riemann Usually supports client Dependencies is various languages. ex C,C++,Java,Perl,Python.
=> Riemann Client Python dependency was installed.
=> The client library aims to provide a simple, minimal API, and does not require direct interaction with protocol buffers
=> This was installed where influxdb was there. (VM-2)
   => pip install riemann-client                                                                            // Installs Riemann-Client
```

### SENDING METRICS TO RIEMANN-SERVER
```
=> From Riemann-Client the metrics were sent to Riemann-Server.
   => For collecting normal system metrics Python Library psutil was installed which would collect normal system metrics.
   => The Script to send the metrics is mentiond below.
```

### SCRIPT TO SEND NORMAL METRICS
```

=> From Riemann client and Riemann server the metrics were being sent.

STEP-1=> the script send.py
       
       =>import psutil as p                                                                                         //import psutil library
        from riemann_client.transport import TCPTransport                                                       
        from riemann_client.client import QueuedClient                                              
        with QueuedClient(TCPTransport("192.168.43.173", 5555)) as client:                                       
                                                                            => The above code The QueuedClient class modifies the event
                                                                             method to add events to a queue instead of immediately sending them

        c = p.cpu_times()
        d = c.user
        client.event(service="CPU_Times", metric_f=d,ttl=120)            // Some of the libraries present in psutil were used such as cpu_times,cpu_count,cpu_stats
                                                                        // cpu_freq and virtual_memory was used. and ttl is set to 120 seconds. where they would be shown for 120 seconds       
                                                                       // where they would be displayed for 120 seconds 
        e = p.cpu_times()
        f = e.idle
        client.event(service="idle", metric_f=f,ttl=120)

        g = p.cpu_times()
        h = g.iowait
        client.event(service="idle", metric_f=h,ttl=120) 

        i = p.cpu_count()
        client.event(service="CPUCount", metric_f=i,ttl=120)

        j = p.cpu_stats()
        k = j.interrupts
        client.event(service="Interrupts", metric_f=k,ttl=120)

        l = p.cpu_stats()
        m = l.syscalls
        client.event(service="Systemcalls", metric_f=m,ttl=120)

        n = p.cpu_freq()
        o = n.current
        client.event(service="Current freq", metric_f=o,ttl=120)

        pp = p.cpu_freq()
        q = pp.min
        client.event(service="Min", metric_f=q,ttl=120)

        r = p.virtual_memory()
        s = r.total
        client.event(service="Total Memory", metric_f=s,ttl=120) 

        t = p.virtual_memory() 
        u = t.available
        client.event(service="available", metric_f=u,ttl=120)

        v = p.virtual_memory()
        w = v.used
        client.event(service="Used", metric_f=w,ttl=120) 


        client.flush()                                                  //flush() method to send the current event queue as a single message




STEP-2 => To run the script 
       =>step 1=> Open 2 terminals for the riemann server.
       =>step 2=> start the riemann server    =>  bin/riemann etc/riemann.config                 // On one of the terminal.
       =>step 3=> start the riemann dashboard =>  riemann-dashboard                              // On the second terminal.


 STEP-3 => Post startingg the dashboard.
        => Open open the browser and point to   => http://192.168.43.173:4567/   
        => The metrics sent will be  existed for 120 seconds.
```

### SCRIPT TO SEND RABBIT-MQ METRICS
```

=> The same steps as above is being executed but different code was used.


 STEP-2 => from the curl request the ouput of the request was downloaded to the payload1.json file and then the data was extracted.
        
        => The curl request seemed as follows 
        =>curl --silent -u raju:raju -X GET http://192.168.43.71:15672/api/overview -o payload1.json 
        => Since the metrices of all th ethings keep changing in order to make them dynamic.
             =>import os
               os.system("sh script.sh") 
        =>     The contents of script.sh had the curl request in it.


-----CODE--------
import json
import os
os.system("sh script.sh")

from riemann_client.transport import TCPTransport
from riemann_client.client import QueuedClient
with QueuedClient(TCPTransport("192.168.43.173", 5555)) as client:


  with open('payload.json') as json_file:                                    // Extracting the data of payload.json_file
    data = json.load(json_file)

  a = data['messages_details']
  client.event(service="message details", metric_f=a,ttl=120)               // It had many key-value pair values like a dictionary.
                                                                            // Certain messages related details were extracted from Json file.            
                                                                            // Such as messages_details,messages_ready_ram,message_bytes_unacknowledged etc
  a = data['messages_ready_ram']
  client.event(service="message_ready_ram", metric_f=a,ttl=120)


  b = data['message_bytes_unacknowledged']
  client.event(service="message_bytes", metric_f=b,ttl=120)

  c = data['message_bytes']
  client.event(service="message_bytes", metric_f=c,ttl=120) 


  client.flush()
  
 ```
 
 ### THE METRICS SHOULD GO TO INFLUXDB FROM RIEMANN
 ```
 
=> To send the riemann metrics to influxdb in the RIEMANN-SERVER VM there was a configuration file

=> In the Config file 
=> Define the following function.
=>
(def influx
(influxdb/influxdb {
    :host "192.168.49.34"                        //IP Of Riemann
    :port "8086                                  // Default port of InfluxDB
    :db "riemann"                                // Name of database  all th emetrics would go to the database riemann from riemann server.               
    :username "raju"                     
    :password "raju"
    :version :0.9}
 ))

=> To send the metrics start the riemann server and then =>bin/riemann etc/riemann.config  
=> and then log into the influxdb database VM and check the metrics being transferred from riemann server
=> The metrices collected on influxDb can be Plotted on grafana dashboard as well.
```
### THRESHOLD LIMIT
```

=>metrics such as disk usage/ram usage should have a threshold (80%) and should send a critical alert to riemann once the threshold is breached.
=> For this task the script was written as follows.

=> Some of the metrics collected by python psutils was considered and tags like warning and critical was issuued based on some values.

=> The python script looked like this.

=>
import psutil as p
from riemann_client.transport import TCPTransport
from riemann_client.client import QueuedClient
with QueuedClient(TCPTransport("192.168.43.173", 5555)) as client:


  c = p.cpu_times()
  warning1 = 0.9
  critical1 = 0.95
  
  c = psutil.cpu_times()
  used = c.user + c.system + c.nice
  total = used + c.idle
  f = used/total                                  // Certain limit was considered and then added based on the metrics generated
  state = "ok"                                    // If condition was taken where "warning" or "critical" would be considered.    
  if f > warning1: state="warning"
  if f > critical1: state="critical" 
  client.event(service="Cpu_times", metric_f=f,ttl=120,state=state) 

 warning2 = 3
  critical2 = 8
  l = os.getloadavg()
  f = psutil.cpu_count()
  f1 = l[2]/f
  state = "ok"
  if f1 > warning2: state="warning"
  if f1 > critical2: state="critical" 
  client.event(service="op_cpu", metric_f=f1,ttl=120,state=state) 
  
  warning3 = 0.85
  critical3 = 0.95
  a = psutil.virtual_memory()
  ff = a.percent / 100.0
  state = "ok"
  if ff > warning3: state="warning"
  if ff > critical3: state="critical"
  client.event(service="virtual mem", metric_f=ff,ttl=120,state=state).
```
  
