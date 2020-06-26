import os

import csv

csvpath =os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

outputpath = os.path.join('..', 'PyBank', 'Resources', 'results.txt')

results = open(outputpath, "w")

print("Financial Analysis")
results.write("Financial Analysis\n")
print("----------------------------")
results.write("----------------------------\n")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   
    csvheader = next(csvfile)
    

    Total_Amount = 0
    Total_Months = 0
    Average_Changes = 0
    Total_Changes = 0
    Greatest_Change = 0
    Smallest_Change = 0

    Current_Line = next(csvreader)

    for row in csvreader: 
        Next_Line = row
        Total_Months=(Total_Months+1)
        Total_Amount += float(row[1])
        Change = float(Next_Line[1]) - float(Current_Line[1])
        if Change > Greatest_Change:
            Greatest_Change = Change
            Greatest_Month = row[0]
        if Change < Smallest_Change:
            Smallest_Change = Change
            Smallest_Month = row[0]
        Total_Changes += Change
        

        Current_Line = Next_Line
        

    Average_Changes = round(float(Total_Changes/Total_Months-1), 2)
        
    print(f"Total Months: {Total_Months}")
    results.write(f"Total Months: {Total_Months}\n")
    print(f"Total: ${Total_Amount}")
    results.write(f"Total: ${Total_Amount}\n")
    print(f"Average Change: ${Average_Changes}")
    results.write(f"Average Change: ${Average_Changes}\n")
    print(f"Greatest Increase in Profits: {Greatest_Month} ({Greatest_Change})")
    results.write(f"Greatest Increase in Profits: {Greatest_Month} ({Greatest_Change})\n")
    print(f"Greatest Decrease in Profits: {Smallest_Month} ({Smallest_Change})")
    results.write(f"Greatest Decrease in Profits: {Smallest_Month} ({Smallest_Change})")
   
    