---
title: Start docker automatically as a ```systemd``` service
tags:
- ubuntu
- bash
- docker
---


## Docker Compose Example

copy and paste the folowing text into a new file called ~/script.sh


```bash
#!/bin/bash
SERVICENAME=$(basename $(pwd))

# Create systemd service file
cat | sudo tee /etc/systemd/system/$SERVICENAME.service << EOF
[Unit]
Description=$SERVICENAME
Requires=docker.service
After=docker.service

[Service]
Restart=always
User=root
Group=docker
WorkingDirectory=$(pwd)
ExecStartPre=$(which docker) compose -f docker-compose.yml down
ExecStart=$(which docker) compose -f docker-compose.yml up
ExecStop=$(which docker) compose -f docker-compose.yml down

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable $SERVICENAME.service
sudo systemctl start $SERVICENAME.service
```

```bash
chmod +x ~/script.sh
```

go to the folder where your docker-compose.yml file is,

```bash
sudo bash ~/script.sh
```

## External Resources

edited from [here](https://techoverflow.net/2020/10/24/create-a-systemd-service-for-your-docker-compose-project-in-10-seconds/)
