FROM ubuntu:24.04


# Install packages we need
# RUN snap install hugo --channel=extended
RUN apt update && apt install hugo -y

# # Add new non -root user and switch to it
# RUN useradd pyuser
# RUN chown -R pyuser:pyuser / workspace
RUN mkdir /workspace

# change dir to / workspace
WORKDIR /workspace

USER ubuntu


# ARG NODE_VERSION=18
# FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:${NODE_VERSION}

# VARIANT can be either 'hugo' for the standard version or 'hugo_extended' for the extended version.
# ARG VARIANT=hugo
# VERSION can be either 'latest' or a specific version number
# ARG VERSION=latest

# # Download Hugo
# RUN apt update && apt install -y ca-certificates openssl git curl && \
#     rm -rf /var/lib/apt/lists/* && \
#     case ${VERSION} in \
#     latest) \
#     export VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest | grep "tag_name" | awk '{print substr($2, 3, length($2)-4)}') ;;\
#     esac && \
#     echo ${VERSION} && \
#     case $(uname -m) in \
#     aarch64) \
#     export ARCH=ARM64 ;; \
#     *) \
#     export ARCH=64bit ;; \
#     esac && \
#     echo ${ARCH} && \
#     wget -O ${VERSION}.tar.gz https://github.com/gohugoio/hugo/releases/download/v${VERSION}/${VARIANT}_${VERSION}_Linux-${ARCH}.tar.gz && \
#     tar xf ${VERSION}.tar.gz && \
#     mv hugo /usr/bin/hugo

# Hugo dev server port
EXPOSE 1313

# [Optional] Uncomment this section to install additional OS packages you may want.
#
# RUN apt update && export DEBIAN_FRONTEND=noninteractive \
#     && apt -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment if you want to install more global node packages
# RUN sudo -u node npm install -g <your-package-list-here>