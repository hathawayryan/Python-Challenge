import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    total_months = 0
    sum_profit_loss = 0
    changes = []
    change = 0
    temp_profit_loss = 0
    greatest_increase = 0
    greatest_decrease = 0

    for row in csvreader:
        sum_profit_loss += int(row[1])
        if total_months != 0:
            change = int(row[1]) - temp_profit_loss
            changes.append(change)
        temp_profit_loss = int(row[1])
        total_months += 1
        
        if change > greatest_increase:
            greatest_increase = change
            date_increase = row[0]
        
        if change < greatest_decrease:
            greatest_decrease = change
            date_decrease = row[0]

    change_average = round(sum(changes) / (total_months - 1), 2)

    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${sum_profit_loss}")
    print(f"Average Change: ${change_average}")
    print(f"Greatest Increase in Profits: {date_increase} ${greatest_increase}")
    print(f"Greatest Decrease in Profits: {date_decrease} ${greatest_decrease}")


output_file = os.path.join("Analysis", "PyBank_Analysis.txt")

writer =  open(output_file, 'w')

writer.write("Financial Analysis \n")
writer.write("---------------------------\n")
writer.write(f"Total Months: {total_months}\n")
writer.write(f"Average Change: ${change_average}\n")
writer.write(f"Greatest Increase in Profits: {date_increase} ${greatest_increase}\n")
writer.write(f"Greatest Decrease in Profits: {date_decrease} ${greatest_decrease}")
