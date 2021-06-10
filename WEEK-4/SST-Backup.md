> SST Backup (Manual)

 * The mariabackup SST method uses the Mariabackup utility for performing SSTs. It is one of the methods that does not block the donor node

> mariabackup utility was installed `apt install mariadb-backup` this should match with mariadb version too.

 * Here, for this step 2 nodes were considered namely the `second` and `third` node in the clusters.
    
     > `sd2` was the Vm and then `sd3` was the name of second Vm.
        
  | NAME | IP'S         |   
  |------|--------------|
  | sd2  | 192.168.1.48 |   
  | sd3  | 192.168.1.47 |   


* Choosing Mariabackup for SST
  `SET GLOBAL wsrep_sst_method='mariabackup';`
  
* In one of the configuration file

  * That is `/etc/mysql/mariadb.conf.d/50-server.cnf` on the third node and add the following contents.
 
 ```
   [mariadb]
    .....
   wsrep_sst_method = mariabackup
   wsrep_sst_auth = kanakaraju:kanakaraju      
   wsrep_sst_donor = galera_3                 or galera_3,
 ```
 
 * If `galera_3` is not available. It would consider the other nodes in the cluster by giving `galera_3,`

* Create a user in `mysql` having `RELOAD`, `PROCESS`, `ALTER` , `LOCKTABLES` access.

```
login into mysql
mysql -v
GRANT RELOAD, PROCESS, ALTER, LOCK TABLES, BINLOG MONITOR ON *.* TO `kanakaraju`@`%` IDENTIFIED BY 'kanakaraju';

```

* Create a `backup` directory to store the backup node

```
$ sudo mkdir /home/sd3/sstbackup
$ sudo mariabackup --backup --galera-info --target-dir=/home/sd3/sstbackup --user kanakaraju --password kanakaraju 
```

* Create a `backup` directory to store the contents from `joiner` node

```
mkdir /home/sd2/backup
```

* Form the curent node i,e `sd3` send the contents
`scp  /home/sd4/sstbackup/* sd2@192.168.1.48:/home/sd2/backup/`




   
   
   
   
   


