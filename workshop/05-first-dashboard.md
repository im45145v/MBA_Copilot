# Module 05 — Build Your First Executive Dashboard

> **Estimated Time:** 20 minutes  
> **Difficulty:** Intermediate  
> **Objective:** Use GitHub Copilot Agent Mode to transform your cleaned business data into an interactive executive dashboard.

---

# Workshop Progress

```text
█████████░░░░░░░░░░ 35%
```

---

# Learning Objectives

By the end of this module you will:

- Understand why Agent Mode is the right tool for implementation
- Build a modern executive dashboard
- Generate reusable React components
- Create KPI cards and interactive charts
- Learn how Agent Mode works across multiple files

---

# Business Scenario

The data has been cleaned.

The implementation plan has been approved.

Your CEO sends one final message.

> "Perfect.

> Tomorrow morning I don't want spreadsheets.

> I want a dashboard that tells me everything I need to know within thirty seconds."

The preparation is complete.

It's finally time to build.

---

# Copilot Toolbox

| Capability | Used? | Why? |
|------------|:-----:|------|
| 💬 Ask Mode | ⚪ | Already completed |
| 📝 Plan Mode | ⚪ | Planning approved |
| 🤖 Agent Mode | ✅ | Build the dashboard |

---

# Primary Copilot Mode

## 🤖 Agent Mode

This task involves:

- creating new files
- modifying existing files
- generating components
- wiring everything together

This is exactly what Agent Mode was designed for.

Unlike Ask Mode, Agent Mode doesn't simply explain what to build.

It helps implement it.

---

# Why Agent Mode?

Let's compare.

| Ask Mode | Agent Mode |
|-----------|------------|
| Explains how to build a dashboard | Builds the dashboard |
| Suggests architecture | Creates files |
| Answers questions | Modifies your project |
| Doesn't change code | Generates working code |

Agent Mode is most effective after you've already understood the problem and planned the solution.

That's exactly what you've done in the previous modules.

---

# Hands-on Exercise

## Step 1 — Define the Goal

Open **Agent Mode**.

Start with this prompt:

```text
Build an executive dashboard for Nova Retail.

The dashboard should help senior leadership understand business performance at a glance.

Use the cleaned dataset.

Create a professional dashboard using Next.js, Tailwind CSS and shadcn/ui.

Keep the layout responsive and suitable for desktop and mobile.
```

---

## Step 2 — Build KPI Cards

Continue with:

```text
Create KPI cards for:

- Total Revenue
- Total Profit
- Total Orders
- Average Order Value

Each card should include:

- value
- descriptive title
- trend indicator
- icon
```

Review the generated components before accepting them.

---

## Step 3 — Create Visualisations

Ask Agent to build the first dashboard charts.

```text
Create charts for:

- Monthly Sales Trend
- Profit by Category
- Sales by Region
- Top 10 Products

Use Recharts.

Each chart should include appropriate titles and legends.
```

---

## Step 4 — Assemble the Dashboard

Now bring everything together.

```text
Assemble the executive dashboard.

Include:

- page header
- KPI section
- responsive chart grid
- filters
- consistent spacing
- clean typography

Follow the project's existing structure.
```

Agent may suggest creating multiple files.

Review each proposed change before accepting it.

---

## Step 5 — Run the Application

Start the development server.

Review the dashboard.

Ask yourself:

- Is the layout clear?
- Can I identify the most important KPIs within a few seconds?
- Are the charts readable?
- Does the interface feel professional?

Remember:

Working software isn't necessarily good software.

Good dashboards communicate information quickly.

---

# Expected Output

You should now have:

- An executive dashboard
- KPI cards
- Interactive charts
- Responsive layout
- Reusable React components

---

# Repository Changes

```text
app/
└── dashboard/

components/

KPICard.tsx

ChartCard.tsx

RevenueChart.tsx

ProfitChart.tsx

RegionChart.tsx

ProductChart.tsx

FilterBar.tsx
```

---

# Business Takeaway

Executives rarely have time to study spreadsheets.

A well-designed dashboard highlights what matters most and supports faster, better-informed decisions.

---

# Technical Takeaway

Agent Mode excels at implementation tasks that span multiple files.

Instead of generating isolated snippets, it understands the wider project and helps build complete features while respecting your existing structure.

---

# Reflection

Think back to Module 02.

You started by asking questions about a dataset.

Today you've transformed those insights into an interactive business application.

What part of the dashboard communicates the most valuable insight?

Would an executive immediately understand it?

---

# Module Checkpoint

You should now have:

- ✅ Executive dashboard
- ✅ KPI cards
- ✅ Interactive charts
- ✅ Reusable React components
- ✅ Confidence using Agent Mode for implementation

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
Plan
 (Plan Mode)
        │
        ▼
Execute
 (Agent Mode)
        │
        ▼
Executive Dashboard
```

You've now completed the first major milestone of the project.

From this point onwards, you'll make GitHub Copilot progressively smarter by teaching it about your project.

---

# Looking Ahead

So far, you've been providing context manually.

Every prompt repeats information like:

- use Next.js
- use Tailwind CSS
- follow accessibility best practices
- use business-friendly language

Wouldn't it be better if Copilot already knew these rules?

In the next module, you'll teach GitHub Copilot how your project works using **Repository Instructions**.

---

# Next Module

## Module 06 — Teaching GitHub Copilot About Your Project

You'll create project-wide instructions so GitHub Copilot automatically understands:

- your coding standards
- preferred frameworks
- design conventions
- accessibility requirements
- business language
- project structure

From this point onwards, Copilot will generate responses that are tailored to **your** project instead of generic code.