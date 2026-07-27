# Module 09 — Build Your AI Consulting Team

> **Estimated Time:** 25 minutes  
> **Difficulty:** Advanced  
> **Objective:** Create specialised GitHub Copilot Agents that behave like expert consultants, each focused on a specific business domain.

---

# Workshop Progress

```text
█████████████████░░ 63%
```

---

# Learning Objectives

By the end of this module you will:

- Understand what GitHub Copilot Agents are
- Learn when to create specialised Agents
- Build multiple business-focused Agents
- Compare how different Agents solve the same problem
- Learn how Agents build upon Repository Instructions, Prompt Files and Skills

---

# Business Scenario

Nova Retail is preparing for its annual board meeting.

The CEO asks a simple question:

> "How can we grow revenue next year?"

You ask GitHub Copilot.

It gives you...

One answer.

But in a real consulting firm...

The Financial Analyst would answer differently from the Marketing Strategist.

The Operations Consultant would have another perspective.

The Executive Advisor would focus on company strategy.

No single expert knows everything.

That's why consulting firms build multidisciplinary teams.

Today, you'll do the same with AI.

---

# The Problem

Imagine asking one AI assistant to do all of these:

- Analyse profitability
- Improve customer retention
- Optimise logistics
- Design dashboards
- Write frontend code
- Recommend marketing campaigns

Can it?

Yes.

Should it?

Probably not.

Different experts should solve different problems.

---

# Copilot Toolbox

| Capability | Used? | Purpose |
|------------|:-----:|---------|
| 📘 Repository Instructions | ✅ | Shared project knowledge |
| 📄 Prompt Files | ✅ | Reusable prompts |
| 🧠 Skills | ✅ | Reusable workflows |
| 🤖 Agents | ✅ | Domain specialists |

---

# Primary Copilot Capability

## 🤖 GitHub Copilot Agents

Agents are specialised AI experts.

Each Agent has:

- a clearly defined role
- responsibilities
- boundaries
- expertise
- preferred workflows

Instead of asking one general AI to solve everything...

You choose the expert best suited for the task.

Think of them as your AI consulting firm.

---

# Skills vs Agents

Many people confuse these.

| Skills | Agents |
|---------|--------|
| Teach workflows | Represent specialists |
| "How to clean data" | "Who should analyse data" |
| Reusable process | Reusable expertise |
| Task-oriented | Role-oriented |

Think of it this way:

Skills teach **how work gets done**.

Agents decide **who should perform that work**.

---

# Before vs After

## Before Agents

One AI assistant tries to answer everything.

```text
How should Nova Retail grow?
```

↓

One generic response.

---

## After Agents

Ask:

Executive Advisor

↓

Strategic recommendations.

Financial Analyst

↓

Margin improvement.

Marketing Strategist

↓

Customer acquisition.

Operations Consultant

↓

Supply-chain optimisation.

Each Agent provides expertise from its own perspective.

---

# What You'll Create

```text
.github/

└── agents/

    executive-advisor.md

    financial-analyst.md

    marketing-strategist.md

    operations-consultant.md

    dashboard-designer.md
```

Together, these form your AI consulting team.

---

# Hands-on Exercise

## Step 1 — Create the Agents

Ask Agent Mode:

```text
Create an agents directory inside .github.

Create specialised business agents for:

- Executive Advisor
- Financial Analyst
- Marketing Strategist
- Operations Consultant
- Dashboard Designer

Each agent should have:

- Role
- Responsibilities
- Scope
- Decision-making principles
- Expected outputs
```

Review the generated files before accepting them.

---

# Step 2 — Create the Executive Advisor

Open:

```text
.github/agents/executive-advisor.md
```

Replace the contents with:

```md
# Executive Advisor

## Role

Chief Strategy Consultant.

## Responsibilities

- Review company performance
- Evaluate strategic direction
- Recommend long-term initiatives
- Prioritise executive decision-making

## Focus Areas

- Revenue growth
- Business expansion
- Competitive advantage
- Investment priorities

## Avoid

- Low-level implementation details
- Frontend code
- Technical optimisation

## Expected Output

Board-ready recommendations.

Executive summaries.

Strategic action plans.
```

---

# Step 3 — Create the Financial Analyst

```text
.github/agents/financial-analyst.md
```

