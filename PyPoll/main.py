print("Election Results")
print("----------------------------")

import os

import csv

csvpath =os.path.join('..', 'PyPoll','Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   
    csvheader = next(csvfile)
    

    Total_Votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0
        
    for row in csvreader: 
        Total_Votes=Total_Votes+1 
        if str(row[2]) == 'Khan':
            Khan += 1
        if str(row[2]) == 'Correy':
            Correy += 1
        if str(row[2]) == 'Li':
            Li += 1
        if str(row[2]) == 'O\'Tooley':
            OTooley += 1

    Average_Khan = round (Khan/Total_Votes *100, 3)
    Average_Correy = round (Correy/Total_Votes *100, 3)
    Average_Li = round (Li/Total_Votes *100, 3)
    Average_OTooley = round (OTooley/Total_Votes *100, 3)

    List = [Khan, Correy, Li, OTooley]
        
    print(f'Total Votes: {Total_Votes}')
    print("----------------------------")
    print(f'Khan: {Average_Khan}% ({Khan})')
    print(f'Correy: {Average_Correy}% ({Correy})')
    print(f'Li: {Average_Li}% ({Li})')
    print(f'O\'Tooley: {Average_OTooley}% ({OTooley})')
    print("----------------------------")

    if max(List) == List[0]:
        print("Winner: Khan") 
    if max(List) == List[1]:
        print("Winner: Correy")
    if max(List) == List[2]:
        print("Winner: Li")
    if max(List) == List[3]:
        print("Winner: O\'Tooley")
