### NAGIOS
```
=> NAGIOS is like the continous monitoring tool which follows a client and server architecture.
=> Nagios is usually used to monitor stack and alert us when problems arise. 
=> Nagios allows to monitor every aspect of each of the servers such as running processes,
   CPU usage, disk usage, and more.


=> The NAGIOS Server is installed on one of the Vm and the NAGIOS Server Communicates with the 
    client using the NRPE (Nagios Remote Plugin Executor)
=> The NRPE is installed in the Vm which acts like a Client VM.
```

### NSTALLATION SERVER
```
STEP-1 => sudo apt update
        =>sudo apt install -y autoconf bc gawk dc build-essential gcc libc6 make wget unzip apache2 php 
                libapache2-mod-php libgd-dev libmcrypt-dev make libssl-dev snmp libnet-snmp-perl gettext   // Installs Nagios Dependencies

       =>wget https://github.com/NagiosEnterprises/nagioscore/archive/nagios-4.4.6.tar.gz                 // Installing Nagios Core.
       =>tar -xf nagios-4.4.6.tar.gz                                                                      // Extracting packages
       => cd nagioscore-*/


STEP-2 => sudo ./configure --with-httpd-conf=/etc/apache2/sites-enabled       // Compile Nagios Source code.
       => sudo make all                                                       // and define apache vhost configuration.



STEP-3 => sudo make install-groups-users                                    // Create Nagios Username and Group.
       => sudo make install
       => sudo make install-daemoninit                                     // Install Nagios binaries
       => sudo make install-commandmode                                   // service daemon script and the command mode
       => sudo make install-config                                        // Install the sample script configuration
       => sudo make install-webconf                                       // Then install the Apache configuration for Nagios   
       => sudo a2enmod rewrite cgi                                        // Activate the mod_rewrite and mode_cgi modules
       => systemctl restart apache2


STEP-4 => Adding the Nagios User and Password Authentication.
       =>sudo htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin       
       => This is the apache basic authentication for the user the "nagiosadmin"



STEP-5 =>Install Nagios Plugins and NRPE Plugin
       =>sudo apt install monitoring-plugins nagios-nrpe-plugin   // Installs Nagios Plugins and NRPE Plugin
       =>cd /usr/local/nagios/etc
       => Open "nagios.cfg" file


       => Post opening the file.
       =>Uncomment the 'cfg_dir' option that will be used for sotring all server hots configurations.
       =>cfg_dir=/usr/local/nagios/etc/servers



STEP-6 =>Edit the configuration file "resource.cfg"
       =>$USER1$=/usr/lib/nagios/plugins                 // Define the nagios monitoring path.




STEP-7 =>define the nrpe check command by editing the configuration file "commands.cfg"
       => cd /usr/local/nagios/etc/objects
       =>
         define command{
        command_name check_nrpe
        command_line $USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$
}
 
      => These would be the default command for the user and address.



STEP-8 => Start Nagios service
       => systemctl start nagios
       => systemctl enable nagios
       => systemctl status nagios                 // Returns active when there are no errors.



STEP-9 => Restart the apache service and then point out to the browser with IP/nagios/
       =>systemctl restart apache2
       => In the desired browser => http://192.168.43.93/nagios/


STEP 10 => The app UI get's loaded the default metrics would be shown.
        => Next step would be installing the the NRPE at the Client side to monitor client side metrics.
```

