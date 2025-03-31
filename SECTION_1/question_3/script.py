def read_file_safe(filename):
    with open("testfile.txt","w") as filename:
        filename.write("a file")


    if filename != "testfile.txt":
        print("wrong file name")
    else:
        with open("testfile.txt","r") as filename:
            output = filename.read()
            print(output)
   

read_file_safe("")