import mysql.connector
from app import database_setup
import time
from datetime import datetime, timedelta
import os

# TODO: 
# Tempo de foco/dia


def tempo_terminou():
    con = database_setup.get_connection()
    cur = con.cursor(dictionary=True)

    sql_query = """
        SELECT COUNT(Tempo_Restante_Segundos) as sessoes_completas
        FROM temporizador
        WHERE Tempo_Restante_Segundos = 0
    """

    cur.execute(sql_query, )
    sessoes_nao_completas = cur.fetchone() 
    cur.close()
    return sessoes_nao_completas

def total_dia():
    con = database_setup.get_connection()
    cur = con.cursor(dictionary=True)
    dia = datetime.now().strftime("%Y-%m-%d")

    sql_query = """
        SELECT 
            SUM(Tempo_Modo_Segundos) - SUM(Tempo_Restante_Segundos) AS total_diario
        FROM temporizador
        WHERE DATE(Data_atual) = %s
    """

    cur.execute(sql_query, (dia,))
    metal_dia = cur.fetchone() 
    cur.close()
    return metal_dia


def total_semana():
    con = database_setup.get_connection()

    cur = con.cursor(dictionary=True, buffered=True)

    for i in range(-7, 0):
        atual = datetime.now() + timedelta(days=i)
        if atual.weekday() == 0:
            dia_certo = atual
            break

    inicio_mes = datetime.now()
    menor = datetime(inicio_mes.year, inicio_mes.month, dia_certo.day)
    maior = (menor + timedelta(days=7))

    menor = menor.strftime("%Y-%m-%d")
    maior = maior.strftime("%Y-%m-%d")

    sql_query = """
        SELECT 
            SUM(Tempo_Modo_Segundos) - SUM(Tempo_Restante_Segundos) AS tempo_total
        FROM temporizador
        WHERE DATE(Data_atual) >= %s AND DATE(Data_atual) <= %s
    """
    cur.execute(sql_query, (menor, maior))
    atual = cur.fetchone()
    cur.close()

    cur = con.cursor(dictionary=True, buffered=True)
    sql_query_2 = """
        SELECT tempo_meta_s AS tempo_meta 
        FROM meta 
        WHERE nome_meta = 'Meta semanal'
    """
    cur.execute(sql_query_2)
    total = cur.fetchone()
    cur.close()

    return {
        "tempo_total_semana": atual["tempo_total"],
        "meta_semanal": total["tempo_meta"]
    }


def meta_mensal():
    con = database_setup.get_connection()

    cur = con.cursor(dictionary=True, buffered=True)
    inicio_mes = datetime.now()
    menor = datetime(inicio_mes.year, inicio_mes.month, 1)
    maior = datetime.now().strftime("%Y-%m-%d")

    sql_query = """
        SELECT 
            SUM(Tempo_Modo_Segundos) - SUM(Tempo_Restante_Segundos) AS tempo_total
        FROM temporizador
        WHERE DATE(Data_atual) >= %s AND DATE(Data_atual) <= %s
    """
    cur.execute(sql_query, (menor, maior))
    atual = cur.fetchone()
    cur.close()

    cur = con.cursor(dictionary=True, buffered=True)
    sql_query_2 = """
        SELECT tempo_meta_s AS tempo_meta 
        FROM meta 
        WHERE nome_meta = 'Meta mensal'
    """
    cur.execute(sql_query_2)
    total = cur.fetchone()
    cur.close()

    return {
        "tempo_total_mes": atual["tempo_total"],
        "meta_mensal": total["tempo_meta"]
    }

def desempenho_semanal():
    con = database_setup.get_connection()

    cur = con.cursor(dictionary=True, buffered=True)

    for i in range(-7, 0):
        atual = datetime.now() + timedelta(days=i)
        if atual.weekday() == 0:
            dia_certo = atual
            break
    
    inicio_mes = datetime.now()
    menor = datetime(inicio_mes.year, inicio_mes.month, dia_certo.day)
    maior = (menor + timedelta(days=7))

    menor = menor.strftime("%Y-%m-%d")
    maior = maior.strftime("%Y-%m-%d")

    sql_query = """
        SELECT Dia_da_Semana as dia, SUM(Tempo_Modo_Segundos) - SUM(Tempo_Restante_Segundos) as tempo 
        FROM temporizador 
        WHERE DATE(Data_atual) >= %s and Date(Data_atual) <= %s 
        GROUP BY Dia_da_Semana
    """
    cur.execute(sql_query, (menor, maior))
    atual = cur.fetchall()
    cur.close()

    return atual

def inserir_tempo(Tempo_modo, Tempo_restante, Horario_dia, Dia_da_semana, Data_atual):
    con = database_setup.get_connection()
    cur = con.cursor()

    sql_querry = "INSERT INTO temporizador (Tempo_modo_Segundos, Tempo_restante_Segundos, Data_atual, Horario_dia, Dia_da_semana) values (%s, %s, %s, %s, %s)"
    params = Tempo_modo, Tempo_restante , Data_atual , Horario_dia, Dia_da_semana

    cur.execute(sql_querry, params)
    con.commit()

def consulta_teste():
    con = database_setup.get_connection()
    cur = con.cursor()

    sql_querry = "SELECT id, Tempo_Modo_Segundos, Tempo_Restante_Segundos, Horario_Dia, DATE_FORMAT(Data_atual, '%Y-%m-%d') AS Data_atual, Dia_da_Semana FROM temporizador"
    
    cur.execute(sql_querry)
    result = cur.fetchall()
    cur.close()
    return result