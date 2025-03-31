def read_file_safe(filename):
    with open("testfile.txt","w") as filename:
        filename.write("a file")

    with open("testfile.txt","r") as filename:
        output = filename.readlines()
        print(output)

    if filename :
        ''
    else:
        print("file name not found, write correct filename")

