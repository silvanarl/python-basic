import random

# upper_case = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
# upper_case = upper_case.split()
def pass_generator():
    capitalize = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    symbol = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]

    characters = capitalize + lower + symbol + number
    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    password = ''.join(password)
    return password


def run():
    password = pass_generator()
    print(f'Your new password is {password}')

if __name__ == '__main__':
    run()

