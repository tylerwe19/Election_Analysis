my_votes = int(input('How many votes did you get in the election?'))
total_votes = int(input('What is the total votes in the election?'))
percentage_votes = (my_votes/total_votes) * 100
print(f"I received {percentage_votes}% of the total votes.")

message_to_candidate = (
    f"You received {my_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {percentage_votes:.2f}% of total votes.")

print(message_to_candidate)    
