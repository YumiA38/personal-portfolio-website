# E-commerce Sales & Customer Analysis — Python

A portfolio-ready **Junior Data Analyst** project demonstrating an end-to-end analytics workflow with Python, Pandas, NumPy and Matplotlib.

> **Data note:** The dataset in this repository is synthetic and was generated specifically for this portfolio project. It is intentionally seeded with a small number of duplicates and missing values so the data-cleaning and validation workflow can be demonstrated honestly.

## Business Questions

1. How are sales and order volume changing over time?
2. Which product categories and regions generate the most revenue?
3. Which sales channels perform best?
4. What is the average order value (AOV)?
5. What percentage of customers are repeat customers?
6. How much revenue is affected by cancelled or returned orders?
7. Are there data-quality issues that could affect reporting?

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- pytest
- Git / GitHub

## Workflow

**Raw CSV → Data quality checks → Cleaning → Feature engineering → EDA → KPI analysis → Business recommendations**

## KPIs

- Total completed revenue
- Completed orders
- Average order value (AOV)
- Units sold
- Repeat-customer rate
- Cancellation/return rate
- Revenue by category, region and channel
- Monthly revenue trend

## Run

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
jupyter notebook notebooks/ecommerce_sales_analysis.ipynb
```

## Portfolio Talking Points

- Built a reproducible Python/Pandas workflow for cleaning and analysing transactional data.
- Validated missing values, duplicate records, data types and business-rule consistency before analysis.
- Created reusable KPI functions for revenue, AOV and repeat-customer rate.
- Translated analysis into business recommendations rather than only reporting numbers.
- Added automated tests for core analytical calculations.

This is a portfolio/learning project. The data is synthetic and should not be described as real company data in applications.
