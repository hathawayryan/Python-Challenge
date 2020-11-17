import os
import csv

csvpath = os.path.join('resources', 'PyPoll.csv')




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    total_votes = 0
    candadits = {}
    
    for row in csvreader:
        if row[2] in candadits:
            candadits[row[2]] = candadits[row[2]] + 1
        else:
            new_candadit = {row[2] : 1}
            candadits.update(new_candadit)

        total_votes += 1    
        
    
    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------------")
    
    winner = 0
    final = []
    x = 0

    for candadit in candadits:
        percent_votes = round(candadits[candadit] / total_votes * 100, 3)
        final.append(f"{candadit}: {percent_votes}% ({candadits[candadit]})")
        print(final[x])
        if winner == 0:
            winner = candadit
        elif candadits[candadit] > candadits[winner]:
            winner = candadit
        x += 1


    print("------------------------------")
    print(f"Winner: {winner}")
    print("------------------------------")

output_file = os.path.join("Analysis", "PyPoll_Analysis.txt")

writer =  open(output_file, 'w')

writer.write("Election Results\n")
writer.write("------------------------------\n")
writer.write(f"Total Votes: {total_votes}\n")
writer.write("------------------------------\n")

for candadit in final:
    writer.write(f"{candadit}\n")

writer.write("------------------------------\n")
writer.write(f"Winner: {winner}\n")
writer.write("------------------------------\n")


