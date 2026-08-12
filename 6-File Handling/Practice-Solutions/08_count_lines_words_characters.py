def count_lwc(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        words = sum(len(line.split()) for line in lines)
        characters = sum(len(line) for line in lines)

    return len(lines), words, characters


print(count_lwc("stats.txt"))
