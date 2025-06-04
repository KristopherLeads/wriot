Note: This content was developed during a developer community planning exercise and is shared here for portfolio and attribution purposes.

<p align="center">© 2025 Kristopher Sandoval.</p>

## Task 1 - Community Strategy & Growth Plan

### Goal

Rootly’s community is filled with passionate SREs. To grow that community, we must invest in high-trust, community-driven initiatives that position Rootly as a true reliability partner - not just a vendor. When SREs think about people who care as much as they do, Rootly should be top of mind.

### Target Audiences and ICP

We’ll focus on three core personas:

1. Site Reliability Engineers (SREs) - our primary on-the-ground users. If we can satisfy them, they’ll become internal champions and unlock adoption across teams and co-orgs.
2. Platform & DevOps Engineers - these are the key operators of CI/CD, observability, and internal tooling. Their usage surfaces critical feedback and integration opportunities.
3. Engineering Managers - these leaders connect Rootly’s value to team outcomes and budgets. With their support, we move from tactical to strategic adoption.

### Community Growth Initiatives

#### Rootly House Call Initiative

A small-group session where Rootly collaborates with an org’s engineers to review their reliability stack, identify friction points, and co-design automation or Slack workflows. Each session ends with tailored guidance and a whitepaper documenting the integration.

##### Benefits

1. Consultative trust-building - this initiative positions Rootly as a reliability partner, not just a vendor trying to turn a quick buck
Customer insight - we can leverage this initiative to identify and document common patterns across accounts and utilizations that can inform the overall roadmap as well as our sales playbooks
2. Generates evergreen content - making random articles about features is cool, but making specific whitepapers about use cases and implementations builds high trust and informs the community more effectively, showcasing Rootly workflows in action
3. Community seeding - more broadly, this could lead to bigger case studies, identification and surfacing of internal champions, and cross-org referrals from the “House Call” success stories.
   
#### "The Rootly Games" Simulation Hackathon

A time-boxed competition where teams respond to mock incidents using Rootly in Slack. It tests product fluency in a controlled, gamified environment. Winners - judged on resolution time, communication, and postmortem quality - earn prizes like cash or Rootly credits.

##### Benefits

1. This gamifies onboarding and reduces overall friction - teams are more likely to evangelize Rootly if they see how effective it is in a variety of situations
2. This generates evergreen content. We could stream this in-person, do it virtually, async, etc. - the sky’s the limit for this sort of activation.
3. Rootly gets set as a culture-building tool, bringing a certain polish and excitement to the community that is different from just a straight-up code workshop. This is more fun and engaging, and SREs will remember that when they’re considering who to work with, what to integrate, what to recommend to others, etc.

#### Rootly Runbooks Live

A video and podcast where a Rootly guest walks me through a real incident retrospective, setting the ground for what happened, how they responded, and how Rootly helped.

##### Benefits
1. This effectively demonstrates what Rootly does and what its value is. For the guest, it gives a nice boost to their company name and marketing, and for us, it gives a nice boost to our value prop and our own dev outreach marketing functions. 
2. This also functions as great blog, YouTube, and Spotify content for long-term engagement as well as great sales collateral.

### Measurements and Metrics

The metrics for these efforts will be focused on the top-level goals of generating high community sentiment, establishing community trust, and enabling high retention and expansion through platform evangelism. Accordingly, I would track the following metrics:

1. Event Engagement and Sentiment - how many people came to the event, and what was their surveyed response to the event? Was it positive or negative? Did they walk away better informed? What was the NPS value?
2. Community Signups - new members in Slack, number of trial workspaces post-event, etc.
3. Content Amplification - pageviews, mentions across social, shares, reposts.
4. Champion Contributions - forum posts, community answers, and beta feedback tied to these events and initiatives.
5. Surveyed Trust and Perception - regular and periodic surveys should track the trust and perception of our marketing efforts through this DevRel strategy to ensure people are seeing us as the “go-to” option.

## Task 2 - Educational Content & Technical Writing

### Introducing Rootly’s Incident Prediction: Solve Problems Before They Become Incidents

If you’re passionate about Site Reliability, you’re no stranger to the cycle of incident responses. A problem appears out of nowhere. You get an alert, you scramble to your team, and triage begins. You tackle the problem and do a post-mortem. It requires being on alert, being aware, and always being vigilant.

But what if the next major incident could be predicted - maybe even prevented - before it became an issue? What if you could prevent a problem from becoming an incident altogether?

That’s the dream behind Rootly’s new feature: Incident Prediction.

#### What is Incident Prediction?

