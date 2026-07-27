# Module 02 — Understanding the Business with Ask Mode

> **Estimated Time:** 10 minutes  
> **Difficulty:** Beginner  
> **Objective:** Learn how to use GitHub Copilot's Ask Mode to understand a business problem before writing code or building solutions.

---

# Workshop Progress

```text
███░░░░░░░░░░░░░░░░ 14%
```

---

# Learning Objectives

By the end of this module you will:

- Understand when to use Ask Mode
- Explore an unfamiliar dataset
- Identify business questions before writing code
- Learn the difference between understanding and implementing
- Build the foundation for the rest of the workshop

---

# Business Scenario

You've just joined **Nova Retail** as a Business Analyst.

The CEO hands you a spreadsheet and says:

> "This dataset contains our sales information from the past four years.
>
> Tomorrow morning I need recommendations for the board."

As tempting as it is to start building dashboards immediately...

Professional analysts don't.

They first understand:

- What data they have
- What the business cares about
- What questions need answering

Today you'll do exactly that.

---

# Copilot Toolbox

| Capability | Used? | Why? |
|------------|:-----:|------|
| 💬 Ask Mode | ✅ | Explore the business problem |
| 📝 Plan Mode | ❌ | We'll design a solution later |
| 🤖 Agent Mode | ❌ | We'll build later |

---

# Primary Copilot Mode

## 💬 Ask Mode

Today's goal is simple:

Don't build.

Don't edit.

Don't generate code.

Just understand.

Think of Ask Mode as your AI mentor.

Its job isn't to change your project.

Its job is to help you think.

---

# Choosing the Right Copilot Mode

Throughout this workshop, you'll use three different ways of working with Copilot.

| If you want to... | Use |
|-------------------|-----|
| Learn and understand | 💬 Ask |
| Design an approach | 📝 Plan |
| Build and modify your project | 🤖 Agent |

A simple way to remember them is:

```text
Ask

"What is happening?"

↓

Plan

"What should we do?"

↓

Agent

"Go build it."
```

By the end of this workshop, moving between these modes will become second nature.

---

# Why Understanding Comes First

Imagine a consultant walking into a client meeting.

Would they immediately start creating charts?

Or would they first ask questions?

Great analysts spend more time understanding the problem than building the solution.

AI should help you do the same.

---

# Hands-on Exercise

## Step 1 — Open the Project

Open the workshop repository in Visual Studio Code.

Take a quick look at the project structure.

Notice that very little has been built yet.

That's intentional.

We're starting with a blank canvas.

---

## Step 2 — Explore the Dataset

Open the dataset.

Spend one minute looking through it yourself.

Don't ask Copilot yet.

Try to answer:

- What kind of business is this?
- What information is available?
- Which columns look important?

Human observation should always come before AI assistance.

---

## Step 3 — Start a Conversation

Open **Ask Mode**.

Use the following prompt:

```text
You're a Senior Business Analyst.

Review this dataset.

Without writing any code:

- explain what the business appears to do
- identify the important columns
- list the KPIs an executive would likely care about
- suggest five business questions this dataset could answer

Do not make assumptions that aren't supported by the data.
```

Read the response carefully.

Notice that Copilot is helping you understand the business rather than solving the problem for you.

---

## Step 4 — Ask Better Follow-up Questions

Good analysts don't stop after one answer.

Continue the conversation.

Try prompts like:

```text
Which columns might have data quality issues?
```

```text
Which metrics would be most useful for a CEO?
```

```text
If you were presenting this to executives tomorrow, what additional information would you want before making recommendations?
```

Observe how each follow-up question builds on the previous conversation.

---

## Step 5 — Think Like a Consultant

Now ask:

```text
Imagine you have only 30 minutes with the CEO.

What are the three most important questions you would ask before building a dashboard?

Explain why each question matters.
```

This shifts the focus from data to business value.

---

# Expected Output

By the end of this exercise, you should have:

- A clear understanding of the dataset
- A list of potential KPIs
- Several business questions to investigate
- Confidence using Ask Mode to explore unfamiliar problems

You should **not** have written any code yet.

That's by design.

---

# Business Takeaway

Successful business analysts don't begin with dashboards.

They begin with questions.

The quality of your recommendations depends on how well you understand the business problem.

---

# Technical Takeaway

Ask Mode is designed for exploration and learning.

Use it when you need to:

- Understand unfamiliar code or data
- Brainstorm ideas
- Learn a new concept
- Explore different approaches
- Build context before implementation

In the next module, you'll learn how to make Ask Mode dramatically more effective through better prompting.

---

# Reflection

Before moving on, ask yourself:

- What surprised you about the dataset?
- Which KPI do you think will matter most to the CEO?
- Did Ask Mode reveal something you hadn't noticed yourself?

Remember:

AI answers the questions you ask.

Learning to ask better questions is one of the most valuable skills you'll develop.

---

# Module Checkpoint

You should now be able to:

- ✅ Explain when Ask Mode is the right choice
- ✅ Explore an unfamiliar dataset with AI
- ✅ Identify potential business questions
- ✅ Distinguish understanding from implementation

---

# Architecture Snapshot

```text
Business Challenge
        │
        ▼
Understand the Problem
     (Ask Mode)
```

Every successful project starts with understanding.

Everything else builds on that foundation.

---

# Looking Ahead

You now know how to explore a business problem with AI.

But there's a catch.

Two people can ask Copilot the same question and receive very different answers.

The difference isn't the AI.

It's the prompt.

In the next module, you'll learn how consultants structure prompts to produce clearer, more reliable and more actionable results.

---

# Next Module

## Module 03 — Prompting Like a Consultant

You'll learn how to transform simple questions into professional prompts by adding:

- Role
- Context
- Objective
- Audience
- Constraints
- Desired output format

Small improvements in your prompts can produce dramatically better results—and those techniques will be used throughout the rest of the workshop.