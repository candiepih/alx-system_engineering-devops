# Networking basics #0

This topic was aimed at understanding various networking concepts such as:_

* what is the OSI model layers it has and how it's organized
* what the LAN is it's typical usage and it's typical geographical size
* what the WAN is it's typical usage and it's typical geographical size
* What is the Internet
* What is an IP address
* What are the 2 types of IP address
* What is localhost
* What is a subnet
* Why IPv6 was created

* TCP/UDP
* What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
* difference between TCP and UDP
* What is a port
* Memorizing SSH, HTTP and HTTPS port numbers
* What tool/protocol is often used to check if a device is connected to a network

Below task files helped testing my understanding on the various concepts

[0-OSI_model](../0x07-networking_basics/0-OSI_model)

Tests for 2 questions. Answers are in this file with the answer being the number of answer from questions

Qsn1:

What is the OSI model?

1. Set of specifications that network hardware manufacturers must respect
2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

Qsn2:

How is the OSI model organized?

1. Alphabetically
2. From the lowest to the highest level
3. Randomly

[1-types_of_network](../0x07-networking_basics/1-types_of_network)

Tests for 3 questions. Answers are in this file with the answer being the number of answer from questions

Qsn1:

What type of network a computer in local is connected to?

1. Internet
2. WAN
3. LAN

Qsn2:

What type of network could connect an office in one building to another office in a building a few streets away?

1. Internet
2. WAN
3. LAN

Qsn3:

What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?

1. Internet
2. WAN
3. LAN

[2-MAC_and_IP_address](../0x07-networking_basics/2-MAC_and_IP_address)

Tests for 2 questions. Answers are in this file with the answer being the number of answer from questions

Qsn1:

What is a MAC address?

1. The name of a network interface
2. The unique identifier of a network interface
3. A network interface

Qsn2:

What is an IP address?

1. Is to devices connected to a network what postal address is to houses
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks

[3-UDP_and_TCP](../0x07-networking_basics/3-UDP_and_TCP)

Tests for 3 questions. Answers are in this file with the answer being the number of answer from questions

Qsn1:

Which statement is correct for the TCP box

1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Qsn2:

Which statement is correct for the UDP box:

1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Qsn3:

1. Which statement is correct for the TCP worker:
2. Have you received boxes x, y, z?
3. May I increase the rate at which I am sending you boxes?

[4-TCP_and_UDP_ports](../0x07-networking_basics/4-TCP_and_UDP_ports)

script that displays listening ports:
* That only shows listening sockets
* That shows the PID and name of the program to which each socket belongs

[5-is_the_host_on_the_network](../0x07-networking_basics/5-is_the_host_on_the_network)

Bash script that pings an IP address passed as an argument.

Requirements:
* Accepts a string as an argument
* Displays `Usage: 5-is_the_host_on_the_network {IP_ADDRESS}` if no argument passed
* Ping the IP 5 times