At its core, Incident Prediction uses machine learning to identify the patterns in code changes, deployment behaviors, infrastructure variables, metrics, and historical incident data. We’ve taken the best publicly accessible data sets and fine tuned it based on our own observations and practices, creating an artificial intelligence-driven system designed to detect issues before they become incidents.

The real power of this feature comes into play with your own incident data. Rootly utilizes its integrated systems to analyze telemetry and configuration data in your native instance, and when patterns that resemble past incidents crop up - either based on our data set or in your own historical incident reporting - Rootly flags it as a potential issue, allowing you to triage the issue.

With Incident Prediction, you get the best of both worlds, allowing you to flag common misconfigurations and build issues as well as more specific and hard to discover issues in your development flow.

#### How Does It Work?

Rootly’s Incident Prediction model uses a weighted model combining publicly accessible data as well as instance-specific data to evaluate issues across domains including:

* Deployment frequency and velocity in relation to rollback history
* Unusual diffs in infrastructural code changes that are potentially breaking
* Metrics such as p99 latency or error rates with historical drift detection
* Risk heuristics, such as “changes made to services with >3 recent SEVs”
* Disconnected services or services requiring auth flows that aren’t configured properly

These domains are then converted into a weighted score - the “incident likelihood”. Every client instance can be configured for a conservative or risky incident likelihood, allowing for more flexible alert controls. When a high “incident likelihood” is achieved, these issues can be automatically blocked or simply flagged.

The system continuously scores “incident likelihood” at the service level, updating predictions as new data rolls in. It doesn’t just guess - it learns from real-world operations over time.

#### Integrating Incident Prediction Into CI/CD Flows
Getting started is easy! The [following example](https://github.com/KristopherLeads/wriot/blob/main/Content%20Archive/Rootly/Examples.yaml) is a GitHub action that sets up a call to the Prediction API. You can also adapt this job to apply your own gating logic, based on the verdict and reason returned.

````
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Call Rootly Incident Prediction API
        run: |
          curl -X POST https://api.rootly.io/v1/predict \
            -H "Authorization: Bearer ${{ secrets.ROOTLY_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{
              "repo": "your-service",
              "commit": "${{ github.sha }}",
              "environment": "production"
            }' > prediction.json

      - name: Evaluate verdict from prediction
        run: |
          verdict=$(jq -r .verdict prediction.json)
          reason=$(jq -r .reason prediction.json)

          if [[ "$verdict" == "block" ]]; then
            echo "Deployment blocked by Incident Prediction"
            echo "Reason: $reason"
            exit 1
          fi

      - name: Deploy service
        run: ./scripts/deploy.sh
````
#### Production Example: Quick.ly

Quick.ly is an e-commerce solution offering multi-cart shopping for limited drops like the Nintendo Switch. Last year, during Black Friday, a critical Redis misconfiguration was sent to production. While this did not cause immediate problems, at peak traffic Quick.ly customers began to see huge latency spikes resulting in timeouts on their cart. When ecommerce items are in short supply, this kind of latency cost Quick.ly a lot of customer trust - not to mention revenue.

This year, with Rootly running, Quick.ly identified a change in October that was similar to the pattern which caused last year’s fault. An error was immediately generated in Quick.ly’s Slack instance:

````
Prediction Alert
High-risk configuration change detected in redis-cart-cache
Similar to change preceding SEV-2023-11
Confidence: 91%
Suggested action: Review change in CI before deployment
````

By reviewing both this changelog as well as additional development logs, it was detected that the error was arising from both the Redis misconfiguration as well as a mistake in the stack code handling client side state storage. Rootly flagged the issues early, enabling Quick.ly to triage and fix them before they reached production.

This year, Quick.ly had their most successful Black Friday of all time, with peak traffic exceeding that of last year. No downtime, no issues, no lost revenue - that’s the power of Rootly’s Incident Prediction.

#### Try It Out Today!

