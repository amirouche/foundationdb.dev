---
title: A developer-driven approach to building secondary indexes
date: 2023-03-15
banner: https://unsplash.com/photos/fB4Zo2jPA3E/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8OHx8c3R1ZGlvJTIwcmVjb3JkaW5nfGVufDB8fHx8MTY3OTgzMDgxNQ&force=true&w=1920
abstract: Building secondary indexes for a database is always about balance. A balance between a system that scales and is easy to manage and an API that is intuitive and delightful for a developer to use.
---

## Bio

Garren is a database engineer based in sunny South Africa. He works at
Tigris Data, building a new modern data platform. He’s been a regular
open source contributor over the years, contributing to the Apache
CouchDB project, the Prisma ORM, and the PouchDB browser database,
amongst others. When he’s not coding, you’re likely to find him in the
outdoors - either climbing up a cliff face or taking photographs (not
at the same time, however).

## Summary

Building secondary indexes for a database is always about balance. A
balance between a system that scales and is easy to manage and an API
that is intuitive and delightful for a developer to use. Recently, at
Tigris Data, we have been adding secondary indexes to our database and
have been working hard to achieve a good balance between scale and
developer delight. Tigris is a transactional document database that
runs on top of FoundationDB and is compatible with MongoDB. In this
talk, I cover four aspects we had to balance:1. Handling schema
changes automatically in our secondary indexes so that users don’t
have to worry about it.

- The trade-off between auto-indexing all fields and indexing select fields.
- Changes we made after performance testing.
- How we plan to build indexes in the background with minimal conflicts.

## Slides

<embed src="foundationdb-meetup-building-secondary-indexes.pdf" width="1024" height="375"
 type="application/pdf">

## Video

<iframe width="1024" height="500" src="https://www.youtube.com/embed/qD1h5CyzL0A" title="FoundationDB Online Meetup 01: A developer-driven approach to building secondary indexes" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
