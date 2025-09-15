# Security - Who Owns the Problem?

Security is a very nebulous term – the term itself is so broadly defined and applied that it’s often hard to narrow down the scope of the conversation. Because of this, where exactly the “problem” of security actually lies is often cloudy. Users feel an immense pressure to handle their security, often imagining a thief in the shadows just waiting for the right opening. Providers often fret about security, seeing millions in fines for data breaches as being just around the corner.

The truth is that our conversations about security are often hampered by a malformed definition of what the security conversation scope actually is. To this end, the question bears repeating – who owns the problem? And more specifically, who holds the responsibility?

That’s exactly what we’re going to address today. Keep in mind that this is a general conversation on security, and your specific implementation, situation, and needs may cause some variance in application – accordingly, this should be treated roughly as a guide, and contextualized accordingly.
## Security Has Two Domains
When we discuss security without specifying scope, we run into all of the problems we’ve laid out. There are two chief domains to security, and both are extremely important – without defining these domains, the responsibility is often hard to pinpoint, and is very commonly levied unfairly on one side as opposed to the other.

In fact, this unfair distribution is chiefly caused by a simple lack of understanding in the nature of these scopes – these are not different domains to security altogether, but instead two halves of a single whole, operating in concert with one another, resulting in a product that is greater than the sum of its parts.

To put it simply – understanding both realms and delegating responsibilities correctly and appropriately is the only way to ensure complete security, and the only way to contextualize this conversation. With that being said, let’s look at these two broad domains.
## The Provider Realm
The provider is really one of two types – either the infrastructure provider, that is the one providing the system and the hardware to drive it, or the middle provider, that is the provider who serves business-to-business functions as a middle node. Regardless of what camp the provider falls in, they have largely the same responsibilities and caveats to consider.

The provider arguably has the largest generalized impact on security due to the structural aspects of their implementation and framework. These implementations and frameworks provide choices to the user, and ultimately include methods of transmission, encryption, protocols, and more. It should be noted that these specific implementations are largely generic, meant to serve the user base as a whole, and even in the case of middle providers, they are largely solution-built implementations rather than purpose-built for a given client.

This ultimately means that the provider has a larger share of generalized responsibility, as it is their system upon which all choices are made. Securing user data, payment information, transmission systems, and more is within the realm of the provider, but is distinct from the more specific and single-task choices made by the user.
## The User Realm
The user by definition does not necessarily have the inherent power of the organization that occupies the provider space – despite this, the user is most responsible for their own security, even beyond those responsibilities of the provider. No matter how good the implementation, the “make it or break it” moments and choices reside in this space, and therefore the user is most responsible for their own, localized security.

A good analogy for this difference is to consider the security situation akin to a castle. The provider serves the functions of the outer walls and moat, providing a foundation upon which all security is built. The walls and moat is not concerned with the security of individual gates and people, though. The user this is like the average gate guard, responsible for securing their corner of the world, their access to the system, and their own personal assets.

In the same way, while the provider is responsible for giving the system as a whole to the user, the user specifically is responsible in a much more personal, directed way.
## Where Responsibility Lies
The truth is that nobody has an ultimate responsibility, despite the relative speed that the opposite is claimed in the industry. This speed to claim as such is largely because we only discuss half of the problem, when the reality is that security requires a more holistic, complete consideration, and a larger understanding of the scopes of such responsibilities.

Put simply, the user is responsible for security within the scope of their own implementation and systems, and ultimately, the “buck stops there” for their own solution. Their choices in configuration, judgements in level of security, and ultimate understanding of their ecosystem is going to define a relatively strict scope of responsibility that the provider does not even begin to broach.

The provider more generally is responsible for a global scope, offering the tools and systems by which the user can make such choices. They are responsible for those tools, and those tools only, though education on using those tools quickly become a responsibility of marketing and informative efforts. The user scope is local, but the provider scope is global.
## Implementation as a Responsibility
The core point of this entire argument is a simple statement – “security is only as good as its implementation”. The most perfectly designed provider system is going to fail the second it is improperly set up and configured – and as a counterpoint, even the most poorly designed security system will function more accurately and effectively if properly configured when paired against such a poorly configured system in the long run.

With this in mind, here are a few suggestions to keep at heart when considering security:

* Effective communication is the responsibility of the provider. Give information and training for how to run the situation and implementation you offer. While this is generally considered the scope of the user, their choices can have long-term effects on the global security of your system, and as such, you owe it to your other users to at least attempt to educate those who need it.
* Configuration is both the strongest and weakest point in a system. A bad system properly configured with be better than a great system improperly configured. Accordingly, users should understand that configuration and usability is much more important than theoretical security applications.
* Users should evaluate honestly their level of knowledge. Most users are unable to handle massive configuration systems and complex frontends, and as such, these users should be aware that third party configuration testing and management systems are likely their best bet. While some systems can be learned over time, it’s better to verify configuration and learn from a proper setup example than to try and “wing it” and figure it out as you go along.
* Those castle walls both keep things in and keep things out – the provider can only do so much, and their scope is global in scale. The user is the ultimate source of security for their local resources, and this should always be kept in mind when making any configuration or application choice.

With these simple suggestions, security can be viewed holistically and, at least in terms of scope, completely. Failing to understand these key points and failure to accurately view scope is not a simple matter of lost effectiveness or inefficiency – in some applications, it can mean total system failure. Accordingly, take this to heart, and do the best you can with whatever you can in your little corner of the internet.
