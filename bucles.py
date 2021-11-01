# sumar todas las potencias de 2 hasta 1000

def two_potencia():
    rango = list(range(2,10))
    pot = 0
    for val in rango:
        pot = val**val
    return pot


print(two_potencia())

#  todas las potencias de 2 hasta 1000 recursivo
def run(num, rept):
    if num <= rept:
        cont = num
        print(str(2 ** cont) )
        run(num+1, rept)
    else:
        print("Fin!")

if __name__ == "__main__":
    repeticiones = int(input("Cuantas potencias: "))
    run(0, repeticiones)

def potencias():
    #limit = 1000     # variable, que puede cambiar su valor like let or var
    LIMITE = 1000000 # en ayusculas se vuelve una constante like const

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) +
        ' es igual a : ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

potencias()