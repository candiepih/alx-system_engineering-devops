# Configuration management

Aim of the topic was understanding configuration management which refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. This topic also helped me understand what puppet is, why it's used, where it's necessary used and how to use it to achieve configuration management.

Below task files were used to test understanding on various concepts:-

[0-create_a_file.pp](./0-create_a_file.pp)

Creates a file in `/tmp` using puppet with following requirements.

* File path is `/tmp/holberton`
* File permission is `0744`
* File owner is `www-data`
* File group is `www-data`
* File contains `I love Puppet`

