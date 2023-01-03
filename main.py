import os
import csv 

print("Financial Analysis")

print("------------------------")

budget_csv = os.path.join("Resources", "Budget_data.csv")


max_difference = []
min_difference = []
output = []

# open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    data = list(csv_reader) 
    rows = csv.DictReader(csv_reader)
    data1 = [int(row['amount']) for row in rows]   

# Count number of rows 
    for row in csv_reader:

        pass
    print("Total Months: ", csv_reader.line_num -1)

# Count total amount 

ls = [float(row[1]) for row in data[1:]] 

# built-in sum function
column_sum = sum(ls)

# print result
print(f'Total: ${column_sum}') 

# Count average change 

Difference = {column_sum - column_sum[+1]}

average = {Difference/ (csv_reader.line_num -1)}

print(f"Average change: ", {average})

# max difference 
data1 = [int(number) for number in lines[1:]]
for index, number in enumerate(data[1:],1):
    output.append(number-data[index-1])
print(output)
print("Average: {}".format(sum(output)/len(output)))

# min difference 