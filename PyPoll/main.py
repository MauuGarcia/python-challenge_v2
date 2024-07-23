
import os
import csv

total_votes = 0
candidatesOp = []
candidateVotes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open("C:\\python-tets/election_data.csv") as csv_file:
    csvreader = csv.reader(csv_file)
    csv_header = next(csvreader)
    
    for a in csvreader:
        total_votes += 1
        candidate_name = a[2]
        
        if candidate_name not in candidatesOp:
            candidatesOp.append(candidate_name)
            candidateVotes[candidate_name] = 0
            
        candidateVotes[candidate_name] += 1

with open("C:\\python-tets/election_r.txt", "w") as txtfile:
    election_r = (
        f"\nElection Results\n"
        f"---------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------------------\n"
    )
    print(election_r, end='')
    txtfile.write(election_r)
    
    for candidate, votes in candidateVotes.items():
        vote_percentage = (votes / total_votes) * 100
        candidate_result = f"{candidate}: {vote_percentage:.1f}% ({votes})\n"
        print(candidate_result, end='')
        txtfile.write(candidate_result)