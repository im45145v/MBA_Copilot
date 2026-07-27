---
applyTo: "**/*.py"
description: "Python development standards for business analytics, data processing and reporting."
---

# Python Development Instructions

## Purpose

These instructions define how GitHub Copilot should generate Python code for this repository.

Python is primarily used for:

- Data cleaning
- Data validation
- Business analysis
- Report generation
- Data preparation

The focus should always be on readability, correctness and maintainability.

---

# Philosophy

This repository is educational.

Generated Python code should:

- be easy to understand
- explain business logic clearly
- avoid unnecessary optimisation
- favour readability over clever implementations

Assume contributors have basic Python knowledge.

---

# Technology Stack

Prefer:

- Python 3.13+
- Pandas
- NumPy
- Plotly (only if specifically requested)
- Standard Library

Avoid introducing additional dependencies unless there is a clear benefit.

---

# Code Organisation

Organise code into reusable functions.

Avoid long scripts.

Prefer:

```python
load_data()

↓

clean_data()

↓

validate_data()

↓

analyse_data()

↓

generate_report()
```

Each function should have one responsibility.

---

# Naming Conventions

Use descriptive names.

Good examples:

```python
load_sales_data()

calculate_profit_margin()

validate_order_dates()

generate_executive_report()
```

Avoid names like:

```python
test()

run()

new_function()

temp()
```

---

# Function Design

Functions should:

- perform one task
- have descriptive names
- return predictable values
- avoid side effects

Keep functions small.

---

# Documentation

Every public function should include a docstring.

Example:

```python
def calculate_profit_margin(df):
    """
    Calculate the profit margin for each order.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """
```

---

# Type Hints

Prefer type hints whenever practical.

Example:

```python
def load_data(path: str) -> pd.DataFrame:
```

Avoid untyped public functions.

---

# Pandas Standards

Prefer:

- method chaining where readable
- vectorised operations
- descriptive column names

Avoid:

- unnecessary loops
- modifying DataFrames in unexpected ways
- chained indexing

---

# Data Cleaning Standards

Whenever cleaning data:

Check for:

- duplicate rows
- missing values
- invalid dates
- inconsistent categories
- invalid numerical values

Never silently discard data.

Document every transformation.

---

# Data Validation

Always validate:

- column existence
- data types
- null values
- duplicate records
- date formats

Raise meaningful errors whenever possible.

---

# Error Handling

Provide useful error messages.

Good example:

```text
Column "Profit" not found in dataset.
```

Avoid:

```text
Error
```

---

# Logging

Prefer informative logging.

Example:

```python
Loaded 9,994 records.

Removed 24 duplicate rows.

Generated executive report.
```

Avoid excessive logging.

---

# Performance

Prefer readable code first.

Optimise only when:

- processing large datasets
- repeated calculations become expensive

Avoid premature optimisation.

---

# Business Analysis

When calculating metrics:

Always explain:

- what is being calculated
- why it matters
- any assumptions made

Never fabricate business values.

---

# Report Generation

Reports should include:

- Executive Summary
- KPI Review
- Key Findings
- Risks
- Opportunities
- Recommendations

Use Markdown where appropriate.

---

# Visualisations

Only generate charts that support business decisions.

Always include:

- titles
- axis labels
- legends (when applicable)

Avoid decorative charts.

---

# File Organisation

Prefer:

```
scripts/

analysis/

reports/

utils/
```

Keep business logic separate from presentation logic.

---

# Testing

Whenever practical:

Generate simple unit tests for:

- calculations
- validation functions
- data transformations

Business-critical calculations should be testable.

---

# Collaboration

Python code should work alongside:

- Repository Instructions
- Business Analyst Instructions
- Frontend Instructions

Python prepares trusted data.

The frontend communicates it.

---

# Success Criteria

Generated Python code should:

- be readable
- be maintainable
- be testable
- validate input data
- explain business logic
- support executive decision-making

Every script should improve the quality and trustworthiness of business insights.