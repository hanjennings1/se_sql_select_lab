# SQL SELECT Lab: Northwind Employee & Order Data
**Completed Sept 21, 2026**

A completed lab exploring how to retrieve and transform data with SQL from Python. Working as a data analyst for the fictional Northwind Company, I query the company's SQLite database, load the results into pandas DataFrames, and use SQL features like column selection, aliasing, `CASE` statements, and built-in functions.

> Forked from [learn-co-curriculum/se_sql_select_lab](https://github.com/learn-co-curriculum/se_sql_select_lab).

## Status

All 9 steps are complete and the full test suite passes (`9 passed`).

## What This Project Demonstrates

- Connecting to a SQLite database file with Python's `sqlite3` module
- Running SQL queries and loading the results into pandas with `pd.read_sql`
- Selecting and reordering columns with `SELECT`
- Renaming columns with `AS` aliases
- Labeling rows with `CASE` (which adds a column rather than filtering rows)
- Transforming data with built-in SQL functions: `LENGTH`, `SUBSTR`, `ROUND`, and `strftime`
- Aggregating values with pandas' `.sum()`

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | My solutions for Steps 1 through 9 |
| `test_main.py` | Test suite that checks each step |
| `data.sqlite` | Northwind database (employees, orders, orderDetails, and more) |
| `Pipfile` / `Pipfile.lock` | Project dependencies |

## Setup and Usage

Install dependencies and activate the virtual environment:

```bash
pipenv install
pipenv shell
```

Run the script to see the printed output for each step:

```bash
python main.py
```

Run the tests:

```bash
pytest        # run all tests
pytest -x     # stop at the first failure
```

## Solutions Overview

| Step | Variable | Task | Key concept |
|---|---|---|---|
| 1 | `conn` | Import `sqlite3` and `pandas as pd`; connect to `data.sqlite` | Database connection |
| 2 | `df_first_five` | Employee number and last name for all employees | `SELECT` specific columns |
| 3 | `df_five_reverse` | Same as Step 2, with last name first | Column order follows the `SELECT` list |
| 4 | `df_alias` | Same as Step 3, with `employeeNumber` renamed to `ID` | `AS` alias |
| 5 | `df_executive` | Add a `role` column: "Executive" or "Not Executive" | `CASE` |
| 6 | `df_name_length` | Length of each last name as `name_length` | `LENGTH()` |
| 7 | `df_short_title` | First two letters of each job title as `short_title` | `SUBSTR()` |
| 8 | `sum_total_price` | Total of all rounded order line totals | `ROUND()` and `.sum()` |
| 9 | `df_day_month_year` | Order date plus `day`, `month`, and `year` columns | `strftime()` |

## Highlights

### Step 5: Labeling with `CASE`

`CASE` adds a `role` column without removing any rows. Every employee still appears in the result, labeled by job title.

```sql
SELECT *,
CASE
    WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
    ELSE 'Not Executive'
END AS role
FROM employees
```

### Step 8: Rounding Before Summing

Each order line's total (`priceEach * quantityOrdered`) is rounded first, and then the rounded values are added up. The result is `9,604,251`.

```python
sum_total_price = pd.read_sql("""
SELECT ROUND(priceEach * quantityOrdered) AS total_price
FROM orderDetails
""", conn).sum()
```

Calling `.sum()` on the query result returns a pandas Series, which is the shape the test expects (`sum_total_price[0]`). An equivalent approach uses SQL's `SUM()`, but that returns a DataFrame and needs one extra step to select the column.

### Step 9: Splitting Dates with `strftime`

The `orderDate` column lives in the `orders` table, not `orderDetails`. `strftime` pulls the day, month, and year out of each date.

```sql
SELECT orderDate,
       strftime('%d', orderDate) AS day,
       strftime('%m', orderDate) AS month,
       strftime('%Y', orderDate) AS year
FROM orders
```

## What I Learned

- **`SELECT *` versus named columns:** naming columns controls exactly what comes back and in what order.
- **`CASE` labels, `WHERE` filters:** `CASE` adds information to every row, while `WHERE` removes rows.
- **DataFrame versus Series:** the shape of a result matters. Indexing a DataFrame with `[0]` looks for a column named `0`, while indexing a Series with `[0]` returns the first value.
- **Explore the data first:** printing tables before writing queries showed which table holds which columns, such as finding `orderDate` in `orders`.
- **Reading test output:** the `>` arrow and `E` lines in a `pytest` failure point to the exact assertion and error.

## Tools

- Python 3
- SQLite (`sqlite3`)
- pandas
- pytest
- pipenv