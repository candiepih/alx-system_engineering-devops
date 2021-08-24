# Web stack debugging #1

![image](https://user-images.githubusercontent.com/44834632/130576818-d55f773a-83cb-4229-a464-fc033123f919.png)


Aim of this section was to understand web stack debugging, network basics and nginx and how its used. Also find and determine fixes to given nginx server.

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

On seeing on `Failed to connect to 0 port 80: Connection refused` i figured that there must be 2 problems, either the port is being used by another process or nginx is not currently configured to run on port 80.

After running `netstat -lpn` found that nginx was running and listening to port 8080. So the problem now was nginx wasn't listening on the required port.

So now I had to fix nginx to run on the right port.

Nginx `/ect/nginx/nginx.conf` config file was Ok, also `/etc/nginx/sites-available/default` was OK. After checking `/etc/nginx/sites-enabled/default` I found out that it was  configured to run on port 8080 which wasn't the desired port. After changing ports from 8080 to 80, saved file and restarted nginx, everything was running fine as below.

```.sh
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#

```
