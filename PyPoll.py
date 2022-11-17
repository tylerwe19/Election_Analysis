# #The data we need to retrieve.
#Add our dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("resources","election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

# read and analyze the data:
# Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)



#Print each row in the CSV file
    #for row in file_reader:
        #print(row)



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

