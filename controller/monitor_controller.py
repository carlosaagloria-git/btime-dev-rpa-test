import time
from datetime import datetime

from model.awesomeapi_model import coletar_moedas_por_regex
from view.csv_view import salvar_csv_estado_atual, printar_valores

def monitorar_moedas(caminho_csv, moedas, fonte, intervalo_segundos=300, timeout=10):
    """
    Controlador: mantém o while True, try/except, sleep.
    """
    print(f"Iniciando monitoramento contínuo de moedas ({fonte})...")

    while True:
        try:
            valores, _ = coletar_moedas_por_regex(moedas, timeout=timeout)

            agora = datetime.now()
            data = agora.strftime("%Y-%m-%d")
            hora = agora.strftime("%H:%M:%S")

            salvar_csv_estado_atual(
                caminho_csv=caminho_csv,
                moedas=moedas,
                valores=valores,
                data=data,
                hora=hora,
                fonte=fonte
            )

            printar_valores(moedas, valores)
            print("Arquivo CSV atualizado com sucesso.\n")

            time.sleep(intervalo_segundos)

        except Exception as e:
            print(f"Erro na coleta: {e}")
            time.sleep(60)

