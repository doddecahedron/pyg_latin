VOWELS = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
sentence = (input("Write a sentence and I'll translate it to Pig Latin!: "))
sentence = sentence.split()
pig_latin_word = []

for word in sentence:
    if word[0] in VOWELS:
        pig_latin_word.append(word[1:] + 'say ')
    else:
        pig_latin_word.append(word[1:] + word[0] + 'ay ')

new_sentence = ''.join(pig_latin_word)
print(new_sentence)