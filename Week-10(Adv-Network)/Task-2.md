## GRE Tunnel
```
  Generic routing Encapsulation (GRE) ia a type of tunnel that can encapsulate multiplevlayer 3 protocols.
```

* To setup GRE-Tunnel the first step was to add the loopback Ip's to the respective hosts i.e `Host 1: 10.10.1.1/32`
                                                                                              `Host 2: 10.10.1.2/32`
                                                                                              `Host 3: 10.10.1.3/32`


* The tunnel is setup between `Host 1` and `Host 2`


* For setting up a GRE tunnel on Linux you must have `ip_gre` module loaded in your kernel. To make sure that's present execute
```
sudo modprobe ip_gre
lsmod | grep gre
```

* To forward all the traffic in and out of the GRE tunnel we're going to use iptables and iproute2.
```
sudo apt install iptables iproute2
```
* To enable `ipv4` forwarding
```
sudo echo 'net.ipv4.ip_forward=1' >> /etc/sysctl.conf
sudo sysctl -p
```

* STEP-1

```
setup tunnel from H1 end

sudo ip tunnel add gre1 mode gre local 10.10.1.1 remote 10.10.1.3 ttl 255   // l/o interfaces of H1 and H2
sudo ip addr add 192.168.100.1/24 dev gre1                                  // Add the tunnel interface from H1
sudo ip link set gre1 up                                                    // Name is gre1 and is up

```

* STEP-2

```
sudo ip tunnel add gre1 mode gre local 10.10.1.3 remote 10.10.1.1 ttl 255.   // l/o interfaces of H2 and H1  
sudo ip addr add 192.168.100.2/24 dev gre1                                   // Add the tunnel interface from H2
sudo ip link set gre1 up                                                     // Name is gre1 and is up

```


* STEP-3

```
Test ping connection
On Host 1 do: ping 192.168.100.2
On Host 2 do: ping 192.168.100.1
```

* Check the connectivity the `packet loss` should be preferably  `0%`
