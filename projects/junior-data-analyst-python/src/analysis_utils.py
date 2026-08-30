from __future__ import annotations

import pandas as pd


def completed_orders(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[df["order_status"].eq("Completed")].copy()


def total_revenue(df: pd.DataFrame) -> float:
    completed = completed_orders(df)
    return float(completed["revenue_eur"].sum())


def average_order_value(df: pd.DataFrame) -> float:
    completed = completed_orders(df)
    if completed.empty:
        return 0.0
    return float(completed["revenue_eur"].sum() / completed["order_id"].nunique())


def repeat_customer_rate(df: pd.DataFrame) -> float:
    completed = completed_orders(df)
    orders_per_customer = completed.groupby("customer_id")["order_id"].nunique()
    if orders_per_customer.empty:
        return 0.0
    return float((orders_per_customer.ge(2).mean()) * 100)
