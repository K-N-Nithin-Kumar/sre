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





STEP-1 => To run the script 
       =>step 1=> Open 2 terminals for the riemann server.
       =>step 2=> start the riemann server    =>  bin/riemann etc/riemann.config                 // On one of the terminal.
       =>step 3=> start the riemann dashboard =>  riemann-dashboard                              // On the second terminal.

STEP-2 => Post startingg the dashboard.
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
                Code in RMQMetric.py



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
