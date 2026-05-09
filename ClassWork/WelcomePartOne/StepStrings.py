def do_this(word):
    size = len(word)
    for string in range(size, 0, -1):
        for elements in range(string):
            print(word[elements], end=" ")
        print()

do_this("STEP")
