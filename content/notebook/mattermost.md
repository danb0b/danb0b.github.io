---
title: Mattermost Details
---


git clone https://github.com/mattermost/docker
cd docker
cp env.example .env
mkdir -p ./volumes/app/mattermost/{config,data,logs,plugins,client/plugins,bleve-indexes}
sudo chown -R 2000:2000 ./volumes/app/mattermost

We want https, so follow [these instructions](/notebook/tailscale-details/#turn-on-https)

using the nginx instructions

sudo docker compose -f docker-compose.yml -f docker-compose.nginx.yml up -d

## External Resources

<https://docs.mattermost.com/install/install-docker.html>

## tailscale Cert

sudo tailscale cert --cert-file cert.pem --key-file key.pem <server.domain>.ts.net
