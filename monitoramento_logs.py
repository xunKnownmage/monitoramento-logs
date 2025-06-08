# monitoramento_logs.py
import os
import time
import csv
from datetime import datetime

LOG_ARQUIVO = "eventos_logs.csv"
ARQUIVOS_CRITICOS = ["/etc/passwd", "/etc/shadow"]

def iniciar_arquivo():
    if not os.path.exists(LOG_ARQUIVO):
        with open(LOG_ARQUIVO, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Data/Hora", "Tipo de Evento", "Descrição"])

def registrar_evento(tipo, descricao):
    with open(LOG_ARQUIVO, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now(), tipo, descricao])

def checar_login_invalido():
    try:
        with open("/var/log/auth.log") as f:
            for linha in f:
                if "Failed password" in linha:
                    registrar_evento("Login Inválido", linha.strip())
    except:
        registrar_evento("Aviso", "Arquivo auth.log não disponível.")

def checar_arquivos_modificados():
    for caminho in ARQUIVOS_CRITICOS:
        if os.path.exists(caminho):
            tempo_modificacao = os.path.getmtime(caminho)
            if tempo_modificacao > (time.time() - 60):
                registrar_evento("Arquivo Modificado", f"{camin_
