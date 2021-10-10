a_file = open("sample.txt", "r")

list_of_lines = a_file.readlines()

list_of_lines[1] = "Line2\n"


a_file = open("sample.txt", "w")

a_file.writelines(list_of_lines)

a_file.close()