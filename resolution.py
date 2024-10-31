import psycopg2
from psycopg2 import sql

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="sql_basics",
    user="your_username",
    password="your_password",
    host="localhost"
)

# Create a cursor object
cur = conn.cursor()

# Create the employees table
cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        age INTEGER CHECK (age >= 10),
        joined TIMESTAMP,
        username VARCHAR CHECK (LENGTH(username) >= 8),
        salary NUMERIC CHECK (salary >= 0),
        currency VARCHAR DEFAULT 'EUR'
    )
""")

# Add values to the employees table
values = [
    ('john', 'kennedy', 19, '2020-12-02 14:35', 'jfkennedy', 30000, 'EUR'),
    ('alice', 'kennedy', 19, '2020-02-02 14:35', 'allkennedy', 2000, 'EUR'),
    ('max', 'kennedy', 19, '2020-12-02 14:35', 'maxkennedy', 9000, 'USD'),
    ('bianca', 'kennedy', 19, '2020-12-02 14:35', 'bbkennedy', 1000, 'EUR'),
    ('danny', 'kennedy', 19, '2022-05-02 14:35', 'dffkennedy', 20000, 'NGN'),
    ('rachael', 'kennedy', 19, '2020-12-02 14:35', 'rcckennedy', 35000, 'NGN'),
    ('bob', 'kennedy', 19, '2022-12-02 14:35', 'bobkennedy', 27000, 'EUR'),
    ('peter', 'kennedy', 19, '2023-12-02 14:35', 'petekennedy', 45000, 'YEN'),
    ('maria', 'kennedy', 19, '2022-12-02 14:35', 'mriekennedy', 5000, 'YEN'),
    ('dwayne', 'kennedy', 19, '2021-10-02 14:35', 'dwwkennedy', 4500, 'EUR'),
    ('karl', 'kennedy', 19, '2021-12-02 14:35', 'krlkennedy', 2000, 'EUR'),
    ('agnes', 'kennedy', 19, '2020-12-02 14:35', 'agkennedy', 31000, 'EUR')
]

cur.executemany("""
    INSERT INTO employees (first_name, last_name, age, joined, username, salary, currency)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", values)

# Commit the transaction
conn.commit()

# Generate the required queries
queries = [
    "SELECT * FROM employees WHERE currency = 'EUR'",
    "SELECT * FROM employees WHERE currency = 'USD'",
    "SELECT * FROM employees WHERE currency = 'NGN'",
    "SELECT * FROM employees WHERE currency = 'YEN'",
    "SELECT * FROM employees WHERE salary > 15000 AND currency = 'EUR'",
    "SELECT * FROM employees WHERE salary > 20000 AND currency = 'YEN'",
    "SELECT * FROM employees WHERE salary > 22000",
    "SELECT * FROM employees WHERE EXTRACT(YEAR FROM joined) = 2020",
    "SELECT * FROM employees WHERE EXTRACT(YEAR FROM joined) = 2021",
    "SELECT * FROM employees WHERE EXTRACT(YEAR FROM joined) = 2022",
    "SELECT * FROM employees WHERE EXTRACT(YEAR FROM joined) = 2023",
    "SELECT * FROM employees WHERE EXTRACT(YEAR FROM joined) = 2024",
    "SELECT * FROM employees WHERE EXTRACT(YEAR FROM joined) = 2020 AND salary < 20000"
]

# Execute the queries and print results
for query in queries:
    cur.execute(query)
    results = cur.fetchall()
    print("Results for query:", query)
    for row in results:
        print(row)

# Close the cursor and connection
cur.close()
conn.close()
