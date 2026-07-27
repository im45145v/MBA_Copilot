# Module 06 — Teach GitHub Copilot About Your Project

> **Estimated Time:** 20 minutes  
> **Difficulty:** Intermediate  
> **Objective:** Create Repository Instructions so GitHub Copilot automatically understands your project's standards, technology stack, and business context.

---

# Workshop Progress

```text
███████████░░░░░░░░ 42%
```

---

# Learning Objectives

By the end of this module you will:

- Understand what Repository Instructions are
- Learn when Repository Instructions should be used
- Create project-wide instructions for GitHub Copilot
- Reduce repetitive prompting
- Observe how Copilot changes its behaviour automatically

---

# Business Scenario

Congratulations!

Your dashboard is live and your manager is impressed.

Over the next few weeks, more developers join the Nova Retail project.

Every developer uses GitHub Copilot.

Unfortunately, everyone gets slightly different suggestions.

Some components use different styling.

Some generate JavaScript instead of TypeScript.

Some create inconsistent layouts.

Some forget accessibility.

Some even use completely different chart libraries.

Your Technical Lead says:

> "Instead of repeating our standards in every conversation, let's teach Copilot how this repository works."

---

# The Problem

Think about the prompts you've written so far.

Many of them included instructions like:

- Use Next.js
- Use TypeScript
- Use Tailwind CSS
- Use shadcn/ui
- Make the UI responsive
- Follow accessibility best practices
- Write business-friendly content
- Create reusable components

How many times have you repeated these?

Probably every single prompt.

That isn't scalable.

---

# Copilot Toolbox

| Capability | Used? | Purpose |
|------------|:-----:|---------|
| 💬 Ask Mode | ⚪ | Already completed |
| 📝 Plan Mode | ⚪ | Already completed |
| 🤖 Agent Mode | ✅ | Create repository instructions |
| 📘 Repository Instructions | ✅ | Teach Copilot your project |

---

# Primary Copilot Capability

## 📘 Repository Instructions

Repository Instructions are project-wide guidance that GitHub Copilot automatically considers whenever it generates responses for this repository.

Instead of repeating your preferences every time, you define them once.

Think of Repository Instructions as your project's operating manual.

Every AI suggestion now starts with the same understanding.

---

# Before vs After

## Before Repository Instructions

Every prompt looks like this:

```text
Build a KPI card.

Use Next.js.

Use TypeScript.

Use Tailwind CSS.

Use shadcn/ui.

Follow accessibility best practices.

Use our colour palette.

Make it responsive.

Keep components reusable.
```

---

## After Repository Instructions

Your prompt becomes:

```text
Build another KPI card.
```

Copilot already knows the rest.

That's the power of Repository Instructions.

---

# What You'll Create

```text
.github/

└── copilot-instructions.md
```

This file becomes the shared knowledge base for everyone working on the project.

---

# Hands-on Exercise

## Step 1 — Create the Instructions File

Ask Agent Mode:

```text
Create a Repository Instructions file for this project.

The project is an Executive Dashboard for Nova Retail built using:

- Next.js App Router
- TypeScript
- Tailwind CSS
- shadcn/ui
- Recharts

Include coding standards, UI guidelines, accessibility requirements and business context.

Create the file inside:

.github/copilot-instructions.md
```

Review the generated file before accepting it.

---

## Step 2 — Replace It with Our Standard

For consistency across the workshop, replace the generated content with the following.

