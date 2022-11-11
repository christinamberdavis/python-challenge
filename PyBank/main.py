#------------------------------------------------------------------------------------------------------------
#INSTRUCTIONS
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#------------------------------------------------------------------------------------------------------------

#import modules for os and reading csv
import os
import csv

#set csvpath so that the csv can be found
csvpath = os.path.join('Resources', 'budget_data.csv')

#open the csv
with open(csvpath) as csvfile:
    budget_data_csv = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(budget_data_csv)

    #create lists of the columns
    months = []
    p_l = []

    #add data to the lists
    for csv_rows in budget_data_csv:
        #add month to month
        months.append(csv_rows[0])
        #add p&l data to p_l and cast the list values as int
        p_l.append(int(csv_rows[1]))

#------------------------------------------------------------------------------------------------------------
#The total number of months included in the dataset
#------------------------------------------------------------------------------------------------------------
#let's dedupe months since we need total number of months, not rows
#First, create a dictionary using the List items as keys using (dict.fromkeys(months_list)
#This automatically removes duplicates because dictionaries cannot have duplicate keys.
#convert the dictionary back into the list by adding 'months = list' to the beginning
#reference: https://www.w3schools.com/python/python_howto_remove_duplicates.asp 
#reference retrieve 11/06/2022
    months = list(dict.fromkeys(months))

    #count total number of months in the list
    total_months = len(months)

#------------------------------------------------------------------------------------------------------------
#The net total amount of "Profit/Losses" over the entire period
#------------------------------------------------------------------------------------------------------------
    #sum up all values in profit_loss
    profit_loss = int(sum(p_l))

#------------------------------------------------------------------------------------------------------------
#Set up variables and do math for Average Change, Greatest Increase, and Greatest Decrease
#------------------------------------------------------------------------------------------------------------
 
 #cerate variables
    #difference month over month
    diffs = []
    #track the p_l index we are on
    pl_index = 0
    #set increase to 0
    biggest_increase = 0
    #set decrease to 0
    biggest_decrease = 0
    #set date indices to 0
    date_inc_index = 0
    date_dec_index = 0
    #calculate a value so that we don't try to calculate the last row - 1
    run = len(p_l) - 2
    
    #loop through each value in p_l list
    for value in p_l:
        #if we are not on the last value of p_l, then
        if pl_index <= run:
            #calculate the month over month difference
            diff = p_l[pl_index + 1] - p_l[pl_index]
            #add the diff to the diffs list
            diffs.append(int(diff))
            #set values for biggest increase 
            if (diff > biggest_increase):
                biggest_increase = diff
                #track the index of the biggest increase value
                date_inc_index = pl_index + 1
            #set values for biggest decrease
            if (diff < biggest_decrease):
                biggest_decrease = diff
                #track the index of the biggest decrease value
                date_dec_index = pl_index + 1
            #increment the index tracker for the next set of p_l values
            pl_index = pl_index + 1

        #if on the last row
        elif pl_index > run:

#------------------------------------------------------------------------------------------------------------
#The greatest increase in profits (date and amount) over the entire period
#------------------------------------------------------------------------------------------------------------

            biggest_increase = max(diffs)

#------------------------------------------------------------------------------------------------------------
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#------------------------------------------------------------------------------------------------------------

            average_change = sum(diffs) / len(diffs)


#------------------------------------------------------------------------------------------------------------
#The greatest increase in profits (date and amount) over the entire period
#------------------------------------------------------------------------------------------------------------

            biggest_decrease = min(diffs)

#------------------------------------------------------------------------------------------------------------
#Print out all the data to terminal
#------------------------------------------------------------------------------------------------------------
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: ${:,.2f}".format(profit_loss))
    print("Average Change: ${:,.2f}".format(average_change))
    print("Greatest Increase in Profits: " + months[date_inc_index] + " ${:,.2f}".format(biggest_increase))
    print("Greatest Decrease in Profits: " + months[date_dec_index] + " ${:,.2f}".format(biggest_decrease))


#------------------------------------------------------------------------------------------------------------
#Print out all the data to text file
#------------------------------------------------------------------------------------------------------------
lines = ["Financial Analysis",
         "----------------------------",
         "Total Months: " + str(total_months),
         "Total: ${:,.2f}".format(profit_loss),
         "Average Change: ${:,.2f}".format(average_change),
         "Greatest Increase in Profits: " + months[date_inc_index] + " ${:,.2f}".format(biggest_increase),
         "Greatest Decrease in Profits: " + months[date_dec_index] + " ${:,.2f}".format(biggest_decrease)]
with open('financial_analysis.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')