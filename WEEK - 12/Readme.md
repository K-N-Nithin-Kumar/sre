# TASKS

* Create a Docker container running a python webserver, that listens on port 80 and returns the string "Hello world" for any requests

* Create three VMs and setup the following,

* Mesos master, Marathon, and Zookeeper on VM1

* Mesos slave and Docker on VM2

* Traefik on VM3

* Configure Traefik to get its data from Marathon

* Deploy the docker container that you created in #1 to run as a Marathon app and it should be reachable using the Traefik

* Setup VM4, install Nginx on it. Create a self-signed SSL Certificate and set up a proxy using Nginx which listens on port 443 with SSL enabled and forwards the requests to Traefik
