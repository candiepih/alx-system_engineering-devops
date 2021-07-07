# Networking basics #1

This topic was aimed at understanding networking basics and its concepts like:-

* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine’s active network interfaces

Below task files helped in testing my understanding on various concepts on the above learning objectives

[0-change_your_home_IP](../0x08-networking_basics_2/0-change_your_home_IP)

Bash script that configures an Ubuntu server with the below requirements.

* localhost resolves to `127.0.0.2`
* facebook.com resolves to `8.8.8.8`


[1-show_attached_IPs](../0x08-networking_basics_2/1-show_attached_IPs)

Bash script that displays all active IPv4 IPs on the machine it’s executed on.

[100-port_listening_on_localhost](../0x08-networking_basics_2/100-port_listening_on_localhost)

Bash script that listens on port `98` on `localhost`.

### Terminal 0

Starting my script.

```

$ sudo ./100-port_listening_on_localhost

```

### Terminal 1

Connecting to localhost on port 98 using telnet and typing some text.

```

$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test

```

### Terminal 0

Receiving the text on the other side.

```

$ sudo ./100-port_listening_on_localhost
Hello world
test

```

For the sake of the exercise, this connection is made entirely within `localhost`. This isn’t really exciting as is, but we can use this script across networks as well. 
