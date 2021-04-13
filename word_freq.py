import csv
import sys
import os

file_name = input();

if not os.path.exists(file_name):   					# Make sure file exists
    print('File does not exist!')
    sys.exit(1)                     					# 1 indicates error

items_set = []

with open(file_name, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')      # Returns lines in a list

	
    for row in csv_reader: 
        [items_set.append(item) for item in row if item not in items_set]
        
#    print(row)
#    print(items_set)
    
    for item in items_set:
    	print('{} {}'.format(item, row.count(item)))


# better method:
#   for row in csv_reader: 
#        items_set = set(row)
# or
##   for row in csv_reader: 
#        items_list = list(set(row))
