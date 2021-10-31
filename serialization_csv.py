import csv

# Writing to csv
# open("employees.csv", 'a') mode 'a' selected here, means that new data is added to file, not overwriten
with open("employees.csv", 'a') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Name", "Salary"])
    writer.writerow(["Anna Dylan", 2500])
    writer.writerow(["Anna Dylan2", 2500])
    writer.writerow(["Anna Dylan3", 2500])
    writer.writerow(["Anna Dylan4", 2500])


# Reading from csv
with open("employees.csv") as in_file:
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
        # row is the csv line (row)
