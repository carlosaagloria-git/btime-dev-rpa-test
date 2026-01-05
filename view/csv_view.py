import csv
import os

def salvar_csv_estado_atual(caminho_csv, moedas, valores, data, hora, fonte):
    """
    Sobrescreve o CSV (estado atual).
    """
    os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)

    with open(caminho_csv, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(["moeda", "valor", "data", "hora", "fonte"])

        for moeda in moedas:
            escritor.writerow([
                moeda,
                valores.get(moeda, "ERRO"),
                data,
                hora,
                fonte
            ])

def printar_valores(moedas, valores):
    for moeda in moedas:
        print(f"{moeda} → {valores.get(moeda, 'ERRO')}")

