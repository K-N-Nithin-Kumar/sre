# DB Basics 

* TASK-1 => On a standalone VM, install MariaDB 10.5.6 and create a user same as your laptop login user.
          create database Nginx and restore the SQL file attached in the mail (Was Copied).
 
* Step 1: Update System  
 ```
 ->sudo apt update && sudo apt upgrade
 ->sudo apt -y install software-properties-common
```
* Step 2: Import MariaDB gpg key
```
->sudo apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc'

```

* Step 3: Add MariaDB APT repository
``` 
     ->sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://archive.mariadb.org/mariadb-10.5.6/repo/ubuntu/ focal main'
     -> This above link is for the MariaDB 10.5.6 Version.
```

* Step 4: Install MariaDB Server on 20.04 Linux
```
     ->sudo apt update
     ->sudo apt install mariadb-server mariadb-client (Hit the y key to accept installation of MariaDB 10.5.6 on Ubuntu 20.04 Linux.)
```

* Step 5: Secure MariaDB Server on 20.04 Linux
```
      ->sudo mysql_secure_installation (The database service should be started automatically after installation.)
      ->systemctl status mysql (Shows Active)           
```

* Test login to MariaDB shell using mysql `command:mysql -u root -p`
```
=>Check version using the command: 
   MariaDB [(none)]> SELECT VERSION();
+-----------------------------------------+
| VERSION() |
+-----------------------------------------+
| 10.5.6-MariaDB-1:10.5.6+maria~focal-log |
+-----------------------------------------+
1 row in set (0.000 sec)

```

* TASK -2 =>On an another VM install MariaDB and configure it as the `slave` of the `MariaDB` installed in above step

```
Replication is the process of copying data from one master database server to another slave database server.
In the master-slave topology, one server acts as the master and other servers act as slaves. In master-slave replication.
data is replicated one-way only.
```

* Create another Vm and install mariaDB as  same procedure followed in Step-1 or can (clone it as well)

```
Consider the first VM Created as Master and Second newly create VM as Slave.
Prerequistes => The two Vm's should be able to ping each other. (BGP, NAT-NETWORK or Internal Adapter can be used to establish links)
```

* Step 1– Configure Master Server (VM-1) `/etc/mysql/mariadb.conf.d/50-server.cnf`
```
  -> you will need to enable binary logging and replication on the master server. 
    To do so, open the file /etc/mysql/mariadb.conf.d/50-server.cnf with your preferred text editor
  
  -> Find the line bind-address and change the value to 0.0.0.0 to allow inbound connections.
     bind-address= 0.0.0.0   or bind-address= Vm-1's IP

Next, add the following lines at the end of the file:
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
log_bin_index =/var/log/mysql/mysql-bin.log.index
relay_log = /var/log/mysql/mysql-relay-bin
relay_log_index = /var/log/mysql/mysql-relay-bin.index    
```


* Save and close the file when you are finished. Then, restart the MariaDB service to implement the changes.
  `systemctl restart mariadb`

* Next, we will need to create a replication user. 
``` 
The slave server will use this user to log into the master server and request binary logs.
 First, log in to MariaDB shell with the following command: (mysql -u root -p)

=>create a user with the following command: CREATE USER 'replication'@'%' identified by 'your-password';
=> In my case it was 'replication' => 'raju';
=> In my case it was 'you-password' => 'raju1';

=>Now,grant the replication slave privilege to this user with the following command
=>GRANT REPLICATION SLAVE ON *.* TO 'replication'@'%';             'replication' => 'raju'
=>FLUSH PRIVILEGES;

=>check the master server status
=>show master status;  This will display the  file and position of it  (Note it in one side)
=>+------------------+----------+--------------+------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+------------------+----------+--------------+------------------+
| mysql-bin.000001 |      313 |              |                  |
+------------------+----------+--------------+------------------+
(Output looked like this)

=>EXIT;
```

* Configure Slave Server
```

=>log in to the slave server and open the file /etc/mysql/mariadb.conf.d/50-server.cnf
=>nano /etc/mysql/mariadb.conf.d/50-server.cnf
=>Inside the file
=> bind-address = 0.0.0.0
=>Next, add the following lines at the end of the file:
server-id = 2
log_bin = /var/log/mysql/mysql-bin.log
log_bin_index =/var/log/mysql/mysql-bin.log.index
relay_log = /var/log/mysql/mysql-relay-bin
relay_log_index = /var/log/mysql/mysql-relay-bin.index
=>Save and close the file when you are finished.
 =>Restart the MariaDB service to implement the changes=>systemctl restart mariadb
```

```
=>log in to the MariaDB shell =>mysql -u root -p
=>stop the slave threads      =>stop slave;
=> to set up the slave to replicate the master run the following command
=>CHANGE MASTER TO MASTER_HOST = 'your-master-host-ip', 
                  MASTER_USER = 'replication', 
                  MASTER_PASSWORD = 'your-password', 
                  MASTER_LOG_FILE = 'mysql-bin.000001', 
                  MASTER_LOG_POS = 313;
=> 'replication' => 'raju'
=>  'your-password' => 'raju1' 
=> start the slave threads: start slave;
                            exit;
```
```
=>Test Database Replication
=>On the master server, log in to the MariaDB shell and create a new Database or use existing Nginx database
=>create database mydb;
=>use mydb;
=>CREATE TABLE products(product_id INT NOT NULL, ,submission_date DATE, PRIMARY KEY ( product_id ));

=>On the slave server log in to the MariaDB shell.
=>mysql -u root -p
=>SHOW SLAVE STATUS \G
=> should preferbably show the slave_IO_State and other details.
=> show databases;
=>should see the mydb database that you created on the master server.
=>+--------------------+
| Database           |
+--------------------+
| information_schema |
| mydb               |
| mysql              |
| Nginx              |
| performance_schema | 
+--------------------+

=> NOTE: Slave can only view the contents and edit also if require but it won't get reflected the changed to the master server.

```

* TASK -3 => Convert this setup into Master Master replication b/w both the VMs.
```

=> The same steps was followed as the steps in the TASK-2 but the replication user is created at the SLAVE SIDE as well (VM-2)
=> In the slave side create a new user and grant the replication procedure.

=>SLAVE SIDE(VM-2)
=>mysql -u root -p (login to mariadb shell)
=>CREATE USER 'replication'@'%' identified by 'your-password';   => 'replication' => 'kanaka'
                                                                 => 'your-password=> 'kanaka1'

=>GRANT REPLICATION SLAVE ON *.* TO 'replication'@'%';            => 'replication' => 'kanaka'

=>FLUSH PRIVILEGES;
=> show master status;  (NOTE DOWN THE master statusfile and Position)


=>--------------------- On MASTER VM-----------------
=> mysql -u root -p (logging in)
=>Stop slave;       (stop the slave threads) 
=>CHANGE MASTER TO MASTER_HOST = '192.168.10.5', 
                   MASTER_USER = 'kanaka', 
                   MASTER_PASSWORD = 'kanaka1', 
                   MASTER_LOG_FILE = 'mysql-bin.000001', 
                   MASTER_LOG_POS = 313;
=>  MASTER_HOST= 'VM2-IP"
=> MASTER_USER=  'kanaka'
=>MASTER_PASSWORD = 'kanaka1'

=> result=>The databases create on the both side can be viewed or edited as well.
```
