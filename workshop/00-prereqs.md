# Module 00 — Prerequisites & Environment Setup

> **Estimated Time:** 10 minutes
> **Difficulty:** Beginner
> **Objective:** Prepare your development environment and verify that GitHub Copilot Agent Mode is working before we begin the workshop.

---

# Welcome 👋

Welcome to **Build Your AI Business Analyst with GitHub Copilot**.

In this workshop, you'll transform a messy business dataset into a modern Business Intelligence platform using **GitHub Copilot Agent Mode**.

By the end of this workshop, you'll have built:

* 📊 A professional business analytics dashboard
* 🎯 Multiple executive dashboards (CEO, CFO, Marketing & Operations)
* ✨ A polished UI with Tailwind CSS, shadcn/ui and Framer Motion
* 🌍 A live deployed application
* 📄 A board-ready executive report in PDF
* 🤖 A reusable AI-powered development workflow

Throughout the workshop, you'll work on **one project** that evolves module by module.

---

# Workshop Progress

```text
█░░░░░░░░░░░░░░░░░░░ 0%
```

---

# Learning Objectives

By the end of this module you will:

* Install the required software
* Configure GitHub Copilot
* Enable Agent Mode
* Clone the workshop repository
* Run the starter project locally

---

# Prerequisites

Please complete each step before moving to Module 01.

---

# 1. GitHub Account

Create a GitHub account if you don't already have one.

https://github.com/signup

> **Recommended:** Sign in to GitHub inside Visual Studio Code before continuing.

---

# 2. Install Visual Studio Code

Download Visual Studio Code.

https://code.visualstudio.com/

Recommended extensions:

* GitHub Copilot
* GitHub Copilot Chat
* ESLint
* Prettier
* Tailwind CSS IntelliSense

---

# 3. Install Git

Verify Git is installed.

```bash
git --version
```

If Git is not installed, download it from:

https://git-scm.com/downloads

---

# 4. Install Node.js

Install the latest LTS release.

Verify your installation.

```bash
node -v
npm -v
```

---

# 5. Install Python

Install Python 3.11 or newer.

Verify your installation.

```bash
python --version
```

---

# 6. GitHub Copilot

Open VS Code.

Install:

* GitHub Copilot
* GitHub Copilot Chat

Sign in using your GitHub account.

Open Copilot Chat and verify it opens successfully.

---

# 7. Enable Agent Mode

Throughout this workshop we'll use **Agent Mode**, not standard Chat mode.

Open Copilot Chat and switch to **Agent**.

> **Note**
>
> The interface may change over time as GitHub continues to improve Copilot.
>
> If your UI looks slightly different from the screenshots, that's expected.

---

# 8. Install GitHub Copilot CLI *(Optional)*

Some demonstrations will also use the Copilot CLI.

Install:

```bash
npm install -g @github/copilot
```

Verify installation.

```bash
github-copilot --help
```

> If the CLI installation changes in the future, follow the latest GitHub documentation.

---

# 9. Clone the Workshop Repository

Clone the starter repository.

```bash
git clone <repository-url>
```

Open it.

```bash
code ai-business-analyst-workshop
```

---

# 10. Install Dependencies

Install all project dependencies.

```bash
npm install
```

---

# 11. Start the Development Server

```bash
npm run dev
```

Open your browser.

```
http://localhost:3000
```

You should see the workshop starter application.

Don't worry if it looks very basic—we'll transform it throughout the workshop.

---

# Starter Repository

Your repository should look similar to this.

```text
ai-business-analyst-workshop/

├── app/
├── components/
├── data/
├── public/
├── reports/
├── scripts/
├── .github/
├── package.json
└── README.md
```

We'll explore these folders later.

---

# Verify Your Environment

Before continuing, confirm the following.

| Requirement              | Status |
| ------------------------ | ------ |
| GitHub Account           | ☐      |
| VS Code Installed        | ☐      |
| Git Installed            | ☐      |
| Node.js Installed        | ☐      |
| Python Installed         | ☐      |
| GitHub Copilot Installed | ☐      |
| Copilot Chat Working     | ☐      |
| Agent Mode Enabled       | ☐      |
| Repository Cloned        | ☐      |
| Application Running      | ☐      |

---

# Workshop Structure

We'll improve the same project throughout the workshop.

```text
Messy Dataset
      │
      ▼
Business Analysis
      │
      ▼
Data Cleaning
      │
      ▼
Interactive Dashboard
      │
      ▼
Professional UI
      │
      ▼
Executive Dashboards
      │
      ▼
Deployment
      │
      ▼
Executive Report
```

Every module introduces **one new GitHub Copilot capability**.

By the end, you'll understand not only **how** to use Copilot—but also **when** to use each capability effectively.

---

# Before You Continue

Make sure:

* ✅ Your development server is running
* ✅ GitHub Copilot is responding
* ✅ Agent Mode is enabled
* ✅ The workshop repository opens successfully in VS Code

If everything is working, you're ready for the first challenge.

---

# Up Next

## Module 01 — The Business Challenge

In the next module you'll:

* Meet your client
* Understand the business problem
* Explore the company
* Learn what success looks like
* See the final application you'll build

No coding yet.

First, let's understand **why** we're building it.
