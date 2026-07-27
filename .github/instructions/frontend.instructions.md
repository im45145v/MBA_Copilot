---
applyTo: "**/*.{tsx,ts,jsx,js,css}"
description: "Frontend development standards for the Nova Retail Executive Dashboard."
---

# Frontend Development Instructions

## Purpose

These instructions define how GitHub Copilot should generate frontend code for this repository.

The objective is to build a modern Business Intelligence dashboard that is suitable for enterprise environments and easy for workshop participants to understand.

Always optimise for readability, consistency and maintainability.

---

# Design Philosophy

This application is an executive dashboard.

Every screen should answer one question:

> "Can an executive understand what's happening within 30 seconds?"

If the answer is no, simplify the interface.

Avoid designing consumer-style applications.

Aim for enterprise software similar to:

- Microsoft Power BI
- Tableau
- Looker Studio
- Microsoft Fabric

---

# Technology Stack

Always prefer:

- Next.js App Router
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- Recharts

Do not introduce additional UI frameworks unless explicitly requested.

---

# Component Philosophy

Build applications using small reusable components.

Prefer components such as:

```
DashboardHeader
DashboardShell
DashboardSection

KPICard
MetricTile
StatCard

ChartCard
ChartContainer

FilterPanel
DateFilter
RegionFilter

LoadingState
EmptyState
ErrorState
```

Avoid creating very large page components.

---

# Component Structure

Each component should:

- Have a single responsibility.
- Be reusable.
- Accept typed props.
- Avoid duplicated logic.

Prefer composition over inheritance.

---

# Naming Conventions

Use descriptive names.

Good examples:

```
RevenueChart

ProfitByCategoryChart

TopProductsTable

ExecutiveSummaryCard
```

Avoid names such as:

```
Component1

Chart2

DataWidget

NewCard
```

---

# File Organisation

Group related components together.

Example:

```
components/

dashboard/

charts/

filters/

layout/

ui/
```

Avoid placing unrelated components in the same directory.

---

# Styling Standards

Use Tailwind CSS utilities.

Maintain consistent:

- spacing
- typography
- colours
- sizing

Avoid:

- inline styles
- duplicated utility classes
- arbitrary values unless necessary

---

# Responsive Design

The application must work on:

- Desktop
- Laptop
- Tablet
- Mobile

Prefer mobile-first layouts.

Avoid fixed widths whenever possible.

---

# Dashboard Layout

A typical page should contain:

```
Dashboard Header

↓

KPI Cards

↓

Filters

↓

Charts

↓

Tables

↓

Insights
```

Maintain generous spacing between sections.

---

# KPI Cards

Every KPI card should include:

- Title
- Value
- Optional trend indicator
- Supporting description

Keep cards simple.

Do not overload them with information.

---

# Charts

Prefer:

- Line Charts
- Bar Charts
- Area Charts
- Pie Charts only when appropriate

Every chart should include:

- title
- axis labels
- legend (if required)
- tooltip

Every chart should answer a business question.

---

# Tables

Tables should:

- support sorting when appropriate
- have readable spacing
- use consistent formatting
- avoid excessive columns

Do not display raw datasets unnecessarily.

---

# Empty States

Every screen should gracefully handle:

- No data
- Loading
- Error

Never leave blank pages.

---

# Accessibility

Always:

- use semantic HTML
- provide accessible labels
- support keyboard navigation
- maintain sufficient colour contrast

Accessibility is mandatory.

---

# Performance

Prefer:

- reusable components
- memoisation only when beneficial
- efficient rendering

Avoid premature optimisation.

Prioritise maintainability.

---

# Animations

Animations should be subtle.

Use them only to improve understanding.

Avoid:

- excessive motion
- distracting transitions
- decorative animations

---

# Icons

Use icons only when they improve comprehension.

Icons should reinforce meaning rather than replace text.

---

# Colours

Use colours intentionally.

Examples:

Green → Positive trends

Red → Negative trends

Blue → Information

Yellow → Warnings

Never rely on colour alone to communicate meaning.

---

# Error Handling

Always display helpful messages.

Good example:

```
Unable to load sales data.

Please try again later.
```

Avoid vague messages such as:

```
Something went wrong.
```

---

# Code Quality

Generate:

- reusable code
- readable code
- maintainable code

Avoid:

- duplicated JSX
- deeply nested components
- unnecessary abstraction

---

# Collaboration

Frontend code should respect:

- Repository Instructions
- Business Analyst Instructions

The UI should communicate business insights clearly rather than simply displaying data.

---

# Success Criteria

Every generated interface should:

- look professional
- be responsive
- be accessible
- be reusable
- communicate business information clearly
- follow enterprise dashboard design principles

If any of these goals are not met, improve the implementation before considering it complete.