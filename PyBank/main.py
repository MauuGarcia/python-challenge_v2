import os
import csv

totalmonths = []
profits =[]
change = []

with open ("C:\\python-tets/budget_data.csv") as csv_file:
    csvreader = csv.reader(csv_file)
    csv_header = next (csvreader)
    for a in csvreader:
        totalmonths.append(a[0])
        profits.append(int(a[1]))

for x in range(len(profits) - 1):
    change.append(profits[x+1]-profits[x])

totalofmonths  = len(totalmonths)
sum_profits = sum(profits)
averageCHG = round(sum(change)/len(change),2)
greatest_in = ((totalmonths[change.index(max(change))+1]))
greatest_dec = ((totalmonths[change.index(min(change))+1]))
g_in = max(change)
g_dec = min(change)
print('Financial Analysis')
print('')
print('---------------------------------------')
print('')
print(f'Total of months: {totalofmonths}')
print(f'Sumatoria {sum_profits}')
print(f'Average {averageCHG}')
print(f'Greatest Increase in Profits:{greatest_in}  {g_in}')
print(f'Greatest Decrease in Profits:{greatest_in}  {g_dec}')




