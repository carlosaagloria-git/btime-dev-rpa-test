
# Projeto BTime - Monitoramento de Moedas

## Visão Geral
O BTime é uma aplicação desenvolvida em Python com arquitetura **MVC (Model-View-Controller)**, que realiza a coleta de valores de moedas em tempo real. O sistema integra dados provenientes de fontes online confiáveis, como a AwesomeAPI, e realiza scraping HTML para garantir redundância e confiabilidade das informações. Os resultados são armazenados em arquivos CSV, com timestamp, fonte e valor, possibilitando análises históricas precisas.

---

## Estrutura do Projeto

```
btime/
│
├── api_app.py               # Script principal para coleta via API
├── scraping_app.py          # Script principal para coleta via scraping HTML
├── controller/              # Controladores da aplicação
│   └── monitor_controller.py
├── model/                   # Modelos de coleta de dados
│   └── awesomeapi_model.py
├── view/                    # Visualizações e manipulação de CSV
│   └── csv_view.py
├── moedas_api.csv           # Últimos valores coletados via API
├── moedas_scraping.csv      # Últimos valores coletados via scraping
├── .gitignore
└── README.md
```

---

## Funcionalidades

- Coleta de valores de moedas via **API HTML**.
- Coleta de valores de moedas via **scraping HTML**.
- Armazenamento automático em **CSV**, incluindo:
  - Moeda
  - Valor
  - Data
  - Hora
  - Fonte
- Monitoramento contínuo com intervalo configurável.
- Estrutura modular baseada em **MVC** para fácil manutenção e escalabilidade.

---

## Tecnologias Utilizadas

- **Python 3.13+**
- **Requests** (requisições HTTP)
- **CSV** (armazenamento de dados)
- **Regex** (extração de dados HTML)
- Arquitetura **MVC** para separação clara de responsabilidades.

---

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/carlosaagloria-git/btime-dev-rpa-test.git
```

2. Navegue até a pasta do projeto:
```bash
cd btime
```

3. Instale as dependências necessárias (caso ainda não tenha o `requests`):
```bash
pip install requests
```

4. Execute a coleta via API:
```bash
python api_app.py
```

5. Execute a coleta via scraping HTML:
```bash
python scraping_app.py
```

6. Os arquivos CSV serão atualizados automaticamente na pasta do projeto:
- `moedas_api.csv`
- `moedas_scraping.csv`

---

## Boas Práticas

- **Modularidade:** cada camada tem responsabilidade única.
- **Reuso:** funções no model podem ser reaproveitadas para novas moedas ou fontes.
- **Manutenibilidade:** logs simples e CSV legível para acompanhamento histórico.
- **Escalabilidade:** arquitetura pronta para integração de novas fontes de dados.

---

## Contato

Carlos A. Gloria  
[GitHub](https://github.com/carlosaagloria-git)  
E-mail: carlos@email.com
