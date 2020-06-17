#---------PyBank_Challenge-----------
#-----------INSTRUCTIONS--------
'''In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
(Thankfully, your company has rather lax standards for accounting so the records are simple.)
Your task is to create a Python script that analyzes the records to calculate each of the following:
    The total number of months included in the dataset - DONE
    The net total amount of "Profit/Losses" over the entire period - DONE
    The average OF THE CHANGES in "Profit/Losses" over the entire period - DONE
    The greatest increase in profits (date and amount) over the entire period -DONE
    The greatest decrease in losses (date and amount) over the entire period -DONE'''

# I will need to import os ans csv to begin
import os
import csv 

# create a csvpath
bank_csv = os.path.join('..','PyBank','Resources','budget_data.csv')

total_months2 = []
total_profit = []
monthly_prof_change = []
total_months = 1

# now I need to open with csv
with open (bank_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')     # create a csvreader variable with a delimiter
    #header = next(csvfile)       #skip the header
    #print(f'Header: {header}')   #This will print out the header. The first turns everything into strings and variables can be inserted.
    #print("Financial Analysis")
    #print("------------------")
    for row in reader:
        lines = len(list(reader))    #my variable for finding the total number of lines--this is now an int
    #print(f"Total Months: {lines}")

with open (bank_csv) as csvfile:  
    reader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)       #skip the header                  #establish a total variable for column[1] and set it to 0
    for row in reader:           #Cycle through each row in the csvfile
        total_months += int(row[1])     #for every row, add each row to the total
    #print(f"Total: ${total_months}")    #print total number of row[1]

#I need to cycle through all the months and their associative change in profits and losses
with open (bank_csv) as csvfile:  
    reader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)  
    for row in reader:          #cycles through my reader again
        total_months2.append(row[0])    #append the total number of months to open list variable
        total_profit.append(row[1])     #append the total profit from row[1] to open list variable
    for row in range(len(total_profit)-1):        #for the range in the length of total profit minus one since this is the change between each number of months (86 instead of 87)
        monthly_prof_change.append(int(total_profit[row+1])-int(total_profit[row]))     #append the formula for total profit between two months minus the one month
    #print(f"Average Change: {round(sum(monthly_prof_change)/len(monthly_prof_change),2)}")  #formula for avg change
#Now I need to find the largest increase and decrease from the monthly_prof_change list
    max_greatest = max(monthly_prof_change) #setting a max increase variable 
    max_lowest = min(monthly_prof_change)   #setting a min increase variable
    max_greatest_prof = monthly_prof_change.index(max(monthly_prof_change)) + 1   #this will search through mpf and find the index where the greatest profit is
    max_lowest_prof = monthly_prof_change.index(min(monthly_prof_change)) + 1       #this will search through mpf and find the index where the lowest profit/loss is
    #print(f"Greatest Increase in Profits: {total_months2[max_greatest_prof]} (${(str(max_greatest))})")
    #print(f"Greatest Decrease in Profits: {total_months2[max_lowest_prof]} (${(str(max_lowest))})")




    #--------Final Print Statements-------#
print("Financial Analysis")
print("------------------")
print(f"Total Months: {lines}")
print(f"Total: ${total_months}") 
print(f"Average Change: {round(sum(monthly_prof_change)/len(monthly_prof_change),2)}")
print(f"Greatest Increase in Profits: {total_months2[max_greatest_prof]} (${(str(max_greatest))})")
print(f"Greatest Decrease in Profits: {total_months2[max_lowest_prof]} (${(str(max_lowest))})")

    #--------Output to File---------#








        



