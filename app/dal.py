from app.db import get_db_connection


def get_customers_by_credit_limit_range():
    """1. Return customers with credit limits outside the normal range."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT customerName,
                             creditLimit
                      FROM customers
                      WHERE creditLimit < 10000
                         OR creditLimit > 100000;""")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def get_orders_with_null_comments():
    """2. Return orders that have null comments."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT orderNumber, comments
                      FROM orders
                      WHERE comments IS NULL
                      ORDER BY orderDate;""")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def get_first_5_customers():
    """3. Return the first 5 customers."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT c.customerName,
                             e.lastName  AS salesLastName,
                             e.firstName AS salesFirstName
                      FROM customers c
                               NATURAL JOIN employees e
                      ORDER BY salesLastName LIMIT 5;""")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def get_payments_total_and_average():
    """4. Return total and average payment amounts."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT SUM(amount) AS total_sum,
                             AVG(amount) AS average_sum,
                             MAX(amount) AS max_sum,
                             MIN(amount) AS min_sum
                      FROM payments;""")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def get_employees_with_office_phone():
    """5. Return employees with their office phone numbers."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT e.firstName,
                             e.lastName,
                             o.phone AS officePhone
                      FROM employees e
                               NATURAL JOIN offices o;""")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def get_customers_with_shipping_dates():
    """6. Return customers with their order shipping dates."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT c.customerName, o.shippedDate
                      FROM customers c
                               LEFT JOIN orders o ON c.customerNumber = o.customerNumber;""")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def get_customer_quantity_per_order():
    """7. Return customer name and quantity for each order."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT c.customerName, SUM(od.quantityOrdered) AS totalQuantity
                      FROM customers c
                               NATURAL JOIN orders o
                               NATURAL JOIN orderdetails od
                      GROUP BY c.customerName, o.orderNumber
                      ORDER BY c.customerName;""")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """8. Return customers and payments for last names matching pattern."""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT c.customerName,
                             CONCAT(e.firstName, ' ', e.lastName) AS salesRepName,
                             SUM(p.amount)                        AS totalPayments
                      FROM customers c
                               NATURAL JOIN employees e
                               NATURAL JOIN orders o
                               NATURAL JOIN payments p
                      WHERE e.firstName LIKE '%Mu%'
                         OR e.firstName LIKE '%ly%'
                      GROUP BY c.customerName, salesRepName;""")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
