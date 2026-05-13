def word_frequency(sentence):
    '''
    This function takes a string and returns
    the number of occurrences of each word in that string.
    '''
    word_count = {}

    sentence = sentence.split()

    for word in sentence:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count



print(word_frequency("hello world hello python world"))