# Application server

![image](https://user-images.githubusercontent.com/44834632/136392310-4920a79f-120e-4d20-affa-dc8b9cced2eb.png)

Aim of this topic was to understand the following concepts:-

* Application server vs web server
* How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 
* Running Gunicorn
* Difference between server and a web server.

# Background Context

Web infrastructure is already serving web pages via `Nginx` that was installed in the first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project we will add this piece to our infrastructure, plug it to `Nginx` and make is serve Airbnb clone project.

# Files

The following task files were used to test understanding on the concepts

[2-app_server-nginx_config](./2-app_server-nginx_config)

`Nginx` onfiguration file to serve page from the route `/airbnb-onepage/`:-

Requirements:

* `Nginx` must serve this page both locally and on its public IP on port `80`.
* `Nginx` should proxy requests to the process listening on port `5000`.

[3-app_server-nginx_config](./3-app_server-nginx_config)

`Nginx` onfiguration file to serve page from the route /airbnb-dynamic/number_odd_or_even/(any integer). `/number_odd_or_even/<int:n>` route is defined in the flask app.

Requirements:

* `Nginx` must serve this page both locally and on its public IP on port `80`.
* `Nginx` should proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` the process listening on port `5001`.

[4-app_server-nginx_config](./4-app_server-nginx_config)

`Nginx` configuration file that serves what was built for [AirBnB clone v3 - RESTful API](https://github.com/candiepih/AirBnB_clone_v3) on `web-01`

Requirements:

* Setup `Nginx` so that the route `/api/` points to a Gunicorn instance listening on port `5002`
* `Nginx` must serve this page both locally and on its public IP on port `80`
* To test your setup you should bind Gunicorn to `api/v1/app.py`

[dump.sql](./dump.sql)

SQL dump file used to populate database with data.
