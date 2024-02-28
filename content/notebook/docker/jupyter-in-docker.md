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

Python is a bit of a mess these days.  There are a number of ways to install packages, and no one seems to agree what the right way forward is.  Dependencies work or don't work depending on how the package was installed.  Anaconda, which used to be my tried-and-true approach to a uniform experience across operating systems, has fallen victim to both "dependency hell" and a number of graphics issues on Linux lately for me.

So, to support courses and to provide a uniform experience, I've been looking into docker  more.  There are a number of good reasons to use Docker, including

* You get the same experience everywhere
* A lot of the installation fuss is taken care of (by me)
* You can share a small image with the whole class that is pre-tested

There are also some significant downsides to using it, including:

* Traditional GUI-based windowing systems are not supported.  Linux's migration towards Wayland has complicated matters that may have been solved earlier.
* dockerfiles are a black box.  Unless they were intentionally shared and documented, you don't necessarily know what the creator put inside.  This can be a security issue, but in terms of education it obscures some of the learning.  (This can be a good thing _and_ a bad thing.)
* then you have to learn docker too!

But, we have interactive web apps like Jupyter that can bridge some of the gap.  Docker compose has also solved some of the configuration issues associatd with running traditional docker images and containers, because you can put almost everything you need in a much better, self-documented yaml file.

Finally, while tools like Google Colab may use similar approaches to provide a jupyter front-end to python over the web, there is no guarantee that those tools are going to be available and free in the longer term.  I thought it would be a good idea to see what the state of Jupyter over Docker is, to see if I can commonize the Python experience for students and take some of the installation guesswork out of the process, while enabling as much of the traditional python programming experience as I can.

## Implementation

### File Structure

```bash
.
├── build
│   └── Dockerfile
├── build.bash
├── code
│   └── your_code.py
├── docker-compose.yaml
└── jupyter-config
    ├── jupyter_server_config.py
```

### Dockerfile

in ```./build``` make a file called ```Dockerfile```.  Paste in the following

```dockerfile
FROM python:3.11-bookworm
WORKDIR /code

RUN apt update && apt install -y python3-distutils python3-pip && \
python -m pip install --upgrade pip && \
python -m pip install numpy scipy jupyter matplotlib pillow
#... add any other packages here
#RUN python -m pip install ...

EXPOSE 8888 
```

### Build Script

create a new file called ```build.bash```

```bash
#!/usr/bin/bash

docker build ./build/ -t jupyter
```

To build it for the first time, make it executable with ```chmod +x build.bash```, then run it with

```bash
. build.bash
```

There are a lot of other useful build options.  For more ideas, see here

### Jupyter Config File

By default, Jupyter lab requires a token.  Normally when you boot up jupyter using ```jupyter lab```, the command line will spit out a link with the token embedded in it.  In a (personal) dockerized environment using docker compose, the token is not as easy to find on the command line because the ```docker compose -d``` command will hide output from the container.  

If you want to access the token, you have to sign on to the container and identify the token using

```bash
jupyter server list
```

However, there is a different way.  This config file sets the token and password to empty strings so that you can sign on without any password.  in the ./jupyter-config folder, make ```jupyter_server_config.py``` with the following code inside:

```python
c.ServerApp.token = ""
c.ServerApp.password = ""
```

> **Caution:** as noted in the [documentation](https://jupyter-server.readthedocs.io/en/latest/operators/security.html#alternatives-to-token-authentication), this approach is not intended for publicly accessible docker containers as it is a security issue.

## Docker Compose

This is the bare-bones implementation.

* ```--no-browser``` doesn't launch theh browser
* ```--port=8888``` specifies port 8888 for the website
* ```--allow-root``` allows the root user to launch it
* ```--ip=0.0.0.0``` The address the Jupyter server will listen on.  Specifying 0.0.0.0 allows the site to be available through docker

```yaml
version: "3.9"
services:
  sofa:
    image: my_jupyter:latest
    container_name: jupyter
    volumes: 
    - ./jupyter-config:/root/.jupyter
    - ./code:/code
    command: bash -c "jupyter lab --allow-root --ip='0.0.0.0' --port=8888 --no-browser"
    ports:
      - 8888:8888  
```

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

### Jupyter setup and security

* <https://jupyter-server.readthedocs.io/en/latest/operators/security.html#>
* <https://jupyter-server.readthedocs.io/en/latest/users/configuration.html>

