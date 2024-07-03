FROM ubuntu:24.04

RUN mkdir /workspace

# Install packages we need
# RUN snap install hugo --channel=extended
RUN apt update && apt install hugo -y

# # Add new non -root user and switch to it
# RUN useradd pyuser
# RUN chown -R pyuser:pyuser / workspace
# USER pyuser

# change dir to / workspace
WORKDIR /workspace