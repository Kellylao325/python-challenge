import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv" )
with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 # go to next row since row 1 is header
    csv_header = next(csvreader)

    month = []
    net_total = []

# Total Month (count rows of data) 
    for row in csvreader:
        month.append(row[0])
        total_month = len(month)

# Net Total (sum of profit/losses)
        net_total.append(int(row[1]) 
    
# Average change= Average of(current month - previous month)
    revenue_change = []
        for i in range(1, len(net_total)):
            revenue_change.append((int(net_total)[i])-int(net_total[i-1]))

    revenue_average = sum(revenue_change)/len(revenue_change)

# Greatest increase= Max of (current month - previous month)
        greatest_increase = max(revenue_change)

# Greatest decrease= Min of (current month - previous month)
        greatest_decrease = min(revenue_change)

print("Financial Analysis")
print("....................")
print(f'Total Months: {total_month')
print(f'Total: {net_total}')
print(f'Greatest Increase: {greatest_increase')
print(f'Greatest Descrease: {greatest_decrease')
