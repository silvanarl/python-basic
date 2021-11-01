def run():
    my_dictionary = {
        'clave': 1,
        'clave2': 2,
        'clave3': 3
    }
    print(my_dictionary['clave'])

    people = {
        'Arg': 5168814,
        'Bol': 151664122,
        'Ecu': 15889633
    }

    for pais in people.keys():
        print(pais)
    for pais in people.values():
        print(pais)
    for pais, population in people.items():
        print(f'{pais} tiene {population} habitantes')


if __name__ == '__main__':
    run()