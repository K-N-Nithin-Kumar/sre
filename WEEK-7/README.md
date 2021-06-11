RMQ:

* Install and configure 3 node RMQ cluster version 3.7.9

* The RMQ cluster should be on TLS and have a username/password

* Data should be persisted on disk

* Create a vhost and a user with read-write permissions to the vhost

* Create a user with monitoring access.

* Add rabbitmq_management plugins.

## Initial Setup

> RMQ
>For automating scripts 4 new Vm's were created and one Vm was considered as an (Ansible-Control-Machine)
> Ansible was Installed in one Vm

> ANSIBLE INSTALLATION 

```
On one of the Machine called as Ansible Control Machine.
=> Ansible was installed.

=> sudo apt update
=> sudo apt install ansible                                                         // Installs Ansible Software.

=>Post installing ansible software.
=>In the directory /etc/ansible.
=>Two files were present =>ansible.cfg and hosts files were present.

Configuring ansible.cfg file add the following lines                          (applicable for only on Ubuntu -18.04 version only)

[defaults]
ansible_python_interpreter=/usr/bin/python3                                        // Add default python version as python3
```

> SSH CONNECTION
```
 For ansible, we have to communicate between the Ansible Control Machine and the 3 Hosts
 In the Ansible Control Machine 
 execute => ssh-keygen -t rsa

 For vm-1 =>  ssh-copy-id ans22@192.168.1.38 
 For vm-2 =>  ssh-copy-id ans40@192.168.1.49 
 For vm-3 =>  ssh-copy-id ans43@192.168.1.50
```
> cd /etc/ansible/hosts
```
=> In the hosts file add.
=> Add the Neighbour's Vm's IP's where the playbook is used to be implemented.
=> Add  the  groups and name those under the group.

=> In my case it was added under Different groups where the clustering procces can be implemented smoothly.
=>
[all1]
ans22@192.168.1.38                                                                                  // VM-1 Hosts Username and IP group name =[all1]
[all2]
ans40@192.168.1.49                                                                                 // VM-2 Hosts Username and IP group name =[all2]
[all3]
ans43@192.168.1.50                                                                                // VM-3 Hosts Username and IP group name =[all3]
[all4]
ans22@192.168.1.38  
ans40@192.168.1.49  
ans43@192.168.1.50    
```
> Check Connectivity
```
=> On ansible control machine execute the command => ansible -m ping all ( This shows "ping -pong green color )
=> This says the connection is successful.
```



