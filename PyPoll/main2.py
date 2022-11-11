#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:






#The winner of the election based on popular vote

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

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #---------------------------------------
    #A complete list of candidates who received votes. Create a variable that includes a list of unique candidates
    #---------------------------------------    
    for row in csvreader:
        candidateslist.append(row[2])
    #convert list to dict to dedupe
    candidates = dict.fromkeys(candidateslist)
    #convert to dictionary
    print(candidates)
   #{'Charles Casper Stockham': None, 'Diana DeGette': None, 'Raymon Anthony Doane': None}

    vote = 0
    for candidate in candidates:
        for row in csvreader:
            if row[2] == candidate:
                vote = vote + 1
    print("vote: " + str(vote))


    #loop through tthe csv
    #find the candidates name in [2]
    #add 1 to their vote count

    #---------------------------------------
    #The total number of votes cast is the same as the length of the candidates list (that is, the same as the number of rows in the csv)
    #---------------------------------------
    total_votes = len(candidateslist)








    # ['Ballot ID', 'County', 'Candidate']
    #1323913  Jefferson  Charles Casper Stockham


    

    

 
    #---------------------------------------
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #---------------------------------------


\
   



    #---------------------------------------
    #Print to terminal
    #---------------------------------------
    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    #print(summary_df.to_string(index=True, header=True))
    print("-------------------------")
    #print("Winner: " + winner_votes )
    print("-------------------------")
    #print(summary_df[winner_votes])

    #---------------------------------------
    #Output to text file
    #---------------------------------------

    # Export file as a CSV, without the Pandas index, but with the header
    #election_output.to_csv("Output/fileOne.csv", index=False, header=True)