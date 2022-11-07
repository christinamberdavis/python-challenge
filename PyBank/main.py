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

#QC: open the file and read it into the terminal
with open(csvpath) as csvfile:
    budget_data_csv = csv.reader(csvfile, delimiter=',')
    #print(budget_data_csv)
    #output: <_csv.reader object at 0x7fde0de89890>


    # Read the header row first (skip this step if there is no header)
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
    #print(months)

    #count total number of months in the list
    total_months = len(months)

#------------------------------------------------------------------------------------------------------------
#The net total amount of "Profit/Losses" over the entire period
#------------------------------------------------------------------------------------------------------------
#sum up all values in profit_loss
    #for row in budget_data_csv: 
    profit_loss = int(sum(p_l))

    #convert profit_loss to string
    #profit_string = str(profit_loss)

#------------------------------------------------------------------------------------------------------------
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#------------------------------------------------------------------------------------------------------------
    differences = []
    pl_index = 0
    run = len(p_l) - 2
    #print(run)

    for value in p_l:
        #difference = p_l(pl_index) - p_l(pl_index + 1)
        if pl_index <= run:
            difference = p_l[pl_index] - p_l[pl_index + 1]
            #print(difference)
            differences.append(int(difference))
            pl_index = pl_index + 1

        elif pl_index > run:
            average_change = sum(differences) / len(differences)

#------------------------------------------------------------------------------------------------------------
#The greatest increase in profits (date and amount) over the entire period
#------------------------------------------------------------------------------------------------------------
    increases = []
    pl_index = 0
    
    for value in p_l:
        if pl_index <= run:
            increase = p_l[pl_index + 1] - p_l[pl_index]
            increases.append(int(increase))
            pl_index = pl_index + 1

        elif pl_index > run:
            biggest_increase = max(increases)

#------------------------------------------------------------------------------------------------------------
#The greatest increase in profits (date and amount) over the entire period
#------------------------------------------------------------------------------------------------------------
            biggest_decrease = min(increases)

#------------------------------------------------------------------------------------------------------------
#Print out all the data
#------------------------------------------------------------------------------------------------------------
    print("Total Months: " + str(total_months))
    print("Total: ${:,.2f}".format(profit_loss))
    print("Average Change: ${:,.2f}".format(average_change))
    print("Greatest Increase in Profits: ${:,.2f}".format(biggest_increase))
    print("Greatest Decrease in Profits: ${:,.2f}".format(biggest_decrease))



    #print("CSV Header: {}".format(csv_header))
    #output: CSV Header: ['Date', 'Profit/Losses']

    #Create a list of lists of rows
    #csv_rows = list(budget_data_csv)
    #output a row to see what the data looks like
    #print(csv_rows)
    #output: CSV Rows: ['Feb-10', '-354534']

    #figure out the total number of rows
    #total_rows = int(len(csv_rows))
    #print(total_rows)