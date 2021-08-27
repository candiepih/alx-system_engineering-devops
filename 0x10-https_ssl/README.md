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
