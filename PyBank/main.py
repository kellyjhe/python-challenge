# Dependencies
import os
import csv

# Set path for CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

# Set initial variables
unique_months = set()
profit_added = 0
profit_amt = 0
loss_amt = 0

# Open CSV to read
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip header row
    header = next(csvreader)

    # Set loop through CSV
    for row in csvreader:
        
        # Find total months
        # Code help from Xpert
        date = row[0]
        month = date.split(',')[0]
        unique_months.add(month)

        # Find total profit
        profit_loss = int(row[1])
        profit_added += profit_loss

        # Use conditional to find greatest increase and decrease amounts
        if profit_loss > profit_amt:
            profit_amt = profit_loss
            greatest_date = row[0]

        if profit_loss < loss_amt:
            loss_amt = profit_loss
            least_date = row[0]
            
# Count unique values in total months and convert to integer
total_months = int(len(unique_months))

total_profit = round(profit_added, 1)

# Calculate average change
avg_change = round((profit_added / total_months), 2)

# Print in Terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_date} (${profit_amt})")
print(f"Greatest Decrease in Profits: {least_date} (${loss_amt})")

# Print in text file
with open("analysis/analysis.txt", "w") as file:
    file.write("Financial Analysis\n" +
               "----------------------------\n" +
               "Total Months: " + str(total_months) + "\n" +
               "Total: $" + str(total_profit) + "\n" +
               "Average Change: $" + str(avg_change) + "\n" +
               "Greatest Increase in Profits: " + str(greatest_date) + " ($" + str(profit_amt) + ")" + "\n" +
               "Greatest Decrease in Profits: " + str(least_date) + " ($" + str(loss_amt) + ")")