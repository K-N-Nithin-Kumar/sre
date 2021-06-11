# DOCKER 

> Create a Docker container running a python webserver, that listens on port 80 and returns the string `Hello world` for any requests

> On `VM-2` these configurations were made.

> STEP-1
`DOCKER INSTALLATION`

> Install Docker on `VM-2`

> STEP-1
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```

> STEP-2 Import the repository’s GPG key using the following `curl` command
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

>STEP-3 Add the Docker APT repository to your system:
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

> STEP-4 Install Docker  (community edition)

```
sudo apt install docker-ce docker-ce-cli containerd.io
sudo apt install docker-ce
```
> STEP-5 Check Status
```
sudo systemctl status docker
```


# NOW THAT THE DOCKER IS INSTALLED
## We Have to deploy Flask App

> Prerequisites 
```
Python version 3.8 or later
Docker running locally
```

> Sample Application
```
For this flask application was installed

mkdir ~/python-docker
cd /home/neha/python-docker
pip3 install Flask
pip3 freeze > requirements.txt
```

> Edit `requirements.txt` file
```
Add only FLASK==2.0.0
```

> create `app.py` sample application
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
if __name__=='__main__':
    app.run('0.0.0.0',port=5000)
```

> Test the app

* Run `python app.py` and point the browser to `<Host-ip>:5000 to get the details

> Create a Dockerfile for Python

```
# syntax=docker/dockerfile:1                         // The first line to add to the Dockerfile is a # syntax parser directive

FROM python:3.8-slim-buster                         //  What base image we would like to use for our application.

WORKDIR /app                                        // Creates Working Directory 

COPY requirements.txt requirements.txt              // Copy requirements.txt file created above
RUN pip3 install -r requirements.txt                // This works exactly the same as if we were running pip3 install

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]   // Coomad to be executed

```

> Directory structure
```
python-docker
|____ app.py
|____ requirements.txt
|____ Dockerfile

```
>Build an image

```
docker build --tag python-docker .
```

> View local images To list images,run the `docker images` command.

> Tag images (Optional step)

```
To tag the image as the latest 
To create a new tag for the image we’ve built above, run the following command
docker tag python-docker:latest python-docker:v1.0.0
```

>Run your image as a container

```
To run an image inside of a container, we use the docker run command.
docker run python-docker
```

> `docker run -d -p 80:5000 python-docker` listens on port 80 and hosted at port 5000






















