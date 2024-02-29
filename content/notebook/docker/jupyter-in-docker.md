---
title: Using Python in a Docker Container
tags:
- python
- jupyter
- docker
- linux
- ubuntu
---

## Introduction

This tutorial makes it possible to spin up a container with everything you need to run Python in a Jupyter notebook.

## Implementation

### File Structure

The following is the folder structure of the project.

```bash
.
├── build
│   └── Dockerfile
├── build.bash
├── code
│   └── your_code.ipynb
├── docker-compose.yaml
└── jupyter-config
    ├── jupyter_server_config.py
```

### Dockerfile

in ```./build```, create an empty text file called ```Dockerfile```.  Paste in the following:

```dockerfile
FROM python:3.11-bookworm
WORKDIR /code

RUN apt update && apt install -y python3-distutils python3-pip && \
python -m pip install numpy scipy jupyter matplotlib pillow
#... add any other packages here
#RUN python -m pip install ...

EXPOSE 8888 
```

This short script is the recipe to create a new docker "image".  A docker image is a static, portable, shareable, and minimal operating system, with everything you need to perform typically one task.  In this case, the docker image starts from a release of Debian called "bookworm" with python 3.11 installed on top of it.  From this base image, we install the numpy, scipy, jupyter, matplotlib, and pillow packages.  This is enough to do some serious computing and plotting!

### Build Script

Next, in the top folder, create a new file called ```build.bash```.  

```bash
#!/usr/bin/bash

docker build ./build/ -t my_jupyter_image
```

To build it for the first time, make it executable with ```chmod +x build.bash```, then run it with

```bash
. build.bash
```

This will create a new image called "my_jupyter_image"

Why do I like to create my own build script?  Because if I want to customize how I built the image, I can store that approach in a clearly-labeled file rather than remember I built it a certain way last time.  (I can also comment out other approaches in case I want to switch back).  There are a lot of other useful build options.  For more ideas, see [here](/notebook/docker/docker-commands/#build-options)

### Jupyter Config File

By default, Jupyter lab requires a token for logging on to the website, and normally when you boot up jupyter using ```jupyter lab```, the command line will spit out a link with the token embedded in it.  In a (personal) dockerized environment using docker compose, the token is not as easy to find on the command line, because the ```docker compose -d``` command will hide output from the container.  

If you want to access the token, you have to access the container's shell using


```bash
docker exec -it jupyter /bin/bash
```

and then retrieve the token using the following command:

```bash
jupyter server list
```

However, there is a different way.  This config file sets the token and password to empty strings so that you can sign on without any password.  in the ./jupyter-config folder, make ```jupyter_server_config.py``` with the following code inside:

```python
c.ServerApp.token = ""
c.ServerApp.password = ""
```

> **Caution:** as noted in the [documentation](https://jupyter-server.readthedocs.io/en/latest/operators/security.html#alternatives-to-token-authentication), this approach is not intended for publicly accessible docker containers as it is a security issue.  For a personal computing project, this should be just fine.

## Docker Compose

This is the bare-bones implementation.  The ```docker-compose.yaml``` file starts up a container called jupyter, using the "my_jupyter_image" image we built above.  The docker-compose file can also build the image if needed, and looks for the same dockerfile in the ```./build``` folder.  We will access the container by the name  ```jupyter``` when it is running.  It will have access to two folders, the jupyter config folder we placed our config file in earlier, as well as a code folder.  The locations on our machine are specified in the folder structure above

* ```--no-browser``` doesn't launch theh browser
* ```--port=8888``` specifies port 8888 for the website
* ```--allow-root``` allows the root user to launch it
* ```--ip=0.0.0.0``` The address the Jupyter server will listen on.  Specifying 0.0.0.0 allows the site to be available through docker

```yaml
version: "3.9"
services:
  jupyter:
    image: my_jupyter_image:latest
    build: ./build
    container_name: jupyter
    volumes: 
    - ./jupyter-config:/root/.jupyter
    - ./code:/code
    command: bash -c "jupyter lab --allow-root --ip='0.0.0.0' --port=8888 --no-browser"
    ports:
      - 8888:8888  
```

##  Putting it all together

To bring up your new container, all you have to do is, from the top folder, call

```bash
docker compose up
```

This will create a new running instance of your image, which we call a "container" in docker-speak.  Once it is loaded and running, navigate in your browser to ```localhost:8888```.  A new jupyter lab window will open and provide access to your ```code/``` folder and any files already inside.

## Future work

I hope to be able to share more examples of this approach to getting python running, with specific recipes we use in our lab, research, and classroom.  Look out for more.

## Words of warning

This solution does not work very well for cases that

* require hardware acceleration
* require opengl
* require PyQt5 or other GUIs

this all comes down to the fact that docker out of the box does not support guis or connect well to user-specific hardware.  I have gotten some workarounds to this, but nothing coherent enough that it provides a general solution to the above problems.  So for now, its great for basic computing, but not so great for visualization or accelerated tasks.

## External Resources

### Docker info

* <https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f>
* <https://medium.com/@18bhavyasharma/setting-up-and-running-jupyter-notebook-in-a-docker-container-d2acd713ce66>
* <https://www.dataquest.io/blog/docker-data-science/>
* <https://towardsdev.com/run-a-jupyter-notebook-in-a-docker-container-on-your-local-device-80ccd9570e4f>

### About Docker Base Images

* <https://pythonspeed.com/articles/base-image-python-docker-images/>
  
### Jupyter setup and security

* <https://jupyter-server.readthedocs.io/en/latest/operators/security.html#>
* <https://jupyter-server.readthedocs.io/en/latest/users/configuration.html>
