import re


class Customer:
    def __init__(self, data_list):
        self.e_mail = data_list[0]
        self.tel = data_list[1]
        self.name = data_list[2]
        self.first_name = self.name.split(" ")[0]
        self.last_name = self.name.split(" ")[1]

    def __repr__(self):
        return f"Vardas: { self.first_name } Pavarde: { self.last_name } Telefonas: {self.tel} E-mail: {self.e_mail}"


patterns = [
    (r"([a-zA-Z]{1,}@[a-zA-Z]{1,}\.[a-zA-Z]{1,})", 1),
    (r"(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+", 0),
    (r"([A-Z]{1}[a-z]{1,}\s[A-Z]{1}[a-z]{1,})", 1)
]



def regex_search(text, pattern, target_group):
    res = ''
    search_res = re.search(pattern, text)
    if search_res:
        if len(search_res.groups()) >= target_group:
            res = search_res.group(target_group).strip()
    # print(search_res)
    # print(search_res.groups(), target_group)
    # print(res)
    # print(len(search_res.groups()))
    return res


a_file = open("marius_regex_rask.txt", "r")

list_of_lines = a_file.readlines()
a_file.close()

# print(list_of_lines)
line_array = []
for file_line in list_of_lines:
    line_data = []
    for pattern in patterns:
        # print(file_line)
        # print(pattern)
        result = regex_search(file_line, pattern[0], pattern[1])
        line_data.append(result)
    line_array.append(line_data)
# print(line_array)

customer_array = []
for customer_data in line_array:
    customer_array.append(Customer(customer_data))

# print(customer_array)
# a = [e for e in customer_array if "karolis" in e.first_name.lower()]
# a = (a and a[0].first_name)
# print(a)

def finde_customer(customer_array, field_name, search_keyword):
    result_list = [getattr(e, field_name) for e in customer_array if search_keyword.lower() in getattr(e, field_name).lower()]
    return result_list and result_list[0] or ""

a = finde_customer(customer_array, "first_name", "karolis")
print(a)


# b = [e.first_name for e in customer_array if "karolis" in e.first_name.lower()]
# print(b)

# e_mails = [e[0] for e in line_array if "karolis" not in e[0]]
# print(e_mails)
#
# tel = [e[1] for e in line_array]
# print(tel)
#
# name = [e[2] for e in line_array]
# print(name)
