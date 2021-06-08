## EVPN-VXLAN
  
  * The first step would be establishing the BGP Connection between R1, R2, R3 with R4.
     
     *  After establishing the BGP between R1, R2, R3, & R4, we need to setup loopback interfaces for all leaves to enable VTEP and activate neighbors through `evpn` address family
  
     * On `R1`
       ```
        $ net add loopback lo ip add 1.1.1.1/32
        $ net add bgp l2vpn evpn neighbor 172.10.0.1 activate
        $ net commit
      ```
      
   * On `R2`
     ```
        $ net add loopback lo ip add 1.1.1.1/32
        $ net add bgp l2vpn evpn neighbor 172.10.0.5 activate
        $ net commit
     ```
   * On `R3`
     ```
        $ net add loopback lo ip add 1.1.1.1/32
        $ net add bgp l2vpn evpn neighbor 172.10.0.9 activate
        $ net commit
     ```   
 
 * On `R4`
    ```
       $ net add loopback lo ip add 100.0.0.100/32
      $ net add bgp l2vpn evpn neighbor 172.10.0.2 activate
      $ net add bgp l2vpn evpn neighbor 172.10.0.6 activate
      $ net add bgp l2vpn evpn neighbor 172.10.0.10 activate
      $ net commit
    ```
  * Verify the configurations on spine using
    ```
    $ net show bgp l2vpn evpn summary
    ```
    
  * We need to advertise loopback IPs, each leaf node advertises its own lo IP
    ```
    $ net add bgp network 1.1.1.1/32. ,2.2.2.2/32 & 3.3.3.3/32
    $ net commit
    ```
   * Now, each leaf would be aware of other leaf's loopback IP, check using
    ```
     $ net show bgp ipv4 unicast
    ```
    and verify the connection using `ping` between loopback IPs using `-I` option,
    $ ping 2.2.2.2 -I 1.1.1.1       #from R1's lo to R2's lo
    ```
  * So, we have the complete underlay setup, now we need the overlay for creating the required tunnel and learning the addresses using Control-pane learning method (BUM traffic not handled). So now, we have to create a VNID using a VLAN number and create a virtual interface for VTEP.

    ```
  * Create a new virtual interface `vni10`, and associate it with VNID `10` & add VLAN `10` to `vni10`. On all leaf nodes,
    ```
    $ net add vxlan vni10 vxlan id 10
    $ net add vxlan vni10 bridge access 10
    $ net add vxlan vni10 bridge learning off
    $ net add bgp evpn advertise-all-vni          #to provision all locally configured VNIs to be advertised by the BGP control plane      
   ```

*    now we need to specify the loopback IP for making it as the source tunnel ip
   ```
    net add vxlan vni10 vxlan local-tunnelip 1.1.1.1  
    net add vxlan vni10 vxlan local-tunnelip 2.2.2.2 
    net add vxlan vni10 vxlan local-tunnelip 3.3.3.3
   ```
   
* Now, check the macs available per leaf node
 
 ```
 net show bridge macs vlan 10
 ```
You should be seeing no nodes, or only one i.e the current leaf node's mac. For making vni to learn hosts mac addresses,
we need to restart all hosts `H1`, `H2`, & `H3`, one by one. This forces a GARP to be sent out when each host comes up and this GARP causes hosts'
mac to be learnt on swp2 of each leaf node.
$ net show bridge macs
```

Test the connectvity between the hosts `H1` , `H2` and `H3` using `ping` commands..







    
    
   
    
    
  
   
      
