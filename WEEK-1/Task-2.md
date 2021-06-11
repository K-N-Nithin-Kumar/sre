## Task -6 
* Add another 10GB disk to the Vm and add it to existing LVM


*  Adding another 10GB disk.
*  Click on the created Vm -> Settings-> Storage-> Controller: SATA->hard disk->create-> 
   asks for the type of hard disk to be created (VDI-VirtualBox Disk Image) 
   should be chosen->Continue->Dynamically allocated->select size and name-> Create.

* After adding the external disk we have to follow certain sets of commands
* check the name of disks which was created (In my case it was /dev/sdc)
* Create physical Volume by using pvcreate /dev/sdc
* The physical volumes were already created and we are adding extra 10GB disk size.
* So, use command (vgextend vol1/dev/sdc). vol1= Name of the volume group 
* To display the details of the volume groups use (vgdisplay vol1

 * Note Copy down the (FreePe) Value. Ex -> FreePe : 2582
         * extend the logical volume. (Lvextend -l -t 2582 /dev/vol1/lv1)
         * The above command is used for resizing and adding the creating disk into the logicalVolume. 


## SUBTASK  ->(Should be done for task 5 and task 6)- To mount logical Volume permanently.				   

 * blkid -> This command is used to obtain the block devices and the type of content a block device holds, the attributes from the content metadata.
 * sudo blkid /dev/vol1/lv1.  (Vol1 -> volume group, lv1 ->Logical Volume)
 *  Copy the UUID ( Universally unique identifier) 
 * in my case UUID= 637476f4-3fc5-4775-b477-3527f65f9bf0.
 * In the  `etc/fstab file`.
 * Open /etc/fstab file.
 * vi or nano editor can be used. 
 *  vi `/etc/fstab`.
 * Traverse to the last and type. 
```
-> (UUID=637476f4-3fc5-4775-b477-3527f65f9bf0 /data xfs defaults 0 0.)
-> sudo mount -a  (or) sudo mount /data
-> mount = instructs the Operating system that the file is read to use.
-> reboot to check if the mount persists.

```

## Task - 7
* Run a HTTP server on the Vm and make sure that the server starts automatically when the system starts

```
-> HTTP Server ->  A HTTP or a web server processes requests via HTTP
                   A network protocol used to exchange information on the World Wide Web(WWW). 
                   The main Function of a HTTP server is to store, process and deliver webpages to clients.
```
> Firstly, in the created VM click on -> Settings->Network-> Change ->(Attached to Nat to Bridged adapter).

		
* Open Terminal and install apache server 
* sudo apt update ( To check for any updates)
* sudo apt install apache2 (To install apache webserver)
* sudo systemctl start apache2 (To start apace webserver)
* sudo systemctl enable apache2 ( To start on system reboot) 
* sudo systemctl status apache2 ( To check the status of apache webserver)
*  sudo systemctl stop apache2(To stop apache2)
* sudo systemctl restrart apache2(To start apache2)
* To check the IP address of the system
* (ip addr show) ->shows the IP address.
* Go to the browser and paste the IP address found -> if it loads then it’s working properly.


## Task- 8
> Mount /var/log on a separate mount point

```
*  The /var/log can be mounted onto the separate disk when there is no space on the root directory or the disk. 
   Sometime the root directory gets filled and then mount /var/log onto the different directory.
    /var, the case has the advantage of isolating applications filling the root from Interfering from /var, 
    but this increases the chances that a filesystem will fill
```   

* So, by filling the root directory would also cause a kernel panic. 
* The steps followed are as follows.
* Add the additional disk for 10GB.
* To add the disks the steps to be followed as
* Click on the created Vm -> Settings-> Storage-> Controller: 
* SATA->hard disk->create-> asks for the type of hard disk to be created (VDI-VirtualBox Disk Image) 
* should be chosen->Continue->Dynamically 	  allocated->select size and name-> Create.
    	
* The /var/log can be moved by adding the external disks and directly copying as well.
* This method is performed using the concept of creating the logical group ->creating  the directory-> go to the single user mode -> perform mount.
* The steps and commands are as follows.


```
-> Using LVM create the logical values group.
-> Create a physical Volume. (pvcreate /dev/sdc (the external disk created))
-> To display the physical volume created (pvs or pvdisplay)
-> Create  volume groups and add the physical volumes created.
-> vgcreate (name of the volume) /dev/sdb /dev/sdc
-> vgcreate vol1 /dev/sdb /dev/sdc
-> To display the volume group.
-> vgdisplay /dev/vol1 (name of the volume group created previously)  
-> Create Logical Volumes.
-> lvcreate -n (name of lv-group) —size (Desired size) (volume group)
->(lvcreate -n lv1 —size 19.9G vol1) 
```

```
-> Mount = create a directory -> mkdir /mnt/temp_vol (mnt = directory and temp_vol = file inside the directory)  
-> Create ext4 file system only . (/var/log files are of type ext type)
-> mkfs -t ext4 /dev/vol1/lv1.    
    Vol1->volume group and lv1->logical volume.
```
```
		 
->  mount -t ext4 /dev/vol1/lv1 /mnt/temp_vol/
-> to view the details or the contents of the file (ls-la /mnt/temp_vol/)
-> Go To single user mode to  move the contents.
-> init 1
```
```                 
( mv /var/log/* /mnt/temp_vol).
 Var/log -> /temp/vol. (*)-> Everything 
```

```
-> To view the contents.
-> ls -l /var/log (Will show total=0)
->  View the contents of the /mnt/temp_vol.-> Umount -> logically detaching a filesystem from the currently accessible filesystem.
-> umount /mnt/temp_vol.
-> df -H (details of the disk)
-> It should be mounted the /var/log
->Edit etc/fstab file.
->the fstab can be edited as.
-> (echo /dev/vol1/lv1 /var/log ext4 defaults 0 0 >> /etc/fstab.)
->  df -H it shows that it’s mounted.
```
## Task- 9 
> The users in the group interns should web able to login via a private key, and not a password.

```
-> This concept uses the SSH encryption where the public key and private key will be available for the users.
-> The SSH->  Means Secure Shell. Where the protocol is created where the operating network services securely over an unsecured network.
-> The normal User id and password a particular user logs in the Password might be weak one or the Password can be hacked using various means.
-> The SSH provides 2 keys the public keys and the Private keys  which can be used to authenticate the server.
```

```
-> Creating 2 Virtual Machine’s which acts as a Server and Client.
-> In the Server Side the commands followed are as follows.
->The prerequisite is that the SSH server should be installed.
->It can be installed when we are in the creating phase of the new Vm where It asks to Install SSH.
-> Or use command (sudo apt-get install SSH
-> To check the status (sudo systemctl status SSH)
```

## IN THE SERVER SIDE. (Vm-1)
```
-> create a user new user (sudo adduser name)
-> Copy the particular IP- Address of the machine( copy and keep)
         
 IN THE CLIENT SIDE. (Vm-2)
-> Generate a Public and private key at the client side.
-> using (ssh -keygen).
-> The key generated can be of SHA-256 or RSA Type.
 			   
-> Send the Public key -> (file ~/ssh/id_rsa)	 		   
->example -> username =raju.
-> ssh raju@ipaddress.
-> copy the keys.
-> ssh -copy -id @raju(ipaddress).        
-> server IP address 192.168.10.65
-> change the configuration file at server	      	I

```

 ## IN THE SERVER SIDE. (Vm-1)
```
-> sudo name /etc/ssh/sshd_config file.
-> Change the settings in the file as
-> Password Authentication as (NO)		
-> When the user logs in for the first time it asks for password 
-> After that it’s directly logs in the user.

login via private key instead of password-(VM-2)

Change a user’s password
   ->sudo passwd username

switch to a user
 ->su -l username

run a command as a user: 
 ->sudo -u user command
```


IN THE CLIENT SIDE (VM-2)

```
cat .ssh/id_rsa.pub
To check if port 22 is active  ->sudo lsof -i -P -n | grep LISTEN
```


