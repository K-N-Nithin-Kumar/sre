* Task-1
   > Mesos master, Marathon, and Zookeeper on VM1 
    
   #### For this on VM-1 Mesos, Marathon and Zookeper was Installed and Configured.
    
    * INSTALL MESOS
       * Install Enviromental Dependencies.
        ```
      sudo apt-get -y install build-essential python3-dev python3-six python3-virtualenv 
      libcurl4-nss-dev libsasl2-dev libsasl2-modules maven libapr1-dev libsvn-dev zlib1g-dev iputils-ping
      
      STEP 2: sudo apt-get install libcurl4-openssl-dev
      STEP 3: sudo dpkg -i mesos-1.9.0-0.1.20200901105608.deb   (The deb package was provided)
      STEP 4: apt-cache policy mesos 
      ```
        * INSTALL ZOOKEEPER
        ```
        STEP 1: apt-cache policy zookeeper
        STEP 2: sudo apt-get install zookeeper
        ```
        
        * INSTALL MARATHON
         ```
         STEP 1: setup deb repository 
         sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF
         DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]')
         CODENAME=xenial
         
         STEP 2: Add repository 
         echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" | sudo tee /etc/apt/sources.list.d/mesosphere.list
         sudo apt-get -y update

         STEP 3: check version and install
         apt-cache policy marathon
         sudo apt-get install marathon
         ```
         * SETUP CLUSTERS
          
            In the file `sudo nano /etc/mesos/zk`  
          ```
            replace localhost with IP address of our mesos master servers
            zk://192.168.43.154:2181/mesos 
          ```
         * ON MASTER SERVERS
         ```
          STEP 2: Give each master server a unique id from 1 to 255  
          sudo nano /etc/zookeeper/conf/myid
          `1`
          

         ```   
     * STEP 3: specify all zookeeper server in the following file
         
        ```
          sudo nano /etc/zookeeper/conf/zoo.cfg
           server.1=192.168.43.154:2888:3888

        ```
    * STEP 4: Mesos Config On Master Servers
       ```
         STEP 1: set it to over 50% of master members 
         sudo nano /etc/mesos-master/quorum
         1
       ```
    * STEP 5: Setup IP
      ```
       sudo nano /etc/mesos-master/ip
       192.168.43.154
    
       STEP 6: setup hostname
       192.168.43.154
       
       
      ```
     * STEP 6: Marathon Config On Master
       ```
       sudo nano /etc/default/marathon 
       MARATHON_MESOS_USER=root
       MARATHON_MASTER="zk://192.168.43.154:2181/mesos"
       MARATHON_ZK="zk://192.168.43.154:2181/marathon"
       MARATHON_HOSTNAME="192.168.43.154"
       
       ```
     * STEP 7: Restart Services
       ```
     we need to make sure that our master servers are only running the Mesos master process,
     and not running the slave process. We can ensure that the server doesn’t start the slave process at boot by creating an override file
     
     echo manual | sudo tee /etc/init.d/mesos-slave.override
      ```
    * STEP 8: 
     ```
     Now, all we need to do is restart zookeeper, which will set up our master elections. We can then start our Mesos master and Marathon processes
     
    start zookeeper
    cd /usr/share/zookeeper/bin
    ./zkServer.sh status
    ./zkServer.sh start
    
    ```
   * STEP 9: start mesos-master
    ```
    sudo service mesos-master start
    
    ```
   * start marathon (runs on java 8)
   ```
   sudo service marathon start 
    
   ```
   
    * Point browser to http://192.168.43.154:5050 `for Mesos UI`
    * Point browser to http://192.168.43.154:8080 `for Marathon UI`
   
    
    
* MESOS SLAVE

> For Mesos-Slave

* Enable some configurations and add some files in the `VM-2`
* Only some slave package dependencies were installed there is no requirement of zookeeper too in slave side. But slave sometimes depends on zookeeper too

```
Install Packages and Dependencies.
sudo apt-get update

=> sudo apt install -y openjdk-11-jre-headless

=>sudo apt-get -y install build-essential python3-dev python3-six python3-virtualenv libcurl4-nss-dev libsasl2-dev libsasl2-modules maven libapr1-dev libsvn-dev zlib1g-dev iputils-ping

=>sudo apt-get install -y libcurl4-openssl-dev

=>sudo apt install -y libevent-dev
```

> Install mesos
`sudo dpkg -i mesos-1.9.0-0.1.20200901105608.deb`

> Configure ZooKeeper connection info to point to the master servers
> In the file `sudo nano /etc/mesos/zk`
```
zk://<IP OF VM Linked>:2181/mesos
```

> Zookeeper is not required at the slave side to it's better to force disable them
```
sudo service zookeeper stop
sudo sh -c "echo manual > /etc/init/zookeeper.override"
```
> Mesos-Master is also not required so better force disable them
```
sudo service mesos-master stop
sudo sh -c "echo manual > /etc/init/mesos-master.override"
```

> set the IP address and hostname in `/etc/mesos-slave dir`

```
echo \<VM's IP\> | sudo tee /etc/mesos-slave/ip
sudo cp /etc/mesos-slave/ip /etc/mesos-slave/hostname
```

> Post doing this restart slave
```
sudo service mesos-slave restart
```

> Post doing these configuration point the browser to => `http://192.168.43.154:5050` and check the slave under `agents` tab





            
         
