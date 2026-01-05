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

Siga os passos abaixo para executar a aplicação na sua máquina Windows:

### 1. Clonar o repositório

```cmd
cd C:\Users\SeuUsuario\Downloads
git clone https://github.com/carlosaagloria-git/btime-dev-rpa-test.git
```

### 2. Entrar na pasta do projeto

```cmd
cd btime-dev-rpa-test
```

### 3. Criar e ativar ambiente virtual (opcional, mas recomendado)

```cmd
python -m venv venv
venv\Scripts\activate
```

### 4. Instalar dependências

```cmd
pip install -r requirements.txt
```

Se não houver `requirements.txt`, crie com:

```
requests
```

### 5. Executar a aplicação

Via API (dados da AwesomeAPI):

```cmd
python api_app.py
```

Via Scraping (HTML da AwesomeAPI):

```cmd
python scraping_app.py
```

### 6. Verificar os arquivos gerados

Os CSVs serão criados na pasta `moedas/data` (ou `data`) com o layout atualizado:

```
moeda;valor;data;hora;fonte
USD-BRL;5.4216;2026-01-02;23:43:50;API_HTML
EUR-BRL;6.35324;2026-01-02;23:43:50;API_HTML
```

### 7. Encerrar o monitoramento

Pressione **CTRL + C** no CMD para interromper o monitoramento contínuo.

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