If you’d like to get started with Incident Prediction, you can book a [free trial](https://rootly.com/users/sign_up) today! 

If you’re an existing Rootly customer, just ping us on Slack - we’ll help you get set up.

## Task 3 - Community Engagement & Troubleshooting

A response to a support ticket:

Hey there! First off, I totally understand where you're coming from - false positives are super frustrating. Incident Prediction is meant to be a helpful tool, but it sounds like it’s getting in your way in this case. Let’s get this working correctly for you.

A few things that will help to reduce false positives:

* Threshold Configuration - in your workspace settings, try adjusting the sensitivity for the prediction model. If you’ve deployed this as a GitHub action, you can also manually adjust the value there.
* Training Data Coverage - if you just enabled this, it might be that you don’t have enough data in the model yet to make accurate predictions. If upping the Threshold doesn’t help, I would push it up even higher until you have more data in the model set.
* Alerts and Workflows - you might actually be getting a lot of positives that just aren’t super impactful. In that case, they’re not really “false positives”, they’re just overly cautious. They’re still good info to have, but they shouldn’t block the build - you can set the action on the Incident Prediction flow to just record this and filter to a secondary channel without blocking.

If you’d be open to it, I’d love to help you set this up and look at your use case! I can connect with you directly today or tomorrow for a 15-minute troubleshooting session. Your feedback helps shape everything we do at Rootly, so I want to make sure we’re building better!

Let me know if you’d like to connect! 

## Task 4 - Product Feedback & Alignment

Gathering feedback to influence the product roadmap requires meeting the developers and users of Rootly where they are. I’d prioritize three primary feedback loops: (1) quarterly Slack, Discord, and X polls and deep dives in our public community to gauge interest in upcoming features; (2) regular 1:1 user interviews in-person and virtually with key accounts and active community contributors to ascertain friction points and desired feature sets; and (3) a GitHub Discussions board for transparent feedback and feature requests. These insights would be documented as themes and pain points for specific user personas, which I'd summarize bi-weekly in a shared internal Confluence doc for Product and Engineering. I’d also facilitate a monthly “Voice of the Community” sync to directly align user insights with roadmap prioritization.

### Social Channel Engagements

For additional context on the previous answer, I did a bit of a deep dive to see where our community efforts, especially around product feedback, might be best targeted. Based on my research, these are the top channels I would target for Rootly:

* Discord/Slac/Mastodon - Very impersonal, but very direct - these are our best channels for direct feedback, surveys, collective information gathering, and persona generation. Engagement types: direct conversations, polls, surveys, roundtable discussions.
  
* X/Threads - Although X is somewhat problematic, it is still a strong source of active conversation in the tech community, and would be a great place to drop in where SRE is discussed. Threads is a notable secondary option. Engagement types: individual callouts, documenting features, long-form threaded conversations around industry trends, thought leadership, problem resolution with the product.
  
* Reddit - High value casual channel, especially on subreddits such as /r/sre, which can allow us to directly interface with both naysayers as well as product champions. Engagement types: thread answers, deep dives, contact with projects that would benefit from our product, Q&A/AMA threads, etc.

* Instagram/TikTok - Great for short form shareable content. A series like “getting started with Rootly in five minutes” or “solving X problem in thirty seconds” would do really well in engineering circles. Engagement types: short-form directed content, memes (within reason), comment feedback
  

* YouTube - A channel that could make great use of product guides, walkthroughs, etc. This would be much more evergreen in value, but could also help us guide our efforts based on what others talk about in relation to us, e.g. “Why I chose Rootly vs. PagerDuty” style content videos. Engagement types: evergreen video, threaded conversations, partnerships.

* Rootly Blog - This is always going to be a strong evergreen system for us, and we could benefit from enabling something like Gravatar for direct involvement. Engagement types: direct engagement with consumers, feedback cycles.

* LinkedIn - Professional resource that tends to lean more product-oriented. This would be our best bet for pre-seed through late series clients, and could help us narrow our ICP and get more targeted feedback. Engagement types: long-form posts, directly in-thread convos, thought leadership.


## Task 5 - CFP & Public Speaking
CFP Submission for AI Engineer World's Fair 2025
**Title**: Rethinking Postmortems - Using LLMs to Auto-Synthesize Retrospectives
**Track**: AI in Action OR Agent Reliability
**Link**: [redacted]
**Password**: [redacted]
**Slidedeck**: [redacted]

### Abstract
You’ve just put out a five-alarm fire, and now you have to deal with the worst part of the incident - filling out the paperwork. Postmortems are a critical part of incident management, but they can often feel pretty burdensome, leading to documentation delays, inconsistencies, and even neglect.

What if we could transform this process using AI? What if we could make postmortems easy? 

In this session, we’re explore how Rootly leverages Large Language Models (LLMs) to automate the creation of incident retrospectives. We’ll look at how you can take this approach into your own hands, leveraging incident timelines, chat transcripts, and system data to generate auto-synthesized and comprehensive root cause summaries and next step guidelines.

We can’t make it fun - but we can make it less not-fun!

In this talk, attendees will learn:

* Techniques for structuring incident data to optimize LLM analysis
* Methods to extract meaningful insights and recommendations automatically
* Strategies to integrate AI-generated postmortems into existing workflows

Join us to discover how AI can not only streamline the postmortem process but also enhance the quality and consistency of incident reviews, turning every incident into an opportunity for improvement.
