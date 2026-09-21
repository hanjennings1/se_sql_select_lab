# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

### Add code below and run file to see data from employees table ###
# employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
# print("---------------------Employee Data---------------------")
# print(employee_data)
# print("-------------------End Employee Data-------------------")


# STEP 2 - EMPLOYEE NUMBER AND LAST NAME FOR ALL EMPLOYEES
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName FROM employees
""", conn)
print(df_first_five)

# STEP 3 - SAME AS STEP 2, BUT LAST NAME THEN EMPLOYEE #
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber FROM employees
""", conn)
print(df_five_reverse)

# STEP 4 - SAME AS STEP 3, BUT ADD AN ALIAS EMPLOYEE # = 'ID'
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID FROM employees
""", conn)
print(df_alias)

# STEP 5 - LABEL EACH EMPLOYEE AS EXECUTIVE OR NOT EXECUTIVE
df_executive = pd.read_sql("""
SELECT *,
CASE
    WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
    ELSE 'Not Executive'
END AS role
FROM employees
""", conn)
print(df_executive)

# STEP 6 - LENGTH OF EACH LAST NAME, AS A COLUMN CALLED name_length
df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length
FROM employees
""", conn)
print(df_name_length)

# STEP 7 - FIRST TWO LETTERS OF EACH JOB TITLE AS NEW COLUMN CALLED short_title
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees
""", conn)
print(df_short_title)


### Add the code below and run the file to see order details data ###
# order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
# print("------------------Order Details Data------------------")
# print(order_details)
# print("----------------End Order Details Data----------------")

# STEP 8 - TOTAL AMOUNT OF ALL ORDERS, ROUNDED
sum_total_price = pd.read_sql("""
SELECT 
(ROUND(priceEach * quantityOrdered)) AS total_price
FROM orderDetails
""", conn).sum()
print(sum_total_price)

# STEP 9 - ORDER DATE PLUS DAY, MONTH, AND YEAR COLUMNS
df_day_month_year = pd.read_sql("""
SELECT orderDate,
       strftime('%d', orderDate) AS day,
       strftime('%m', orderDate) AS month,
       strftime('%Y', orderDate) AS year
FROM orders
""", conn)
print(df_day_month_year)


# CLOSE THE CONNECTION
conn.close()