# Module 08 — Teach Copilot New Skills

> **Estimated Time:** 25 minutes  
> **Difficulty:** Advanced  
> **Objective:** Create reusable GitHub Copilot Skills that encapsulate complete business workflows, enabling Copilot to solve recurring problems consistently with minimal prompting.

---

# Workshop Progress

```text
███████████████░░░░ 56%
```

---

# Learning Objectives

By the end of this module you will:

- Understand what GitHub Copilot Skills are
- Learn when Skills should be used
- Differentiate Skills from Prompt Files
- Build reusable business Skills
- Observe Copilot automatically selecting the appropriate Skill

---

# Business Scenario

Nova Retail has grown.

Your analytics team now has multiple business analysts.

Every day they perform similar work:

- Clean incoming datasets
- Analyse sales
- Review dashboards
- Generate executive reports

Although Prompt Files helped standardise prompts...

Everyone is still manually telling Copilot **how** to perform these workflows.

Some analysts forget steps.

Others skip validation.

Some generate incomplete reports.

Your Head of Analytics says:

> "We're no longer solving one-off problems. We're repeating the same workflows every day."

> "Let's teach Copilot those workflows."

---

# The Problem

Consider cleaning a dataset.

Your prompt might look like this:

```text
Remove duplicate records.

Identify missing values.

Standardise category names.

Validate dates.

Check for invalid discounts.

Generate a quality report.

Export the cleaned dataset.
```

Every single time.

Even though...

This workflow never changes.

---

# Copilot Toolbox

| Capability | Used? | Purpose |
|------------|:-----:|---------|
| 💬 Ask Mode | ✅ | Use Skills |
| 🤖 Agent Mode | ✅ | Create Skills |
| 📘 Repository Instructions | ✅ | Project standards |
| 📄 Prompt Files | ✅ | Reusable prompts |
| 🧠 Skills | ✅ | Reusable workflows |

---

# Primary Copilot Capability

## 🧠 GitHub Copilot Skills

Skills allow you to package an entire workflow into a reusable capability.

Unlike Prompt Files...

A Skill isn't just a prompt.

It defines:

- the objective
- the process
- the expected outcome
- supporting examples
- guidance for Copilot

Think of a Skill as teaching Copilot **how your team performs a job**.

---

# Repository Instructions vs Prompt Files vs Skills

| Repository Instructions | Prompt Files | Skills |
|--------------------------|--------------|--------|
| Project standards | Reusable prompts | Reusable workflows |
| Always active | Invoked when needed | Selected for suitable tasks |
| "Use TypeScript" | "Generate report" | "Perform business analysis" |
| "Use Tailwind" | "Review dashboard" | "Clean business data" |

A useful way to think about them:

Repository Instructions answer:

> **How should this project behave?**

Prompt Files answer:

> **What should Copilot do?**

Skills answer:

> **How should Copilot perform this type of work?**

---

# Before vs After

## Before Skills

Every time you clean a dataset:

```text
Remove duplicates.

Validate dates.

Check missing values.

Generate report.

Export CSV.
```

Again.

Again.

Again.

---

## After Skills

You simply ask:

```text
Clean this dataset.
```

Copilot already understands your preferred workflow.

---

# What You'll Create

```text
.github/

└── skills/

    clean-business-data/

        skill.md

        examples.md

    executive-analysis/

        skill.md

        examples.md
```

These Skills become reusable capabilities for your team.

---

# Hands-on Exercise

## Step 1 — Create the Skills Directory

Ask Agent Mode:

```text
Create a GitHub Copilot Skills directory.

Inside .github/skills create:

- clean-business-data
- executive-analysis

Each Skill should contain:

- skill.md
- examples.md
```

Review the generated structure before accepting it.

---

# Step 2 — Create Your First Skill

Open:

```text
.github/skills/clean-business-data/skill.md
```

Replace its contents with:

