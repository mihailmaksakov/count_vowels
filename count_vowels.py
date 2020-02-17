sentence = 'Hello, my name Mikhail!'
vowels = 'aeiouy'
print({v: sentence.lower().count(v) for v in vowels})