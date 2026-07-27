# Module 11 — Give Your AI Real Superpowers with MCP

> **Estimated Time:** 30 minutes  
> **Difficulty:** Advanced  
> **Objective:** Connect GitHub Copilot to external tools using the Model Context Protocol (MCP), enabling your AI to interact with your development environment instead of only generating suggestions.

---

# Workshop Progress

```text
████████████████████░ 77%
```

---

# Learning Objectives

By the end of this module you will:

- Understand what MCP is
- Learn why MCP exists
- Connect GitHub Copilot to external tools
- Test multiple MCP servers
- Understand when to use each MCP server
- Observe how MCP transforms GitHub Copilot from an assistant into an active collaborator

---

# Business Scenario

Your AI consulting team has become incredibly capable.

The Executive Advisor creates business strategies.

The Financial Analyst analyses profitability.

The Dashboard Designer improves user experience.

The Frontend Engineer writes production-ready code.

But then your manager asks:

> "Great."

> "Can your AI deploy the dashboard?"

...

"No."

> "Can it create a GitHub issue?"

"No."

> "Can it run browser tests?"

"No."

> "Can it inspect our repository?"

"Not yet."

Your AI knows **what** should happen.

It just can't **do** anything.

Today's goal is to change that.

---

# The Problem

Imagine asking your AI:

```text
Deploy the dashboard.
```

Without MCP, it replies:

> "Here's how you can deploy it..."

It gives instructions.

It cannot perform the task.

Now imagine the same request **after** connecting the appropriate MCP server.

```text
Deploy the dashboard.
```

↓

The AI can actually perform the deployment using the connected tool (subject to your approval and permissions).

That's the difference MCP makes.

---

# Copilot Toolbox

| Capability | Used? | Purpose |
|------------|:-----:|---------|
| 📘 Repository Instructions | ✅ | Project context |
| 📄 Prompt Files | ✅ | Reusable prompts |
| 🧠 Skills | ✅ | Reusable workflows |
| 🤖 Agents | ✅ | Business specialists |
| 🔌 MCP | ✅ | Connect external tools |

---

# Primary Copilot Capability

## 🔌 Model Context Protocol (MCP)

Model Context Protocol (MCP) is an open standard that allows AI assistants to securely communicate with external tools and services.

Without MCP:

AI can think.

With MCP:

AI can interact.

Think of MCP as a bridge between your AI assistant and the software you already use every day.

---

# Before vs After

## Before MCP

```text
Can you deploy my dashboard?

↓

Here are the deployment steps...
```

---

## After MCP

```text
Deploy my dashboard.

↓

AI connects to the deployment platform.

↓

Deployment begins.

↓

Status is returned.
```

The AI moves beyond giving advice and starts assisting with real actions.

---

# Meet Your MCP Servers

Today you'll connect three useful servers.

| MCP Server | Purpose |
|------------|---------|
| GitHub | Work with repositories, issues and pull requests |
| Playwright | Test your application in a real browser |
| Vercel | Deploy your dashboard |

Each server gives Copilot a new capability.

---

# What You'll Configure

Depending on your GitHub Copilot environment and editor, you'll connect MCP servers through the available MCP configuration interface.

You'll connect:

```text
GitHub MCP

↓

Playwright MCP

↓

Vercel MCP
```

After they're connected, Copilot can use these tools when appropriate.

---

# Hands-on Exercise

## Step 1 — Open MCP Settings

Open your GitHub Copilot MCP configuration.

Depending on your editor or IDE, this may be available under:

- GitHub Copilot settings
- AI tools
- MCP configuration

Locate the section for managing MCP servers.

---

## Step 2 — Connect GitHub MCP

Add the GitHub MCP server.

Authenticate with your GitHub account when prompted.

Verify that Copilot can access your current repository.

Once connected, ask:

```text
Summarise the open issues in this repository.
```

If your repository has no issues, try:

```text
Review the repository structure and suggest three improvements.
```

Observe that Copilot is now working with live repository information rather than only your prompt.

---

## Step 3 — Connect Playwright MCP

Next, connect the Playwright MCP server.

Once connected, ask:

```text
Open the dashboard.

Navigate through the application.

Check for:

- broken navigation
- layout problems
- responsive issues

Summarise your findings.
```

Instead of imagining your application...

Copilot can inspect it through browser automation.

---

## Step 4 — Connect Vercel MCP

Connect the Vercel MCP server.

Authenticate if required.

Then ask:

```text
Review the deployment configuration.

Identify any issues that could prevent deployment.

Recommend fixes if necessary.
```

If your environment and permissions support deployment actions, you can also ask Copilot to initiate a deployment and monitor its progress.

Always review the proposed action before approving it.

---

# Choosing the Right MCP Server

Not every task needs the same tool.

| Task | MCP Server |
|------|------------|
| Create GitHub Issue | GitHub |
| Review Pull Request | GitHub |
| Test Dashboard | Playwright |
| Verify Responsiveness | Playwright |
| Deploy Application | Vercel |
| Review Deployment | Vercel |

Choose the server that matches the task.

---

# How Everything Fits Together

Let's review your AI architecture.

```text
Repository Instructions
        │
        ▼
Project Standards

Prompt Files
        │
        ▼
Reusable Prompts

Skills
        │
        ▼
Reusable Workflows

Agents
        │
        ▼
Specialised Experts

MCP
        │
        ▼
Real-World Actions
```

Each layer builds upon the previous one.

Your AI now understands your project, follows your workflows, adopts specialist roles and can interact with connected tools.

---

# Expected Output

You should now have:

- Connected MCP servers
- AI access to external tools
- Browser testing capability
- Repository interaction
- Deployment capability (where supported)

---

# Business Takeaway

Modern organisations expect AI to do more than answer questions.

By securely connecting AI to trusted business tools, repetitive operational work can become faster and more consistent while still remaining under human oversight.

---

# Technical Takeaway

Model Context Protocol extends GitHub Copilot beyond code generation.

By connecting external tools through standardised interfaces, Copilot can gather live context and assist with real-world development tasks instead of relying solely on user-provided information.

---

# Reflection

Think back to the beginning of this workshop.

Your AI started as a chatbot.

Now it:

- understands your project
- follows your standards
- performs reusable workflows
- acts as specialised experts
- interacts with external tools

How has your role changed?

Are you still writing every line of code...

Or are you directing an AI-powered development team?

---

# Module Checkpoint

You should now have:

- ✅ Repository Instructions
- ✅ Prompt Files
- ✅ Skills
- ✅ Agents
- ✅ MCP Servers
- ✅ AI connected to real tools

---

# Architecture Snapshot

```text
Business Challenge
        │
        ▼
Ask
        │
        ▼
Plan
        │
        ▼
Agent
        │
        ▼
Repository Instructions
        │
        ▼
Prompt Files
        │
        ▼
Skills
        │
        ▼
Agents
        │
        ▼
MCP
        │
        ▼
AI That Can Act
```

Your GitHub Copilot setup has evolved from a coding assistant into a collaborative AI platform capable of understanding context, applying expertise and interacting with your development ecosystem.

---

# Looking Ahead

Your AI can now help build, test and deploy software.

Before presenting your work to leadership, there's one final step.

Professional software must be validated.

In the next module, you'll use your AI team and connected tools to test your application, fix issues and prepare it for production.

---

# Next Module

## Module 12 — Testing, Validation and Production Readiness

You'll combine GitHub Copilot, specialised Agents and MCP-powered tools to validate your dashboard, improve reliability and prepare it for deployment in a real business environment.