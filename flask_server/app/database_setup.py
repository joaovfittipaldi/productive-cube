import mysql.connector
import os

def setup_connection(user, password, database):
    db = mysql.connector.connect(
        host='localhost',
        user= user,
        password= password,
    )
    cur = db.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS focus_cube")
    cur.close()
    return get_connection()

def get_connection():
    db = mysql.connector.connect(
        host='localhost',
        user= os.getenv('USER'),
        password= os.getenv('PASSWORD'),
        database='focus_cube'
    )
    return db

def run_schema(db):
    cursor = db.cursor()
    cursor.execute("USE focus_cube")

    schema_path = os.path.join(os.path.dirname(__file__), "..", "schema.sql")
    with open(schema_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    for statement in sql_script.split(";"):
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt + ";")

    db.commit()
    cursor.close()
