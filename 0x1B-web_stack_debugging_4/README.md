# Web stack debugging #4

Topics aim was to understand webstack debugging.

# Files

The following task file was used for this project

[0-the_sky_is_the_limit_not.pp](./0-the_sky_is_the_limit_not.pp)

Puppet file that configures nginx to fix failed requests issue.

By running `ab -c 100 -n 2000 localhost/` we can check the number of request/sec and also the number of failed requests. In my case there's 754 failed request. But we have ensure that nginx servers all the reqeust and bring the failed reqeust number down to 0.

By checking the error log file (`/var/log/nginx/error.log`) of nginx which indicates the following error `34#0: accept4() failed (24: Too many open files)`.
This can be simply fixed by editing the `/etc/default/nginx` file and change the limit to anything higher, in my case 10000. Then restart `nginx`.

Now `nginx` will serve all requests with 0 failed requests.
