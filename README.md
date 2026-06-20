# ForgeAI: Multi-Agent Autonomous Software Factory

## 1. Introduction

ForgeAI is a Multi-Agent Autonomous Software Factory that converts natural language product ideas into full-stack application skeletons using collaborating AI agents powered by Ollama and Qwen3. The system simulates a real software company where specialized AI agents cooperate to perform different stages of software development, including requirement engineering, architecture design, task planning, backend generation, and frontend generation.

The objective of this project is to explore how multiple autonomous AI agents can collaborate through shared state and event-driven communication to automate the software development lifecycle.

---

## 2. Motivation

Traditional AI coding assistants typically follow the pipeline:

**Prompt → LLM → Code**

This approach suffers from several limitations:

* Lack of separation of responsibilities.
* No structured software engineering workflow.
* Difficult to scale for large projects.
* No collaboration among specialized agents.

ForgeAI addresses these limitations by introducing multiple specialized agents that emulate the workflow of a software company:

**Idea → CEO → Architect → Planner → Developer → Frontend**

This modular design improves maintainability, extensibility, and allows each agent to specialize in a particular task.

---

## 3. System Architecture

The overall architecture of ForgeAI is illustrated below:

```text
User Idea
    │
    ▼

CEO Agent
(Product Requirements)

    │
    ▼

Architect Agent
(System Architecture)

    │
    ▼

Planner Agent
(Task Planning)

    │
    ▼

Developer Agent
(Backend Generation)

    │
    ▼

Frontend Agent
(Frontend Generation)


Shared Components

• Ollama + Qwen3
• ProjectState
• EventBus
• AgentRegistry
• CodeGeneratorTool
• FileWriterTool
```

---

## 4. Agents

### 4.1 CEO Agent

The CEO Agent is responsible for requirement engineering.

#### Input

Natural language product idea.

#### Output

* Vision
* Target Users
* Features
* Requirements
* User Stories
* Success Metrics

The output is stored as a Product Requirements Document (PRD).

---

### 4.2 Architect Agent

The Architect Agent converts the PRD into a software architecture.

#### Output

* Frontend Stack
* Backend Stack
* Database
* Authentication Strategy
* Cache
* Deployment Strategy
* Software Modules

Example modules:

* AIRecommendationEngine
* UserProfileManager
* BookCatalogService
* CommunityInsights
* SmartSearch

---

### 4.3 Planner Agent

The Planner Agent decomposes the architecture into executable tasks.

Example:

```
BookCatalogService

↓

Build BookCatalogService

↓

Task Created
```

The tasks are stored in the shared project state.

---

### 4.4 Developer Agent

The Developer Agent generates backend code automatically using Ollama and Qwen3.

For each software module, it generates:

* router.py
* service.py
* model.py

Generated files are stored as File objects and written to disk using FileWriterTool.

---

### 4.5 Frontend Agent

The Frontend Agent generates React-based frontend code using the architecture and backend APIs.

Generated files include:

* App.jsx
* Navbar.jsx
* api.js
* Module-specific pages

Example:

```
frontend/

App.jsx

components/

Navbar.jsx

services/

api.js

pages/

AIRecommendationEngine.jsx

UserProfileManager.jsx
```

---

## 5. Shared Components

### 5.1 ProjectState

ProjectState acts as a centralized memory shared among all agents.

It stores:

* idea
* prd
* architecture
* tasks
* backend_files
* frontend_files

---

### 5.2 EventBus

EventBus implements event-driven communication between agents.

Example:

```
Developer -> Frontend

Frontend -> CEO
```

This decouples agents and enables asynchronous communication.

---

### 5.3 AgentRegistry

AgentRegistry manages all active agents.

It provides:

* register()
* unregister()
* get()
* exists()
* list_agents()

---

### 5.4 CodeGeneratorTool

CodeGeneratorTool is a reusable abstraction responsible for:

* Sending prompts to Ollama
* Cleaning markdown outputs
* Returning generated code

---

### 5.5 FileWriterTool

FileWriterTool writes generated File objects to disk.

This separates code generation from file management and improves modularity.

---
# 5. Core Components and Their Significance

Apart from the specialized agents, ForgeAI contains several reusable components that enable modularity, extensibility, and communication among agents. These components form the foundation of the system architecture.

---

## 5.1 BaseAgent

`BaseAgent` is the parent class for all specialized agents such as CEOAgent, ArchitectAgent, PlannerAgent, DeveloperAgent, and FrontendAgent.

### Responsibilities

* Stores common attributes such as:

  * Agent name
  * Shared memory
  * Event bus
  * Project state
* Provides common methods:

  * `think()`
  * `act()`
  * `send_message()`
  * `receive_message()`

### Significance

The BaseAgent ensures that all agents follow a common interface and behavior. It promotes:

* Code reusability
* Extensibility
* Reduced code duplication
* Polymorphism

By inheriting from BaseAgent, new agents can be added without modifying the existing architecture.

---

## 5.2 ProjectState

ProjectState acts as a centralized shared memory accessible by all agents.

### Stored Information

* Product Idea
* Product Requirements Document (PRD)
* Architecture
* Tasks
* Backend Files
* Frontend Files

### Significance

ProjectState enables indirect communication among agents.

For example:

