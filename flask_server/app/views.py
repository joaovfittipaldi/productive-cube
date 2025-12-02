from flask import Blueprint
from flask import json
from flask_cors import cross_origin
from app import database_manager    

bp = Blueprint("endpoints", __name__)

# Definindo endpoints

@bp.route("/sessoes_completas")
@cross_origin(origins=["http://localhost:3000"])
def teste_view():
    # Retorno {"sessoes_nao_completas": X}
    return database_manager.tempo_terminou()

@bp.route("/dia")
@cross_origin(origins=["http://localhost:3000"])
def meta_diaria():
    # Retorno: {"total_diario": X}

    meta_diaria = database_manager.total_dia()
    return meta_diaria

@bp.route("/semana")
@cross_origin(origins=["http://localhost:3000"])
def meta_semanal():
    # Retorno: {
    # "meta_semanal": X
    # "tempo_total_semana": Y
    #  }

    return database_manager.total_semana()

@bp.route("/mes")
@cross_origin(origins=["http://localhost:3000"])
def meta_mensal():
    # Retorno: {
    # "meta_mensal": X
    # "tempo_total_mes": Y
    #  }

    return database_manager.meta_mensal()

@bp.route("/dashboard")
@cross_origin(origins=["http://localhost:3000"])
def dashboard_semanal():
    return database_manager.desempenho_semanal()