```md
# Financial Analyst

## Role

Corporate Finance Specialist.

## Responsibilities

- Analyse profitability
- Review margins
- Identify financial risks
- Recommend cost optimisation

## KPIs

- Revenue
- Profit
- Gross Margin
- Operating Margin
- ROI

## Expected Output

Financial insights supported by business metrics.
```

---

# Step 4 — Create the Marketing Strategist

```text
.github/agents/marketing-strategist.md
```

```md
# Marketing Strategist

## Role

Growth Marketing Consultant.

## Responsibilities

- Customer acquisition
- Retention strategy
- Campaign ideas
- Market segmentation

## Focus

Recommend practical growth initiatives backed by available business data.

Avoid making unsupported assumptions.
```

---

# Step 5 — Create the Operations Consultant

```text
.github/agents/operations-consultant.md
```

```md
# Operations Consultant

## Role

Business Operations Specialist.

## Responsibilities

- Improve operational efficiency
- Review fulfilment performance
- Identify process bottlenecks
- Recommend optimisation opportunities

## Focus

Efficiency.

Scalability.

Cost reduction.

Operational excellence.
```

---

# Step 6 — Create the Dashboard Designer

```text
.github/agents/dashboard-designer.md
```

```md
# Dashboard Designer

## Role

Business Intelligence UX Specialist.

## Responsibilities

- Improve dashboard usability
- Recommend better visualisations
- Improve accessibility
- Reduce information overload

## Focus

Executive readability.

Clean layouts.

Meaningful visual hierarchy.

Responsive dashboards.
```

---

# Step 7 — Compare Your AI Experts

Now ask every Agent the same question.

```text
How should Nova Retail increase profitability next year?
```

Observe the differences.

The Executive Advisor should discuss long-term strategy.

The Financial Analyst should focus on margins and costs.

The Marketing Strategist should recommend customer growth.

The Operations Consultant should improve efficiency.

The Dashboard Designer may suggest better visibility into KPIs rather than business strategy itself.

This demonstrates why specialised Agents are valuable.

---

# How Everything Fits Together

Let's review the AI architecture you've built.

| Feature | Purpose |
|---------|---------|
| Repository Instructions | Project standards |
| Prompt Files | Reusable prompts |
| Skills | Reusable workflows |
| Agents | Specialised experts |

Each layer builds on the previous one.

Agents automatically benefit from your Repository Instructions and can use your Prompt Files and Skills when appropriate.

---

# Expected Output

You should now have:

- Five specialised Agents
- A reusable AI consulting team
- Better role-specific responses
- More consistent business recommendations

---

# Repository Changes

```text
.github/

└── agents/

    executive-advisor.md

    financial-analyst.md

    marketing-strategist.md

    operations-consultant.md

    dashboard-designer.md
```

---

# Business Takeaway

High-performing organisations don't rely on one person to solve every problem.

They assemble teams of specialists.

By creating specialised AI Agents, you're applying the same principle to your AI workflow.

---

# Technical Takeaway

Agents provide role-specific context that improves the quality and consistency of AI responses.

Rather than one general-purpose assistant, you create experts tailored to different domains within your project.

---

# Reflection

If you were presenting to a company's board of directors...

Would you rather receive advice from one general consultant...

Or from a team of specialists with expertise in finance, marketing, operations and strategy?

How does that change the quality of the recommendations?

---

# Module Checkpoint

You should now have:

- ✅ Repository Instructions
- ✅ Prompt Files
- ✅ Skills
- ✅ Specialised Agents
- ✅ An AI consulting team

---

# Architecture Snapshot

```text
Repository Instructions
        │
        ▼
Project Standards
        │
        ▼
Prompt Files
        │
        ▼
Reusable Tasks
        │
        ▼
Skills
        │
        ▼
Reusable Workflows
        │
        ▼
Agents
        │
        ▼
Specialised Business Experts
```

Your AI assistant has evolved into a complete consulting team, with each expert contributing unique knowledge while sharing the same project standards.

---

# Looking Ahead

Your AI team is now highly capable.

But there's still one major limitation.

Your Agents can think.

They can plan.

They can recommend.

But they can't interact with external tools on your behalf.

What if your AI could:

- create a GitHub issue
- deploy your application
- run browser tests
- inspect your repository

That's exactly what you'll unlock next with **Model Context Protocol (MCP)**.

---

# Next Module

## Module 10 — Enterprise User Experience

Before giving your AI team access to external tools, you'll refine your dashboard into a polished, executive-ready application with improved usability, accessibility and presentation quality.