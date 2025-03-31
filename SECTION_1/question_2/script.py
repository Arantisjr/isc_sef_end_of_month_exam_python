def write_names_to_file(filename, names=[]):
    names = []

    with open("names.txt","w") as filename:
            filename.write(str(names.append(names)))

    with open("names.txt", "r") as filename:
        your_names = filename.readlines()
        print(your_names)




write_names_to_file("names.txt",["arantis","mola"])