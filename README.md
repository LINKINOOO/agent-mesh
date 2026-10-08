# AgentMesh

A programmable communication and orchestration layer for multi-agent AI systems.

## What is AgentMesh?

AgentMesh explores how multiple AI agents can work together through explicit communication rules.

Instead of treating agents as isolated chatbots, AgentMesh defines:

- which agents can communicate with each other
- what information can be passed between agents
- when communication is triggered
- how one agent's result becomes another agent's input

## Core Model

AgentMesh is built around four concepts:

- **Agent** — a source of capabilities
- **Task** — the work that needs to be accomplished
- **Thread** — an active execution context
- **Communication Rule** — defines how information flows between agents

The initial goal is simple:

> Build a small, inspectable runtime where a user can define an agent network and observe information flowing through it.

## Status

Early prototype.

The first version will focus on:

1. Defining agents
2. Connecting agents
3. Controlling communication
4. Running a simple multi-agent workflow
5. Inspecting the execution flow
