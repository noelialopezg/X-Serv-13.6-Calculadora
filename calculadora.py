#!/usr/bin/python3

import sys 

def sum(sum1, sum2):
    return sum1 + sum2

def rest(sum1, sum2):
    return sum1 - sum2
    
def mul(sum1, sum2):
    return sum1 * sum2
    
def div(sum1, sum2):
    try:
        return sum1 / sum2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        sys.exit()
        
num_args = len(sys.argv)-1
resultado = 0;

if num_args == 3:
    funcion = sys.argv[1]
    try: 
        op_1 = float(sys.argv[2])
        op_2 = float(sys.argv[3])
        
        if funcion == "suma":
            resultado = sum(op_1, op_2)
        elif funcion == "resta":
            resultado = rest(op_1, op_2)
        elif funcion == "mul":
            resultado = mul(op_1, op_2)
        elif funcion == "div":
            resultado = div(op_1, op_2)
        else:
            print("No es operacion correcta")
            
        print(resultado)
        
    except ValueError:
        print("No has introducido un numero como operando")
        sys.exit()
else:
    print("Numero de argumentos introducido incorrecto")




