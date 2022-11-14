
print("Financial Analysis")
print("----------------------------------")

import os
import csv

csv_path = os.path.join('..','Resources','budget_data.csv')

with open('budget_data.csv' , 'r') as bank_data:
    bank_data_reader = csv.reader(bank_data)

#Total Months:

    next(bank_data_reader)

    bank_data_list = list(bank_data_reader)
    Total_Profit = 0
    for row in bank_data_list:
        Total_Profit += int(row[1])
print("Total Months:", len(bank_data_list))
print("Total :$",Total_Profit)

months = []
revenue = []

with open('budget_data.csv' , 'r') as bank_data:
    bank_data_reader = csv.reader(bank_data)

    for row in bank_data_reader:
        months.append(row[0])
        revenue.append(row[1])

revenue = [float(number) for number in revenue[1:]]
months = [date for date in months[1:]]
profit_lastmon = 0
change_sum = [0]

for i in range(1,len(revenue)):
    profit_current = float(revenue[i])
    change_mtm = profit_current - profit_lastmon
    change_sum.append(change_mtm)
    profit_lastmon = profit_current
greatest_increase = change_sum.index(max(change_sum))
greatest_decrease = change_sum.index(min(change_sum))
# print(monthlychanges)
print("Average Change: $",(sum(change_sum)/len(change_sum)))
print("Greatest Increase in Profits:", months[greatest_increase],max(change_sum))
print("Greatest Decrease in Profits:", months[greatest_decrease],min(change_sum))














