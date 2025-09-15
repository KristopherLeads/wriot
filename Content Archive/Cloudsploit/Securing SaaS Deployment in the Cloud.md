# Securing SaaS Deployment in the Cloud
SaaS, or Software as a Service, has become an integral part of most enterprise solutions. The principle is relatively simple and sound - but with anything that is simply done, it can be done woefully incorrectly, resulting in major damage, loss of revenue, and breach of security. Accordingly, SaaS providers and enterprise users leveraging SaaS solutions must be proactive in their security.

On this post, we’re going to talk about SaaS security. We’ll discuss what SaaS actually is, and how it differs from other “as a service” cloud types. We’ll also discuss some basic security holes that are common in SaaS applications, and how to properly deal with them.

## What is SaaS?

Broadly speaking, there are a handful of “as a service” types of cloud choices. While there are a great many other niche “as a service” types, we’re only going to cover the general “big three” today - IaaS, PaaS, and SaaS.

IaaS, or Infrastructure as a Service, is a type of cloud provision in which all of the infrastructure typically held locally by an enterprise is instead rented from a provider. These resources include things like the operating systems, data pipelines, and storage media. Some major examples of this would include AWS, DigitalOcean, and Microsoft Azure.

PaaS, or Platform as a Service, provides a much more specific type of cloud provision. PaaS solutions offer the actual platform upon which applications are developed and run as a service - in other words, you are renting a platform rather than the underlying infrastructure. Some major examples of this would include Heroku, AWS Elastic Beanstalk, and OpenShift.

SaaS, or Software as a Service, is perhaps the best known of the cloud provision types in this piece. SaaS implementations offer specific software solutions to the end user, typically as part of a licensed suite of services. Sometimes these are a la carte, other times they are offered as packages for enterprise integration. Some major examples of this would include Salesforce, Dropbox, and Google Apps like Hangouts, Gmail, etc.

## What Security Concerns Exist Specifically Around SaaS?

Let’s look at some SaaS specific security concerns. SaaS by its very nature has any and all data acted upon routed through external servers - everything is done in the cloud, which seems like an obvious statement, but is an overlooked part of the equation when faced with the magic of “the cloud”. Accordingly, enterprise data, that highly-valued, highly-coveted data that is the fundamental revenue underpinning most businesses, is made vulnerable during this step.

SaaS data transfer and storage doesn’t stop there, either. IN many cases, the SaaS data could be transformed, bucketed with other data, and pushed off into other IaaS providers whom the SaaS might be partnered with. In this case, your data is now replicated, shared, and worked upon by multiple different entities, which drastically increases both risk and surface area for attack.

There are also concerns over what kind of data is being handled by the SaaS in question. By using SaaS, you are implicitly trusting its provider - as such, you are also trusting their credentials, their valid authorization, and any other promises towards data security. This includes things like ensuring that your SaaS provider is trustworthy when it comes to HIPAA, GDPR, and other kinds of regulated data. In many cases this trust is proper, but in some cases, smaller SaaS providers may not be tested and proven, which makes integration all the more worrisome.

## Solutions for SaaS Security

SaaS applications require some specialized solutions, but once adopted, they can be easily maintained and utilized for greater data security and transportability.

First and foremost, SaaS integrations need to be planned, understood, and contextualized. There’s often a certain amount of desire to simply adopt the shiniest, brightest, and newest solution on the market. This is exactly the wrong approach here, as you should only adopt vetted and proven applications. 

As part of this, you should also design and implement a secure method of deployment, especially if the SaaS solution is being adopted into an enterprise. Ensuring that only those accounts which require access, read, write, and comment permissions on relevant data, functions, or processes can go a very long way to securing the underlying functional systems.

Ensure as well that any certifications relevant to your data or data processing are met and verified. Data is not just data - some of it is qualified, and some of it is covered by rigorous, often intense regulatory agreements and oversight bodies. Thus, while you may be HIPAA compliant, if your SaaS provider is not, you are creating data insecurity (to say nothing of the legal concerns this situation would create).

Finally, and most importantly, your data should be encrypted from end to end. You can still leverage SaaS applications without exposing the data to the open web - in the modern cloud space, this can quickly become a very real possibility, so encryption is paramount. Utilizing SSL transmission will ensure data is kept private and secure.

## Conclusion

Of course, none of this matters if server configurations are incorrect, and you are breaking everything at the locally-owned transit level. For this reason, scanning configurations using a solution like Cloudsploit will solve many commonly overlooked woes, providing better security and efficiency. Once these policies are put into place, and the underlying configuration and transit systems tested, verified, and secured, SaaS can be leveraged to do amazing things - you just need to put in the work to ensure that value is not lost to data loss, theft, or destruction.
