---
title: Real-time first person Epic game
date: 2022-08-31
banner: https://unsplash.com/photos/XN4T2PVUUgk/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjkzNTExOTg3fA&force=true&w=1920
abstract: Scaling Fortnite is undoubtedly a testament to the services our engineers build. Every service must be built at “Fortnite Scale”, and so, even the most rudimentary applications quickly turn into a distributed system exercise.
---

# Abstract

Scaling Fortnite is undoubtedly a testament to the services our
engineers build. Every service must be built at “Fortnite Scale”, and
so, even the most rudimentary applications quickly turn into a
distributed system exercise.

The data engineering team at Epic was tasked with solving one of the
first problems an online video game encounters. From the moment a game
client (console, PC) emits an event, it should be observable and
actionable as soon as possible. Keep in mind that data in events could
span many different contexts, such as a client (player data) or server
(service data). The heterogeneous nature, and sheer volume of data
required a novel and modern solution.

**The Proposal**

Events contain a vast amount of actionable information (e.g. client
performance, matchmaking durations, item usage). With millions of
events firing every second, we knew it was paramount to provide
meaningful real-time insights. Furthermore, the system should be
self-serviceable to the extent that an engineer can inject a new
workload that becomes available within seconds.

Enter Metrics Royale, a real-time Flink application that extracts,
aggregates and persists arbitrary values from JSON
payloads. Aggregations may be grouped on arbitrary keys to allow
fine-grained reporting (e.g. per-platform, per-region, etc). Data is
immediately available for monitoring and alerting through a custom
Grafana plugin.

**The Solution**

It was clear that we wanted to use Apache Flink due to how strong its
streaming capabilities were without the headache of micro
batching. Secondly, being a JVM based system, we could leverage the
massive ecosystem of libraries, such as Jayway for JSON processing or
Scala for a purely functional data interface.

We wanted to run many of these Flink clusters in unison, and so a
transactional persistence layer was key to achieving this. Although a
tough decision in itself, we ultimately chose FoundationDB for many
reasons, namely the excellent support for 3-AZ deployments and its
strong consistency guarantees.

# Real-Time Metrics at Fortnite Scale - Ricky Saltzer

<iframe width="1024" height="500" src="https://www.youtube.com/embed/93b--lTq2ng" title="Real-Time Metrics at Fortnite Scale - Ricky Saltzer" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
