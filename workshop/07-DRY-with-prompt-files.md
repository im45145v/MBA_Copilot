# Module 07 — Stop Rewriting the Same Prompt

> **Estimated Time:** 20 minutes  
> **Difficulty:** Intermediate  
> **Objective:** Learn how Prompt Files let you save and reuse complex prompts across your project.

---

# Workshop Progress

```text
█████████████░░░░░░ 49%
```

---

# Learning Objectives

By the end of this module you will:

- Understand what Prompt Files are
- Learn when to use Prompt Files instead of Repository Instructions
- Create reusable prompt templates
- Invoke Prompt Files from GitHub Copilot
- Build a library of business analysis prompts

---

# Business Scenario

Over the past few days, your team has started using GitHub Copilot extensively.

Every Monday morning, someone asks Copilot to analyse weekly sales.

Every Friday, someone generates an executive summary.

Every month, someone prepares a profitability report.

Although everyone is asking for the same information...

They're all writing huge prompts from scratch.

One analyst uses 30 lines.

Another uses 15.

Someone else forgets to include risks.

Another forgets recommendations.

The Business Intelligence Manager says:

> "We're wasting time writing the same prompts over and over again. Let's standardise them."

---

# The Problem

Look at this prompt.

```text
Analyse the cleaned sales dataset.

Create an executive summary.

Identify key KPIs.

Highlight risks.

Identify growth opportunities.

Compare categories.

Recommend business actions.

Write professionally.

Keep it suitable for senior leadership.

Don't fabricate insights.

Return the results using Markdown.
```

Imagine typing this every week.

Eventually...

Copy & paste becomes your workflow.

There has to be a better way.

---

# Copilot Toolbox

| Capability | Used? | Purpose |
|------------|:-----:|---------|
| 💬 Ask Mode | ✅ | Execute Prompt Files |
| 📝 Plan Mode | ⚪ | Already completed |
| 🤖 Agent Mode | ✅ | Create Prompt Files |
| 📘 Repository Instructions | ✅ | Already configured |
| 📄 Prompt Files | ✅ | Reusable prompt templates |

---

# Primary Copilot Capability

## 📄 Prompt Files

Prompt Files allow you to save prompts inside your repository.

Instead of repeatedly writing long instructions...

You write them once.

Everyone on your team can reuse them.

Think of Prompt Files as reusable consulting playbooks.

---

# Repository Instructions vs Prompt Files

Many people confuse these two.

| Repository Instructions | Prompt Files |
|--------------------------|--------------|
| Project standards | Reusable tasks |
| Always active | Used when needed |
| "Use TypeScript" | "Generate Executive Report" |
| "Use Tailwind" | "Analyse Customer Segments" |
| "Use Recharts" | "Evaluate Profitability" |

A simple rule:

> Repository Instructions describe **how your project should behave**.

> Prompt Files describe **what you want Copilot to do repeatedly**.

---

# Before vs After

## Before Prompt Files

Every report starts with:

```text
Analyse...

Summarise...

Recommend...

Write professionally...

Use Markdown...

Include KPIs...

Explain risks...

Identify opportunities...
```

Again.

And again.

And again.

---

## After Prompt Files

You simply tell Copilot:

```text
Use the Executive Analysis prompt.
```

The detailed prompt is already stored in your repository.

---

# What You'll Create

```text
.github/

└── prompts/

    executive-analysis.prompt.md

    dashboard-review.prompt.md

    profitability-analysis.prompt.md

    customer-insights.prompt.md

    executive-report.prompt.md
```

These become reusable business workflows.

---

# Hands-on Exercise

## Step 1 — Create the Prompt Files

Ask Agent Mode:

```text
Create a .github/prompts directory.

Inside it create prompt files for:

- Executive Analysis
- Dashboard Review
- Profitability Analysis
- Customer Insights
- Executive Report

Use GitHub Prompt File format.
```

Review the generated files before accepting them.

---

## Step 2 — Build Your First Prompt File

Replace the contents of:

```text
.github/prompts/executive-analysis.prompt.md
```

