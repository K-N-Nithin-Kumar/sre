# BGP SETUP 

Task -4 and Task -6 required BGP Setup so integrated the Vm's created in Task-4 and Task-6

```

=>Consider 4 Virtuals machines which adapaters like bridged and one Internal Network.
=> A topology was given (Filename = Topology)

=> Created 4 vm's
=> Installed FRR Software for BGP Implementation
=> Enabled BGP =Yes (in ((/etc/frr/daemons)
=> Enabled IPV4 Forwarding  etc/sysctl.conf file
=> Assigned IP addresses in the /etc/netplan/00-config.yaml file

=> One VM acted as a Router.
=>
vm-router : Interfaces :
              lo - 10.1.1.1/32              //Loopback IP
              enp0s3 - 172.10.0.1/30        // Interface with VM-1  (Internal adapter)
              enp0s8 - 172.10.0.5/30        // Interface with VM-2   (Internal adapter)
              enp0s9 - 172.10.0.9/30        // Interface with VM-3   (Internal adapter)


=> The Second Vm
=> Interfaces :lo - 10.1.1.2/32            //Loopback IP
                 enp0s3 - 172.10.0.2/30     //Interface IP  (Internal adapter)


=>The Third Vm
=>Interfaces : lo - 10.1.1.3/32              //Loopback IP
               enp0s3 - 172.10.0.6/30         //Interface IP  (Internal adapter)


=>The Fourth Vm
=> Interfaces :lo - 10.1.1.4/32              //Loopback IP  
               enp0s3 - 172.10.0.10/30       //Interface IP  (Internal adapter)
```

Router VM

```
=> Go to vtysh->configure terminal -> adding
=> (config)#router bgp 10                                          //AS Number =10
            (config-router)#neighbor 172.10.0.2 remote-as 1         //AS Number =1
            (config-router)#neighbor 172.10.0.6 remote-as 2         //AS Number =2
            (config-router)#neighbor 172.10.0.10 remote-as 3         //AS Number =3     // External AS system is implemented
            (config-router-af)#neighbor 172.10.0.2 activate
            (config-router-af)#neighbor 172.10.0.6 activate
            (config-router-af)#neighbor 172.10.0.10 activate
```

The Second Vm

```
=>=> Go to vtysh->configure terminal -> adding
=>   (config)#router bgp 1
    (config-router)#neighbor 172.10.0.1 remote-as 10
    (config-router-af)#neighbor 172.10.0.1 activate

```
The Third Vm

```=>Go to vtysh->configure terminal -> adding
=> (config)#router bgp 2
   (config-router)#neighbor 172.10.0.5 remote-as 10
    (config-router-af)#neighbor 172.10.0.5 activate
```
The Fouth VM

```
=> The Fourth Vm
=> (config)#router bgp 3
   (config-router)#neighbor 172.10.0.9 remote-as 10
    (config-router-af)#neighbor 172.10.0.9 activate
```

```
=> To check (sh ip bgp summary) => Shows the BGP summary 
=> Basic BGP level is setup
```

BGP FILTERS 
- vm-router orginates and sends default route to vm-1 , vm-3 and vm-4  (VM-2 router)
```
=> The each Vm's Ip's is added as default originate.
=>     (config)#router bgp 10
       (config-router-af)#neighbor 172.10.0.2 default-originate
       (config-router-af)#neighbor 172.10.0.6 default-originate
       (config-router-af)#neighbor 172.10.0.10 default-originate
```
Each of the vms ( vm1, 2, 3 ) will accept only default route from its bgp peer ( vm-router)
and advertise their own loopback(IP on its lo interface ) to vm-router.

```
=> IP Prefix List is used for this purpose.
=> In all vm's used IP Prefixx list as OUT and In
=>
(config)#ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0      // This can be replaced b Vm's IP address
=>  (config-router)#network 10.1.1.2/32     // in vm-1      // Advertised it's own loopback ip's in all the Vm's as same

=> The same thing was done is all the VM's

```
vm-router to accept /32 IPs that belong to subnet (10.1.1.0/24) and reject all other routes

```
=> Here prefix lift is used.
=> (config)#ip prefix-list DEFAULT seq 10 permit 10.1.1.0/24 le 32
   (config)#ip prefix-list DEFAULT seq 5 deny any
=>  (config-router)#neighbor 172.10.0.2 prefix-list DEFAULT in
    (config-router)#neighbor 172.10.0.2 prefix-list DEFAULT in
    (config-router)#neighbor 172.10.0.2 prefix-list DEFAULT in
    
    // In router VM

```

    
    
    
            
