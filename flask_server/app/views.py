from flask import Blueprint
from app import database_manager

bp = Blueprint("check", __name__)

@bp.route("/check")
def teste_view():
    return database_manager.consulta_teste()