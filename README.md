# MCP Server Suite

A collection of **Model Context Protocol (MCP)** servers, a proxy server, and a client demonstrating how Large Language Models (LLMs) can interact with external tools using the MCP standard.

This repository contains examples of:

- Local MCP servers
- Remote MCP servers
- MCP proxy server
- MCP client using LangChain
- FastMCP framework

---

## Project Structure

```
MCP_Server/
│
├── Local-MCP-Server/
│   └── Expense Tracker MCP Server
│
├── Local-MCP-Server-for_Math/
│   └── Arithmetic MCP Server
│
├── Remote-MCP-Server/
│   └── Hosted Expense Tracker MCP Server
│
├── Proxy-Server/
│   └── Proxy to Remote MCP Server
│
└── MCP-Client/
    └── LangChain Client
```

---

# Components

## 1. Local MCP Server

A local FastMCP server implementing an **Expense Tracker**.

### Features

- Add expenses
- Store expenses in SQLite
- Categorize expenses
- Query expense information
- Local database storage

Technology used

- Python
- FastMCP
- SQLite

---

## 2. Local Math MCP Server

A lightweight arithmetic MCP server exposing mathematical operations.

### Available Tools

- Add
- Subtract
- Multiply
- Divide
- Modulo
- Power

Example

```
multiply(2, 12)

Output:
24
```

---

## 3. Remote MCP Server

A hosted version of the Expense Tracker server.

Unlike the local server, this version:

- Uses asynchronous SQLite (`aiosqlite`)
- Is designed to run remotely
- Can be accessed over HTTP
- Uses FastMCP remote transport

---

## 4. Proxy Server

The proxy server forwards requests to the hosted remote MCP server.

```
Client
    │
    ▼
Proxy Server
    │
    ▼
Remote MCP Server
```

This allows clients to communicate with remote tools without directly exposing the hosted server.

---

## 5. MCP Client

The client demonstrates how to connect an LLM with MCP servers.

It uses:

- LangChain
- MultiServerMCPClient
- OpenRouter
- GPT-4o Mini

Workflow:

1. Connect to MCP server.
2. Discover available tools.
3. Bind tools to the LLM.
4. Ask a question.
5. Let the LLM choose the appropriate tool.
6. Execute the tool.
7. Return the final answer.

Example prompt:

```
What is the product of 2 and 12?
```

The LLM automatically calls:

```
multiply(2,12)
```

and produces the final answer.

---

# Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/MCP_Server.git
cd MCP_Server
```

Install dependencies (using uv)

```bash
uv sync
```

or

```bash
pip install -e .
```

---

# Running the Servers

## Local Expense Server

```bash
cd Local-MCP-Server

uv run python main.py
```

---

## Local Math Server

```bash
cd Local-MCP-Server-for_Math

uv run fastmcp run src/local_mcp_server_for_math/main.py
```

---

## Remote MCP Server

```bash
cd Remote-MCP-Server

uv run fastmcp run src/remote_mcp_server/main.py
```

---

## Proxy Server

```bash
cd Proxy-Server

uv run fastmcp run src/proxy_server/main.py
```

---

## MCP Client

```bash
cd MCP-Client

uv run python src/mcp_client/client1.py
```

---

# Environment Variables

Create a `.env` file inside the client project.

```
OPENAI_API_KEY=your_openrouter_api_key
```

**Do not commit your `.env` file.**

Add the following to `.gitignore`:

```
.env
*.env
```

---

# Technologies Used

- Python 3
- FastMCP
- LangChain
- LangChain MCP Adapters
- OpenRouter
- GPT-4o Mini
- SQLite
- aiosqlite
- uv

---

# Learning Objectives

This repository demonstrates:

- Building custom MCP tools
- Creating local MCP servers
- Deploying remote MCP servers
- Using MCP proxy servers
- Connecting MCP with LangChain
- Enabling LLM tool calling
- Managing structured tool execution with FastMCP

---

# Future Improvements

- Authentication support
- Docker deployment
- Logging
- Unit tests
- Additional MCP tools
- Multiple remote servers
- Streaming responses
- Better configuration management

---

# License

This project is intended for educational and learning purposes.
