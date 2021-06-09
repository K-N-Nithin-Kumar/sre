## GRE Tunnel
```
*   Create L3 connectivity between all 3 Hosts, Each host will form BGP with its corresponding router and advertise its own loopback ip
    Host 1: 10.10.1.1/32
    Host 2: 10.10.1.2/32
    Host 3: 10.10.1.3/32
```
```
   Verify the ping between each hosts
   - Setup a GRE tunnel between Host 1 and Host 3
   - Set 192.168.100.1/24 on Host 1 tunnel interface
   - Set 192.168.100.2/24 on Host 3 Tunnel interface
   - Test the ping between 192.168.100.1 and 100.2

```


