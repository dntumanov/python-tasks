import os.path

file_input = "supp_files/task-3/example-input.txt"
if os.path.isfile(file_input):
    list_str: list = list(open(file_input, 'r'))
    file_output = open("supp_files/task-3/example-output.txt", "w")
    for line in reversed(list_str):
        file_output.write(line.rstrip() + "\n")
    file_output.close()
else:
    print("File not found")
