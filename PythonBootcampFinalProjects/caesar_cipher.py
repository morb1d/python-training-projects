import string

alphabets_list = list(string.ascii_uppercase)
key = 4
cipher_list = []
ciphered_text = []
deciphered_text = []

def create_cipher_list(alphabet_table, cipher_key, cipher_table):
    for counter, letter in enumerate(alphabet_table):
        if (counter < cipher_key):
            item_move = len(alphabet_table) + counter - cipher_key
        else:
            item_move = counter - cipher_key

        cipher_list.insert(item_move, letter)
    return cipher_list

def caesar_cipher(input_text, alphabet_table, cipher_table, output_text):
    for letter in input_text:
        if (letter in cipher_table):
            output_text.append(alphabet_table[cipher_table.index(letter)])
        else:
            output_text.append(letter)
    return output_text

### MAIN
cipher_list = create_cipher_list(alphabets_list, key, [])

print(alphabets_list)
print(cipher_list)

text_to_cipher = list(input('What string you want to cipher: ').upper())
ciphered_text = caesar_cipher(text_to_cipher,cipher_list,alphabets_list,[])

print('\nText to encrypt: {}', text_to_cipher)
print('\nEncrypted text: {}', ''.join(str(e) for e in ciphered_text))

text_to_decipher = list(input('\nWhat string you want to decrypt: ').upper())
deciphered_text = caesar_cipher(text_to_decipher,alphabets_list, cipher_list, [])
print('\nText to decrypt: {}', text_to_decipher)
print('\nDecrypted text: {}', ''.join(str(e) for e in deciphered_text))