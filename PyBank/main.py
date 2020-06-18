#---------PyBank_Challenge-----------
# I will need to import os ans csv to begin
import os, csv

# create a csvpath
bank_csv = os.path.join('..','PyBank','Resources','budget_data.csv')

#---variables/lists----
total_months = []
total_profit = []
monthly_prof_change = []
months = 0

#---Capture the total number of months in my list----
#---Loop through [0] and [1] to find to the total net profit and append it to my empty list variables above---
with open (bank_csv) as csvfile:  
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)                           #skip the header                  
    for row in reader:                              #Cycle through each row in the csvfile
        months += int(row[1])                       #for every row, add each row to the total
        total_months.append(row[0])                 #append the total number of months to open list variable
        total_profit.append(row[1])                 #append the total profit from row[1] to open list variable
    for row in range(len(total_profit)-1):          #for the range in the length of total profit minus one since we are calculating the average rate of change (85 instead of 86)
        #append the formula for total profit between two months minus the one month
        monthly_prof_change.append(int(total_profit[row+1])-int(total_profit[row]))     
                                                    #print(f"Average Change: {round(sum(monthly_prof_change)/len(monthly_prof_change),2)}")  
                                                    #formula for printing avg change, I will put down below where I want to print all my statements
                                                    #Now I need to find the largest increase and decrease from the monthly_prof_change list
        max_greatest = max(monthly_prof_change)     #setting a max variable 
        max_lowest = min(monthly_prof_change)       #setting a min increase variable
        max_greatest_prof = monthly_prof_change.index(max(monthly_prof_change)) + 1     #this will search through mpf and find the index where the greatest profit is
        max_lowest_prof = monthly_prof_change.index(min(monthly_prof_change)) + 1       #this will search through mpf and find the index where the lowest profit/loss is
    
#--------Final Print Statements-------#
print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${months}") 
print(f"Average Change: {round(sum(monthly_prof_change)/len(monthly_prof_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_greatest_prof]} (${(str(max_greatest))})")
print(f"Greatest Decrease in Profits: {total_months[max_lowest_prof]} (${(str(max_lowest))})")

#--------Output to File---------#
#create a text file

file = open("analysisoutput.txt","w+")
#file_path = os.path.join('..','PyBank','Analysis','analysisoutput.txt')

file.write(
f"Financial Analysis\n ------------------\nTotal Months: {len(total_months)}\nAverage Change: {round(sum(monthly_prof_change)/len(monthly_prof_change),2)}\n"
)
file.write(
f"Greatest Increase in Profits: {total_months[max_greatest_prof]} (${(str(max_greatest))})\nGreatest Decrease in Profits: {total_months[max_lowest_prof]} (${(str(max_lowest))})\n"
)
file.close()

