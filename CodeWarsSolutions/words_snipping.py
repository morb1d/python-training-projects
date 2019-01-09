def spin_words(sentence):
    reversed_array=[]
    for word in sentence.split( ):
        if len(word)>=5:
            reversed_array.append(word[::-1])
        else :
            reversed_array.append(word)
    return print(' '.join(reversed_array))