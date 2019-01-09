def remove_duplicate_words(s):
    words_array=[]
    for word in s.split():
        if word not in words_array:
            words_array.append(word)
    return print(words_array)

remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")