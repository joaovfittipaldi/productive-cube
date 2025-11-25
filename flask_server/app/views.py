from flask import Blueprint
from flask import json
from app import database_manager

bp = Blueprint("endpoints", __name__)

# Definindo endpoints

@bp.route("/sessoes_sem_fim")
def teste_view():
    return database_manager.update_tempo_nao_terminou()

@bp.route("/dia")
def meta_diaria():
    meta_diaria = database_manager.total_dia()
    return meta_diaria

@bp.route("/semana")
def meta_semanal():
    return database_manager.total_semana()

@bp.route("/mes")
def meta_mensal():
    return database_manager.total_mes()