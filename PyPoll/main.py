#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:






#The winner of the election based on popular vote

#import modules for os and reading csv
import os
import pandas as pd

#set csvpath so that the csv can be found
csvpath = os.path.join('Resources', 'election_data.csv')

#open the csv
with open(csvpath) as csvfile:
    #election_data_csv = csv.reader(csvfile, delimiter=',')

    #create a dataframe
    df = pd.read_csv(csvpath)
    #print(df.head())
    # ['Ballot ID', 'County', 'Candidate']
    #1323913  Jefferson  Charles Casper Stockham

    #---------------------------------------
    #The total number of votes cast is the same as the number of unique ballot IDs
    #---------------------------------------
    number_votes = len(pd.unique(df['Ballot ID']))
    
    #---------------------------------------
    #A complete list of candidates who received votes. Create a variable that includes a list of unique candidates
    #---------------------------------------
    candidates = df["Candidate"].unique()
    #this returns a list of candidates
    #print(candidates)
 
    #---------------------------------------
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #---------------------------------------
    #get the % of votes for each candidate
    percentage = df["Candidate"].value_counts()/number_votes * 100
    #get the total votes for each candidate
    votes_each = df["Candidate"].value_counts()

    # Place all of the data found into a summary DataFrame
    summary_df = pd.DataFrame({
                              "Percentage of Votes": percentage,
                              "Total Votes": votes_each,
                              })
    

    #format the columns in the summary_df: % as float, total votes as # with commas
    summary_df.loc[:, "Total Votes"] = summary_df["Total Votes"].map('{:,d}'.format)
    summary_df.loc[:, "Percentage of Votes"] = summary_df["Percentage of Votes"].map('{:.3f}'.format)

    #find the number of votes for the winner
    winner_votes = summary_df["Percentage of Votes"].max()
   



    #---------------------------------------
    #Print to terminal
    #---------------------------------------
    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(number_votes))
    print("-------------------------")
    print(summary_df.to_string(index=True, header=True))
    print("-------------------------")
    print("Winner: " + winner_votes )
    print("-------------------------")
    print(summary_df[winner_votes])

    #---------------------------------------
    #Output to text file
    #---------------------------------------

    # Export file as a CSV, without the Pandas index, but with the header
    #election_output.to_csv("Output/fileOne.csv", index=False, header=True)