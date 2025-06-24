import psycopg2
import numpy as np
import pandas as pd

def get_data(lista=None):
    
    conn = psycopg2.connect(
        host='localhost',
        database='postgres', 
        user='postgres',
        password='senha',
        port=5432
    )
    cur = conn.cursor()

    sql = 'SELECT * FROM jogadores'
    
    if lista is not None:
        sql += ' WHERE'
        for i in range(len(lista)):
            if i == 0:
                sql += ' ' + lista[i]
            else:
                sql += ' AND ' + lista[i]


    try:
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        npArray = np.array(rows)
        data = pd.DataFrame(npArray, columns=['nome', 'n_camisa', 'time', 'selecao', 'salario'])
    except Exception:
        print(f"Error executing query")
        cur.close()
        conn.close()
        data = pd.DataFrame()
    finally:
        return data
