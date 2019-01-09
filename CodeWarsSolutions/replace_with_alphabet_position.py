import string

alphabet = string.ascii_lowercase

def alphabet_position(text):
    indexed_alphabet=[]
    for letter in text.lower():
        if letter in string.ascii_letters:
            indexed_alphabet.append(str(alphabet.index(letter)+1))
    return print(' '.join(indexed_alphabet))

alphabet_position("The sunset sets at twelve o' clock.")