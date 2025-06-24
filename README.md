# API de Jogadores

Este repositório contém uma API desenvolvida com Flask que permite consultar informações sobre jogadores a partir de parâmetros fornecidos na URL. A API valida os dados de entrada, realiza consultas a um banco de dados PostgreSQL e retorna os resultados no formato solicitado.

## Funcionalidades

- Recebe parâmetros via URL
- Valida os parâmetros fornecidos
- Consulta o banco de dados com base nos parâmetros
- Retorna os dados no formato JSON, CSV, HTML e TXT

## Tecnologias Utilizadas

- Python
- Flask
- Psycopg2 (PostgreSQL)
- Pandas (para manipulação de dados)

## Estrutura do Projeto

```
API_jogadores/
├── main.py             # Arquivo principal da aplicação Flask
├── bd_request.py       # Conexão com o banco de dados
├── file_format.py      # Define o formato de saída
├── error_verify.py     # Script que valida os parâmetros
├── requirements.txt    # Dependências da aplicação
└── README.md           # Documentação do projeto
```

## \:gear: Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/lucasBorille/API_jogadores.git
cd API_jogadores
```

2. Crie um ambiente virtual e ative-o (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente (ex: informações do banco de dados):

bd_request
```python!
 conn = psycopg2.connect(
        host='localhost',
        database='postgres', 
        user='postgres',
        password='senha',
        port=5432
    )
```
O seu banco de dados deve ter a tabela jogadores nesse formato:
```sql
 \d jogadores
                     Table "public.jogadores"
  Column  |         Type          | Collation | Nullable | Default
----------+-----------------------+-----------+----------+---------
 nome     | character varying(55) |           | not null |
 n_camisa | integer               |           |          |
 time     | character varying(55) |           | not null |
 selecao  | character varying(55) |           |          |
 salario  | double precision      |           |          |
Indexes:
    "jogadores_pkey" PRIMARY KEY, btree (nome, "time")
```

5. Execute a aplicação:

```bash
python3 main.py
```

A aplicação estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Exemplo de Uso

Requisição:

```
GET /jogadores?nome=Neymar Jr&time=Santos
```

Resposta:

```json
[
    {
        "nome": "Neymar Jr",
        "n_camisa": "10",
        "time": "Santos",
        "selecao": "Brasil",
        "salario": "6000.0"
    }
]
```

---

Desenvolvido por [Lucas Borille](https://github.com/lucasBorille)

