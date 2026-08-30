# E-commerce Sales & Customer Analysis — Python

Portfolio-ready Junior Data Analyst project demonstrating an end-to-end analytics workflow with Python, Pandas, NumPy and Matplotlib.

> **Data note:** The dataset is synthetic and created for this portfolio project. It intentionally contains a small number of data-quality issues so cleaning and validation can be demonstrated honestly.

## Business Questions

1. How are sales and order volume changing over time?
2. Which categories and regions generate the most revenue?
3. Which sales channels perform best?
4. What is the average order value (AOV)?
5. What percentage of customers are repeat customers?
6. What share of orders are cancelled or returned?
7. Are there data-quality issues that could affect reporting?

## Tools

Python • Pandas • NumPy • Matplotlib • Jupyter • pytest • Git/GitHub

## Workflow

**Raw CSV → Data quality checks → Cleaning → KPI analysis → EDA → Business recommendations**

## KPIs

- Completed revenue
- Completed orders
- Units sold
- Average order value (AOV)
- Repeat-customer rate
- Cancellation and return rate
- Revenue by category, region and channel
- Monthly revenue trend

## Run

```bash
python -m venv .venv
pip install -r requirements.txt
python src/analysis.py
pytest -q
```

The Jupyter notebook in `notebooks/` provides the step-by-step analysis workflow.

## Portfolio Talking Points

- Built a reproducible Python/Pandas workflow for transactional data.
- Validated duplicates, missing values, data types and business-rule consistency before analysis.
- Created reusable KPI functions for revenue, AOV and repeat-customer rate.
- Used visual analysis to turn data into business-oriented findings.
- Added automated tests for core analytical calculations.

This is a portfolio/learning project; the data must not be presented as real company data.