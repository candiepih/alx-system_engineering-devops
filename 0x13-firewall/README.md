# Firewall

This topic's aim was to understand the following concepts:-

* What a firewall is
* Using telnet to check if sockets are open with `telnet IP PORT`
* Using `iptables` and `ufw` to check if the server has the correct firewall rules

# Files

The following files were used to test understanding on the concepts of this topic.

[0-block_all_incoming_traffic_but](./0-block_all_incoming_traffic_but)

Contains commands to install the ufw firewall and setup a few rules on web-01.

Requirements:

* The requirements below must be applied to `web-01`
* Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
  * 22 (SSH)
  * 443 (HTTPS SSL)
  * 80 (HTTP)

[100-port_forwarding](./100-port_forwarding)

Firewalls can not only filter requests, they can also forward them.

Requirements:

* Configure `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP`.
* This task file is a copy of the `ufw` configuration file that is modified to make this happen
