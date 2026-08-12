def split_file(filename, lines_per_file):
    with open(filename, "r") as file:
        lines = file.readlines()

    for i in range(0, len(lines), lines_per_file):
        part_number = i // lines_per_file + 1

        with open(f"{filename}_part{part_number}.txt", "w") as part_file:
            part_file.writelines(lines[i:i + lines_per_file])


split_file("large.txt", 100)
