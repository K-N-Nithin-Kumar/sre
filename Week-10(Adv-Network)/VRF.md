## VRF 

```
All 3 Hosts will form BGP with its corresponding Routers
Host 1 and Host 2 will belong to VRF1
Host 3 will belong to VRF 2

Test case: ( Hosts within the same vrf will be able to ping each other )

Host 1 will be able to ping the loopback IP of Host 2 and vice versa
Host 3 will not be reachable from host 1 and host 2

Move host 2 to VRF 2, and repeat the tests
```

> Before setting up the VRF we have to make sure that the respective `HOSTS` will be able to reach each other using `loopback IP's`

```
The respective loopback Ip's
> HOST-1 IP -> 10.10.1.1/32
> HOST-2 IP -> 10.10.1.2/32
> HOST-3 IP -> 10.10.1.3/32

```

> In the main Router `R4`
> Add `VRF` Interfaces 

## Host 1 and Host 2 will belong to VRF1 & Host 3 will belong to VRF 2

```
      $ net add vrf VRF1 vrf-table auto 
      $ net add vrf VRF2 vrf-table auto
      $ net commit
```

## Adding Interface for `VRF'S`

```
        $ net add interface swp1 vrf VRF1
        $ net add interface swp2 vrf VRF1
        $ net commit
```

## Adding Interface `HOST-3` for VRF

```
        $ net add interface swp3 vrf VRF2
        $ net commit
```

## Show VRF's list:
```
      $ net show vrf list
 ```

## Remove Existing VRF Configuration

```
      $ net del bgp autonomous-system 10
      $ net commit
      
```      

## Add BGP in `VRF-1` Configuration

```
        $ net add bgp vrf VRF1 autonomous-system 2
        $ net add bgp vrf VRF1 neighbor 172.10.0.2 remote-as 1
        $ net add bgp vrf VRF1 neighbor 172.10.0.6 remote-as 2
        $ net add bgp vrf VRF1 ipv4 unicast network 10.10.1.14/32
        $ net commit
```
## Add BGP in `VRF-2` Configuration

```
        $ net add bgp vrf VRF2 autonomous-system 3
        $ net add bgp vrf VRF2 neighbor 172.10.0.10 remote-as 3
        $ net add bgp vrf VRF2 ipv4 unicast network 10.10.1.14/32
        $ net commit
```        

## Try to ping `between the hosts`

> `HOST1` & `HOST2` are able to ping each other

      
