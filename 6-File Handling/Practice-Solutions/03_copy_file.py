def copy_file(source, destination):
    with open(source, "r") as src:
        with open(destination, "w") as dest:
            dest.write(src.read())


copy_file("source.txt", "destination.txt")
