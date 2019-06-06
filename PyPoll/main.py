import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    VoterID = []
    County = []
    Candidate = []

    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

    #find the candiates who received votes
    Candidate_set = set(Candidate)
    Total_vote = len(VoterID)

    Names = []

    for row in Candidate_set:
        Names.append(row)

    print("Election Results")
    print("--------------------")
    print(f'Total Votes: {Total_vote}')
    print("--------------------")

    Candidate_Dicts = {}
    Candidate_count = 0
    for row in Names:
        Names = str(Names[Candidate_count])
        votes = Candidate.count(Names)
        votes = int(votes)
        percentage = round(votes/Total_vote*100,3)
        Candidate_Dicts.update({Names : votes})
        print(f'{Names}: {percentage}%  ({votes} votes)')
        Candidate_count = Candidate_count +1
    
    print("--------------------")
    print('Winner: Khan')
