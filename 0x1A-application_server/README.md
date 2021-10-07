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

`Nginx` configuration file that serves what was built for [AirBnB clone v3 - RESTful API](https://github.com/candiepih/AirBnB_clone_v3/tree/main/api) on `web-01`

Requirements:

* Setup `Nginx` so that the route `/api/` points to a Gunicorn instance listening on port `5002`
* `Nginx` must serve this page both locally and on its public IP on port `80`
* To test your setup you should bind Gunicorn to `api/v1/app.py`

[dump.sql](./dump.sql)

SQL dump file used to populate database with data.

[5-app_server-nginx_config](./5-app_server-nginx_config)

`Nginx` configuration file that serves what was built for [AirBnB clone - Web dynamic](https://github.com/candiepih/AirBnB_clone_v4/tree/master/web_dynamic) on `web-01`

Requirements:

* Your Gunicorn instance should serve content from `web_dynamic/2-hbnb.py` on port `5003`
* Setup Nginx so that the route `/` points to your `Gunicorn` instance
* Setup Nginx so that it properly serves the static assets found in `web_dynamic/static/` (this is essential for page to render properly)
* For your website to be fully functional, you will need to reconfigure `web_dynamic/static/scripts/2-hbnb.js` to the correct IP
* Nginx must serve this page both locally and on its public IP and port `5003`
* Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors

[gunicorn.service](./gunicorn.service)

`systemd` script which starts a `Gunicorn` process to serve the same content as the previous task (`web_dynamic/2-hbnb.py`)

Requirements:

* The Gunicorn process should spawn 3 worker processes
* The process should log errors in /tmp/airbnb-error.log
* The process should log access in /tmp/airbnb-access.log
* The process should be bound to port 5003
* Your systemd script should be stored in the appropriate directory on `web-01`
* Make sure that you start the systemd service and leave it running
