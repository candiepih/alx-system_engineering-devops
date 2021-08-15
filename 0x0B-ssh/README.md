# SSH

Aim of topic was to understand the following:-

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

The following task files helped in testing understanding on topic

[0-use_a_private_key](./0-use_a_private_key)

Bash script that uses ssh to connect to server using the private key `~/.ssh/holberton` with the user `ubuntu`

[1-create_ssh_key_pair](./1-create_ssh_key_pair)

Bash script that creates an RSA key pair.

Requirements:-

* ame of the created private key must be `holberton`
* Number of bits in the created key to be created `4096`
* The created key must be protected by the passphrase `betty`

[2-ssh_config](./2-ssh_config)

SSH configuraton to my ubuntu Vagrant machine file to suit our need to connect to a server without typing a password

[100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp)

Puppet manifest file that make changes to `/etc/ssh/sshd_config` configuration file

Requrements:
* Configuration must be configured to use the private key `~/.ssh/holberton`
* Configuration must be configured to refuse to authenticate using a password

