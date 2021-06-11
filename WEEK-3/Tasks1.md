# NETWORKING

> TASK-1

*For this particular task. 
*NAT-ADAPTER was added where the desired subnet of Ip's was given
* Preferably to add the NAT ADAPTER of desired Subnet.
* The steps followed are mentioned below.
* Open Vbox -> Tools -> Preference -> network -> Add a NAT network (new one by clicking the first icon which indicates as +)
* After that provide the necessary details the IP address range => in my case it was provided as (192.168.1.0/24)  =>(it will assign the values of Ip in the range)
* Example => 192.168.1.4, 192.168.1.6 .... and so on.

> Post adding the NAT NETWORK create new two fresh Vm's.

* The Vm's in my case was => (Vm-1 Server)   (Vm-2 Client)
* While configuring the VM. Consider (Vm-1 Server)  Add the NAT-ADAPTER which was created in the before step in the network settings.
* (Vm-1 Server -> settings -> network -> Add NAT-NETWORK)
*(Vm-2  Client -> settings -> network -> Add NAT-network)
```
The network CIDR was in the range 192.168.1.0/24 => So, the IP of Vm-1 Server is => 192.168.1.4
                                                 =>IP of Vm-2 Client is => 192.168.1.5
 ```
``` 
On the VM server => check for the IP address using => ip a command
                                                   => (192.168.1.4)  
```
```
On the VM Client => check for the IP address using => ip a command
                                                   => (192.168.1.5)
```


* To check if the connection is established and they are pinging each other =>
* In the server Vm => ping 192.168.1.5 (Vm-2 Client's IP address)
* In the client Vm => ping 192.168.1.4 (Vm-1 Server's IP address)
* If sucessfull they should be able to transfer data packets to and fro with 0% packet loss.
* Sucessful connection was established because they were in the NAT-NETWORK State and were able to ping each other. (STATICTALLY Routing was done)


## TASK-2

* For this particular task.
* 3 New Vm's was Initialized where'in they were named as (CLIENT) (ROUTER) (SERVER)
* While initializing the Vm's the INTERNAL NETWORK WAS IMPLEMENTED (STATIC Routing)
* The underlying structure would be as follows.
* CLIENT -> (neta) -> ROUTER -> (netb) -> SERVER
* (neta) and (netb) are the internal adapters which was added.
```
Client communicates with the router via (neta) internal adapter.
Router communicates with the server via (netb) internal adapter.
Router has two interface adapters i.e (neta) and (netb)
```
* The IP adresses for all the Vm's was assigned and configured via `netplan configuration`.

> CLIENT
```
=> In the client Vm =>
                    => network:
                        version: 2
                            ethernets:
                                enp0s8:             #interface with neta internal network
                                    dhcp4: no
                                    addresses:
                                     - 192.168.10.4/24          # Providing IP address
                                    gateway4: 192.168.10.1      # Providing gateway -> to-> via
                                    routes:
                                    - to: 192.168.20.0/24
                                    via: 192.168.10.5
                                    metric: 100
```
> this is done at => sudo nano /etc/netplan/00-config.yaml (client)

> ROUTER
```
=>In the Router Vm =>
                   => network:
        version: 2
        ethernets:
            enp0s3:             #interface with neta internal network
                dhcp4: no
                addresses:
                    - 192.168.10.5/24
                gateway4: 192.168.10.1
                routes:
                    - to: 192.168.10.0/24
                      via: 192.168.20.1
                      metric: 100
            enp0s8:             #interface with netb internal network
                dhcp4: no
                addresses:
                    - 192.168.20.5/24
                gateway4: 192.168.20.1
                routes:
                    - to: 192.168.20.0/24
                      via: 192.168.10.1
                      metric: 100

```

> this is done at => sudo nano /etc/netplan/00-config.yaml (router)

> SERVER

```

=>In the Server Vm =>
                    =>network:
        version: 2
        ethernets:
            enp0s8:             #interface with netb internal network
                dhcp4: no
                addresses:
                    - 192.168.20.4/24
                gateway4: 192.168.20.1
                routes:
                    - to: 192.168.10.0/24
                      via: 192.168.20.5
                      metric: 100

this is done at => sudo nano /etc/netplan/00-config.yaml (Server)
```

> TESTING THE CONNECTIVITY
```

=>Post adding these all netplan configurations in all the 3 Vm's 
   => sudo netplan try    ( This shows weather there is some error or some indentation error in netplan configuration file)
   => sudo netplan apply   ( This reverts the changes done in the netplan file)
   => sudo reboot          ( The reflect the changes done in netpaln configuration and assigning Ip's via netplan configuration has been reflected) 


   => Do this on all the 3 Vm's ie CLIENT, ROUTER, SERVER


=>Post rebooting the Vm's.
=> the IP assigned will be as follows
=> Client => adapter  (neta) Internal =>> 192.168.10.4/24  
=> Server => adapter  (netb) Internal =>> 192.168.20.4/24 
=>Router => adapter  (neta) Internal =>> 192.168.10.5/24  
=>Client => adapter  (neta) Internal =>> 192.168.20.5/24       (The IP assigned in the netplan file can we of the user choice)


=> Now try to ping 
=> In client Vm => ping 192.168.10.5/24 
=> In router Vm => ping 192.168.10.4/24
=> In router Vm => ping 192.168.20.4/24
=> In Server Vm => ping 192.168.20.5/24

=> Preferably these Vm's should be supposed to Ping each other with (0% packet loss)
```

##TASK-3

* Port Forwarding can be done via Multiple ways.
* Using UI Interface
* Select Vm => Go to Network Settings => Click on Adapters => Advanced => Port Forwarding => Mention the IP's and Port
* Or By using IPTABLE-PRECEED (tool)
* Install IPtables tool if not available.
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 2222 -j DNAT --to-destination 192.168.20.4:22
```
* This setup is done on the router VM. 
```
This forwards all the requests coming to the router port number 2222 and forwards to the server (Vm') port 22
```
```
sudo iptables -A FORWARD -p tcp -d 192.168.2.2 --dport 22 -j ACCEPT (accept request)
```
```
Post doing this =>  sudo nano /etc/iptables/rules.v4
                    sudo iptables-save > /etc/iptables/rules.v4
 To save the changes made and make it persistent.

```
