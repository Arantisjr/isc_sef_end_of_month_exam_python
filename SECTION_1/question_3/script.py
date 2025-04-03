def read_file_safe(filename):
    try:
         with open(filename,"r") as file:
            return file.read()
    except FileNotFoundError:
            print(f"Eror file name '{filename}' does not exist")
            return None

output = read_file_safe("dklsl")
if output:
     print(output)