
print("Election Results")
print("------------------------------------")

import os
import csv

csv_path = os.path.join('Resources_PyPoll','election_data.csv')

with open(csv_path, 'r') as election_data:
    election_data_reader = csv.reader(election_data, delimiter=",")

    next(election_data_reader)

    election_data_list = list(election_data_reader)

Total_votes = len(election_data_list)
print("Total Votes:", Total_votes)

row_count_1 = 0
row_count_2 = 0
row_count_3 = 0

for row in election_data_list:
  candidate1 = "Charles Casper Stockham"
  candidate2 = "Diana DeGette"
  candidate3 = "Raymon Anthony Doane"
  if row[2] == candidate1:
    row_count_1 += 1
  elif row[2] == candidate2:
    row_count_2 += 1
  elif row[2] == candidate3:
    row_count_3 += 1
    
print("Charles Casper Stockham:", row_count_1/Total_votes*100,"% (",row_count_1,")")
print("Diana DeGette:", row_count_2/Total_votes*100,"% (",row_count_2,")")
print("Raymon Anthony Doane:", row_count_3/Total_votes*100,"% (",row_count_3,")")
print("------------------------------------")

if row_count_1 > row_count_2 and row_count_1 > row_count_3:
  print("Winner:" + candidate1 )
elif row_count_3 > row_count_1 and row_count_3 > row_count_2:
  print("Winner:" + candidate3)
elif row_count_2 > row_count_1 and row_count_2 > row_count_3:
  print("Winner:" + candidate2)

with open('Analysis_Result_Pypoll.txt','w') as text:
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write(f"Total Votes: {Total_votes}\n")
    text.write(f"Charles Casper Stockham: {row_count_1/Total_votes*100}% ({row_count_1})\n")
    text.write(f"Diana DeGette: {row_count_2/Total_votes*100}% ({row_count_2})\n")
    text.write(f"Raymond Anthony Doane: {row_count_3/Total_votes*100}% ({row_count_3})\n")
    text.write('-------------------------\n')
    text.write(f"Winner: {candidate2}")







