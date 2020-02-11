# improt modules or dependencies
import os
import csv
# assign the file path and open CSV File
data_analysis = os.path.join("budget_data.csv")
with open(data_analysis) as csvfile:
# Variables declaration with values for each
    total_months = 0
    profits = 0
# Read csv file 
    csvreader=csv.reader(csvfile,delimiter=',')
# count total Rows in our csv file
    rows=[x for x in csvreader]
    # determine the first row in our csv file 
    change_profits = int(rows[1][1])
    max = rows[1]
    min=rows[1]
    # apply for loop to the Data 
    for i in range(1,len(rows)):
        
        total_months += 1
        row = rows[i]
        profits = int(row[1]) + profits
        
        # Exclude Header, since we do not need it 
        if i > 1:
            change_profits = change_profits + int(row[1]) - int(rows[i-1][1])
        # calculate max profits
        if int(max[1]) < int(row[1]):
            max = row
        # calculate min profits
        if int(min[1]) > int(row[1]):
            min=row
# Calculate Average and Average Change in profits
average = int(profits /total_months)
average_change_profits = int(change_profits/total_months)

# printout the results
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(total_months))
print("Total profits: " +"$" +str(profits))       
print("Average profits Change: " +"$"+ str(average))
print("Average Change in profits Change: " +"$"+ str(average_change_profits))
print("Greatest Increase in profits:" + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease in profits:" + str(min[0])+" ($" + str(min[1])+")")


# export txt.file to be printed out when running this Python file
with open("my_PyBank_output.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("-------------------", file=text_file)
    print("Total Months: " + str(total_months), file=text_file)
    print("Total profits: " +"$" +str(profits), file=text_file)       
    print("Average profits Change: " +"$"+ str(average), file=text_file)
    print("Average Change in profits Change: " +"$"+ str(average_change_profits), file=text_file)
    print("Greatest Increase in profits:" + str(max[0])+" ($" + str(max[1])+")", file=text_file)
    print("Greatest Decrease in profits:" + str(min[0])+" ($" + str(min[1])+")", file=text_file)
# this work is finaly done, ready to be added, commited and pushed to github!