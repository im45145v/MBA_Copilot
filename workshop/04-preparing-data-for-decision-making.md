# Module 04 — Planning Before Building

> **Estimated Time:** 15 minutes  
> **Difficulty:** Beginner–Intermediate  
> **Objective:** Learn how to use GitHub Copilot Plan Mode to design an implementation strategy, review the proposed approach, and hand it off to Agent Mode for execution.

---

# Workshop Progress

```text
███████░░░░░░░░░░░░ 28%
```

---

# Learning Objectives

By the end of this module you will:

- Understand when to use Plan Mode
- Review AI-generated implementation plans
- Learn the Plan → Agent handoff workflow
- Execute an approved plan using Agent Mode
- Build confidence working with AI like a professional team

---

# Business Scenario

You've spent time understanding the business.

You've identified the KPIs.

You've explored the dataset.

Now you're ready to begin cleaning the data.

You excitedly open Agent Mode...

Your manager stops you.

> "Hold on."

> "Before changing thousands of rows of business data, I want to know **exactly** what you're planning to do."

Professional organisations don't let developers—or AI—make large changes without first reviewing the approach.

That's where **Plan Mode** comes in.

---

# Copilot Toolbox

| Capability | Used? | Why? |
|------------|:-----:|------|
| 💬 Ask Mode | ✅ | Clarify questions while planning |
| 📝 Plan Mode | ✅ | Design the implementation strategy |
| 🤖 Agent Mode | ✅ | Execute the approved plan |

---

# Primary Copilot Mode

## 📝 Plan Mode → 🤖 Agent Mode

Today's workflow introduces one of the most powerful features in GitHub Copilot.

Instead of asking AI to immediately write code...

You'll first ask it to think.

Then you'll review its proposal.

Only after approval will Agent Mode begin implementation.

Professional AI workflows separate:

- Understanding
- Planning
- Execution
- Review

---

# Why Plan First?

Imagine asking a contractor to renovate your house.

Would you say:

> "Just start."

Or would you first ask for:

- a design
- a timeline
- a list of changes
- expected costs

Software projects are no different.

Planning reduces mistakes.

Planning creates alignment.

Planning builds confidence.

---

# Ask vs Plan vs Agent

Each mode has a different responsibility.

| Mode | Purpose | Example |
|------|---------|---------|
| 💬 Ask | Learn and explore | "Which columns have missing values?" |
| 📝 Plan | Design the solution | "Create a data-cleaning strategy." |
| 🤖 Agent | Execute the work | "Implement the approved strategy." |

Remember:

```text
Ask

↓

Understand

↓

Plan

↓

Design

↓

Agent

↓

Build
```

---

# Hands-on Exercise

## Step 1 — Switch to Plan Mode

Open **Plan Mode**.

Rather than asking Copilot to clean the data immediately, ask it to prepare a strategy.

Use the following prompt:

```text
Create a complete implementation plan for preparing this dataset for executive reporting.

Include:

- overall approach
- data quality assessment
- duplicate handling
- missing value strategy
- category standardisation
- date validation
- validation steps
- expected output files

Do not generate code.

Explain why each step is necessary.
```

Read the proposed plan carefully.

---

## Step 2 — Review the Plan

Before approving anything, review it as if you were a project manager.

Ask yourself:

- Does the order make sense?
- Are any important steps missing?
- Is anything unnecessary?
- Would this approach work for a real business?

Remember:

AI creates the proposal.

You approve the proposal.

---

## Step 3 — Refine the Plan

Plans are meant to evolve.

If needed, continue the conversation.

Examples:

```text
Add a step for validating business calculations after cleaning.
```

```text
Include a summary report that explains every transformation made.
```

```text
Suggest any risks associated with this cleaning process.
```

Continue refining until you're happy with the final plan.

---

# Plan → Agent Handoff

Now comes the exciting part.

Instead of copying prompts into another chat...

GitHub Copilot lets you hand the approved plan directly to Agent Mode.

The workflow now becomes:

```text
Problem

↓

Plan Mode

↓

Review

↓

Approve

↓

Agent Mode

↓

Implementation
```

This keeps the reasoning and execution connected.

---

## Step 4 — Execute the Plan

After approving the plan, hand it off to **Agent Mode**.

Use a prompt similar to:

```text
Execute the approved implementation plan.

Generate:

- clean_data.py
- cleaned_superstore.csv
- data_quality_report.md

Explain each major transformation and why it was performed.
```

Watch Agent Mode begin implementing the approved strategy.

Notice that you're no longer asking **what** should happen.

You're asking Copilot to execute an already approved plan.

---

## Step 5 — Review the Results

Never assume AI is correct.

Open each generated file.

Review:

- the cleaning script
- the cleaned dataset
- the data quality report

Ask yourself:

- Did Agent follow the plan?
- Are the transformations reasonable?
- Has any important data been lost?
- Would you approve this for tomorrow's board meeting?

Professional AI workflows always include human review.

---

# Expected Output

By the end of this exercise, you should have:

- A reviewed implementation plan
- A completed Plan → Agent handoff
- A cleaned dataset
- A reusable cleaning script
- A data quality report

---

# Repository Changes

```text
datasets/

cleaned_superstore.csv

scripts/

clean_data.py

reports/

data_quality_report.md
```

---

# Business Takeaway

Business leaders rarely approve work without first reviewing the approach.

The same principle applies when working with AI.

Planning creates transparency.

Review creates trust.

Execution becomes safer.

---

# Technical Takeaway

Professional AI-assisted development follows a repeatable workflow:

```text
Understand

↓

Ask

↓

Plan

↓

Review

↓

Agent

↓

Review Again
```

Don't skip the planning stage simply because AI can generate code quickly.

---

# Reflection

Think about today's workflow.

Would you feel comfortable letting AI modify an important production system without first reviewing its plan?

Why or why not?

How might Plan Mode reduce risk in your own projects?

---

# Module Checkpoint

You should now be able to:

- ✅ Explain when to use Plan Mode
- ✅ Review AI-generated implementation plans
- ✅ Perform a Plan → Agent handoff
- ✅ Execute work with Agent Mode
- ✅ Review AI-generated changes before accepting them

---

# Architecture Snapshot

```text
Business Challenge
        │
        ▼
Understand
 (Ask Mode)
        │
        ▼
Better Questions
 (Prompt Engineering)
        │
        ▼
Implementation Plan
   (Plan Mode)
        │
        ▼
Approved
        │
        ▼
Execute
 (Agent Mode)
```

You've now learned a professional AI workflow used by modern development teams.

Everything from this point onwards builds on this foundation.

---

# Looking Ahead

Your data is now clean.

You understand the business.

The implementation workflow is in place.

It's finally time to build something executives can use.

In the next module, you'll use Agent Mode to create your first Executive Dashboard.

Because the planning work is already complete, Agent Mode can focus entirely on implementation.

---

# Next Module

## Module 05 — Build Your First Executive Dashboard

You'll use Agent Mode to:

- Build KPI cards
- Create interactive charts
- Design an executive dashboard
- Organise reusable React components
- Turn cleaned data into business insights

For the first time in the workshop, you'll transform analysis into a real, interactive business application.