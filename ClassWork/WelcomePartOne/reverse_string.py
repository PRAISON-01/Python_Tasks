def reverse_string(word):
    reverse = ""
    for elements in(word):
        reverse = elements + reverse
    return reverse

word = "SEAT"
print("Word: ", word)
print("Reverse: ", reverse_string(word))