with:

```md
---
mode: ask
description: Analyse business performance for executives
---

# Executive Analysis

You are a Senior Business Consultant.

Analyse the provided business dataset.

Return:

## Executive Summary

Provide a concise overview.

## Key KPIs

Highlight the most important business metrics.

## Positive Trends

Identify areas performing well.

## Risks

Highlight business concerns.

## Opportunities

Recommend growth opportunities.

## Strategic Recommendations

Provide actionable recommendations for senior leadership.

Never invent information.

Clearly distinguish facts from recommendations.

Write using professional business language.
```

---

## Step 3 — Create a Dashboard Review Prompt

Create:

```text
.github/prompts/dashboard-review.prompt.md
```

```md
---
mode: ask
description: Review dashboard quality
---

Review this dashboard.

Evaluate:

- clarity
- accessibility
- executive readability
- KPI selection
- chart quality
- responsiveness

Suggest improvements.

Rank the dashboard from 1–10.
```

---

## Step 4 — Create an Executive Report Prompt

Create:

```text
.github/prompts/executive-report.prompt.md
```

```md
---
mode: ask
description: Generate executive report
---

Create a board-ready executive report.

Include:

- Executive Summary
- Financial Performance
- Operational Performance
- Business Risks
- Growth Opportunities
- Strategic Recommendations

Write professionally.

Avoid technical jargon.

Target audience:

Senior executives.
```

---

## Step 5 — Use a Prompt File

Now try using one.

Instead of writing a long prompt...

Ask Copilot something similar to:

```text
Use the Executive Analysis prompt to analyse this dataset.
```

Or, depending on your editor's GitHub Copilot workflow, invoke the saved Prompt File and provide the relevant dataset or context.

Notice how the reusable prompt supplies the detailed instructions automatically.

---

# Why Not Put This in Repository Instructions?

Repository Instructions answer questions like:

- Which framework?
- Which coding style?
- Which UI library?

Prompt Files answer questions like:

- Analyse this dataset.
- Generate this report.
- Review this dashboard.

They're solving completely different problems.

---

# Expected Output

You should now have:

- Reusable Prompt Files
- Standardised business analyses
- Consistent executive reports
- Less prompt repetition

---

# Repository Changes

```text
.github/

└── prompts/

    executive-analysis.prompt.md

    dashboard-review.prompt.md

    profitability-analysis.prompt.md

    customer-insights.prompt.md

    executive-report.prompt.md
```

---

# Business Takeaway

Businesses standardise recurring work.

Finance teams use templates.

Consultants use playbooks.

Legal teams use document precedents.

Prompt Files are the AI equivalent of those reusable assets.

---

# Technical Takeaway

Prompt Files package repeatable AI tasks into reusable templates.

Instead of remembering complex prompts, you create them once and share them with your entire team through your repository.

---

# Reflection

Think about the prompts you've written during this workshop.

Which ones do you think you'll use repeatedly in future projects?

Could those become Prompt Files instead?

---

# Module Checkpoint

You should now have:

- ✅ Repository Instructions
- ✅ Prompt Files
- ✅ Standardised business prompts
- ✅ Faster AI workflows
- ✅ A reusable prompt library

---

# Architecture Snapshot

```text
Repository Instructions
        │
        ▼
Project Standards

Prompt Files
        │
        ▼
Reusable Business Tasks

        │
        ▼
Smarter & Faster Copilot
```

Your AI assistant now knows **how your project works** and has reusable workflows for common business tasks.

---

# Looking Ahead

Prompt Files solve one problem:

> Reusing prompts.

But another problem still exists.

Every time you ask Copilot to clean data, review dashboards or analyse sales...

It still has to figure out the workflow.

What if you could package an entire workflow—not just a prompt—into something reusable?

That's exactly what you'll build next with **GitHub Copilot Skills**.

---

# Next Module

## Module 08 — Build Reusable AI Skills

You'll create reusable Skills that encapsulate complete business workflows, allowing GitHub Copilot to perform complex tasks consistently across projects instead of relying on ad hoc prompting.