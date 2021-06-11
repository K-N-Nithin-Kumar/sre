* Traefik on VM3
* Configure Traefik to get its data from Marathon

# STEP-1

* Install and Configure Traefik
* Traefik was installed and configured as `Docker Container`
* Traefik acts as  `Reverse proxy` and `Load Balancer`

# STEP-2
>Create a configuration files and set up an encrypted password to access the traefik dashboard
```
sudo apt-get install -y apache2-utils
htpasswd -nb raju raju                  // username and password
```

>You will get encrypted password

```
vm3@traefik:~$ htpasswd -nb raju raju 
admin:$apr1$V.9MT9VH$MtLgwiAa4jq1ngDVvTdJu/
vm3@traefik:~$

Copy this output and save it somewhere as we need to use this encrypted password in Traefik configuration. 
 To setup basic authentication for Traefik dashboard.
```

> The `traefik.toml` file the following contents [Traefik.toml](https://github.com/r-aju/SRE-Internship/blob/master/WEEK-12/Tomlfiles/traefik.toml)

>  The `traefiksecure.toml` file had the following contents [Traefiksecure.toml](https://github.com/r-aju/SRE-Internship/blob/master/WEEK-12/Tomlfiles/traefik_secure.toml)

 # Running traefik container
 
 * `docker network create web`

* Create an empty file which holds Let’s encrypt information and modify the permission accordingly
```
$ touch acme.json
$ chmod 600 acme.json.   //Contains Private key!
```
* Create a traefik container using the following command
```
$ docker run -d \
   -v /var/run/docker.sock:/var/run/docker.sock \
   -v $PWD/traefik.toml:/traefik.toml \
   -v $PWD/traefik_secure.toml:/traefik_secure.toml \
   -v $PWD/acme.json:/acme.json \
   -p 80:80 \
   -p 443:443 \
   --network web \
   --name traefik \
    traefik:v2.4
```
# Configure Traefik to get its data from Marathon

* In the `traefik.toml` file these particular lines were appended.
```
[providers.marathon]
  endpoint = "http://192.168.43.154:8080"
  exposedByDefault = true
  watch = true
  respectReadinessChecks = true
```  
  