```md
# Nova Retail Executive Dashboard

## Project Overview

This repository contains an executive dashboard for Nova Retail.

The application helps senior leadership understand business performance through interactive dashboards, KPI cards and visual analytics.

Always optimise for clarity and executive decision-making.

---

## Technology Stack

- Next.js (App Router)
- TypeScript
- Tailwind CSS
- shadcn/ui
- Recharts
- Pandas (data processing)

---

## Coding Standards

- Prefer functional React components.
- Use TypeScript for all new code.
- Avoid duplicated logic.
- Keep components modular and reusable.
- Prefer composition over large components.
- Use descriptive variable names.

---

## UI Standards

- Mobile-first responsive layouts.
- Accessible interfaces.
- Consistent spacing.
- Clear typography.
- Professional business appearance.
- Avoid unnecessary animations.

---

## Dashboard Standards

Every dashboard should include:

- Clear page title
- KPI cards
- Well-labelled charts
- Filters where appropriate
- Consistent spacing
- Loading and empty states

---

## Business Context

The target audience is senior executives.

Prioritise:

- clarity
- readability
- meaningful KPIs
- actionable insights

Never invent business insights.

Always explain calculations clearly.

---

## Data Visualisation

Prefer:

- Recharts
- Simple colour palettes
- Proper axis labels
- Tooltips
- Legends

Avoid misleading visualisations.

---

## Accessibility

Always:

- Use semantic HTML.
- Include ARIA labels when appropriate.
- Ensure sufficient colour contrast.
- Support keyboard navigation.

---

## Code Quality

Generate production-ready code.

Keep files organised.

Avoid unnecessary complexity.

Follow existing project structure whenever possible.
```

---

## Step 3 — Test the Difference

Before Repository Instructions, you probably wrote prompts like:

```text
Create a responsive KPI card using TypeScript, Tailwind CSS and shadcn/ui.
```

Now simply ask:

```text
Create a KPI card showing Customer Satisfaction.
```

Notice what happens.

Copilot already knows:

- TypeScript
- Tailwind
- shadcn/ui
- component style
- accessibility
- reusable structure

You didn't have to repeat any of it.

---

## Step 4 — Try Another Example

Ask Agent:

```text
Create a Revenue Breakdown chart.
```

Observe:

- Does it follow the existing design?
- Does it use Recharts?
- Does it match previous components?
- Does it respect your coding standards?

Repository Instructions should improve consistency across the project.

---

# Why Not Put Everything Here?

Repository Instructions describe **how the project should work**.

They are **not** for reusable tasks like:

- analysing sales
- generating executive reports
- cleaning datasets

Those belong in Prompt Files and Skills, which you'll build in the next modules.

A good rule of thumb is:

> Repository Instructions define the project's standards, not its workflows.

---

# Expected Output

You should now have:

- A Repository Instructions file
- More consistent AI-generated code
- Less repetitive prompting
- Better collaboration across your team

---

# Repository Changes

```text
.github/

└── copilot-instructions.md
```

---

# Business Takeaway

Successful teams rely on shared standards.

Repository Instructions give your AI assistant those same standards, making its suggestions more consistent for everyone contributing to the project.

---

# Technical Takeaway

Repository Instructions provide persistent project context.

Instead of embedding the same guidance into every prompt, you define it once and let GitHub Copilot apply it automatically throughout the repository.

---

# Reflection

Imagine five developers joining your project tomorrow.

Without Repository Instructions, each person may receive different suggestions from Copilot.

With Repository Instructions, everyone starts from the same foundation.

How might that improve consistency and code reviews?

---

# Module Checkpoint

You should now have:

- ✅ Repository Instructions
- ✅ Project-wide AI guidance
- ✅ Consistent coding standards
- ✅ Less repetitive prompting
- ✅ A smarter GitHub Copilot experience

---

# Architecture Snapshot

```text
Business Challenge
        │
        ▼
Understand
 (Ask)
        │
        ▼
Prompt Better
 (Ask)
        │
        ▼
Plan
 (Plan)
        │
        ▼
Build
 (Agent)
        │
        ▼
Repository Instructions
        │
        ▼
Smarter AI Suggestions
```

Your AI assistant now understands your project before you even ask a question.

---

# Looking Ahead

Repository Instructions define **how your project should behave**.

But what about tasks you perform again and again?

For example:

- analysing sales performance
- generating executive summaries
- reviewing customer segments
- evaluating profitability

Instead of rewriting those prompts every time, you'll package them into reusable Prompt Files.

---

# Next Module

## Module 07 — Reusable Prompt Files

You'll learn how to create prompt templates that let you reuse complex business workflows with a single command, making your interactions with GitHub Copilot faster, more consistent and easier to maintain.