### INSTALLATION OF CLIENT
```

=> On the Vm which would be considered as the Client Install some of the NRPE Plugins.


STEP-1 => sudo apt update                                                                           // Update Ubuntu repository
       => sudo apt install nagios-nrpe-server monitoring-plugins                                   // Install Nagios Plugins and NRPE server



STEP-2 =>Go to the NRPE installation directory "/etc/nagios" and edit the configuration file.
       =>cd /etc/nagios/
       => nano nrpe.conf


STEP-3 => In the file nrpe.conf
       => Uncomment => "server_address" line and change the value with the "clients" IP address.
       => server_address=192.168.43.43


       => Next uncomment the next part of file => "allowed_hosts" line and add SERVER'S IP here
       => allowed_hosts=127.0.0.1,::1,192.168.43.93


STEP-4 => In the file "nrpe_local.cfg" configuration. 
       => Add the following con figurations which was followed.
       => 

command[check_root]=/usr/lib/nagios/plugins/check_disk -w 20% -c 10% -p /
command[check_ping]=/usr/lib/nagios/plugins/check_ping -H 192.168.43.43 -w 100.0,20% -c 500.0,60% -p 5
command[check_ssh]=/usr/lib/nagios/plugins/check_ssh -4 192.168.43.43
command[check_http]=/usr/lib/nagios/plugins/check_http -I 192.168.43.43
command[check_apt]=/usr/lib/nagios/plugins/check_apt

=> the IP used is the Client's Ip.



STEP-5 => systemctl restart nagios-nrpe-server
       =>systemctl enable nagios-nrpe-server
       =>systemctl status nagios-nrpe-server                    // Start the nrpe service.
```

### CHECK SERVER CLIENT CONNECTIVITY
```
=> From server Vm execute the following command.
   =>/usr/lib/nagios/plugins/check_nrpe -H 192.168.43.43.     // This would actually check the connectivity between server and client.
   =>/usr/lib/nagios/plugins/check_nrpe -H 192.168.43.43 -c check_ping 
```
### ADD HOSTS CONFIGURATION TO THE SERVER
```

=> In the directory =>"/usr/local/nagios/etc/servers 
=> Create a new file corresponding to the host name ex => na2.cfg
=>
 And add these configurations below.

 =>
# Ubuntu Host configuration file1

define host {
        use                          linux-server
        host_name                    na2
        alias                        Ubuntu Host
        address                      192.168.43.43
        register                     1
}

define service {
      host_name                       na2
      service_description             PING
      check_command                   check_nrpe!check_ping
      max_check_attempts              2
      check_interval                  2
      retry_interval                  2
      check_period                    24x7
      check_freshness                 1
      contact_groups                  admins
      notification_interval           2
      notification_period             24x7
      notifications_enabled           1
      register                        1
}

define service {
      host_name                       na2
      service_description             Check Users
      check_command                   check_nrpe!check_users
      max_check_attempts              2
      check_interval                  2
      retry_interval                  2
      check_period                    24x7
      check_freshness                 1
      contact_groups                  admins
      notification_interval           2
      notification_period             24x7
      notifications_enabled           1
      register                        1
}

define service {
      host_name                       na2
      service_description             Check SSH
      check_command                   check_nrpe!check_ssh
      max_check_attempts              2
      check_interval                  2
      retry_interval                  2
      check_period                    24x7
      check_freshness                 1
      contact_groups                  admins
      notification_interval           2
      notification_period             24x7
      notifications_enabled           1
      register                        1
}

define service {
      host_name                       na2
      service_description             Check Root / Disk
      check_command                   check_nrpe!check_root
      max_check_attempts              2
      check_interval                  2
      retry_interval                  2
      check_period                    24x7
      check_freshness                 1
      contact_groups                  admins
      notification_interval           2
      notification_period             24x7
      notifications_enabled           1
      register                        1
}

define service {
      host_name                       na2
      service_description             Check APT Update
      check_command                   check_nrpe!check_apt
      max_check_attempts              2
      check_interval                  2
      retry_interval                  2
      check_period                    24x7
      check_freshness                 1
      contact_groups                  admins
      notification_interval           2
      notification_period             24x7
      notifications_enabled           1
      register                        1
}

define service {
      host_name                       na2
      service_description             Check HTTP
      check_command                   check_nrpe!check_http
      max_check_attempts              2
      check_interval                  2
      retry_interval                  2
      check_period                    24x7
      check_freshness                 1
      contact_groups                  admins
      notification_interval           2
      notification_period             24x7
      notifications_enabled           1
      register                        1
}

=> The metrics description would be like,
    => host_name           = Name of the host
    => service_description = Name of the service being executed.
    => check_command       = Name of service being executed.
    => notifications_enabled = 1 

=> The value 1 corresponds to true ie, (collect) and 0 corresponds to False ie, (Dont consider)

=> systemctl restart nagios

=> Point the browser to the => http://192.168.43.93/nagios/ 
=> It would probably show up the hosts added and the selected metrices.
```

  
   
