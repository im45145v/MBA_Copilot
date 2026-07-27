# Examples — Clean Business Dataset Skill

This document demonstrates how to use the **Clean Business Dataset** skill effectively.

---

# Example 1 — Clean a Newly Imported Dataset

## Prompt

```text
Clean the Global Superstore dataset before any analysis.

Validate the dataset, identify missing values, remove duplicate records, standardise categorical values, validate dates and numeric fields, then generate a cleaned dataset together with a data quality report.
```

---

## Expected Workflow

```text
Inspect Dataset

↓

Validate Structure

↓

Review Missing Values

↓

Remove Duplicates

↓

Standardise Categories

↓

Validate Dates

↓

Validate Numeric Fields

↓

Generate Quality Report

↓

Export Clean Dataset
```

---

## Expected Output

```text
cleaned_dataset.csv

data_quality_report.md
```

---

# Example 2 — Validate an Existing Dataset

## Prompt

```text
Review the dataset and identify any data quality issues without modifying the original file.

Produce a report describing missing values, duplicate records, invalid values and inconsistent categories.
```

---

## Expected Output

```text
## Dataset Summary

Rows:
Columns:

---

## Data Quality Findings

Duplicate Records

Missing Values

Invalid Dates

Invalid Numeric Values

Inconsistent Categories

---

## Overall Assessment

The dataset is suitable for business analysis after the identified issues are resolved.
```

---

# Example 3 — Prepare Data for an Executive Dashboard

## Prompt

```text
Prepare the sales dataset for use in an executive dashboard.

Ensure all business metrics can be calculated reliably and document every transformation performed.
```

---

## Expected Tasks

- Validate required columns
- Remove duplicate records
- Standardise categories
- Verify date formats
- Check profit calculations
- Export cleaned dataset

---

# Example 4 — Standardise Regional Data

## Prompt

```text
Review all regional values and standardise inconsistent naming.

Examples include:

US
U.S.
USA
United States

Ensure a single naming convention is used throughout the dataset.
```

---

## Expected Result

Before

```text
US
USA
United States
U.S.
```

After

```text
United States
```

Every transformation should be documented.

---

# Example 5 — Missing Value Assessment

## Prompt

```text
Analyse all missing values in the dataset.

Explain their potential business impact and recommend an appropriate handling strategy instead of automatically deleting records.
```

---

## Expected Output

```text
Column

Missing Count

Percentage

Business Impact

Recommended Action
```

---

# Example 6 — Numeric Validation

## Prompt

```text
Identify suspicious numerical values including:

- negative revenue
- impossible discounts
- invalid quantities
- unrealistic profit values

Explain why each issue should be investigated.
```

---

## Expected Output

```text
Issue

Affected Records

Business Impact

Recommended Resolution
```

---

# Example 7 — Data Quality Report

## Prompt

```text
Generate a professional Markdown report summarising all data quality checks performed during dataset preparation.
```

---

## Example Structure

```text
# Data Quality Report

## Dataset Summary

## Validation Checks

## Duplicate Records

## Missing Values

## Category Standardisation

## Date Validation

## Numeric Validation

## Remaining Issues

## Overall Data Quality Assessment
```

---

# Best Practices

Always:

- preserve the original dataset
- explain every transformation
- document assumptions
- generate reproducible outputs
- report unresolved issues

Never:

- silently delete records
- fabricate missing values
- ignore validation failures
- overwrite source data

---

# Success Example

A successful execution of this skill results in:

- a validated dataset
- a cleaned export
- a documented transformation process
- a data quality report
- data ready for business analysis and executive dashboards