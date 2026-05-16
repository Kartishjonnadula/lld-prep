 # Low Level Design (LLD) Roadmap for SDE2/SDE3

---

# Progress Legend

- [ ] Not Started
- [/] In Progress
- [x] Completed

---

# Phase 1 — OOP Foundations

## OOP Basics

- [ ] Classes & Objects
- [ ] Encapsulation
- [ ] Abstraction
- [ ] Inheritance
- [ ] Polymorphism
- [ ] Method Overriding
- [ ] Method Overloading
- [ ] Access Modifiers
- [ ] Static vs Instance Members
- [ ] Interfaces vs Abstract Classes

---

## Composition vs Inheritance

- [ ] HAS-A vs IS-A relationship
- [ ] Favor composition over inheritance
- [ ] Tight coupling problems
- [ ] Flexible design with composition
- [ ] Real-world examples

---

## SOLID Principles

### Single Responsibility Principle (SRP)
- [ ] Understand SRP
- [ ] Identify SRP violations
- [ ] Refactor bad designs

### Open Closed Principle (OCP)
- [ ] Open for extension
- [ ] Closed for modification
- [ ] Replace if-else chains using patterns

### Liskov Substitution Principle (LSP)
- [ ] Proper inheritance usage
- [ ] Avoid broken polymorphism

### Interface Segregation Principle (ISP)
- [ ] Small focused interfaces
- [ ] Fat interface problems

### Dependency Inversion Principle (DIP)
- [ ] Depend on abstractions
- [ ] Dependency injection basics

---

## Coupling & Cohesion

- [ ] Tight coupling
- [ ] Loose coupling
- [ ] High cohesion
- [ ] Dependency management
- [ ] Maintainable code practices

---

# Phase 2 — Design Patterns

---

# Creational Patterns

## Factory Pattern

- [ ] Simple Factory
- [ ] Factory Method
- [ ] Abstract Factory
- [ ] Remove if-else using factories
- [ ] Build NotificationFactory
- [ ] Build PaymentFactory
- [ ] Build VehicleFactory

---

## Builder Pattern

- [ ] Immutable objects
- [ ] Optional parameters
- [ ] Fluent APIs
- [ ] Build UserBuilder
- [ ] Build HTTPRequestBuilder

---

## Singleton Pattern

- [ ] Lazy initialization
- [ ] Eager initialization
- [ ] Thread-safe singleton
- [ ] Singleton pitfalls

---

# Structural Patterns

## Adapter Pattern

- [ ] Legacy system integration
- [ ] Third-party API adapters
- [ ] Payment gateway adapter example

---

## Decorator Pattern

- [ ] Dynamic behavior extension
- [ ] Logging decorators
- [ ] Retry decorators
- [ ] Caching decorators

---

## Facade Pattern

- [ ] Simplify complex systems
- [ ] Build OrderService facade

---

# Behavioral Patterns

## Strategy Pattern

- [ ] Runtime behavior switching
- [ ] Payment strategies
- [ ] Pricing strategies
- [ ] Routing strategies

---

## Observer Pattern

- [ ] Pub/Sub systems
- [ ] Notification systems
- [ ] Event-driven architecture

---

## State Pattern

- [ ] Workflow state management
- [ ] Order state machine
- [ ] Vending machine states

---

## Command Pattern

- [ ] Task queues
- [ ] Undo/Redo systems
- [ ] Job scheduling

---

# Phase 3 — Production Engineering Concepts

---

# API Design

- [ ] REST principles
- [ ] Resource modeling
- [ ] API versioning
- [ ] Pagination
- [ ] Filtering
- [ ] Sorting
- [ ] Idempotency
- [ ] Request validation
- [ ] Error handling
- [ ] Authentication
- [ ] Authorization
- [ ] Rate limiting
- [ ] PUT vs PATCH
- [ ] Sync vs Async APIs
- [ ] Polling vs Webhooks

---

# Database Design

## Relational Database Basics

- [ ] Primary keys
- [ ] Foreign keys
- [ ] Normalization
- [ ] Denormalization
- [ ] Indexes
- [ ] Transactions
- [ ] ACID properties
- [ ] Joins

---

## Advanced DB Concepts

- [ ] Optimistic locking
- [ ] Pessimistic locking
- [ ] Read replicas
- [ ] Sharding basics
- [ ] Partitioning
- [ ] Materialized views

---

## Database Modeling Practice

- [ ] User system
- [ ] Orders system
- [ ] Payments system
- [ ] Inventory system
- [ ] Subscription system

---

# Concurrency & Multithreading

## General Concepts

- [ ] Race conditions
- [ ] Deadlocks
- [ ] Mutexes
- [ ] Semaphores
- [ ] Thread pools
- [ ] Producer-consumer pattern

---

## Go Concurrency

- [ ] Goroutines
- [ ] Channels
- [ ] Buffered channels
- [ ] Worker pools
- [ ] Context cancellation
- [ ] sync.Mutex
- [ ] sync.RWMutex
- [ ] sync.WaitGroup
- [ ] sync.Once
- [ ] Atomic operations

---

# Caching

