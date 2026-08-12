def write_file(lines, filename):
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


write_file(["Hello", "World"], "output.txt")
