import mysql.connector
from app import database_setup
import time
import os


def update_tempo_nao_terminou():
    return

def inserir_tempo(Tempo_modo, Tempo_restante, Horario_dia, Dia_da_semana):
    time_start = time.time()
    con = database_setup.get_connection()
    cur = con.cursor()

    sql_querry = "INSERT INTO temporizador (Tempo_modo, Tempo_restante, Horario_dia, Dia_da_semana) values (%s, %s, %s, %s)"
    params = Tempo_modo, Tempo_restante, Horario_dia, Dia_da_semana

    cur.execute(sql_querry, params)
    con.commit()

def consulta_teste():
    con = database_setup.get_connection()
    cur = con.cursor()

    sql_querry = "SELECT * FROM temporizador"
    
    cur.execute(sql_querry)
    result = cur.fetchall()
    cur.close()
    return result