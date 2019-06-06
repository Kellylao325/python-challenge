import os
import csv

VoterID = []
County = []
Candidate = []

# csvpath = os.path.join("..", "Resources", "election_data.csv")
with open('../Resources/election_data.csv', newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    print("===========")

    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

    #find the candiates who received votes
    # ? create a list to hold candiate names if they have a vote
    Candidate_set = set(Candidate)
    # the length of the voter ID list = total votes
    Total_vote = len(VoterID)

    print(Candidate_set)
    print(Total_vote)
    print("===========")

    Names = []
    

    for row in Candidate_set:
        Names.append(row)

    print(Names)
    print(Names[0])
    print("===========")

    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {Total_vote}")
    print("--------------------")

    Candidate_Dicts = {}
    Candidate_count = 0
    for VoterID in Candidate:
        # Candidate_count = Candidate_count +1
        # Names = str(Names[Candidate_count])
        
        #need to count each person's votes
        votes = Names[0].count(VoterID)
        votes = int(votes)
    print(votes)
    # Candidate_TotalCount = votes + 1
    percentage = round(votes/Total_vote*100,3)
    # Candidate_Dicts.update({Names : votes})
    print(f'{Names}: {percentage}%  ({votes} votes)')
        

    
    print("--------------------")
    print('Winner: Khan')