# Assign a variable for the file to load and the path.
#file_to_load = 'C:\\Users\\roark\\OneDrive\\Desktop\\Election_Analysis\\Resources\\election_results.csv'



# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Close the file.
election_data.close()

# Assign a variable for the file to load and the path.
#file_to_load = 'C:\\Users\\roark\\OneDrive\\Desktop\\Election_Analysis\\Resources\\election_results.csv'

import csv
import os

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


