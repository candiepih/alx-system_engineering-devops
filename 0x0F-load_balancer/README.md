# Load balancer

Aim of this topic was to understand the following concepts:-

* What Load-balancing is and Load-balancing algorithms 
* Web stack debugging
* Load balancing and HAproxy
* HTTP header
* How to install HAproxy on ubuntu machine



![image](https://user-images.githubusercontent.com/44834632/130483718-e2652c7a-3577-49cd-87a1-d950fee5f553.png)


# Background Context

Given 2 additional servers:

* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
* gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

We mprove our web stack so that there is `redundancy` for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

# Files

The following task files were used for various tasks:-

[0-custom_http_response_header](./0-custom_http_response_header)

Script that configures `web-02` to be identical to `web-01`.

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:-

Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)

* The name of the custom HTTP header must be `X-Served-By`
* The value of the custom HTTP header must be the hostname of the server Nginx is running on

[1-install_load_balancer](./1-install_load_balancer)

Script that installs and configures HAproxy on `lb-01` server.

Requirements:

* Configure HAproxy with version equal or greater than 1.5 so that it send traffic to `web-01` and `web-02`
* Distribute requests using a roundrobin algorithm
* Make sure that HAproxy can be managed via an init script
* Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`

[2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp)

Just as in [0-custom_http_response_header](./0-custom_http_response_header), we automate the task of creating a custom HTTP header response, but with Puppet.

* The name of the custom HTTP header must be `X-Served-By`
* The value of the custom HTTP header must be the hostname of the server Nginx is running on
