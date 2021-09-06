# Web stack debugging #2

Task was aimed at understanding web-stack debugging and how we can run commands and services as other users.

# Files

Following task files were used to test understanding on the concepts

[0-iamsomeoneelse](./0-iamsomeoneelse)

* Bash script that accepts one argument
* The script should run the whoami command under the user passed as an argument

[1-run_nginx_as_nginx](./1-run_nginx_as_nginx)

Script fixes container so that Nginx is running as the nginx user.

Requirements:

* `nginx` must be running as `nginx` user
* `nginx` must be listening on all active IPs on port `8080`
* You cannot use `apt-get remove`

[100-fix_in_7_lines_or_less](./100-fix_in_7_lines_or_less)

Short version of [1-run_nginx_as_nginx](./1-run_nginx_as_nginx). Short and sweet.

Requirements:

* Your Bash script must be 7 lines long or less
* There must be a new line at the end of the file
* You respect Bash script requirements
* You cannot use `;`
* You cannot use `&&`
* You cannot use `wget`
* You cannot execute your previous answer file (Do not include the name of the previous script in this one)
