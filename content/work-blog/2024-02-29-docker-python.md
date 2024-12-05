---
title: "Python and Jupyter in Containers"
date: 2024-02-29
summary: " "
---

Python for me has always been easy to learn, but hard to get working.  There are a number of ways to install and manage packages -- pip, anaconda, virtual environments, poetry --  unfortunately, each code project has spent different amounts of effort tuning their install approach to suit one, maybe two of these paradigms.  This means that the success of installing a complex python codebase depends heavily on the approach you took to install it, and it may or may not work.  Anaconda, for example, which has been my tried-and-true approach to a uniform package management experience across operating systems for many years, has itself fallen victim to the increasing complexity of managing dependencies, or "dependency hell".

This only gets harder as the connections between the operating system and programming language grow.  As code projects start to depend on specific compiled binaries, environment flags, or specific network setups, the challenge of getting a working environment grows from a Python problem to a system problem.  So, to support courses and to provide a uniform experience, I've been looking into how to use containers for sharing working systems.  There are a number of good reasons to use Docker, including:

* You get the same experience everywhere
* A lot of the installation fuss is taken care of (by an expert)
* You can share a smaller image with the whole class that is pre-tested, or at least common.

There are also some significant downsides to using it, including:

* Traditional GUI-based windowing systems are not supported out of the box.  Web-based tools are much easier to integrate, though.  
* dockerfiles are a black box.  Unless they were intentionally shared and documented, you don't necessarily know what the creator put inside.  This can be a security issue, but in terms of education it obscures some of the learning.  (This can be a good thing _and_ a bad thing.)
* It also means you need  to learn a little about docker, too!

To mitigate some of these issues we can use interactive web apps like Jupyter that can facilitate interaction with containers.  Docker's compose file has also solved some of the configuration issues associated with running traditional docker images and containers, because you can put almost everything you need in a self-documented yaml file.

Finally, while tools like Google Colab may use similar approaches to provide a jupyter front-end to python over the web, there is no guarantee that those tools are going to be available and free in the longer term.  I thought it would be a good idea to see what the state of Jupyter over Docker is, to see if I can commonize the Python experience for students and take some of the installation guesswork out of the process, while enabling as much of the traditional python programming experience as I can.

So to provide a starting point, here is a [tutorial](/notebook/docker/jupyter-in-docker/) for setting up a docker container complete with Python, a web-based interface, and some starter packages.  This can be augmented from here with your own packages and then shared with others.  But getting a working jupyter interface is a good starting point for the tutorial.  I will share other containers based on this in the future.

## Resources

* [Using Python in a Docker Container](/notebook/docker/jupyter-in-docker/)