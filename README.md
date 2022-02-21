# Discord Docker Image Lookup
A bot to display :latest of particular docker image from docker hub.

# Installation
```
pip install -r requirements.txt
```

# Run
```
export DOCKER_USERNAME=... DOCKER_TOKEN=... DOCKER_BOT_TOKEN=... 
python discord-docker-image-lookup.py
```

# Use
```
# call via $docker some/image, e.g.:
[3:08 PM] chad: $docker linuxserver/wireguard

# bot response:
[3:08 PM] 
BOT
 docker-notify.py: latest arm:v7 2022-02-06T02:34:25.801956Z
[3:08 PM] 
BOT
 docker-notify.py: latest arm64:v8 2022-02-06T02:34:29.010395Z
[3:08 PM] 
BOT
 docker-notify.py: latest amd64 2022-02-06T02:34:22.603676Z
```
