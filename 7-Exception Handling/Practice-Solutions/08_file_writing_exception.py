def write_strings_to_file(strings, filename):
    file = None

    try:
        file = open(filename, "w")
        for string in strings:
            file.write(string + "\n")
    except IOError as e:
        print(f"Error: {e}")
    finally:
        if file is not None:
            file.close()


write_strings_to_file(["Hello", "World"], "output.txt")
