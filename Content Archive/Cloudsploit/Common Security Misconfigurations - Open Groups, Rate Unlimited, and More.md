# Common Security Misconfigurations - Open Groups, Rate Unlimited, and More
When popular media discusses data breaches, leaks, or exposures, the narrative is often around “hacking” or “breaking into” systems. The reality is that this is actually a very small percentage of the data exposure incidents in the global community - in fact, hacked content is much less common than simple exposed content, with some of the largest data exposures in recent memory being due to misconfiguration. In the first quarter of 2019 alone, billions - yes, billions with a “b” - of records were exposed by various advertising organizations, combo list generators, and marketing groups due to simple misconfigurations which allowed external users to contact internal databases.

That’s a far cry from a “hack” - this data wasn’t broken into by an expertly skilled hacker, this data was exposed because of simple misconfiguration, especially when it came to AWS and general MongoDB services.

This is the reality we are going to talk about today. Most data breaches come from misconfigurations - therefore, knowing these misconfigurations is a big first step to stopping them from becoming a major problem.

## Unsecured Databases

Perhaps the most common and obvious of this list, having an unsecured database is the worst possible situation a database administrator can imagine. Unfortunately, as impactful as this is, it’s incredibly easy to do without even noticing. Because many database packages default to unencrypted, open connections without password requirements, many database providers find themselves setting up a fundamentally insecure server without ever knowing it - this is especially true if the server in question is spun up on an external service purely for staging or testing purposes.

While there is some headway being made towards fixing this, the problem is fundamental in the nature of the solution. A good practice is to ensure that every piece of data in your ecosystem is protected as if it’s vitally important, regardless of content - this means encryption at rest, encryption during transport, and authenticated access only. This is not true for every single use case, but as a common practice, it is advisable.

## Rate Unlimited Access

Another common vulnerability lies in the rate limiting of the resource - or, in this case, the lack of rate limiting. Simply put, the process of rate limiting ensures that only those who are requesting the resources are allowed a stemmed amount of access - that is, a limited rate of requests, calls, and general interactions. For a given server, rate limits might state that only 1k requests of a specific size can be made per hour - this protects both the integrity of the system by preventing DDoS or other types of flooding attacks as well as the integrity of the data, preventing buffer overflows and other errors that come with unmitigated data flow.

Therein lies the problem - when there is no rate limiting, the service experiences access akin to a firehose. Anyone and everyone can send anything they want at any rate they want, resulting in either the system breaking or additional resources being spun up to support the load, which in turn causes drastic cost runup.

The solution is to limit access, of course, but there are issues with this approach - when a client legitimately needs more access, how this is handled, how this data is segmented from other data being requested, and how the rate flow is ensured are all important variables that add complexity and points of failure to the system.

## Open Groups

When dealing with core group access to a resource, it’s important to remember that the rights of the group are just as important as to how someone joins that group - in other words, limiting power to only a set user group only works if that user group has an exclusive membership process. Open group errors are when stated groups are allowed to either immediately enter the system as that group or a user is able to upgrade their rights to that group without oversight. This is commonly also called “privilege escalation”.

As an example, say a user enters your server as a basic User class. If you have no methods to prevent their promotion, or even if you do have such methods but you have one method in error that allows a user to take advantage of said error, a simple User could promote themselves into the Administrator class, accessing resources and commands that the original designer never meant them to be able to access.

The solution is to close groups, but keep in mind that some groups do need to be able to self promote in certain circumstances. Support staff, for instance, might need to temporarily self-promote given delegated authentication during times of emergency - in these cases, this self promotion should be authenticated and guided, not an outright ability that can be invoked at any time.

## Lack of Sanitation

In computer terms, sanitation is the process of removing potentially harmful aspects of a piece of data during input in order to ensure no errors are caused. There are certain characters, phrases, or words that, when invoked in a computer system, can cause damage and absolutely wreck an internal system for data management.

Failure to sanitize results in some pretty significant issues. For instance, if a user is able to register using a command specifically designed to cause table issues (see https://xkcd.com/327/ for a classic example), your entire database can be ruined in a matter of minutes.

The solution is to enforce sanitation. Strip all entry of characters, phrases, and other combinations known to be possible for this type of attack. Strip out numbers if text is expected, and vice-versa - or simply enforce input type. Limiting to a certain length, though restrictive on your users, is also effective at combating this type of attack.

## Automatic Detection

All told, much of this is simple to fix - but also simple to make the mistake in the first place. Services like Cloudsploit go a long way towards automatically detecting many of these issues, but as with any tool, proactive management is the first step towards effective implementation. Applying lessons learned around these simple error examples can go a long way towards securing your servers, your data, and your services.
