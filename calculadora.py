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
        

resultado = 0;

def main(funcion, op_1, op_2):

        dicc = {"suma": sum, "resta": rest, "mul": mul, "div": div}
        print(dicc[funcion](op_1, op_2))
        


if __name__ == "__main__":
    num_args = len(sys.argv)-1
    if num_args != 3:
        sys.exit("Usage Error: operacion operando_1 operando_2 ")
    try: 
        op_1 = float(sys.argv[2])
        op_2 = float(sys.argv[3])
    except ValueError:
        sys.exit("No has introducido un numero como operando")

    funcion = sys.argv[1]
    main(funcion, op_1, op_2)

