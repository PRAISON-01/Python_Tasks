word = input("Enter a word to reverse: ")

for characters in reversed(word):
    print(characters, end="-")
