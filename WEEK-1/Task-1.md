# WEEK-1

## Task-1
* Install VBOX on your Laptop
> Steps of installing VBOX is as follows.
* Oracle VM box is a virtual machine which is uses to create multiple operating systems in the same machine using the concept of virtualization.
    * Open your browser of desired choice and type Vbox in the search bar. 
    * Open the first link available.
    * Click on the Download VirtualBox option and the versions next to that will also we obtained. 
    * In the VirtualBox package manager click on OS X hosts (For Mac)
    * Your Virtual Box will be installed after that
    * While Installing it asks as system extension blocked. Give system permission as 
    * We have to do some configuration to our Mac OS. ( settings->security and privacy->the particular installation will be blocked(allow access)
       Come back to Vbox installer ->click on VirtualBox.pkg->install-> installation was successful.

## Task-2
* Download Ubuntu Focal ISO
   * Ubuntu 20.04 LTS using GNOME 3.36 as default desktop environment.
   * Some of the features of Ubuntu Focal Fossa are as follows.
   * Latest Linux Kernel.
   * Improved ZFS Support.
   * Ubuntu focal fossa will be supported with security and software updates for 5 years.
   * Steps Includes -> Open browser-> type ubuntu Focal Fossa 20.04->Click on Server side image (which does not contain GUI properties)
   * so, the ISO file of the ubuntu Operating system is installed.
   * Install the Ubuntu OS by extracting it.


## Task-3
* Install Ubuntu Focal ISO (give 2 CPU Cores and 512MB of RAM)
    * This steps involves in creating a new Virtual machine.
    * To create a Virtual Machine the steps would be followed as
    * (Click on Vbox -> Click on New -> Name the VM name and the type (type = Linux,Version= Ubuntu64-bit) -> Continue .
    * Select Memory size as (512 MB) ->Continue-> Checkbox option as create Virtual  hard disk now->create.
    * To give 2 CPU Cores(Click on Created VM -> Settings -> System -> Processor -> Select as (2) Cpu’s-> Ok.

## Task-4.
* Create the users who are part of the group
```
-> To create a particular user in the Linux.
-> The steps are as follows.
->Login as the rot user first and add login id and Password credentials.
-> after adding the valid credentials you will be logged in to the system.
-> To Add Users.
 Command Used ->( sudo adduser raju)
              -> asks for Password and other credentials 
              -> The other members were created by this way.
              ->( sudo adduser chayank)
              ->( sudo adduser Mehul)
 	     -> ( sudo adduser Risteesh)
              -> ( sudo adduser  Kiran)
              ->( sudo adduser Neha)
 -> To view the list of users created -> (cat /etc/passwd) gives the details ofuser created.
                
	        -> To create the group 
                -> Command -> (sudo groupadd intern) (name=intern)
                -> to add members to the group 
                -> sudo usermod -a -G intern raju
                -> intern = Name of the group.
                -> raju = name of the member.
                -> -a =  Indicates us that we are appending.
                ->-G = Indicates us that group name that we are appending the user
                   (-G group name)
	     -> to list the group details (grep intern /etc/group)
```

## Task -5
* Add two disks of 10GB each to this VM create a LVM using these two disks and Create XFS file system on it
* Mount this on /data directory and make sure that mount persists on the across the reboots.

> To add 2 new disk to the the steps are as follows
* Click on the created Vm -> Settings-> Storage-> Controller: SATA->hard disk->create-> asks for the type of hard disk to be created (VDI-VirtualBox Disk Image) should be chosen->Continue->Dynamically allocated->select size and name-> Create.
* To check the partition/name of the disk create.
    Command -> (sudo lvmdiskscan)
* Suppose the disks are /dev/sdb and /dev/sdc
* to know the details 
* fdisk -l /dev/sdb   and  fdisk -l /dev/sdc
* details of the particular disks will be obtained.
*  To do anything on the disk the mode should be in root user mode So command -> (sudo su).

* LVM (Logical Volume Manager) ->In Linux, Logical Volume Manager is a device mapper framework that provides logical volume management for the Linux kernel. 
* Most modern Linux distributions are LVM-aware to the point of being able to have their root file systems on a logical volume.
* It’s used in taking the secondary hard drive and add it to the main disk using LVM.

* LVM Contains -> Physical Volume -> Volume groups->Logical Volumes.
* Logical Volumes contains the partitions.
```
Steps followed are 
-> Create a physical Volume. (pvcreate /dev/sdb  and pvcreate /dev/sdc)
-> To display the physical volume created (pvs or pvdisplay)
-> Create  volume groups and add the physical volumes created.
-> vgcreate (name of the volume) /dev/sdb /dev/sdc
-> vgcreate vol1 /dev/sdb /dev/sdc
-> To display the volume group.
-> vgdisplay /dev/vol1 (name of the volume group created previously)
```
```
-> Create Logical Volumes.
-> lvcreate -n (name of lv-group) —size (Desired size) (volume group)
->(lvcreate -n lv1 —size 19.9G vol1) 
-> Creating the XFS File system.
-> mkfs.xfs -f/dev/vol1/lv1.
->.xfs -> Indicates it is a xfs file system.
-> -f  -> file system created.
-> /dev/(volume group)/(logical volume)
```
```
-> Creating the Directory to mount file.
-> mkdir /data
-> mount /dev/vol1/lv1 /data
-> df -hT /data
-> The directory /data
->  mounting /dev/vol1/lv1   (to)  /data
-> df -hT /data -> To display the mounted data file in the directory)
```
 