- [ ] Cache-aside pattern
- [ ] Write-through cache
- [ ] Write-back cache
- [ ] TTL handling
- [ ] Cache invalidation
- [ ] LRU eviction
- [ ] Redis basics

---

# Messaging Systems

## Kafka

- [ ] Topics
- [ ] Partitions
- [ ] Consumer groups
- [ ] Ordering guarantees
- [ ] Replication
- [ ] Offset management

---

## RabbitMQ

- [ ] Exchanges
- [ ] Queues
- [ ] Routing
- [ ] Retry queues
- [ ] DLQ

---

## SQS

- [ ] FIFO queues
- [ ] Standard queues
- [ ] Visibility timeout
- [ ] DLQ

---

## General Messaging Concepts

- [ ] Idempotency
- [ ] Retry handling
- [ ] At-least-once delivery
- [ ] At-most-once delivery
- [ ] Exactly-once semantics
- [ ] Event-driven systems

---

# Logging & Monitoring

- [ ] Structured logging
- [ ] Correlation IDs
- [ ] Metrics
- [ ] Distributed tracing
- [ ] Alerting
- [ ] Observability basics

---

# File & Storage Systems

- [ ] Blob storage
- [ ] Chunk uploads
- [ ] CDN basics
- [ ] Metadata storage
- [ ] Object storage basics

---

# Phase 4 — LLD Problem Practice

---

# Beginner Problems

- [ ] Parking Lot
- [ ] Library Management System
- [ ] ATM Machine
- [ ] Elevator System
- [ ] Vending Machine
- [ ] Movie Ticket Booking
- [ ] Hotel Booking

---

# Intermediate Problems

- [ ] Splitwise
- [ ] Cab Booking
- [ ] Food Delivery App
- [ ] Chess Game
- [ ] Snake & Ladder
- [ ] Cricbuzz
- [ ] Inventory Management
- [ ] Rate Limiter

---

# Advanced Problems

- [ ] Notification System
- [ ] Payment Gateway
- [ ] Job Scheduler
- [ ] Distributed Cache
- [ ] API Gateway
- [ ] URL Shortener Internals
- [ ] Pub/Sub System
- [ ] Logging Framework
- [ ] Workflow Engine
- [ ] Feature Flag System
- [ ] Distributed Lock Manager
- [ ] Metrics Aggregator

---

# Interview Preparation

---

# Requirement Gathering

- [ ] Functional requirements
- [ ] Non-functional requirements
- [ ] Clarifying ambiguous requirements
- [ ] Scale estimation
- [ ] Failure handling discussion

---

# Design Discussion Skills

- [ ] Explain tradeoffs
- [ ] Explain scalability
- [ ] Explain extensibility
- [ ] Discuss edge cases
- [ ] Discuss concurrency issues
- [ ] Discuss database tradeoffs

---

# UML & Diagramming

- [ ] Class diagrams
- [ ] Sequence diagrams
- [ ] Component diagrams
- [ ] State diagrams

---

# Mock Interview Practice

- [ ] Timed LLD interviews
- [ ] Whiteboard explanation practice
- [ ] Verbal communication practice
- [ ] Explain designs clearly
- [ ] Defend design decisions

---

# Real Production-Level Topics

- [ ] Backpressure handling
- [ ] Retry mechanisms
- [ ] Circuit breakers
- [ ] Bulkheads
- [ ] Service discovery
- [ ] Feature toggles
- [ ] Graceful degradation
- [ ] Idempotency keys

---

# Weekly Goals Tracker

## Week 1
- [ ] Finish OOP basics
- [ ] Finish SOLID principles
- [ ] Solve 2 beginner LLD problems

---

## Week 2
- [ ] Finish creational patterns
- [ ] Finish structural patterns
- [ ] Solve 2 more LLD problems

---

## Week 3
- [ ] Finish behavioral patterns
- [ ] Start API design
- [ ] Start database modeling

---

## Week 4
- [ ] Learn concurrency deeply
- [ ] Learn caching
- [ ] Learn messaging systems

---

## Week 5
- [ ] Solve intermediate LLD problems
- [ ] Conduct mock interviews
- [ ] Improve communication

---

## Week 6
- [ ] Solve advanced LLD problems
- [ ] Review weak areas
- [ ] Revise patterns & tradeoffs

---

# Final Readiness Checklist

## I can:

- [ ] Clarify requirements confidently
- [ ] Identify entities quickly
- [ ] Build extensible systems
- [ ] Use interfaces properly
- [ ] Apply correct design patterns
- [ ] Explain tradeoffs clearly
- [ ] Handle concurrency discussions
- [ ] Think about production issues
- [ ] Design maintainable code
- [ ] Handle changing requirements
- [ ] Think like a senior engineer

---

# Recommended Resources

## Books

- [ ] Head First Design Patterns
- [ ] Clean Code
- [ ] Designing Data-Intensive Applications

---

## YouTube

- [ ] Refactoring Guru
- [ ] Gaurav Sen
- [ ] Jordan has no life

---

# Daily Practice Checklist

- [ ] Solve 1 LLD problem
- [ ] Learn 1 design pattern
- [ ] Read production code
- [ ] Practice concurrency
- [ ] Revise SOLID principles
- [ ] Explain one design verbally

---