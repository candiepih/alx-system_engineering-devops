# Web stack debugging #0

This topic's aim was to understand the following concepts:-

* Network basics
* What docker is and it's uses.
* Wha web stack debugging is.
* usage of `curl`

# FILES

The below task files helped in testing understanding on the concepts:-

[0-give_me_a_page](./0-give_me_a_page)

Contains commands that were used to configure apache server to run on port 8080 and return desired page when querying.

Requirements

* Setup an apache server to run on the container and to return a page containing `Hello Holberton` when querying the root of it.
* curl the port `8080` mapped to the Docker container port `80`

This is how i was able to debug:-

1. When trying to `curl 0:8080` for the first time an error like `curl: (7) Failed to connect to 0 port 8080: Connection refused` appears which is probably apache isn't running or port 8080 isn't available. In my case apache wasn't started so i restarted it with command `sudo service apache2 restart`.
2. Now if you try again to `curl 0:8080` you might get the same error, but this time probably the port 8080 to listen to is unavailable. This is configured by adding a `Listen 8080` to /etc/apache2/ports.conf apache ports config file. Changing the file means also adding other change to virtualhost file. By editing Virtualhost to have `*:8080`.
3. After success on 2nd step, trying again to `curl 0:8080` gives the following output:-

```.sh

vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$

```
