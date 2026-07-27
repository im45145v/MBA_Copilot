# Examples — Executive Dashboard Review Skill

This document demonstrates how to use the **Executive Dashboard Review** skill to evaluate business intelligence dashboards from an executive perspective.

---

# Example 1 — Complete Dashboard Review

## Prompt

```text
Review the executive dashboard as if you were a Chief Executive Officer preparing for the monthly business review.

Evaluate:

- KPI relevance
- dashboard layout
- information hierarchy
- visualisations
- accessibility
- usability

Prioritise recommendations based on business impact.
```

---

## Expected Workflow

```text
Understand Purpose

↓

Review KPIs

↓

Review Layout

↓

Review Charts

↓

Review Accessibility

↓

Identify Issues

↓

Prioritise Improvements

↓

Generate Review
```

---

## Expected Output

```text
Executive Dashboard Review

Overall Assessment

Strengths

Critical Issues

Recommended Improvements

Priority Actions
```

---

# Example 2 — KPI Evaluation

## Prompt

```text
Review the dashboard KPIs.

Determine whether they answer the most important executive business questions.

Identify unnecessary metrics and recommend a better KPI hierarchy.
```

---

## Example Output

| KPI | Business Value | Priority | Recommendation |
|------|----------------|----------|----------------|
| Revenue | High | High | Keep |
| Profit Margin | High | High | Move above Revenue |
| Orders | Medium | Medium | Keep |
| Number of Products | Low | Low | Remove |

---

# Example 3 — Information Hierarchy

## Prompt

```text
Review the dashboard layout.

Determine whether executives naturally see the most important information first.

Suggest a better information hierarchy if necessary.
```

---

## Example Review

```text
Current Order

Charts

↓

KPIs

↓

Filters

↓

Tables
```

Recommended

```text
Executive Summary

↓

KPIs

↓

Filters

↓

Charts

↓

Tables

↓

Recommendations
```

---

# Example 4 — Chart Review

## Prompt

```text
Review every chart on the dashboard.

Determine:

- Does the chart answer a business question?
- Is it easy to interpret?
- Would another chart type communicate the insight more effectively?
```

---

## Expected Output

| Chart | Assessment | Recommendation |
|---------|------------|----------------|
| Revenue Trend | Good | Keep |
| Profit by Region | Good | Add data labels |
| Pie Chart (Products) | Poor | Replace with horizontal bar chart |

---

# Example 5 — Accessibility Review

## Prompt

```text
Evaluate the dashboard for accessibility.

Review keyboard navigation, semantic HTML, colour contrast and screen reader support.

Recommend improvements where necessary.
```

---

## Expected Output

```text
Accessibility Review

Keyboard Navigation

✓ Good

Colour Contrast

⚠ Improve contrast on KPI cards

Semantic HTML

✓ Good

ARIA Labels

⚠ Missing chart descriptions
```

---

# Example 6 — Mobile Responsiveness

## Prompt

```text
Review the dashboard on mobile devices.

Identify layouts that become difficult to read or interact with.

Recommend responsive improvements.
```

---

## Expected Findings

- KPI cards stack correctly
- Charts require additional spacing
- Tables should become horizontally scrollable
- Filters should collapse into a drawer

---

# Example 7 — Executive Readability

## Prompt

```text
Can an executive understand the dashboard in less than 30 seconds?

Identify anything that slows comprehension.

Recommend improvements.
```

---

## Example Output

Strengths

- Clear KPI cards
- Consistent spacing
- Logical navigation

Issues

- Too many charts above the fold
- Small chart labels
- Repeated information

Recommendations

- Reduce chart count
- Increase typography size
- Move detailed tables below summaries

---

# Example 8 — Overall Dashboard Assessment

## Prompt

```text
Provide an overall assessment of this dashboard.

Score the following areas from 1–10:

- Business Value
- Usability
- Accessibility
- Visual Design
- Performance
- Maintainability

Explain every score and recommend the highest-priority improvements.
```

---

## Example Output

| Category | Score | Comments |
|----------|------:|----------|
| Business Value | 9 | Answers key executive questions |
| Usability | 8 | Navigation is intuitive |
| Accessibility | 7 | Improve colour contrast and ARIA labels |
| Visual Design | 8 | Consistent enterprise styling |
| Performance | 8 | Good overall responsiveness |
| Maintainability | 9 | Modular component architecture |

---

# Best Practices

Always:

- review the dashboard from the user's perspective
- explain why recommendations matter
- prioritise improvements by business impact
- focus on decision-making rather than aesthetics

Never:

- recommend changes based solely on personal preference
- ignore accessibility
- overload the dashboard with additional metrics
- prioritise visual effects over clarity

---

# Success Example

A successful dashboard review should produce:

- a structured assessment
- prioritised recommendations
- improved executive usability
- stronger information hierarchy
- better accessibility
- a clearer path to business decision-making