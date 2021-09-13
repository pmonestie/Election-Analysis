#The data we need to retrieve
#1. The total number of votes cast.
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4 The total number of votes each candidate won
#5. The winnner of the election based on popular vote


import csv
import os
#Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes=0

#Candidate Options list
candidate_options = []

#Candidate votes dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candiare=""
winning_count=0
winning_percentage=0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        total_votes +=1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]+=1
    
#Determine the percentage of votes for each candidate by looping through the counts.
#1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate.
    votes=candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes)*100
    #To do: print out each candidate's name, vote count, and percentage of votes to the terminal

    #Determine winning vote count and candidate
    #Determine if the votes are greater than the winning count.
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        #2. If true then set winning_count=votes and winning_percent=
        #vote_percentage.
        winning_count=votes
        winning_percentage=vote_percentage
        #Set the winning_candiare equal to the candidate's name.
        winning_candidate=candidate_name
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)

    #Print each candidate's name, vote count, and percentage of votes 
    #votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


print(candidate_votes)