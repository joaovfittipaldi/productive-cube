from flask import Blueprint
from flask import json
from app import database_manager

bp = Blueprint("endpoints", __name__)

# Definindo endpoints

@bp.route("/sessoes_completas")
def teste_view():
    # Retorno {"sessoes_nao_completas": X}
    return database_manager.tempo_terminou()

@bp.route("/dia")
def meta_diaria():
    # Retorno: {"total_diario": X}

    meta_diaria = database_manager.total_dia()
    return meta_diaria

@bp.route("/semana")
def meta_semanal():
    # Retorno: {
    # "meta_semanal": X
    # "tempo_total_semana": Y
    #  }

    return database_manager.total_semana()

@bp.route("/mes")
def meta_mensal():
    # Retorno: {
    # "meta_mensal": X
    # "tempo_total_mes": Y
    #  }

    return database_manager.meta_mensal()

@bp.route("/dashboard")
def dashboard_semanal():
    return database_manager.desempenho_semanal()