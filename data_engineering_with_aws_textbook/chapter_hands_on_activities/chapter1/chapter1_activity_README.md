<h2>Chapter 1 Hands-on Activity: Creating and Accessing AWS Account</h2>


* Some of the services used in this book will fall under AWS Free Tier usage, and some will not.
  * Set up budget alerts within your account.
* Note that you can re-use an existing email address to set up an AWS account by using the "+" symbol in your email. 
  For example, `test@email.com` and `test+de@email.com` are considered two different email addresses, but emails 
  will still arrive at the primary email account.
  * I used this to get another 12 months of free tier for this new account.


<h3>Account Best Practices</h3>

* Do not use the <i>root user</i> unless absolutely necessary (e.g., creating your first IAM user, deleting the 
  account, or changing account settings).
* Create an `Admin` user for day-to-day activities.
* Strongly recommended to set up <b>Multi-Factor Authentication (MFA)</b> on root account and other administrative 
  accounts.


<h3>Region Selection Considerations</h3>

* Which region should you use?
  * Refer to this [AWS blog post](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/).
  * In summary, use the following four areas to determine region:
1. <b>Compliance</b> (laws and regulations)
2. <b>Latency</b> (proximity to users)
3. <b>Cost</b> (varies by region)
4. <b>Services and features</b> (offerings differ by region)
* If the workload is bound by any regulations, shortlist the Regions that are compliant. Measure the network latency 
  between each Region and the location of the user base. Estimate the workload cost for each Region. Check that the 
  shortlisted Regions have the services and features your workload requires. And finally, determine if your workload
  can benefit from running in multiple Regions.

