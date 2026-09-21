# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# Add code below and run file to see data from employees table
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

# STEP 5
# Replace None with your code
df_executive = None

# STEP 6
# Replace None with your code
df_name_length = None

# STEP 7
# Replace None with your code
df_short_title = None

# STEP 8
# Replace None with your code
sum_total_price = None

# STEP 9
# Replace None with your code
df_day_month_year = None

conn.close()