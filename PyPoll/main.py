# Dependencies
import os
import csv

# Set file path
csvpath = os.path.join('Resources', 'election_data.csv')

# Set variables
unique_votes = set()
names = []
candidate_votes_list = []

# Open CSV file in both reader and dictionary
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    dictreader = csv.DictReader(csvfile)

    # Skip header row
    header = next(csvreader)

    # Dictionary
    candidate_votes = {}

    # Set loop
    for row in csvreader:
        # Count amount of votes
        # Code help from Xpert
        vote_count = row[0]
        vote = vote_count.split(',')[0]
        unique_votes.add(vote)

        # Create list of candidates
        name = row[2]
        if name not in names:
            names.append(name)
        
        # Find candidate votes
        # Code help from Xpert
        candidate = row[2]

        if candidate in candidate_votes:
                candidate_votes[candidate] += 1
        else:
             candidate_votes[candidate] = 1

    # Create list from dictionary to pull from
    candidate_votes_list = list(candidate_votes.items())

    # Find percentages
    candidate1_votes = int(candidate_votes_list[0][1])
    candidate2_votes = int(candidate_votes_list[1][1])
    candidate3_votes = int(candidate_votes_list[2][1])

    # Create a tuple that compares greatest value of votes in the Candidate Vote list
    # Code from Xpert
    winner = max(candidate_votes_list, key=lambda x: x[1])

# Count amount of total votes       
total_votes = int(len(unique_votes))

# Calculate percentages
candidate1_percentage = round(((candidate1_votes / total_votes) * 100), 3)
candidate2_percentage = round(((candidate2_votes / total_votes) * 100), 3)
candidate3_percentage = round(((candidate3_votes / total_votes) * 100), 3)

# Print in Terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{names[0]}: {candidate1_percentage}% ({candidate1_votes})")
print(f"{names[1]}: {candidate2_percentage}% ({candidate2_votes})")
print(f"{names[2]}: {candidate3_percentage}% ({candidate3_votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")

# Print in text file
with open("analysis/analysis.txt", "w") as file:
     file.write("Election Results\n" +
                "-------------------------" + "\n" +
                "Total Votes: " + str(total_votes) + "\n" +
                "-------------------------" + "\n" +
                str(names[0]) + ": " + str(candidate1_percentage) + "% (" + str(candidate1_votes) + ")" + "\n" +
                str(names[1]) + ": " + str(candidate2_percentage) + "% (" + str(candidate2_votes) + ")" + "\n" +
                str(names[2]) + ": " + str(candidate3_percentage) + "% (" + str(candidate3_votes) + ")" + "\n" +
                "-------------------------" + "\n" +
                "Winner: " + str(winner[0]) + "\n" +
                "-------------------------" + "\n")