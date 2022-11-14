
print("Election Results")
print("------------------------------------")

import os
import csv

csv_path = os.path.join('Resources_PyPoll','election_data.csv')

with open('election_data.csv' , 'r') as election_data:
    election_data_reader = csv.reader(election_data, delimiter=",")

    next(election_data_reader)

    election_data_list = list(election_data_reader)

Total_votes = len(election_data_list)
print("Total Votes:", Total_votes)

row_count_Charles = 0
row_count_Diana = 0
row_count_Raymon = 0

for row in election_data_list:
  if row[2] == "Charles Casper Stockham":
    row_count_Charles += 1
  elif row[2] == "Diana DeGette":
    row_count_Diana += 1
  elif row[2] == "Raymon Anthony Doane":
    row_count_Raymon += 1
    
print("Charles Casper Stockham:", row_count_Charles/Total_votes*100,"% (",row_count_Charles,")")
print("Diana DeGette:", row_count_Diana/Total_votes*100,"% (",row_count_Diana,")")
print("Raymon Anthony Doane:", row_count_Raymon/Total_votes*100,"% (",row_count_Raymon,")")
print("------------------------------------")

if row_count_Charles > row_count_Diana and row_count_Charles > row_count_Raymon:
  print("Winner: Charles Casper Stockham", )
elif row_count_Raymon > row_count_Charles and row_count_Raymon > row_count_Diana:
  print("Winner: Raymon Anthony Doane")
elif row_count_Diana > row_count_Charles and row_count_Diana > row_count_Raymon:
  print("Winner: Diana DeGette")