```md
# Skill

## Name

Clean Business Dataset

## Purpose

Prepare business datasets for executive analysis.

## Workflow

1. Detect duplicate records.
2. Remove duplicates.
3. Standardise category names.
4. Identify missing values.
5. Validate date fields.
6. Detect invalid numerical values.
7. Generate a data quality summary.
8. Export the cleaned dataset.

## Expected Outputs

- cleaned_dataset.csv
- data_quality_report.md

## Success Criteria

- No duplicate rows
- Consistent categories
- Valid dates
- Missing values identified
- Report generated
```

---

# Step 3 — Add Examples

Open:

```text
.github/skills/clean-business-data/examples.md
```

Add:

```md
## Example 1

Input:

Global Superstore dataset

Output:

- cleaned_dataset.csv
- data_quality_report.md

---

## Example 2

Input:

Sales dataset containing duplicate orders

Output:

Duplicate records removed.

Quality report generated.
```

Examples help Copilot understand how the Skill should be applied.

---

# Step 4 — Create an Executive Analysis Skill

Open:

```text
.github/skills/executive-analysis/skill.md
```

Add:

```md
# Skill

## Name

Executive Business Analysis

## Purpose

Generate executive-level business insights.

## Workflow

1. Review KPIs.
2. Analyse trends.
3. Identify risks.
4. Highlight opportunities.
5. Recommend business actions.
6. Summarise findings.

## Expected Output

Markdown report suitable for senior leadership.
```

---

# Step 5 — Use a Skill

Now ask Copilot:

```text
Clean this newly uploaded sales dataset.
```

Notice what happens.

Instead of requiring a detailed workflow...

Copilot can apply the Skill you've created.

Now try:

```text
Perform an executive analysis on this dataset.
```

Again...

Much less prompting is required.

---

# Prompt Files vs Skills

Let's compare one last time.

Suppose you want a quarterly report.

A Prompt File contains:

```text
Generate a quarterly executive report.
```

A Skill knows:

- how to analyse the data
- which KPIs matter
- how to evaluate trends
- how to structure recommendations

Prompt Files tell Copilot **what** you want.

Skills teach Copilot **how** your organisation performs that work.

---

# Expected Output

You should now have:

- Two reusable Skills
- Standardised business workflows
- Consistent AI behaviour
- Reduced prompt complexity

---

# Repository Changes

```text
.github/

└── skills/

    clean-business-data/

        skill.md

        examples.md

    executive-analysis/

        skill.md

        examples.md
```

---

# Business Takeaway

Successful organisations document their best practices.

New employees don't reinvent business processes.

They follow established workflows.

Skills allow you to teach those workflows to GitHub Copilot.

---

# Technical Takeaway

Skills extend GitHub Copilot beyond reusable prompts.

They capture structured workflows that Copilot can apply consistently across similar tasks, improving quality and reducing repetitive instructions.

---

# Reflection

Imagine your team grows from five analysts to fifty.

Would you rather train each analyst individually...

Or provide reusable Skills that ensure everyone follows the same process?

How might that improve consistency and onboarding?

---

# Module Checkpoint

You should now have:

- ✅ Repository Instructions
- ✅ Prompt Files
- ✅ GitHub Copilot Skills
- ✅ Reusable business workflows
- ✅ Less repetitive prompting

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
Reusable Prompts

Skills
        │
        ▼
Reusable Workflows

        │
        ▼
Consistent AI Assistance
```

Your AI assistant now understands your project, has reusable prompt templates, and can follow your team's established business workflows.

---

# Looking Ahead

Your AI assistant has become much more capable.

But there's still one limitation.

It acts like a highly knowledgeable generalist.

Wouldn't it be better if different AI experts handled different business problems?

Instead of one assistant doing everything...

You'll create a team of specialised AI consultants.

---

# Next Module

## Module 09 — Build Your AI Consulting Team

You'll create specialised GitHub Copilot Agents—such as an Executive Advisor, Financial Analyst and Marketing Strategist—each with a focused role, responsibilities and expertise, allowing Copilot to approach different business challenges from the right perspective.