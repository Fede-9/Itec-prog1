def inputString(msg,**condiciones):
    strng = input(msg)
    cond = False
    try: 
        while cond == False:
            string_len = len(strng)
            if "max" in condiciones.keys() and "min" in condiciones.keys():
                max = condiciones["max"]
                min = condiciones["min"]
                if (string_len >= min) and (string_len <= max):
                    cond = True
                    return strng
                else:
                    print(f'El largo de la string tiene que ser mayor que {min} y menor que {max}')
                    strng = input(msg)
            elif 'max' in condiciones.keys() and 'min' not in condiciones.keys():
                max = condiciones['max']
                if string_len <= max:
                    cond = True
                    return strng
                else:
                    print(f'El largo de la string tiene que ser menor que {max}')
                    strng = input(msg)
            elif 'min' in condiciones.keys() and 'max' not in condiciones.keys():
                min = condiciones['min']
                print(min)
                if string_len >= min:
                    cond = True
                    return strng
                else:
                    print(f'El largo de la string tiene que ser mayor que {min}')
                    strng = input(msg)
            else:
                return strng
    except ValueError:
        print('Valor invalido')