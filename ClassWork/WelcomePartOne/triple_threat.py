def triple_threat(word):
    triple = ""
    for char in word:
        triple += char * 3
    return triple


word = "CODE"
print(triple_threat(word))
