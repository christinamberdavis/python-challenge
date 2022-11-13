#import modules for os and reading csv
import os
import csv

#set csvpath so that the csv can be found
csvpath = os.path.join('Resources', 'election_data.csv')
#lists to store data
candidateslist = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #---------------------------------------
    #A complete list of candidates who received votes. Create a variable that includes a list of unique candidates
    #---------------------------------------    
    for row in csvreader:
        candidateslist.append(row[2])
        #print(row)
    #print('------------------------')
    #print(candidateslist)
    
    #---------------------------------------
    #The total number of votes cast is the same as the length of the candidates list (that is, the same as the number of rows in the csv)
    #---------------------------------------
    total_votes = len(candidateslist)
    #print(total_votes)

    #convert list to dict to dedupe. Candidate names are Keys. 
    #you can't make the nested dictionary here because it treats it as ONE OBJECT that is being shared by all candidates
    candidates_votes = dict.fromkeys(candidateslist, 0)
    #print (candidates) = {'Charles Casper Stockham': 0, 'Diana DeGette': 0, 'Raymon Anthony Doane': 0}

    #loop through the keys in candidateslist
    for candidate in candidateslist:
        #the first time we find the candidate in the list, check to see if it's key value in the dictionary is 0. 
        if candidates_votes[candidate] == 0:
            #If yes, create a dictionary for each candidate to hold the vote count and percentage of votes calculation
            candidates_votes[candidate] = {'vote_count':0, 'percentage':0.0 }
        #If no, incremente the candidates's vote count
        candidates_votes[candidate]['vote_count'] +=1
    
    winner_votes = 0
    #calculate the percentage for each candidate
    for candidate in candidates_votes:
        candidates_votes[candidate]['percentage'] = (candidates_votes[candidate]['vote_count']/total_votes)*100
        #if candidates's vote_count > winner_vote, set winner_vote = vote_count 
        if candidates_votes[candidate]['vote_count'] > winner_votes:
            winner_votes = candidates_votes[candidate]['vote_count']
            #because we know who the candidate with the biggest count is right now, we know who the candidate is
            #so we set the winner to the key we are on (the candidate)
            winner = candidate
    #print(winner + " " + str(winner_votes)) = Diana DeGette 272892


    #---------------------------------------
    #Print to terminal
    #---------------------------------------
    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    for candidate in candidates_votes:
        print(candidate + ": {:,.3f}".format(candidates_votes[candidate]['percentage']) + "% (" + str(candidates_votes[candidate]['vote_count'])+ ")")
    print("-------------------------")
    print("Winner: " + winner )
    print("-------------------------")

#------------------------------------------------------------------------------------------------------------
#Print out all the data to text file
#------------------------------------------------------------------------------------------------------------
lines = [("-------------------------\n"),
         ("Election Results\n"),
         ("-------------------------\n"),
         ("Total Votes: " + str(total_votes)) + "\n",
         ("-------------------------\n")]
for candidate in candidates_votes:
    lines.append(candidate + ": {:,.3f}".format(candidates_votes[candidate]['percentage']) + "% (" + str(candidates_votes[candidate]['vote_count'])+ ")" + "\n")

lines.append(("-------------------------\n"))
lines.append(("Winner: " + winner) + "\n")
lines.append(("-------------------------\n"))

with open('election_results.txt', 'w') as f:
    f.writelines(lines)
f.close