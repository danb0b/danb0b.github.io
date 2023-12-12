---
title: Using tailscale with docker
---

1. Settings-->keys
1. check reusable, ephemeral, pre-approved
1. Copy the key
1. paste the following in your bashrc

    ```bash
    export DOCKERKEY=<your-key-here>
    ```

1. paste the following to run docker so that you can access all other devices on tailnet.  In this case, replace <my_subnet> with your subnet, eg 10.0.0.0/24

    ```bash
    docker run -v /var/lib:/var/lib -v /dev/net/tun:/dev/net/tun --network=host --cap-add=NET_ADMIN --cap-add=NET_RAW --env TS_AUTHKEY=$DOCKERKEY_PERM --env TS_ROUTES=10.0.0.0/8 tailscale/tailscale
    ```

    ```bash
    docker run -v /var/lib:/var/lib -v /var/lib/tailscale:/var/lib/tailscale -d /dev/net/tun:/dev/net/tun --network=host --cap-add=NET_ADMIN --cap-add=NET_RAW --env TS_AUTHKEY=$DOCKERKEY_PERM --env TS_ROUTES=10.0.0.0/8 tailscale/tailscale
    ```


```bash
sudo docker run -d --name=tailscaled -v /var/lib:/var/lib -v /dev/net/tun:/dev/net/tun --network=host --cap-add=NET_ADMIN --restart unless-stopped --cap-add=NET_RAW --env TS_AUTHKEY=[AUTH KEY] --env TS_EXTRA_ARGS=--advertise-exit-node --env TS_ROUTES=[SUBNET] tailscale/tailscale
```


sudo ip tuntap add dev tun0 mode tun
sudo ip addr add 10.0.0.1/24 dev tun0
sudo ip link set up dev tun0


## External Resources

* <https://hub.docker.com/r/tailscale/tailscale>
* <https://www.wundertech.net/how-to-set-up-tailscale-on-docker/>
* <https://tailscale.com/kb/1184/docker-desktop/>
* <https://tailscale.com/kb/1282/docker/>
* <https://tailscale.com/blog/kubecon-21/>


### TUN devices

* <https://www.baeldung.com/linux/tun-interface-purpose>
    * [OSI Model](https://www.baeldung.com/cs/osi-model)
* <https://stackoverflow.com/questions/59451531/how-to-create-tun-interface-inside-docker-container-image>
* <https://www.kernel.org/doc/html/latest/networking/tuntap.html>
* <https://stackoverflow.com/questions/17529345/ubuntu-remove-network-tap-interface>

### Docker Compose

* <https://docs.docker.com/compose/environment-variables/set-environment-variables/>
* <https://docs.docker.com/engine/reference/commandline/run/>
* <https://docs.docker.com/compose/compose-file/compose-file-v3/>

### Do it yourself

* <https://rnorth.org/tailscale-docker/>
* <https://www.reddit.com/r/Tailscale/comments/w8gda3/official_docker_image_with_subnet_routing/>
* <https://hub.docker.com/r/fastandfearless/tailscale/dockerfile>
* <https://forum.level1techs.com/t/truenas-scale-ultimate-home-setup-incl-tailscale/186444/3>
* <https://pastebin.com/vC2vzyjG>
* <https://www.reddit.com/r/Tailscale/comments/103ib0a/tailscale_on_portainer_via_stack/>
* jonohill
    * <https://github.com/hillnz/docker-tailscale>
    * <https://hub.docker.com/r/jonoh/tailscale>