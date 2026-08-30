from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from analysis_utils import total_revenue, average_order_value, repeat_customer_rate

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "ecommerce_orders_raw.csv", parse_dates=["order_date"])

print("Raw shape:", df.shape)
print("Duplicate rows:", df.duplicated().sum())
print("Missing values:\n", df.isna().sum().sort_values(ascending=False))

clean = df.drop_duplicates().copy()
clean["region"] = clean["region"].fillna("Unknown")
clean["payment_method"] = clean["payment_method"].fillna("Unknown")
clean["discount_pct"] = clean["discount_pct"].fillna(0)
clean["revenue_eur"] = (clean["unit_price"] * clean["quantity"] * (1 - clean["discount_pct"])).round(2)

assert clean["order_id"].is_unique
assert clean["revenue_eur"].ge(0).all()

completed = clean[clean["order_status"].eq("Completed")].copy()

kpis = {
    "Completed revenue (€)": total_revenue(clean),
    "Completed orders": completed["order_id"].nunique(),
    "Units sold": int(completed["quantity"].sum()),
    "Average order value (€)": average_order_value(clean),
    "Repeat customer rate (%)": repeat_customer_rate(clean),
    "Cancellation rate (%)": clean["order_status"].eq("Cancelled").mean() * 100,
    "Return rate (%)": clean["order_status"].eq("Returned").mean() * 100,
}
print("\nKPI SUMMARY")
for key, value in kpis.items():
    print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")

category = completed.groupby("category")["revenue_eur"].sum().sort_values(ascending=False)
region = completed.groupby("region")["revenue_eur"].sum().sort_values(ascending=False)

print("\nRevenue by category:\n", category)
print("\nRevenue by region:\n", region)

monthly = completed.assign(month=completed["order_date"].dt.to_period("M").dt.to_timestamp()).groupby("month")["revenue_eur"].sum()

plt.figure(figsize=(10, 4.5))
plt.plot(monthly.index, monthly.values, marker="o")
plt.title("Monthly Completed Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(ROOT / "monthly_revenue.png", dpi=160)
plt.show()
