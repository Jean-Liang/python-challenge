# Read budget data file
import os
import csv
budget_csv=os.path.join("..","Resources","election_data.csv")

# open and read csv
with open (budget_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

# Read the header row
    csv_header=next(csv_reader)

# Define the variables
# Use dictionary to count the candidate votes numbers
    total_votes=0
    candidate_counts ={}
    

# The total number of votes cast
    for row in csv_reader:
        total_votes+=1
        candidate=row[2]
# A complete list of candidates who received votes
# The total number of votes each candidate won
        if candidate in candidate_counts:
            candidate_counts[candidate]+=1
        else:
            candidate_counts[candidate]=1
  

# Print the final results as requested format
print(f"Election Results")
print("------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------")

# The percentage of votes each candidate won
# The percentage for each candidate is in below loop
for candidate,votes,in candidate_counts.items():
    vote_percentage=(votes/total_votes)*100
    print (f"{candidate}:{format(vote_percentage,'.3f')}% ({votes})")

print("------------------------------")
# The winner of the election based on popular vote
# Go  through the dictionary to find the winner who has the max vote
max_votes =0
winner =""

for candidate in candidate_counts:
    if candidate_counts[candidate]>max_votes:
        max_votes=candidate_counts[candidate]
        winner=candidate
print (f"Winner: {winner}")

print("------------------------------")

#create results as there is print inside of the loop,need create a list to bring all the results into one
results_list=[
"Election Results",
"------------------------------",
f"Total Votes: {total_votes}",
"------------------------------"]

for candidate,votes,in candidate_counts.items():
    vote_percentage=(votes/total_votes)*100
    results_list.append(f"{candidate}:{format(vote_percentage,'.3f')}% ({votes})")

results_list.append("------------------------------")

max_votes =0
winner =""
for candidate in candidate_counts:
    if candidate_counts[candidate]>max_votes:
        max_votes=candidate_counts[candidate]
        winner=candidate
results_list.append(f"Winner: {winner}")
results_list.append("------------------------------")

results="\n".join(results_list)

#create the output pathway in txt format
output_file=os.path.join("..","analysis","Election_results.txt")

with open(output_file,'w') as file:
   file.write(results)

print(results)