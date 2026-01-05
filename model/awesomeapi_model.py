import requests
import re

def coletar_moedas_por_regex(moedas, timeout=10):
    """
    Faz request na AwesomeAPI e extrai o 'bid' via regex.
    Retorna um dict: { "USD-BRL": "5.12", ... } e o texto bruto.
    """
    moedas_url = ",".join(moedas)
    url = f"https://economia.awesomeapi.com.br/json/last/{moedas_url}"

    resposta = requests.get(url, timeout=timeout)
    html_texto = resposta.text  # texto puro

    valores = {}

    for moeda in moedas:
        codigo = moeda.replace("-", "")
        regex = rf'"{codigo}".*?"bid":"([0-9.]+)"'
        match = re.search(regex, html_texto, re.DOTALL)
        valor = match.group(1) if match else "ERRO"
        valores[moeda] = valor

    return valores, html_texto

