#1 Retrieve Data
#a Add our dependencies
import csv
import os
#b Assign a variable to load a file from a path
file_to_load = os.path.join("resources","election_results.csv")
#c Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#d Declare Variables
#Initialize total vote counter
total_votes = 0
#Candidate options
candidate_options = []
#Create Dictionary with each Candidate and their vote count
candidate_votes = {}
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#e Open the election results and read the file
with open(file_to_load) as election_data:

#2 read and analyze the data:
#a Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file
    for row in file_reader:
    #Add to the toal_votes count
        total_votes += 1
    #Print the candidate name from each row
        candidate_name = row[2]

    #Gathers Unique count of candidate names - keeps them from repeating endlessly
        if candidate_name not in candidate_options:

    #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
    #Create Key for candidate_votes dictionary - the key will be candidate_name. This will track each candidate's vote count
            candidate_votes[candidate_name] = 0
    #Increment the candidate_votes[candidate_name] variable. This will count up every time a candidate's name appears (not in if statement, but in for loop)
        candidate_votes[candidate_name] += 1


#Determine the percentage of votes for each candidate by looping through the counts
#1. Iterate through the candidate list
for candidate_name in candidate_votes:
    #2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes
    vote_percentage = float(votes)/float(total_votes)*100

    #Determine winning count and candidate
    #1. Determine if votes are greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2 If true then set winning_count = votes and winning_percent = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #3 Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

#Print out each candidate's name, vote count, and % of votes to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#Winning Candidate:
winning_candidate_summary = (f"--------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"------------------------\n")

print(winning_candidate_summary)


# Close File
election_data.close()

# Create a filename variable to a direct or indirect path to the file


#Using the open() function with the "w" mode we will write data to the file
# with open(file_to_save,"w") as txt_file:
#Write some data to the file
    # txt_file.write("Hello World ")
    # txt_file.write("\nCounties in the Election\n----------\nArapahoe\nDenver\nJefferson")

    # txt_file.close()
# 1. The total number of votes cast

# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

