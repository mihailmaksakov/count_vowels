vowels = 'aeiouy'

def get_vowels_count(sentence):
    return {v: sentence.lower().count(v) for v in vowels}

sentence = 'Hello, my name Mikhail!'

print(get_vowels_count(sentence))