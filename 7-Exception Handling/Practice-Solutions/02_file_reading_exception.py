def read_file(filename):
    file = None

    try:
        file = open(filename, "r")
        content = file.read()
        return content
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        if file is not None:
            file.close()


print(read_file("data.txt"))
