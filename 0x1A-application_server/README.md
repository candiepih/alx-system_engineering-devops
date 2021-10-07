# Application server

![image](https://user-images.githubusercontent.com/44834632/136392310-4920a79f-120e-4d20-affa-dc8b9cced2eb.png)

Aim of this topic was to understand the following concepts:-

* Application server vs web server
* How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 
* Running Gunicorn
* Difference between server and a web server.

# Background Context

Web infrastructure is already serving web pages via `Nginx` that was installed in the first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project we will add this piece to our infrastructure, plug it to `Nginx` and make is serve Airbnb clone project.
