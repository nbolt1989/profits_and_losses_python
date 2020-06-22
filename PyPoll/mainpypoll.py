#---------PyPoll---------
#Instructions: see GitLabL UNC BC
#----import/join-------
#I will need to bring the os and csv like in PyBank
import os, csv
#create csv path and assign to a variable
csvpoll = os.path.join('..','PyPoll','Resources','ElectionDataPyPoll.csv')

#----Variables/Lists------
#I am going the list and conditional route so I will need to build out a few empty lists and variables
# this is a little clunky 
# Make sure I add them here if new variables/lists are needed down the line to keep my code organized
total_votes = []
candidates = []
#manualcandidates = ["Khan","Correy","Li","O'Tooley"]
khanvotes = []
correyvotes = []
livotes = []
otooleyvotes = []
candidatesvoteslist = []
total = 0
winning_count =0
#----Open-----
#I am opening up the csv file and reading it
with open (csvpoll,'+r') as csvfile:
#assign to a variable and then delimit at the ,
    reader = csv.reader(csvfile, delimiter=',')
#skip the header
    header = next(reader)
#I will need to run a for loop through column 1 and column 3 and assigned to lists. 
    for row in reader:
        total_votes.append(row[0])               
        candidates.append(row[2]) 

# I can print out a list of unique items in row[2] to find there are four unique candidates
# The candidates list has now been filled. I am now running a for loop through candidates and looking for each individual 
#candidate
# I am going primarily with conditionals and lists as opposed to lists and dictionaries for practice. I will likely create a new
# script utilizing dictionaries and loops down the road. But for now, you get conditionals.
    for row in (candidates):
#search for Khan and append the count to khanvotes
        if row == "Khan":
            a = "Khan"
# this will allow me to add each vote for Khan to his list. I am creating a,b,c,and d variables to call in my final
# print statement below
            total += 1
            khanvotes.append(total)
#repeat for each candidate
        elif row == "Correy":
            b = "Correy"
            total += 1
            correyvotes.append(total)
        elif row == "Li":
            c = "Li"
            total += +1
            livotes.append(total)
        elif row == "O'Tooley":
            d = "O'Tooley"
            total += +1
            otooleyvotes.append(total)

# I could do an else here and make another list to catch any other items but I know the four candidates so it is unneccessary
# Now that I have caught all my candidates and their votes I need to compare their votes to the total vote count
# in order to find the percentage--make sure to multiply by 100 and round. 
khanpercent = round(int(len(khanvotes))/int(len(total_votes)),3)*100
correypercent = round(int(len(correyvotes))/int(len(total_votes)),3)*100
lipercent = round(int(len(livotes))/int(len(total_votes)),2)* 100
otooleyvotespercent = round(int(len(otooleyvotes))/int(len(total_votes)),3)*100
# I want to now bring my lists into a dictionary in order to see which key:value pair has the greatest/max number 
# of votes. 
#I am assigning candidate name to Key and the length of their votes as the Value. 
mydict = {"Khan": len(khanvotes),"Correy":len(correyvotes), "Li": len(livotes), "O'Tooley": len(otooleyvotes)}
# I need to use the max function through my dictionary
maxvalue = max(mydict.values())  # maximum value
# Loop through my dictionary and I will need to set up a conditional to find votes greater than winning count. This will find the highest number of votes and spit
#out the candidate. 
for candidate in mydict:
    votes = mydict.get(candidate)
    if (votes > winning_count):
        winning_count=votes
        winning_candidate = candidate
    
   
#--------Final Print Statements-------#
print("Election Results\n" + "------------------\n")
print(f"Total Votes: {len(total_votes)}\n------------------")
print(f'{a}: {khanpercent}% ({len(khanvotes)})\n{b}: {correypercent}% ({len(correyvotes)})\n{c}: {round((lipercent),2)}% ({len(livotes)})\n{d}: {otooleyvotespercent}% ({len(otooleyvotes)})')
print("------------------")
print(f'Winner: {winning_candidate}')
print("------------------")

#--------Output to File---------#
#create a text file
#import os.path
#file_path = os.path.join('..','PyBank','Analysis')
file = open("Analysis/pollanalysisoutput.txt","w+")

#file_path = os.path.join('..','PyBank','Analysis','analysisoutput.txt')

file.write("Election Results\n")
file.write("------------------\n")
file.write(f"Total Votes: {len(total_votes)}\n")
file.write("------------------\n")
file.write(f'{a}: {khanpercent}% ({len(khanvotes)})\n{b}: {correypercent}% ({len(correyvotes)})\n{c}: {round((lipercent),2)}% ({len(livotes)})\n{d}: {otooleyvotespercent}% ({len(otooleyvotes)})\n')
file.write("------------------\n")
file.write(f'Winner: {winning_candidate}\n')
file.write("------------------\n")

file.close()