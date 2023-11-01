---
title: Why, and how FoundationDB is moving to Swift
date: 2023-10-13
banner: https://unsplash.com/photos/XN4T2PVUUgk/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjkzNTExOTg3fA&force=true&w=1920
---

> <center>
> 📺 ["Swift as C++ Successor in FoundationDB" by Konrad Malawski (Strange Loop 2023](https://www.youtube.com/watch?v=ZQc9-seU-5k) 🖥️
> </center>

Programming languages often prioritize either performance or
ergonomics. Swift offers a unique modern type-safe low-ceremony
approach taking the best of both worlds that scales from mobile apps
to high-performance systems where previously memory-unsafe languages
would be used. It also interoperates seamlessly with C and C++.

In this talk, we show how we successfully adopted Swift in
FoundationDB, a distributed database struggling to modernize its C++
codebase. Swift's interoperability features allowed the team to
incrementally move single functions, or entire types, to Swift. This
transition was done without generating any bindings and while
preserving the existing semantics.

FoundationDB uses a custom actor runtime, which enables reproducible
simulation testing. Again, Swift's flexible concurrency and
distributed actor model enabled an incremental side-by-side approach
by having Swift concurrency seamlessly execute on the existing
scheduling infrastructure.

Konrad Malawski
Swift Team, Apple
@ktosopl

Konrad works in the Swift team at Apple, where he focuses on
foundational server-side Swift libraries and concurrency features of
the language. He was part of the design and implementation of Swift’s
structured concurrency and actor model, as well as the distributed
actors language feature and cluster library. He also maintains
server-side observability libraries for logging, metrics and
distributed tracing. Previously, he worked on Akka at
Lightbend/Typesafe, where he maintained core pieces of the ecosystem,
including the clustering, event sourcing, streaming and HTTP
libraries. He also made significant contributions to the
reactive-streams specification and TCK which later became the
foundation of the JDK’s java.util.concurrent.Flow types.

> <center>
> 📺 ["Swift as C++ Successor in FoundationDB" by Konrad Malawski (Strange Loop 2023](https://www.youtube.com/watch?v=ZQc9-seU-5k) 🖥️
> <center>

