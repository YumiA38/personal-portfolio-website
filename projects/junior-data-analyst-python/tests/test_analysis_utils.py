import pandas as pd

from src.analysis_utils import average_order_value, repeat_customer_rate, total_revenue


def sample_df():
    return pd.DataFrame({
        "order_id": ["1", "2", "3"],
        "customer_id": [10, 10, 20],
        "order_status": ["Completed", "Completed", "Cancelled"],
        "revenue_eur": [100.0, 50.0, 999.0],
    })


def test_total_revenue_ignores_cancelled_orders():
    assert total_revenue(sample_df()) == 150.0


def test_average_order_value_uses_completed_orders():
    assert average_order_value(sample_df()) == 75.0


def test_repeat_customer_rate():
    assert repeat_customer_rate(sample_df()) == 100.0
