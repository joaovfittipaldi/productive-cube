import mysql.connector
import os

def setup_connection(user, password, database):
    db = mysql.connector.connect(
        host='localhost',
        user= user,
        password= password,
    )
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS teste")
    cur.close()
    return db

def run_schema(db):
    cursor = db.cursor()
    cursor.execute("USE teste")

    schema_path = os.path.join(os.path.dirname(__file__), "..", "schema.sql")
    with open(schema_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    for statement in sql_script.split(";"):
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt + ";")

    db.commit()
    cursor.close()
    db.close()
    
