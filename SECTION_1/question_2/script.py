def write_names_to_file(names,filename= 'names.txt'):
    with open(filename,"w") as file:
        for name in names:
            file.write(name + '\n')





write_names_to_file(['alice','lois'])