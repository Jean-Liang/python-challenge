# Read budget data file
import os
import csv
budget_csv=os.path.join("..","Resources","budget_data.csv")

# open and read csv
with open (budget_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

# Read the header row
    csv_header=next(csv_reader)
# Get the next row after the header
    first_row=next(csv_reader)
# Define the variables 
# The first_row read from the first row of data after the header.So total_months starts from 1
    total_months = 1
    total_profit_losses=int(first_row[1])
    previous_month_profit_losses= int(first_row[1])
    monthly_change=[]
    greatest_increase=0
    greatest_decrease=0
    greatest_increase_date=''
    greatest_decrease_date=''
# Read through each row of data after the header
    for row in csv_reader:
# The total number of months included in the dataset
       total_months += 1
  
# The net total amount of "Profit/Losses" over the entire period
       total_profit_losses +=int(row[1])

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period   
# The greatest decrease in profits (date and amount) over the entire period   
       
       change_from_previous_month=int(row[1])-previous_month_profit_losses
       if change_from_previous_month > greatest_increase:
          greatest_increase=change_from_previous_month
          greatest_increase_date=row[0]
          
       if  change_from_previous_month < greatest_decrease:
          greatest_decrease=change_from_previous_month
          greatest_decrease_date=row[0]
       monthly_change.append(change_from_previous_month)
       previous_month_profit_losses=int(row[1])
       total_monthly_change=sum(monthly_change)
       average_change=total_monthly_change/(total_months-1)
    
# Print the final results as requested format
    print(f"Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${format(average_change,'.2f')}")
    print(f"Greatest Increase in profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Increase in profits: {greatest_decrease_date} (${(greatest_decrease)})")

#create strings for the results
results=(
   f"Financial Analysis\n"
   f"------------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_profit_losses}\n"
   f"Average Change: ${format(average_change,'.2f')}\n"
   f"Greatest Increase in profits: {greatest_increase_date} (${greatest_increase})\n"
   f"Greatest Increase in profits: {greatest_decrease_date} (${(greatest_decrease)})\n"
)

#create the output pathway in txt format
output_file=os.path.join("..","analysis","financial_analysis.txt")

with open(output_file,'w') as file:
   file.write(results)

print(results)
