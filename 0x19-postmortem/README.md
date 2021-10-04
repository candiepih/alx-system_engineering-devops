# Issue Summary

Website's mailing service received downtime which was encoutered on 01/10/2021 at 10:37 A.M EAT and recovered same day at 10:45 A.M EAT, causing 8 minutes service inaccessibility to 4% of the website clients visiting the website within the downtime range. Clients received an error 404(Not Found) when visiting website's /mail route usually used for the mailing system. Root cause of this problem was route mistype, expecting route as /mail instead of /mial.

# Timeline (01/10/2021)

10:37 A.M (EAT) - Deployed flask update when one of the developers noticed /mail route wasn't returning /mail page.
10:38 A.M (EAT) - Troubleshooting of issue, starting from the webpage where the route path was /mail which was OK.
10:40 A.M (EAT) - Checking of the paths on the flask routes blueprint discovering /mial the mistyped route.
10:42 A.M (EAT) - Fixing the typo to the intended /mail route.
10:43 A.M (EAT) - Testing in development to ensure /mail is working as intended
10:45 A.M (EAT) - Redeployed flask update ensuring service back to normal.

# Root cause and resolution

Root cause of this problem was route typo, expecting route as /mail instead of /mial. According to links on the webpage the desired path to access the mail page was intended to be /mail. So on the webpage we were trying to access /mail whose route didn't exist on the flask framework. To fix this issue this typo had to be changed manually typing the correct route(/mail) in the code. Testing had to be done to ensure path was working before redeploying the code.

# Corrective and preventative measures 

To prevent such an issue from occuring again in future we had to ensure that however small a change on the code is, all the code should undergo testing before deploying ensuring continuous service to the clients on the webpage. Some of the tasks to address this issue in future are: Adding a monitoring service to the servers to report server metrics and information in realtime, running tests on code to ensure that it's working as intended and not breaking other areas while fixing others and setting up isolated servers for testing purposes.
