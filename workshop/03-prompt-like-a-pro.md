# Module 03 — Prompting Like a Consultant

> **Estimated Time:** 12 minutes  
> **Difficulty:** Beginner  
> **Objective:** Learn how to write structured prompts that produce clearer, more reliable and more actionable responses from GitHub Copilot.

---

# Workshop Progress

```text
█████░░░░░░░░░░░░░░ 21%
```

---

# Learning Objectives

By the end of this module you will:

- Understand why prompt quality matters
- Learn the anatomy of a great prompt
- Compare weak prompts with structured prompts
- Produce more reliable business analysis
- Prepare for using Plan Mode in the next module

---

# Business Scenario

You've now explored the dataset.

You understand the business.

Your manager walks over and says:

> "I asked Copilot the same question you did, but I got a completely different answer."

Why?

Because AI doesn't only depend on the model.

It depends on **how you communicate your intent**.

Professional consultants don't ask vague questions.

They provide context, define objectives and clearly describe the expected outcome.

Today, you'll learn to do the same.

---

# Copilot Toolbox

| Capability | Used? | Why? |
|------------|:-----:|------|
| 💬 Ask Mode | ✅ | Compare prompts and refine analysis |
| 📝 Plan Mode | ❌ | Next module |
| 🤖 Agent Mode | ❌ | We'll build later |

---

# Primary Copilot Mode

## 💬 Ask Mode

Today we're still using Ask Mode.

We're not changing files.

We're improving our thinking.

Better prompts lead to better answers.

---

# Why Prompting Matters

Imagine asking a consultant:

> "Tell me about our business."

Now compare it to:

> "You're preparing tomorrow's board meeting. Analyse our sales performance, identify the biggest business risks and recommend three strategic priorities."

Which question would produce the more useful answer?

The same principle applies to AI.

---

# Anatomy of a Great Prompt

A simple framework you can use throughout this workshop:

```text
Role

↓

Context

↓

Objective

↓

Constraints

↓

Desired Output
```

Think of prompts as writing a project brief.

The clearer the brief, the better the outcome.

---

# Example Comparison

## Weak Prompt

```text
Analyse this dataset.
```

Possible result:

- Generic observations
- Missing business context
- No prioritisation
- Difficult to act on

---

## Better Prompt

```text
You are a Senior Business Analyst preparing tomorrow's executive board meeting.

Analyse the sales dataset.

Focus on:

- overall business performance
- profit trends
- customer behaviour
- regional performance

Identify:

- three major insights
- two business risks
- three recommendations

Present your findings in clear executive language.
```

Notice how much more context you've provided.

---

# Hands-on Exercise

## Step 1 — Start with a Simple Prompt

Open **Ask Mode**.

Try this prompt:

```text
Analyse this dataset.
```

Read the response.

It's useful...

But also quite generic.

---

## Step 2 — Improve the Prompt

Now try:

```text
You are the Lead Business Analyst at Nova Retail.

Tomorrow you are presenting to the executive board.

Review the dataset and provide:

- Executive Summary
- Top 5 Insights
- Biggest Business Risk
- Largest Growth Opportunity
- Three Strategic Recommendations

Write for senior executives.

Avoid technical language.
```

Compare both answers.

Which one would you actually use in a board meeting?

---

## Step 3 — Add Constraints

Prompt engineering isn't only about adding information.

It's also about removing ambiguity.

Try:

```text
Limit your response to 300 words.

Prioritise findings based on business impact.

Do not speculate beyond the available data.

Use bullet points where appropriate.
```

Notice how the output becomes more focused.

---

## Step 4 — Iterate

Professional AI users rarely stop after one response.

Continue the conversation.

Try prompts such as:

```text
Expand on recommendation two.
```

```text
Explain this finding using simpler business language.
```

```text
Rank these recommendations by expected business impact.
```

Small follow-up prompts often produce better results than rewriting everything.

---

# Prompt Improvement Checklist

Before sending a prompt, ask yourself:

✅ Have I defined a role?

✅ Have I provided enough context?

✅ Is my objective clear?

✅ Have I included useful constraints?

✅ Have I specified the desired output?

If the answer is "yes" to all five, you're likely to receive a much better response.

---

# Expected Output

By the end of this exercise, you should have:

- A well-structured executive analysis
- Better business recommendations
- More confidence writing prompts
- A repeatable prompt framework

---

# Business Takeaway

Clear communication is one of the most valuable business skills.

The same applies when working with AI.

The quality of the output is strongly influenced by the quality of the instructions.

---

# Technical Takeaway

Prompt engineering isn't about memorising magic phrases.

It's about providing:

- context
- clarity
- structure
- expectations

These principles will improve your interactions with any AI assistant.

---

# Reflection

Think about your first prompt.

How many important details were missing?

Now compare it to your improved prompt.

Which changes made the biggest difference?

How might you apply this approach in your own work?

---

# Module Checkpoint

You should now be able to:

- ✅ Structure effective prompts
- ✅ Improve AI responses through context
- ✅ Compare weak and strong prompts
- ✅ Use Ask Mode more effectively

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
```

You've learned how to ask better questions.

Now it's time to decide **how** to solve the problem.

---

# Looking Ahead

Until now, you've focused on understanding the business.

The next step is deciding **how** to approach the work.

Should you clean the data first?

Which files should be created?

What order should the tasks happen in?

Rather than jumping straight into implementation, you'll first create a plan.

Then you'll hand that plan to GitHub Copilot's Agent Mode for execution.

This is how many professional teams work with AI today.

---

# Next Module

## Module 04 — Planning Before Building

You'll learn how to:

- Use Plan Mode to design a solution
- Review and refine AI-generated plans
- Hand off an approved plan to Agent Mode
- Execute the implementation with confidence

Instead of asking AI to immediately write code, you'll learn a workflow that separates **thinking**, **planning** and **execution**.