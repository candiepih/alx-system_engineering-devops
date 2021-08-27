# HTTPS SSL

This topic was aimed at understanding the following concepts:-

* What is HTTPS?
* What are the 2 main elements that SSL is providing
* HAProxy SSL termination on Ubuntu16.04
* SSL termination
* Bash function

# FILES
The following task files were used to test understanding on the various concepts

[0-world_wide_web](./0-world_wide_web)

Configures [domain](https://toolit.tech) zone so that the subdomain `www` points to load-balancer IP (`lb-01`).
* Add the subdomain www to your domain, point it to your `lb-01 IP` (your domain name might be configured with default subdomains, feel free to remove them)
* Add the subdomain `lb-01` to your domain, point it to your `lb-01 IP`
* Add the subdomain `web-01` to your domain, point it to your `web-01 IP`
* Add the subdomain `web-02` to your domain, point it to your `web-02 IP`

script must accept 2 arguments:

`domain`:
* type: string
* what: domain name to audit
* mandatory: yes


`subdomain`:
* type: string
* what: specific subdomain to audit
* mandatory: no


* Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
* When only the parameter domain is provided, display information for its subdomains `www, lb-01, web-01 and web-02` - in this specific order
* When passing domain and subdomain parameters, display information for the specified subdomain
* Ignore `shellcheck` case `SC2086`

[1-haproxy_ssl_termination](./1-haproxy_ssl_termination)

Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www.`.

Requirements:

* HAproxy must be listening on port TCP 443
* HAproxy must be accepting SSL traffic
* HAproxy must serve encrypted traffic that will return the `/` of your web server
* When querying the root of your domain name, the page returned must contain `Holberton School`
* Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

This file is HAproxy configuration file

[100-redirect_http_to_https](./100-redirect_http_to_https)

This file is HAproxy configuration file that has Configured HAproxy to automatically redirect HTTP traffic to HTTPS.
Requirements:

* HAproxy should return a 301
* HAproxy should redirect HTTP traffic to HTTPS
