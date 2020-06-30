#import os and csv file
import os

import csv

#find csv path
csvpath =os.path.join('..', 'PyPoll','Resources', 'election_data.csv')

#write to text
outputpath = os.path.join('..', 'PyPoll', 'Resources', 'results.txt')

results = open(outputpath, "w")

#print titles
print("Election Results")
results.write("Financial Analysis\n")
print("----------------------------")
results.write("----------------------------\n")

#loop
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   
    csvheader = next(csvfile)
    

    Total_Votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0

    #Calculate totals    
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

    #Calculate averages
    Average_Khan = round (Khan/Total_Votes *100, 3)
    Average_Correy = round (Correy/Total_Votes *100, 3)
    Average_Li = round (Li/Total_Votes *100, 3)
    Average_OTooley = round (OTooley/Total_Votes *100, 3)

    List = [Khan, Correy, Li, OTooley]
    
    #print totals
    print(f'Total Votes: {Total_Votes}')
    results.write(f"Total Votes: {Total_Votes}\n")
    print("----------------------------")
    results.write("----------------------------\n")
    print(f'Khan: {Average_Khan}% ({Khan})')
    results.write(f'Khan: {Average_Khan}% ({Khan})\n')
    print(f'Correy: {Average_Correy}% ({Correy})')
    results.write(f'Correy: {Average_Correy}% ({Correy})\n')
    print(f'Li: {Average_Li}% ({Li})')
    results.write(f'Li: {Average_Li}% ({Li})\n')
    print(f'O\'Tooley: {Average_OTooley}% ({OTooley})')
    results.write(f'O\'Tooley: {Average_OTooley}% ({OTooley})\n')
    print("----------------------------")
    results.write("----------------------------\n")

    #Find winner and print
    if max(List) == List[0]:
        print("Winner: Khan")
        results.write("Winner: Khan\n")
    if max(List) == List[1]:
        print("Winner: Correy")
        results.write("Winner: Correy\n")
    if max(List) == List[2]:
        print("Winner: Li")
        results.write("Winner: Li\n")
    if max(List) == List[3]:
        print("Winner: O\'Tooley")
        results.write("Winner: O\'Tooley\n")