---
name: Clean Business Dataset
description: Clean, validate and prepare business datasets for analysis and executive dashboards.
---

# Clean Business Dataset

## Purpose

This skill standardises how datasets are prepared throughout the workshop.

Use this skill whenever a dataset must be cleaned before analysis, dashboard creation or report generation.

Never analyse raw business data without validating it first.

---

# When To Use

Use this skill when:

- importing a new dataset
- preparing data for dashboards
- generating reports
- analysing sales
- validating business data
- creating KPI calculations

Do not use this skill if the user only wants to visualise already validated data.

---

# Objectives

Produce a dataset that is:

- accurate
- complete
- consistent
- ready for analysis

The resulting dataset should be suitable for executive reporting.

---

# Workflow

Follow these steps.

## 1. Inspect Dataset

Determine:

- number of rows
- number of columns
- column names
- data types

Identify obvious anomalies.

---

## 2. Validate Structure

Verify:

- required columns exist
- data types are appropriate
- identifiers are unique where expected

Report structural issues before making changes.

---

## 3. Identify Missing Values

Review every column.

Determine:

- missing count
- percentage missing
- possible business impact

Never silently discard missing values.

---

## 4. Remove Duplicate Records

Detect duplicate rows.

Document:

- duplicate count
- removal strategy

Only remove duplicates when justified.

---

## 5. Standardise Values

Standardise:

- category names
- regions
- dates
- currency formats
- text casing

Ensure values are consistent across the dataset.

---

## 6. Validate Numeric Fields

Check for:

- negative revenue
- impossible discounts
- invalid quantities
- unrealistic profit values

Document every anomaly.

---

## 7. Validate Dates

Verify:

- date format
- invalid dates
- future dates where inappropriate

Ensure chronological consistency.

---

## 8. Generate Data Quality Report

Summarise:

- issues found
- issues corrected
- remaining concerns
- confidence level

---

## 9. Export Results

Produce:

```
cleaned_dataset.csv

data_quality_report.md
```

Do not overwrite original data.

---

# Expected Output

Always produce:

- cleaned dataset
- quality report

When requested, also generate:

- summary statistics
- validation tables
- issue log

---

# Validation Checklist

Before completion verify:

☐ Duplicate records removed

☐ Missing values reviewed

☐ Categories standardised

☐ Dates validated

☐ Numeric fields validated

☐ Quality report generated

---

# Best Practices

Always:

- preserve original data
- document transformations
- explain business impact
- keep cleaning reproducible

Avoid hidden transformations.

Every modification should be explainable.

---

# Success Criteria

The cleaned dataset should:

- be internally consistent
- support reliable KPI calculations
- require no additional cleaning before analysis
- be suitable for dashboards and executive reporting