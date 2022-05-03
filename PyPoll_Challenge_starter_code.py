# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os
#from turtle import update


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load,'r') as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(election_data)
    print(headers)

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
#candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_votes = {}

#Open election results and read the file 
with open(file_to_load,'r') as election_data: 
    csvreader = csv.reader(election_data) 
        #Loop through election data  
    headers = next(csvreader)
    for row in (csvreader):
        if row == 0: 
            print(['Ballot','County','Canidate']) 
        if row[2] in candidate_votes: 
            candidate_votes[row[2]] +=1 
        else: 
            candidate_votes[row[2]] = 1 
        total_votes +=1 
    # Track the winning candidate, vote count and percentage
    winning_candidate = None
    winning_count = None
    winning_percentage = 0
    for entry in candidate_votes.items(): 
        if winning_candidate is None or entry[1] > winning_count: 
            winning_candidate= entry[0] 
            winning_count= entry[1] 
    winning_percentage = (winning_count/total_votes)*100

# 2: Track the largest county and county voter turnout. 
with open(file_to_load,'r') as election_data: 
    csvreader = csv.reader(election_data) 
        #Loop through election data  
    headers = next(csvreader)
    for row in (csvreader):
        if row == 0: 
            print(['Ballot','County','Canidate']) 
        if row[1] in county_votes: 
            county_votes[row[1]] +=1 
        else: 
            county_votes[row[1]] = 1 

    #Track the winning county
    winning_county = None
    winning_count_county = None
    for entry in county_votes.items(): 
        if winning_county is None or entry[1] > winning_count_county: 
            winning_county= entry[0] 
            winning_count_county= entry[1] 

# Save the results to our text file.
with open('election_results.csv', "w") as f:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    f.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    #This is whre I left off
    for key,value in county_votes.items(): 
        p = value/total_votes *100 
        m = f"{key}:{p:.1f}% ({value})\n" 
        print(m,end="") 
        f.write(m)
        # 6b: Retrieve the county vote count.
        #votes=county_votes.get(county_votes)
        # 6c: Calculate the percentage of votes for the county.
        #vote_percentage = float(votes) / float(total_votes) * 100
         # 6d: Print the county results to the terminal.
        #print(votes, end="")
         # 6e: Save the county votes to a text file.
        #txt_file.write(votes)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        #if (votes > winning_county) and (vote_percentage > winning_c_percentage):
           # winning_county = votes
          #  winning_c_candidate = c
         #   winning_c_percentage = vote_percentage
        #Finished here
    # 7: Print the county with the largest turnout to the terminal. 
        f"n\--------------------\n"
        m=f"Largest County Turnout: {winning_county}"
    # 8: Save the county with the largest turnout to a text file.


    # Save the final candidate vote count to the text file.
    for key,value in candidate_votes.items(): 
        p = value/total_votes *100 
        m = f"{key}:{p:.1f}% ({value})\n" 
        print(m,end="") 
        f.write(m)
        # Retrieve vote count and percentage
        #vote_percentage = float(votes) / float(total_votes) * 100
        #candidate_results = (
        #    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        
        #  Save the candidate results to our text file.
        #txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        #if (votes > winning_count) and (vote_percentage > winning_percentage):
        ###  winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
     
    # Save the winning candidate's name to the text file
    f.write(winning_candidate_summary)
