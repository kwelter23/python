print("Financial Analysis")
print("----------------------------")

import os

import csv

csvpath =os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   
    csvheader = next(csvfile)
    
       #Profits and Losses Added 
    Total_Amount = 0
    Total_Months = 0
    Average_Changes = 0
    Greatest_Increase = []
    for row in csvreader: 
        Total_Months=Total_Months+1 
        Total_Amount += float(row[1])
        Average_Changes = float(Total_Amount/Total_Months)
        If float (row[1])>
    print(f"Total Months: {Total_Months}")
    print(f"Total: ${Total_Amount}")
    print(f"Average Change: ${Average_Changes}")
    print(Greatest_Increase)
    