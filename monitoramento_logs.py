import os
import csv
from datetime import datetime

LOG_ARQUIVO = "eventos_logs.csv"
ARQUIVO_TESTE = "teste.txt"

def iniciar_arquivo():
    if not os.path.exists(LOG_ARQUIVO):
        with open(LOG_ARQUIVO, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Data/Hora", "Tipo de Evento", "Descrição"])

def registrar_evento(tipo, descricao):
    with open(LOG_ARQUIVO, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now(), tipo, descricao])

def simular_eventos():
    registrar_evento("Login Inválido", "Tentativa de login simulada no ambiente GitHub.")
    
    # Simula modificação de um arquivo de teste
    with open(ARQUIVO_TESTE, "w") as f:
        f.write("Arquivo modificado.")
    registrar_evento("Arquivo Modificado", f"{ARQUIVO_TESTE} foi criado/modificado.")

if __name__ == "__main__":
    iniciar_arquivo()
    simular_eventos()
