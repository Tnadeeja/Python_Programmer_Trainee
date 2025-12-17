# ==========================================================
# 📘 3.3 Accessing a Database (Python + MySQL using PyMySQL)
# ==========================================================

# Accessing a database means:
# - Connecting Python to a DB server
# - Sending SQL commands (CRUD)
# - Receiving results
# - Closing the connection safely

# Python follows a standard called DB-API (PEP 249)
# Most database libraries follow this structure:
# 1) Import module
# 2) Connect to DB
# 3) Create cursor
# 4) Execute SQL
# 5) Commit / Fetch
# 6) Close connection


# ----------------------------------------------------------
# 1️⃣ Install & Import PyMySQL
# ----------------------------------------------------------
# Install once (in terminal):
# pip install pymysql

import pymysql


# ----------------------------------------------------------
# 2️⃣ Connect to MySQL Database
# ----------------------------------------------------------
# connect(host, user, password, database)

db = pymysql.connect(
    host="localhost",
    user="testuser",
    password="test123",
    database="TESTDB"
)

# Cursor is used to execute SQL commands
cursor = db.cursor()


# ----------------------------------------------------------
# 3️⃣ CREATE TABLE (DDL)
# ----------------------------------------------------------
# Used to create database structure

cursor.execute("""
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME  CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT
)
""")

db.commit()   # Save changes


# ----------------------------------------------------------
# 4️⃣ INSERT DATA (CREATE)
# ----------------------------------------------------------
sql_insert = """
INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
VALUES (%s, %s, %s, %s, %s)
"""

try:
    cursor.execute(sql_insert, ("Mac", "Mohan", 20, "M", 2000))
    db.commit()
except:
    db.rollback()


# ----------------------------------------------------------
# 5️⃣ READ DATA (SELECT)
# ----------------------------------------------------------
cursor.execute("SELECT * FROM EMPLOYEE WHERE INCOME > %s", (1000,))
results = cursor.fetchall()

for row in results:
    print(row)


# ----------------------------------------------------------
# 6️⃣ UPDATE DATA
# ----------------------------------------------------------
sql_update = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = %s"

try:
    cursor.execute(sql_update, ("M",))
    db.commit()
except:
    db.rollback()


# ----------------------------------------------------------
# 7️⃣ DELETE DATA
# ----------------------------------------------------------
sql_delete = "DELETE FROM EMPLOYEE WHERE AGE > %s"

try:
    cursor.execute(sql_delete, (25,))
    db.commit()
except:
    db.rollback()


# ----------------------------------------------------------
# 8️⃣ TRANSACTIONS
# ----------------------------------------------------------
# commit()  -> permanently save changes
# rollback() -> undo changes if error occurs

# ACID Properties:
# Atomicity, Consistency, Isolation, Durability


# ----------------------------------------------------------
# 9️⃣ Close Connection
# ----------------------------------------------------------
cursor.close()
db.close()

# Always close the DB connection to free resources
