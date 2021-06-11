### Deploy the docker container that you created in #1 to run as a Marathon app and it should be reachable using the Traefik

* The docker App Should run as Marathon Application

* For this Task an Account was created at `docker-hub`
```
login to docker hub
Create a docker account
and upload the app.py app created at the Docker Task.
```

> Post Creating the account
```
In the VM-Terminal

docker login
docker tag python-docker: kanakarajuu/python-docker:latest
docker push kanakarajuu/python-docker:latest

```

```
echo 'docker,mesos' > /etc/mesos-slave/containerizers
echo '10mins' > /etc/mesos-slave/executor_registration_timeout
restart mesos-slave
```

* Create a `json` file and add the particular details
* The `json` contents are in => [basic-app](https://github.com/r-aju/SRE-Internship/blob/master/WEEK-12/jsonfiles/basic-app.json)
* The `json` contents to deploy flask app was in =>[Docker](https://github.com/r-aju/SRE-Internship/blob/master/WEEK-12/jsonfiles/docker.json)


* Push the app to marathon i.e the json files
```
curl -X POST http://192.168.43.154:8080/v2/apps -d @basic_app.json -H “Content-type: application/json”
curl -X POST http://192.168.43.154:8080/v2/apps -d @docker_app.json -H “Content-type: application/json”

Check the application deployed at marathon dashboard

















