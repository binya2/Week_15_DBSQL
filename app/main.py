from fastapi import FastAPI

import dal
from db_init import init_database

app = FastAPI()

init_database()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    results = dal.get_customers_by_credit_limit_range()
    return results


@app.get("/q2/orders-null-comments")
def orders_null_comments():
    results = dal.get_orders_with_null_comments()
    return results


@app.get("/q3/customers-first-5")
def customers_first_5():
    results = dal.get_first_5_customers()
    return results


@app.get("/q4/payments-total-average")
def payments_total_average():
    results = dal.get_payments_total_and_average()
    return results


@app.get("/q5/employees-office-phone")
def employees_office_phone():
    results = dal.get_employees_with_office_phone()
    return results


@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    results = dal.get_customers_with_shipping_dates()
    return results


@app.get("/q7/customer-quantity-per-order")
def get_customer_quantity_per_order():
    results = dal.get_customer_quantity_per_order()
    return results


@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern():
    results = dal.get_customers_payments_by_lastname_pattern()
    return results
