def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    word_inverted = word[::-1]
    if word == word_inverted:
        return True
    else:
        False


def run():  #main()
    word = input('Escribe una palabra: ')
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')
##two lines between fn or code blocks
##
if __name__ == '__main__': #entrypoint en python
    run()
