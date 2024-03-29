# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Resources", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
votes = 0

# 1: Create a county list and county votes dictionary.
counties = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
turnoutcounty = ""
turnoutcountycount = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.

        if county_name not in counties:

            # 4b: Add the existing county to the list of counties.

            counties.append(county_name)
            
            # 4c: Begin tracking the county's vote count.

            county_votes[county_name] = 0
                    
        # 5: Add a vote to that county's vote count.

        county_votes[county_name] += 1
    next

    
# Print the final vote count (to terminal)
election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
print(election_results, end="")

# Save the results to our text file.
with open(file_to_save, "a") as txt_file:
    txt_file.write(election_results)
    txt_file.close()
    # 6a: Write a for loop to get the county from the county dictionary.


for county_name in counties:
        # 6b: Retrieve the county vote count.
    votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
    percentage = float(votes) / float(total_votes) * 100.0

         # 6d: Print the county results to the terminal.

    print(county_name + " County: " + str(county_votes[county_name]) + " votes (" + myformat.format(percentage) + "%) \n")
    myformat = "{0:.1f}"
         # 6e: Save the county votes to a text file.
    with open(file_to_save, "a") as txt_file:
        txt_file.write(county_name + " County: " + myformat.format(percentage) + "% \n")
        txt_file.close()
         # 6f: Write an if statement to determine the winning county and get its vote count.
    if county_votes[county_name] == max(county_votes.values()):
            turnoutcounty = county_name 
            turnoutcountycount = county_votes[county_name]
next 

    # 7: Print the county with the largest turnout to the terminal.
print(str(turnoutcounty) + " County had the highest turnout. (" + str(turnoutcountycount) + " votes) \n")

    # 8: Save the county with the largest turnout to a text file.
with open(file_to_save, "a") as txt_file:
    txt_file.write(str(turnoutcounty) + " County had the highest turnout. (" + str(turnoutcountycount) + " votes) \n")
    txt_file.close()
    # Save the final candidate vote count to the text file.

for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the
        # terminal.
    print(candidate_results)
        #  Save the candidate results to our text file.
    with open(file_to_save, "a") as txt_file:
        txt_file.write(candidate_results)
        txt_file.close()
        # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
next
    # Print the winning candidate (to terminal)
winning_candidate_summary = (
    f"-------Final-Results-----\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
with open(file_to_save, "a") as txt_file:
    txt_file.write(winning_candidate_summary)
    txt_file.close()
