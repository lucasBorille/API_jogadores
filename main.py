from flask import Flask, request
from bd_request import get_data
from error_verify import verify_values
from file_format import file_format

app = Flask(__name__)

@app.route('/')
def teste():
    return get_data().to_json(orient='records')

@app.route('/jogadores')
def filtrar_jogadores():

    nome = request.args.get('nome')
    time = request.args.get('time')
    selecao = request.args.get('selecao')
    camisa = request.args.get('n_camisa')
    min_salario = request.args.get('min_salario')
    max_salario = request.args.get('max_salario')

    verify = verify_values(camisa, min_salario, max_salario)
    # if there is an error in verify_values, it will return a tuple with the error message and status code
    if verify[0] is not None:
        return verify

    # this list will contain the conditions for the SQL query
    lista =[
        f"nome = '{nome}'" if nome != '' and nome is not None else None,
        f"time = '{time}'" if time != '' and time is not None else None,
        f"selecao = '{selecao}'" if selecao != '' and selecao is not None else None,
        f"n_camisa = '{camisa}'" if camisa != '' and camisa is not None else None,
        f"salario >= {min_salario}" if min_salario != '' and min_salario is not None else None,
        f"salario <= {max_salario}" if max_salario != '' and max_salario is not None else None
    ]
    
    lista = [x for x in lista if x is not None]
    data = get_data(lista)

    if data.empty:
        return ('Not found', 404)
    else:

        data = file_format(request.args.get('format'), data)

        # if there is an error in file_format, it will return a tuple with the error message and status code
        if isinstance(data, tuple):
            return data
        return (data, 200)


app.run()