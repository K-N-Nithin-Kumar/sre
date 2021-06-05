>BGP with the routers R1,R2,R3 and R4:

* With cumulus VX. 

  * The Same Ip's which was given in the topology from Week-3 was set and the configuration was like this.
  
       Host | adapter | IP
       :--: | :--: | :--:
       R1 | `enp0s3` | `172.10.0.2/30`
       R2 | `enp0s3` | `172.10.0.6/30`
       R3 | `enp0s3` | `172.10.0.10/30`
       R4 | `enp0s3`<br>`enp0s8`<br>`enp0s9` | `172.10.0.1/30` <br> `172.10.0.5/30`<br>`172.10.0.9/30`
     

1. All the routers were of Cumulus Vx type 
2. frr software for BGP Implementation was installed already.

3. R4 being the router will be formed BGP with R1,R2,R3,R4 
    
     * In the router (R-4)
     * In the Configuration file `/etc/frr/daemons` enable `bgpd` services 
         * vtysh
         * configure terminal
            * R4(config)# router bgp 10
            * R4(config-router)# neighbor 172.10.0.2 remote-as 1
            * R4(config-router)# neighbor 172.10.0.6 remote-as 2
            * R4(config-router)# neighbor 172.10.0.10 remote-as 3
            * R4(config-router)# address-family ipv4
            * R4(config-router-af)# neighbor 172.10.0.2 activate
            * R4(config-router-af)# neighbor 172.10.0.6 activate
            * R4(config-router-af)# neighbor 172.10.0.10 activate
            * R4(config-router-af)# exit
            * R4(config-router)# neighbor 172.10.0.2 prefix-list ROUTE in
            * R4(config-router)# neighbor 172.10.0.2 prefix-list ROUTE out
            * R4(config-router)# neighbor 172.10.0.6 prefix-list ROUTE in
            * R4(config-router)# neighbor 172.10.0.6 prefix-list ROUTE out
            * R4(config-router)# neighbor 172.10.0.10 prefix-list ROUTE in
            * R4(config-router)# neighbor 172.10.0.10 prefix-list ROUTE out
  
  * On other router VMs (`R1`,`R2`,`R3`):
     ```  
           *   R1# conf
           *   R1(config)# router bgp 1
           *   R1(config-router)# neighbor 172.10.0.1 remote-as 100
           *   R1(config-router)# address-family ipv4
           *   R1(config-router-af)# neighbor 172.10.0.1 activate
           *   R1(config-router-af)# exit
           *   R1(config-router)# exit
           *   R1(config)# ip prefix-list ROUTE permit any
           *   R1(config)# router bgp 1
           *   R1(config-router)# neighbor 172.10.0.1 prefix-list ROUTE in
           *   R1(config-router)# neighbor 172.10.0.1 prefix-list ROUTE out
  
     ```
     
     * On other router VMs (`R2`):
     ```
           *   R2# conf
           *   R2(config)# router bgp 2
           *   R2(config-router)# neighbor 172.10.0.5 remote-as 100
           *   R2(config-router)# address-family ipv4
           *   R2(config-router-af)# neighbor 172.10.0.5 activate
           *   R2(config-router-af)# exit
           *   R2(config-router)# exit
           *   R2(config)# ip prefix-list ROUTE permit any
           *   R2(config)# router bgp 2
           *   R2(config-router)# neighbor 172.10.0.5 prefix-list ROUTE in
           *   R2(config-router)# neighbor 172.10.0.5 prefix-list ROUTE out 
     ```
     
      * On other router VMs (`R3`):
     ```
           *   R3# conf
           *   R3(config)# router bgp 3
           *   R3(config-router)# neighbor 172.10.9.remote-as 100
           *   R3(config-router)# address-family ipv4
           *   R3(config-router-af)# neighbor 172.10.0.9 activate
           *   R3(config-router-af)# exit
           *   R3(config-router)# exit
           *   R3(config)# ip prefix-list ROUTE permit any
           *   R3(config)# router bgp 3
           *   R3(config-router)# neighbor 172.10.0.9 prefix-list ROUTE in
           *   R3(config-router)# neighbor 172.10.0.9 prefix-list ROUTE out 
     ```   
     
          
    * Cumulus VX
    * NCLU Commands can also be added
        * On `R4`,
         ```
           $ net add bgp autonomous-system 10
           $ net add bgp neighbor 172.10.0.2remote-as 1
           $ net add bgp neighbor 172.10.0.6remote-as 2
           $ net add bgp neighbor 172.10.0.10 remote-as 3
           $ net pending
           $ net commit

     * Check the connectivity using `ping` and verify using `sh ip bgp summary` 


        
    
