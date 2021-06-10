  
  
# TASKS

* Create a Docker container running a python webserver, that listens on port 80 and returns the string "Hello world" for any requests

* Create three VMs and setup the following,

* Mesos master, Marathon, and Zookeeper on VM1

* Mesos slave and Docker on VM2

* Traefik on VM3

* Configure Traefik to get its data from Marathon

* Deploy the docker container that you created in #1 to run as a Marathon app and it should be reachable using the Traefik

* Setup VM4, install Nginx on it. Create a self-signed SSL Certificate and set up a proxy using Nginx which listens on port 443 with SSL enabled and forwards the requests to Traefik

  
  
  * The Topology was given and the BGP was setup accordingly.


 ![App Deployment (1)](https://user-images.githubusercontent.com/43216503/121065217-26a9cd80-c7e6-11eb-8115-2200011fd39a.png)


   * The overall design should look like this 

  <img width="204" alt="Screenshot 2021-06-07 at 11 15 47 PM" src="https://user-images.githubusercontent.com/43216503/121065400-5953c600-c7e6-11eb-99e9-059644e8b108.png">

