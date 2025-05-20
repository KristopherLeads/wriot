# Success vs. Failure – The Importance of API Metrics
* Author: Kristopher Sandoval
* Original Publish Date: 4/28/2015
* Origin: Nordic APIs
* Link: https://nordicapis.com/success-vs-failure-the-importance-of-api-metrics/

Success and failure are relatively subjective terms — what defines success for one business might be considered a failure for another, and the relative of success in certain areas of performance can change from industry to industry, department to department, and even on a [case to case basis](https://nordicapis.com/open-data-how-to-make-it-work-for-your-business/). This volatility in expectations, outcomes, and impacts can make API documentation, implementation, and support a difficult undertaking.

Luckily, those who work with APIs have a secret tool that can make sense of the hectic world of performance evaluation — **metric analysis**. Proper use of metric analysis can allow businesses to understand their consumers and aid in further development and implementation of user-friendly and effective APIs.

In this piece, we’ll take a look at API metrics to demonstrate how they can be used to amplify success within the API space. We’ll suggest types of API metrics to analyze, demonstrate a theoretical application of metric analysis, and discuss two real-life examples of success and failure arising from differing metric analysis methodologies. By the end of this piece, you should have a firm grasp on the definition, application, and impact of proper API metric analysis.

What Is Metric Analysis?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![success-failure-importance-of-API-metric-analysis](https://nordicapis.com/wp-content/uploads/success-failure-importance-of-API-metric-analysis-300x300.jpg)

According to the Oxford Dictionary, metrics are [“method\[s\] of measuring something, or the results obtained from this”](https://www.oxforddictionaries.com/us/definition/american_english/metrics). Metrics are the way we measure the values of a targeted part of a system, measuring an event from inception to completion, including the effects caused by its implementation.

So now that we know what a metric is, why is it so important to APIs? Metrics, and by extension **API Metric Analysis**, are invaluable tools for the modern business. Metrics can be used to develop new processes, create a fundamental understanding of the product and targeted consumer, drive a holistic understanding of your manufacturing process and methodology of delivery, and create opportunity to [monetize and optimize your API](https://nordicapis.com/how-to-monotize-your-api/). Using API metrics can bring you to a bird’s-eye view of an entire API process, following the age old saying — “you can’t see the forest from the trees.”

Metric Analysis Tools and Services
----------------------------------

There are many types of metrics that can be captured, analyzed, and used to develop more effective API systems. API Metrics can largely be grouped into two categories: **internal metrics** and **external metrics**.

### Internal Metrics

Internal Metrics are those that are derived from data captured by internal web servers, user feedback forms, and trends observable through internal systems. These include:

*   **User type**: Is the consumer a repeat user or new user?
*   **Days since last session**: How long ago was the API last used by repeat users?
*   **Traffic sources**: Are functions within the API being called through your own web application or a third party application?
*   **Function grouping**: How often a user calls a certain function along with other functions.
*   **Types of data requested**: Is your server serving media requests, plain text requests, or other types of requests more often than others?
*   **Access speeds**: How quickly is your system responding to requests? Where is the bottleneck?
*   **Service requests**: How often are some services being requested? Are there any services that are never requested?
*   **Error reporting**: How often does a user report an error with the system, and what is the specific error?

### External Metrics

These metrics are derived through the use of processes and applications that originate outside of the API developer. While internal metrics are concerned more with the functioning of the actual API and overall system, external metrics focus more on the community and potential user bases. These metrics may involve third-party systems:

*   API and service adoption rates – [WebTrends](https://www.webtrends.com)
*   Redirection and publicly facing data – [Google Analytics](https://www.google.com/analytics)
*   Market trends and behaviors – [Adobe](https://www.adobe.com/solutions/digital-analytics/marketing-reports-analytics.html)

Example — The Tokyo Traffic Problem
-----------------------------------

![tokyo-japan-downtown-API-metric-analysis-example](https://nordicapis.com/wp-content/uploads/tokyo-japan-downtown-API-metric-analysis-example-300x200.jpg)A way to understand the importance of metric analysis is to show a situation in which it is applied properly against a situation where it is not, comparing the results of both approaches. Let’s imagine that we are engineers for the roadways of Tokyo, Japan, one of the largest cities in the world. We are tasked with solving a congestion problem in one of the most congested intersections in the entire city.

Let’s first approach this problem without using metric analysis. We will use an **observational approach.** By standing on an overpass straddling the most congested area of the road, we mark down our observations in our notebook, noting both the number of cars and the number of lanes provided. Using these observations, a solution is designed to expand the roadway by an extra two lanes. The time budgeted for construction is set on a 24-hour schedule. You assume the congestion will ease due to your solution, and you step away. Some months later, the congestion you observed has only spilled into the new roadways, worsening the problem. The observational approach has resulted in more problems than it fixed, and is considered an abject failure.

Now let us approach the problem using a **metric-based approach**. After being assigned the project, you first look at the city road maps. You observe that the congested road is likely facing issues arising from a stoplight intersection some miles ahead of the congested area; because the highway empties into a city thoroughfare before continuing onto another highway, this area functions as a “bottleneck”, increasing congestion by constraining the throughput of the system as a whole. Using this data, you decide to add a three-lane highway that bypasses the city thoroughfare, allowing traffic to flow both into and around the intersection, dependent on the driver’s needs. You also decide to implement a roundabout as opposed to a stoplight, thinking the flow of traffic should be eased in this manner. This plan is placed on a construction schedule over a handful of weeks, avoiding work during the rush hour. After implementing this solution, you collect data over an entire week, making notes of points of failure or issues at certain times of the day. Congestion has eased considerably, and the metric-based solution is considered a success.

The Traffic Problem Solution
----------------------------

What was the difference between the two approaches? Both aimed to ease congestion, and while the first approach was different than the second, on paper they both should have worked. The difference is the fundamental use of data in implementation.

*   In the observational approach, the _global issue_ of congestion was attacked by a _specific_ solution. In the metric-based approach, the _global issue_ of congestion was attacked with a _global solution_.
*   Issues arose within the first approach from failure to understand the _end consumer_ (expanding the intercity thoroughfare, and using a 24-hour build schedule interfering with rush hour). The second approach understood the requirements of the end consumer, creating a highway bypass and avoiding construction during the most congested periods of the day.
*   The observational approach eschewed data analysis, assuming a localized solution would fix the problem, while the metric-based solution observed the _measurable results_ of the solution, tweaking and adjusting to any new requirements that arose during construction.

The Traffic Problem and APIs
----------------------------

So what does Tokyo congestion issues have to do with API development? The two approaches above are perfect analogies for the development and implementation cycle of APIs, and show the measurable need for metric analysis. When developing an API, one must monitor internal and external API metrics to ensure their product is effective in the long-term. When an API is developed and implemented, the following vital factors must be considered:

*   The needs of the _end-consumer_, that is, the user who will interact with the API and its front-facing systems
*   The method and timescale of _implementation_, i.e. whether or not the API will be implemented immediately or over time
*   The type of implementation, i.e. whether or not the API is _specific_ (defining a single use or purpose) or _global_ (completely overhauling the already existent structures and systems)
*   The _measurable solution_, or the effects caused by the implementation of your API on your _end-consumer_

API Cycle Example
-----------------

[![api lifecycle](https://nordicapis.com/wp-content/uploads/API-Lifecycle-300x225.png)](https://nordicapis.com/envisioning-the-entire-api-lifecycle/)

The API Lifecycle is an agile process for managing the life of an API. The common API Lifecycle is composed of four distinct phases: Analysis, Development, Operations, and Retirement.

To better understand this concept, let’s break down the [API Lifecycle](https://nordicapis.com/envisioning-the-entire-api-lifecycle/) point by point, examining the role of metric analysis in each stage.

In the first stage of the API Lifecycle, the [Analysis Stage](https://nordicapis.com/api-lifecycle-analysis-stage-preparing-your-api-strategy-pre-launch/), metric analysis is perhaps most effectively and extensively used. While determining the usefulness of an API, the demand for its implementation, and the decisions between Private APIs, Partner APIs, and Public APIs ([a subject covered more fully in our eBook Developing the API Mindset](https://nordicapis.com/developing-the-api-mindset-private-partner-and-public-apis/)), the use of metric analysis is specifically designed to help you understand your client base, their needs, and the relative importance of ease of accessibility and extensibility. By analyzing market trends, reviewing web server data, and polling prospective clients and users, API metrics can help effectively narrow and define the objective of an API system.

During the second stage of the API Lifecycle, the [Development Stage](https://nordicapis.com/api-lifecycle-development/), metric analysis switches from an external role to an internal role. By analyzing the systems available to your developers, tracking the management and implementation of features, and using varied methods of rigorous testing and bug-tracking, quality is supported and the product is refined into its best possible initial state. Failure to perform proper analysis on the varied API metrics in this stage can result in massive hidden failures, missing feature-sets, and an overall displeased user base.

Nearing the end of the API Lifecycle, the **Operations Stage** is nearly as heavy in metric analysis as the first, as it is concerned with the public usage, reception, and internal response through iteration and patching. Monitoring user statistics, including the methods and durations of use, general feedback concerning usability and extensibility, and the overall impression of the API system can not only help you further refine your product, build a confident, strong user base, and quickly respond to bugs and issues, it can also help you prepare for future development projects and make the first stage of your next endeavour that much smoother.

Finally, the fourth stage of the API Lifecycle is the **Retirement Stage**. This stage is often the direct result of effective analysis throughout the previous four stages. When retiring and deprecating APIs, metrics concerning usage rates, operating system and browser support, financial response, and user base confidence can all inform the decision to retire, continue, or reiterate an API.

Failure to conduct API metric analysis could result in a product undergoing an expensive and lengthy development cycle only to find little demand upon release, making the API financially impractical. Effective metric analysis, however, can help create a stellar product, produced quickly and with less expense, resulting in higher demand with a longer lifespan. This is the raw power of metric analysis.

A Real World Failure – Heartbleed
---------------------------------

API security is a huge issue, and is becoming a more prominent concern as more companies adopt the [API-centric design concept](https://nordicapis.com/why-you-should-build-apps-with-an-api-backend-baas/). One of the most well-known examples of security failure arising from poor metric analysis is the infamous [Heartbleed bug](https://en.wikipedia.org/wiki/Heartbleed). This bug, which affected users implementing OpenSSL, a widely used security protocol, had a vulnerability in its data input validation algorithm, which allowed for excess data in its buffer overflow (a system meant to allow data exceeding the maximum buffer size to “overflow” into a secondary buffer registry) to be read in its entirety without being validated or checked for malicious code. Due to this bug, data could be forced through the overflow system without validation, executing commands that made internal data, systems, and services vulnerable to external, malicious attacks.

This bug is directly a result of improper metric analysis. During the initial construction of the OpenSSL system and API, “negative testing”, or the testing of failure scenarios, was not properly conducted against the buffer overflow; if it had been, the issue would likely have been found early on and patched before it was abused. The needs of a secure system for _end-consumers_ was not properly identified, as the vulnerabilities of the system itself were not properly tested against common validation failure and malicious attack scenarios. By not acknowledging the rate of buffer overflow incidents and the type of data that failed validation during such scenarios in the metric analysis process, an entire class of vulnerabilities was essentially ignored until it was too late.

Read On: [How To Properly Secure Your APIs](https://nordicapis.com/api-security-oauth-openid-connect-depth/)

A Real-World Success – The FedEx ShipAPI
----------------------------------------

When FedEx set out to develop an API for their shipping and freight systems, they had one issue in mind — efficiency. By eschewing the “established is better” mantra and focusing on an [agile mode of API and business development](https://nordicapis.com/what-makes-an-agile-api/), FedEx’s API, known as ShipAPI, is about as impressive a success story as one could hope for.

At one time, FedEx was flooded with what they call “WISMO” (Where IS My Order?) calls — customers dealing with extreme variations in ship times, inaccurate delivery dates, and a lack of updates from FedEx to the customer. To rectify this problem, FedEx analyzed the frequency of these calls, the locations from which they were made, the types of packages being sent, and the shipping services used. Additionally, FedEx examined their own internal practices, the rate of adherence to electronic scanning of barcodes upon receipt at a FedEx facility, and the effectiveness of their long-distance package tracking system.

By identifying the weaknesses in their own system through the use of internal metrics (utilizing both anecdotal metrics from users and operators as well as hard metrics derived from servers, scanning systems, and internal sorting reports), FedEx was able to pinpoint their points of failure, decreasing the time it took to deliver a product, and increasing customer satisfaction and confidence. Almost overnight, the FedEx brand became synonymous with quick, efficient shipping, and that is greatly due to their effective development and implementation of an API utilizing proper metric analysis.

Security, Effectiveness, and Commerce
-------------------------------------

Fundamentally, the process of metric analysis is not just one focused on security. Commerce, effectiveness of solutions, and more can all be determined through the proper derivation, analysis, and application of solutions deriving from API metrics. By determining your end-consumer, their needs, the needs of your process, and the total result of the application of an API, you can dramatically increase revenue, security, and even your consumer-base.

The lesson of it all? Understand your consumer base. Understand the API you are developing. And, most importantly, measure your success and learn from your failures.
