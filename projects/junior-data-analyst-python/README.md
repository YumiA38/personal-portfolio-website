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
- Git / GitHub

## Workflow

**Raw CSV → Data quality checks → Cleaning → Feature engineering → EDA → KPI analysis → Business recommendations**

The project follows a reproducible structure rather than presenting only final charts. This is intentional because a strong junior analytics portfolio should show the complete path from raw data to interpretable findings. 

## Key KPIs

- Total completed revenue
- Completed orders
- Average order value (AOV)
- Units sold
- Repeat-customer rate
- Return/cancellation rate
- Revenue by category, region and channel
- Monthly revenue trend

## Project Structure

```text
junior-data-analyst-python-project/
├── data/
│   └── ecommerce_orders_raw.csv
├── notebooks/
│   └── ecommerce_sales_analysis.ipynb
├── src/
│   └── analysis_utils.py
├── tests/
│   └── test_analysis-utils.py
├── requirements.txt
└── README.md
```

## How to Run

```bash
python -m venv .venv#om \nSource or activate the environment as appropriate.\npip install -r requirements.txt\njupyter notebook notebooks/ecommerce_sales_analysis.ipynb
```
