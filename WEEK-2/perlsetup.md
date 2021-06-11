
> PERL SCRIPTING
```
 Learnt few basic usage and syntax of PERL language by following the link =>https://www.youtube.com/watch?v=WEghIXs8F6c
                                                                          =>https://www.youtube.com/watch?v=Wj4DXdeqe3U&t=126s (Perl CGI)
                                                                          =>https://perlmaven.com/perl-cgi-script-with-apache2
                                                                          =>https://foswiki.org/Support.HowToInstallCpanModules

```


> Configuring Perl/Cgi with Apache

> Install apache2 HTTP server.
```
sudo apt-get apache2 (Installs Apache2)`
sudo systemctl start apache2 (Starts Apache2)
ifconfig (Systems IP address.)
``` 
 
> Create a directory to save and run perl/cgi.
```
 mkdir var/cgi-bin.
 Create a file called => /var/cgi-bin/echo.pl
 Give file exectuable permission => chmod +x /var/cgi-bin/echo.pl
 Run it on Command Line once => /var/cgi-bin/echo.pl
 Contents of echo.pl includes=> #!/usr/bin/perl
                                  use strict;
                                  use warnings;
                                  print qq(Content-type: text/plain\n\n);
                                  print "hi\n";                                (This is the basic scriptfor testing purpose)
```

> We need to configure the Apache web server.
```
=>Open the configuration file of Apache /etc/apache2/sites-enabled/000-default.conf
=> nano Apache /etc/apache2/sites-enabled/000-default.conf
=> Add the following lines after the DocumentRoot line:   ScriptAlias /cgi-bin/ /var/cgi-bin/
                                                        <Directory "/var/cgi-bin">
                                                        AllowOverride None
                                                        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                                                        Require all granted
                                                        </Directory>
=> This will configure http. For a real public site consider using https                                                        
```

* By default this Apache instance does not have the CGI module enabled. This we can see by noticing that the mods-enabled directory does not have any of    the cgi files that are available in the mods-available directory.

```
ls -l /etc/apache2/mods-enabled/ | grep cgi
ls -l /etc/apache2/mods-available/ | grep cgi
```
```
We create symbolic links from the mods-enabled to the mods-available directory for the two cgid.* 
 ln -s /etc/apache2/mods-available/cgid.load /etc/apache2/mods-enabled
 ln -s /etc/apache2/mods-available/cgid.conf /etc/apache2/mods-enabled
 ls -l /etc/apache2/mods-enabled/ | grep cgi
```

```
At this point we can reload the Apache web server by the following command:
    =>service apache2 reload
```

```
This will tell Apache to read the configuration files again.
Then we can browse to http://(IP ADDRESS)/cgi-bin/echo.pl and you will see it shows the word "hi". 

To generate html file => (perl echo1.pl > index.html)
 Index.html contains the HTML Format of the perl scripts.
```






