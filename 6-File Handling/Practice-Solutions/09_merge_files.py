def merge_files(file_list, output_file):
    with open(output_file, "w") as outfile:
        for filename in file_list:
            with open(filename, "r") as infile:
                outfile.write(infile.read() + "\n")


merge_files(["file1.txt", "file2.txt"], "merged.txt")
