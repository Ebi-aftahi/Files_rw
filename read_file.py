# Write a program that first reads in the name of an input file, followed by two strings representing the lower and upper bounds of a search range. The file should be read using the file.readlines() method. The input file contains a list of alphabetical, ten-letter strings, each on a separate line. Your program should output all strings from the list that are within that range (inclusive of the bounds).

import os
import sys

file_name = input();
str_1 = input();
str_2 = input();

if not os.path.exists(file_name):   # Make sure file exists
    print('File does not exist.')
    sys.exit(1)                     # 1 indicates error

with open(file_name) as myfile:
    lines = myfile.readlines()      # Returns lines in a list


for i in range(len(lines)):         # Deletes the '\n' from end
    lines[i] = lines[i][:-1]

lower = 0
while str_1 > lines[lower]:        
        lower += 1


upper = len(lines)-1
while str_2 < lines[upper]:
    upper -= 1    
        

for i in range(lower, upper + 1):
    print(lines[i])

