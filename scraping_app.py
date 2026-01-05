from controller.monitor_controller import monitorar_moedas
import os

# Caminho do CSV

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_CSV = os.path.join(BASE_DIR, "moedas_scraping.csv")

# Moedas monitoradas
MOEDAS = ["USD-BRL", "EUR-BRL", "GBP-BRL", "ARS-BRL", "BTC-BRL"]

if __name__ == "__main__":
    monitorar_moedas(
        caminho_csv=CAMINHO_CSV,
        moedas=MOEDAS,
        fonte="SCRAPING_HTML",      
        intervalo_segundos=300,
        timeout=10
    )

