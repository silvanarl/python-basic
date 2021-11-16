# def is_primo(number):
#     contador = 0
#     for i in range(1, number + 1):
#         if i == 1 or i == number:
#             continue
#         if number % i == 0:
#             contador += 1
#     if contador == 0:
#         return True
#     else:
#         return False


# def run():
#     number =  int(input('Ingresa un número: '))
#     if is_primo(number):
#         print('Es primo')
#     else:
#         print('no es primo')


# def run():
#     num = int(input('Ingresa un número: '))
#     primo_list = [2,3,5,7,11]
#     is_primo = False
#     for i in primo_list:
#         if num % i < i:
#             continue
#         if num % i > i:
#             is_primo = True
#     return is_primo


# print(run())

'''para saber si un número es primo, se divide este entre los primeros números primos hasta su raiz cuadrada;
si el resultado de alguna de estas divisiones es exacto entonces el número no es primo'''

def es_primo(numero):
    validacion = True
    for i in range(1, int(round(numero**(1/2.0),0))+1):
        if i==1 or i==numero:
            continue
        if numero % i ==0:
            validacion=False
            break
    return validacion


def run():
    numero = int(input("Ingresa un número entero  "))
    if es_primo(numero):
        print("El número {} es primo".format(numero))
    else:
        print("El número {} no es primo".format(numero))


if __name__ == "__main__":
    run()

