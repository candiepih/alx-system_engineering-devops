# Webstack monitoring

Topics aim was to understand the following concepts:-

* What is monitoring
* Waht is a server
* Why is monitoring needed
* What are the 2 main area of monitoring
* What are access logs for a web server (such as Nginx)
* What are error logs for a web server (such as Nginx)
* Using [Datadog](https://www.datadoghq.com/) for monitoring

![image](https://user-images.githubusercontent.com/44834632/135334052-17017594-1404-4a9b-be1e-8169f3b51cc8.png)

## Background Context

*“You cannot fix or improve what you cannot measure”* is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

* Application monitoring: getting data about your running software and making sure it is behaving as expected
* Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

# Files

The following task files were used to test understanding on the concepts.

[2-setup_datadog](./2-setup_datadog)

Using [Datadog](https://www.datadoghq.com/) create a dashboard with different metrics displayed in order to get a few different visualizations.

Requirements:-

* Create a new `dashboard`
* Add at least 4 `widgets` to your dashboard. They can be of any type and monitor whatever you’d like
* Create the answer file `2-setup_datadog` which has the `dashboard_id` on the first line. Note: in order to get the id of your dashboard, you may need to use [Datadog’s API](https://docs.datadoghq.com/api/latest/dashboards/#get-all-dashboards)
