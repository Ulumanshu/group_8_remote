a_file = open("sample.txt", "r")

list_of_lines = a_file.readlines()

list_of_lines[1] = "Line2\n"
new_filename = list_of_lines[0] + '.txt'

a_file = open(new_filename, "w")

a_file.writelines(list_of_lines)

a_file.close()