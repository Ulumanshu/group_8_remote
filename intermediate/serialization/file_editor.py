import re


def regex_search(text, pattern, target_group):
    res = ''
    search_res = re.search(pattern, text)
    if search_res:
        if len(search_res.groups()) <= target_group:
            res = search_res.group(target_group).strip()

    return res


a_file = open("sample.txt", "r")

list_of_lines = a_file.readlines()

list_of_lines[1] = "Line2\n"
pattern = r"(new_filename:)(.*);"
line_with_filename = list_of_lines[0]

new_filename = regex_search(line_with_filename, pattern, 2) + '.txt'
print(new_filename)

a_file = open(new_filename, "w")

a_file.writelines(list_of_lines)

a_file.close()