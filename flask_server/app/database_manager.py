import mysql.connector
from app import database_setup
import time
import os

def querry(AcX, AcY, AcZ):
    time_start = time.time()
    con = database_setup.get_connection()
    cur = con.cursor()

    sql_querry = "INSERT INTO temporizador (AcX, AcY, AcZ, Tempo) VALUES (%s, %s, %s, %s)"
    params = AcX, AcY, AcZ, time_start

    cur.execute(sql_querry, params)
    con.commit()