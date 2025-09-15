# Security in Isolation - Why a Holistic Approach is Best

One of the chief problems faced by technically savvy administrators and developers is the fact that their skill is highly specialized. This can lead to great gains, which is obvious, but it can also lead to great potential loss. Being too specialized tends to focus the lens of attention away from generalities and into a very myopic view of singular problems, singular concerns, and singular threats.

This is often leads to security in isolation – in effect, the expertise held by these highly specialized people, while leading to great gains in their specific product, leads to a short-sighted, laser focused security application which may lead other areas of the implementation to be more insecure. In order to demonstrate this point, let’s look at some highly specific security issues for some specific types of provision.

## IaaS Offerings

IaaS, or Infrastructure as a Service, is a type of offering in which the underlying network resources are rented, rather than the things built atop them. AWS is a good example of this type of service – network data is rate limited, allowing for functions to exist in an economically controlled amount as these resources are required. These types of offerings are core to the modern tech landscape, and as such, they are the most often specialized-upon type of offering.

Two security risks in this arena include:

* Misconfiguration - because IaaS services are typically open-ended, allowing access as long as it comes from the client’s specific data stream, misconfiguration can harm this offering pretty severely. Simple misconfigurations can result in the transit stream being able to be read by anyone, interacted with by anyone, and affected by anyone.
* Data escape - many IaaS providers offer their infrastructure in a simulated way. IaaS provisions may include a virtual server or container. A chief concern here is that an attacker (or even a fellow consumer) might find a way to break out of this constraint, and access other data on the same physical system that the digital product occupied.
* Cost Overrun - it is possible that, through vector attacks focusing on technically-allowed but practically-harmful function usage, that an IaaS service user could be faced with cost overruns. This is akin to an economic DDoS, wherein the amount charged for such services will be astronomical, and are often to serve a function that is, in itself, designed not to be useful, but to be expensive.

## SaaS Offerings

SaaS, or Software as a Service, is an offering in which the software is provided via an interface or virtualized GUI over the line. These types of services allow users to access software without requiring extremely powerful local machines, and enhances both collaboration and efficiency. There are some significant security concerns here, however – we are essentially providing an application that has to be extremely powerful for business justification over a connection that must have only the least amount of power to be secure.

This dichotomy has raised a few core issues to SaaS offering security:

* Access and identity control - having user groups and rights assignments that are incorrectly limited or able to escalate one another can lead to more data being accessed than was designed for. In such cases, a user in an improper group may escalate all the way to an admin position, causing excessive harm and damage.
* Application control - in many cases, SaaS offerings are dangerous at their highest potential. Just because that’s true doesn’t mean that every instance of the SaaS offering has to be that way – controlling what the application does, who can invoke that type of function, and what the limits of that function actually is can prevent a lot of attacks hinging on buffer overflows, SQL injection, etc.
* Compliance - when you utilize an SaaS system, you may face issues with ensuring compliance of activity. This can be a problem when working with classified or protected data, and ultimately can be a source of concern for many providers. How, for instance, do you ensure that a SaaS implementation for generating sales leads respects the GDPR? How do you prevent data export? These are serious concerns for this type of implementation.

## PaaS Offerings

PaaS, or Platform as a Service, is an offering which provides the underlying platform for the development, building, and delivery of applications and services via a remote stack. This type of offering is typically used for applications, with examples such as the Google App Engine demonstrating a strong argument for such a remote platform option. Unfortunately, there are some key security concerns with adopting a singular platform that are unique to PaaS itself.

* Vendor Lock-in - because you’re adopting a single platform, this means that the vendor is responsible for most security facets of the underlying architecture. Unfortunately, that also means that, unlike something in the IaaS realm which might have a wide variety of platforms, you are buying in entirely to this vendor doing their due diligence and ensuring comprehensive and accurate security coverage.
* Open Source vs Closed Source - the platform itself can be a source of weakness. In these cases, code issues, flaws, etc., even if they are addressed as part of dealing with vendor lock-in at some point, represent a single flaw that compromises your entire system. You’re essentially, in many cases, putting all your eggs in one basket.

## Conclusion

Ultimately, the best option for dealing with all of these concerns is to adopt a unified, holistic security approach. This necessarily includes looking to holistic security applications. A good product should cover the entire span of offerings utilized by an organization, and should do so with specific security concerns in mind – only by adopting a unified approach can unified security be delivered. 

CloudSploit is working towards this end – providing a holistic, unified security product for the modern industry. As a partner, CloudSploit aims to deliver a crucial part of your holistic security plan – using proper tools, setting proper expectations, and enabling greater understanding will make for a safer stack, a safer application, and a safer world.
