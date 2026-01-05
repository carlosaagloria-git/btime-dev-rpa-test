
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

Como Executar

Siga os passos abaixo para executar a aplicação na sua máquina Windows:

Clonar o repositório

Abra o Prompt de Comando (CMD) e navegue até a pasta onde deseja salvar o projeto, por exemplo C:\Users\SeuUsuario\Downloads:

cd C:\Users\SeuUsuario\Downloads
git clone https://github.com/carlosaagloria-git/btime-dev-rpa-test.git


Isso vai criar uma pasta chamada btime-dev-rpa-test com todos os arquivos do projeto.

Entrar na pasta do projeto

cd btime-dev-rpa-test


Criar e ativar ambiente virtual (opcional, mas recomendado)

Se você tiver Python instalado, crie um ambiente virtual para não misturar bibliotecas com outros projetos:

python -m venv venv
venv\Scripts\activate


Você verá que o prompt vai mudar, mostrando (venv) no início.

Instalar dependências

Caso o projeto use bibliotecas externas (como requests), instale com:

pip install -r requirements.txt


Se ainda não existir o requirements.txt, você pode criar e adicionar:

requests


Executar a aplicação

Existem duas formas de rodar o monitoramento:

Via API (coleta dados da AwesomeAPI):

python api_app.py


Via Scraping (HTML da AwesomeAPI):

python scraping_app.py


Verificar os arquivos gerados

O sistema cria os CSVs dentro da pasta moedas/data (ou data, conforme seu ajuste), com o layout atualizado:

moeda;valor;data;hora;fonte
USD-BRL;5.4216;2026-01-02;23:43:50;API_HTML
EUR-BRL;6.35324;2026-01-02;23:43:50;API_HTML


Encerrar o monitoramento

Basta pressionar CTRL + C no CMD para parar a execução do monitoramento contínuo.
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