```text
CEO

↓

Stores PRD in ProjectState

↓

Architect reads PRD

↓

Stores Architecture

↓

Planner reads Architecture
```

This design avoids tight coupling between agents and allows them to collaborate independently.

---

## 5.3 Message

The Message class represents communication exchanged between agents.

### Attributes

* Sender
* Receiver
* Content
* Timestamp

### Significance

Messages make communication explicit and traceable.

Example:

```text
Developer -> Frontend

"Backend generated."


Frontend -> CEO

"Generated 8 frontend files."
```

This helps in:

* Monitoring agent collaboration
* Logging interactions
* Future debugging and visualization

---

## 5.4 EventBus

EventBus implements event-driven communication among agents.

### Responsibilities

* Publish messages
* Deliver messages to receivers
* Maintain communication history

### Significance

The EventBus decouples agents from each other.

Instead of:

```text
Developer directly calls Frontend
```

the communication becomes:

```text
Developer

↓

EventBus

↓

Frontend
```

Advantages:

* Loose coupling
* Easier extension
* Supports asynchronous communication
* Simplifies testing

This architecture is inspired by event-driven systems used in distributed software systems.

---

## 5.5 AgentRegistry

AgentRegistry maintains references to all active agents.

### Responsibilities

* Register agents
* Remove agents
* Retrieve agents by name
* List all agents

### Significance

The registry acts as a directory service for agents.

Without AgentRegistry:

* Agents would require hardcoded references.
* Adding or removing agents would require modifying multiple files.

With AgentRegistry:

* New agents can be dynamically added.
* The architecture remains modular and scalable.

---

## 5.6 CodeGeneratorTool

CodeGeneratorTool is a reusable abstraction for interacting with the Large Language Model.

### Responsibilities

* Send prompts to Ollama
* Receive generated code
* Remove markdown formatting
* Return clean source code

### Significance

This tool separates:

```text
Code Generation Logic

from

Agent Logic
```

Advantages:

* Reusability
* Easier maintenance
* Consistent output cleaning
* Simplified agent implementation

Both DeveloperAgent and FrontendAgent reuse this tool.

---

## 5.7 FileWriterTool

FileWriterTool is responsible for writing generated File objects to disk.

### Responsibilities

* Create directories
* Write files
* Manage output structure

### Significance

This tool separates:

```text
File Management

from

Code Generation
```

This improves:

* Separation of concerns
* Reusability
* Maintainability

Agents focus on generating content, while FileWriterTool handles storage.

---

## 5.8 File Model

The File model represents generated source files.

### Attributes

* Path
* Content

Example:

```text
backend/

SmartSearch/

router.py


frontend/

App.jsx
```

### Significance

The File abstraction enables:

* Uniform handling of backend and frontend files
* Easy storage in ProjectState
* Simplified file writing
* Future extensions such as versioning and downloads

---

## Summary

These supporting components are crucial because they transform ForgeAI from a collection of prompts into a modular software engineering framework.

Together they provide:

* Object-Oriented Design
* Event-Driven Communication
* Shared State Management
* Loose Coupling
* Extensibility
* Reusability

As a result, ForgeAI is not merely an AI code generator, but a structured multi-agent system capable of modeling the software development lifecycle.

## 6. Technologies Used

### Programming Language

* Python

### Large Language Models

* Ollama
* Qwen3

### Frontend

* React
* React Router
* Axios

### Backend

* FastAPI
* Flask

### Architectural Concepts

* Multi-Agent Systems
* Object-Oriented Programming
* Event-Driven Architecture
* Shared State Architecture

---

## 7. Results

ForgeAI successfully converts natural language software ideas into full-stack application skeletons.

Example:

**Input**

```
AI Powered Book Recommendation Platform
```

**Output**

* Product Requirements Document (PRD)
* Software Architecture
* Task Breakdown
* Backend Modules
* Frontend Components

The complete pipeline:

```
Idea

↓

CEO

↓

Architect

↓

Planner

↓

Developer

↓

Frontend
```

was successfully implemented and tested using Ollama and Qwen3.

---





## 8. Conclusion

ForgeAI demonstrates how multiple specialized AI agents can collaborate to automate software engineering tasks. Instead of relying on a single monolithic LLM call, the system decomposes software generation into multiple stages handled by autonomous agents.

The project highlights the effectiveness of:

* Multi-Agent Collaboration
* Event-Driven Communication
* Shared State Management
* Modular and Extensible Design

ForgeAI serves as an exploration of autonomous software engineering and provides a foundation for future extensions such as QA agents, deployment agents, and live interactive interfaces.

I built ForgeAI to explore whether software development can be decomposed into specialized AI agents instead of relying on a single monolithic LLM call. The project models the software engineering workflow using CEO, Architect, Planner, Developer, and Frontend agents that collaborate through shared state and event-driven communication. This modular design makes the system easier to extend and reflects how software is developed in real organizations.

You can confidently say that **ForgeAI aims to reduce development time by generating an initial project skeleton that developers can refine instead of writing everything from scratch.** This is a practical and believable motivation for the project.

---

## 9. Future Work

Possible extensions include:

* Streamlit-based live visualization
* QA and testing agents
* Deployment automation
* Project export as ZIP
* Improved agent collaboration
* Production-ready backend and frontend generation
