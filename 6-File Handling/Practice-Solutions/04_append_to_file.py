def append_to_file(text, filename):
    with open(filename, "a") as file:
        file.write(text + "\n")


append_to_file("This is a new log entry.", "log.txt")
