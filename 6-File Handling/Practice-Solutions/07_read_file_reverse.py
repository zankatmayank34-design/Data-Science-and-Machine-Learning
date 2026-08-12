def read_reverse(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in reversed(lines):
        print(line.strip())


read_reverse("reverse.txt")
