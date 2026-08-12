def find_and_replace(filename, old_word, new_word):
    with open(filename, "r") as file:
        text = file.read()

    new_text = text.replace(old_word, new_word)

    with open(filename, "w") as file:
        file.write(new_text)


find_and_replace("data.txt", "old", "new")
