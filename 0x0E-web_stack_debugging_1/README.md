# Web stack debugging #1

Aim of this section was to understand web stack debugging, network basics and nginx and how its used.

![image](https://user-images.githubusercontent.com/44834632/130576818-d55f773a-83cb-4229-a464-fc033123f919.png)

# Files

Below task files were used for this project.

[0-nginx_likes_port_80](./0-nginx_likes_port_80)

In this task using my debugging skills it's required to find out what’s keeping the Ubuntu container’s Nginx installation from listening on port 80.

Requirements:

* ginx must be running, and listening on port `80` of all the server’s active IPv4 IPs
* Write a Bash script that configures a server to the above requirements

This is how i debugged :)

First time you make request you get the following

```.sh

root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#

```
