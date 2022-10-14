---
title: Create a ```systemd``` service
---


## Docker Compose Example

go to the folder where your docker-compose.yml file is

```bash
#!/bin/bash
SERVICENAME=$(basename $(pwd))

# Create systemd service file
sudo cat >/etc/systemd/system/$SERVICENAME.service <<EOF
[Unit]
Description=$SERVICENAME
Requires=docker.service
After=docker.service

[Service]
Restart=always
User=root
Group=docker
WorkingDirectory=$(pwd)
ExecStartPre=$(which docker-compose) -f docker-compose.yml down
ExecStart=$(which docker-compose) -f docker-compose.yml up
ExecStop=$(which docker-compose) -f docker-compose.yml down

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable $SERVICENAME.service
sudo systemctl start $SERVICENAME.service
```

## External Resources

from [here](https://techoverflow.net/2020/10/24/create-a-systemd-service-for-your-docker-compose-project-in-10-seconds/)
