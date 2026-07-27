# Module 12 — Trust, But Verify

> **Estimated Time:** 20 minutes  
> **Difficulty:** Advanced  
> **Objective:** Use GitHub Copilot, your AI consulting team and MCP-powered tools to test, validate and prepare your dashboard for production.

---

# Workshop Progress

```text
██████████████████████░░ 84%
```

---

# Learning Objectives

By the end of this module you will:

- Understand why AI-generated code still requires validation
- Test your application using GitHub Copilot
- Use Playwright MCP to automate browser testing
- Identify accessibility and usability issues
- Prepare your application for production deployment

---

# Business Scenario

Your dashboard is complete.

The UI looks professional.

The CEO loves the design.

The AI says everything looks good.

So...

Can you deploy it?

Not yet.

Your CTO reminds everyone:

> "Never deploy software simply because AI says it's correct."

> "Every production application must be tested."

Today your goal isn't building.

It's proving your application deserves to go live.

---

# The Problem

Imagine deploying this dashboard and discovering:

- Revenue displays incorrect values
- Charts fail on mobile devices
- Filters don't work
- Navigation breaks
- Loading states never disappear
- Accessibility requirements aren't met

Every one of these problems could damage trust.

Professional software isn't judged by how quickly it's built.

It's judged by how reliably it works.

---

# Copilot Toolbox

| Capability | Used? | Purpose |
|------------|:-----:|---------|
| 📘 Repository Instructions | ✅ | Maintain project standards |
| 📄 Prompt Files | ✅ | Reuse review prompts |
| 🧠 Skills | ✅ | Apply testing workflows |
| 🤖 Agents | ✅ | Specialist reviews |
| 🔌 Playwright MCP | ✅ | Browser automation |
| 🤖 Agent Mode | ✅ | Fix discovered issues |

---

# Primary Objective

Today's objective is simple.

> **Trust AI. Verify Everything.**

AI accelerates development.

Testing builds confidence.

Production requires both.

---

# Before vs After

## Before Testing

```
"It works on my computer."

↓

Deploy.
```

Risk:

Nobody actually knows if the application is reliable.

---

## After Testing

```
Functional Tests

↓

UI Review

↓

Accessibility Review

↓

Performance Checks

↓

Production Ready
```

Confidence replaces assumptions.

---

# Testing Pyramid

Every production application should be reviewed from multiple perspectives.

```text
            User Experience
                  ▲
         Accessibility Review
                  ▲
          Integration Testing
                  ▲
           Functional Testing
```

Each layer increases confidence before deployment.

---

# Hands-on Exercise

## Step 1 — Review the Application

Ask your Executive Advisor:

```text
Review this dashboard as if you were presenting it to the company's board.

Identify:

- confusing metrics
- missing KPIs
- unclear business insights
- recommendations for improvement
```

Business validation is just as important as technical validation.

---

## Step 2 — Test with Playwright MCP

Ask Copilot:

```text
Launch the application using Playwright.

Verify:

- navigation
- filters
- responsive layout
- charts
- loading behaviour

Summarise any failures.
```

Review the generated report.

---

## Step 3 — Accessibility Review

Ask:

```text
Review this application for accessibility.

Check:

- keyboard navigation
- colour contrast
- semantic HTML
- ARIA labels
- focus states

Prioritise issues by severity.
```

Accessibility isn't optional.

It's part of professional software development.

---

## Step 4 — Production Readiness Review

Ask your AI consulting team:

```text
Perform a production readiness review.

Evaluate:

- maintainability
- scalability
- code quality
- security considerations
- user experience

Return:

- strengths
- risks
- recommendations
```

Notice how different Agents contribute different perspectives.

---

## Step 5 — Fix Remaining Issues

Use Agent Mode.

```text
Address every issue identified during testing.

Do not introduce new features.

Focus only on:

- bug fixes
- accessibility improvements
- usability improvements
- maintainability
```

Review every proposed change before accepting it.

---

# Production Checklist

Before deployment, confirm that you can answer **Yes** to every question.

| Question | Status |
|----------|:------:|
| Does every page load correctly? | ☐ |
| Do all charts render correctly? | ☐ |
| Do filters work? | ☐ |
| Is the layout responsive? | ☐ |
| Is accessibility acceptable? | ☐ |
| Are loading states handled? | ☐ |
| Are empty states handled? | ☐ |
| Would you confidently demo this to a CEO? | ☐ |

If any answer is **No**, keep improving.

---

# Expected Output

You should now have:

- Automated browser testing
- Accessibility review
- Production readiness report
- Bug fixes
- Greater confidence in your application

---

# Repository Changes

```text
tests/

playwright/

Updated components/

Bug fixes

Accessibility improvements

Production readiness notes
```

---

# Business Takeaway

Businesses don't deploy applications because they're finished.

They deploy applications because they're trusted.

Testing transforms confidence from opinion into evidence.

---

# Technical Takeaway

GitHub Copilot can accelerate validation just as effectively as development.

By combining specialised Agents with MCP-powered browser automation, you can identify issues earlier and improve software quality before release.

---

# Reflection

Think back to Module 01.

You started with a messy spreadsheet.

Now you've built, reviewed, tested and refined an executive dashboard ready for real users.

If you were responsible for this application in your organisation...

Would you approve today's build for production?

Why?

---

# Module Checkpoint

You should now have:

- ✅ Tested application
- ✅ Accessibility improvements
- ✅ Production readiness review
- ✅ Bug fixes
- ✅ Deployment confidence

---

# Architecture Snapshot

```text
Business Problem
        │
        ▼
Understand
        │
        ▼
Plan
        │
        ▼
Build
        │
        ▼
Standardise
        │
        ▼
Reuse
        │
        ▼
Specialise
        │
        ▼
Connect
        │
        ▼
Validate
        │
        ▼
Production Ready
```

Your AI is no longer just helping you write software.

It's helping you deliver software that users can trust.

---

# Looking Ahead

Your application is now production-ready.

But executives don't review source code.

They review business outcomes.

In the next module, you'll transform everything you've built into executive deliverables—reports, recommendations and board-ready presentations.

---

# Next Module

## Module 13 — From Dashboard to Boardroom

You'll use GitHub Copilot to generate executive reports, business recommendations and presentation-ready summaries that communicate insights clearly to senior leadership.