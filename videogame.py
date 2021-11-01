import random


"""elegir un numero del 1-100 
adivinarle numero o decir si es mayor o menor 
y decirle si gano si los divinamos
"""




def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Elige un número mas alto')
            # numero_elegido = int(input('Elige otro número: '))
        else:
            print('Elige un número mas pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('Ganaste!')


if __name__ == '__main__':
    run()