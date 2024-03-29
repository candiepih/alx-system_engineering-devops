# Configuration management

Aim of the topic was understanding configuration management which refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. This topic also helped me understand what puppet is, why it's used, where it's necessary used and how to use it to achieve configuration management.

Below task files were used to test understanding on various concepts:-

[0-create_a_file.pp](./0-create_a_file.pp)

Puppet manifest file that creates a file in `/tmp` using puppet with following requirements.

* File path is `/tmp/holberton`
* File permission is `0744`
* File owner is `www-data`
* File group is `www-data`
* File contains `I love Puppet`


[1-install_a_package.pp](./1-install_a_package.pp)

Puppet manifest file that installs `puppet-lint` with following requirements.

* Install `puppet-lint`
* Version `2.1.1`

[2-execute_a_command.pp](./2-execute_a_command.pp)

Puppet manifest file that kills a process named `killmenow` with following requirements.

* Must use the `exec` Puppet resource
* Must use `pkill`

Terminal #0: example of starting a process

```.sh

root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow

```

Terminal #1: executing [2-execute_a_command.pp](./2-execute_a_command.pp) manifest file

```
root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds

```

Terminal #0: check for process termination

```.sh
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#

```
