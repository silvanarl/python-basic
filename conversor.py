menu = """
Bienvenido al conversor de monedas 💲

1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos
"""
option = input(menu)

def convertir_moneda(type_coin, value_dolar):
    pesos = float(input('ingresa tus pesos '+ type_coin +' : '))
    dolares = pesos/value_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $ ' + dolares + ' dólares')

if option == '1':
    convertir_moneda('colombianos', 3875)
elif option == '2':
    convertir_moneda('argentinos', 99.63)
elif option == '3':
    convertir_moneda('mexicanos', 20.42)
else:
    print('Ingresa una opción correcta')


#15000
#3.87

#2000
#503.77

# dolar = float(input('¿cuantos dolares tienes?'))
# dollars_result = dolar*valor_dolar_soles
# dollars_result = round(dollars_result, 2)
# dollars_result = str(dollars_result)
# print('Tienes S/ ' + dollars_result + ' soles')
#200
#794