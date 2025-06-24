def verify_values(camisa, min_salario, max_salario):
    try:
        #verify if the values ​​are numeric
        if max_salario:
            max_salario = float(max_salario)
        if min_salario:
            min_salario = float(min_salario)

        if min_salario and max_salario: 
            if max_salario < min_salario:
                return ('Max salary cannot be less than min salary', 400)
    except ValueError:
        return (f'Invalid salary value: salary values ​​must be of numeric type', 400)
    except Exception as e:
        return (f'Invalid salary value: {e}', 400)
    else:
        if camisa:
            try:
                #verify if the shirt number is numeric
                int(camisa)
            except Exception as e:
                return (f'Invalid shirt number: {e}', 400)
            
        return (None, 200)
        