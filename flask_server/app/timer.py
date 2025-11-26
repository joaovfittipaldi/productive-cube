import time
import threading
from app import database_manager

stop_event = threading.Event()

# Checa pra ver o tempo restante caso haja conflito de modos
def timer(Tempo_modo, Horario_dia, Dia_da_semana, Data_atual):
    tempo_restante = Tempo_modo*60
    Tempo_modo = Tempo_modo*60
    stop_event.clear()

    while tempo_restante > 0:
        print(f"Restam {tempo_restante} segundos")
        time.sleep(1)
        tempo_restante -= 1

        if stop_event.is_set():
            database_manager.inserir_tempo(Tempo_modo=Tempo_modo, Tempo_restante=tempo_restante, Horario_dia=Horario_dia, Dia_da_semana=Dia_da_semana, Data_atual=Data_atual)
            return

        if tempo_restante == 0:
            database_manager.inserir_tempo(Tempo_modo=Tempo_modo, Tempo_restante=tempo_restante, Horario_dia=Horario_dia, Dia_da_semana=Dia_da_semana, Data_atual=Data_atual)
            return

    
