import csv
import sys
import os

file_name = input();

if not os.path.exists(file_name):   					# Make sure file exists
    print('File does not exist!')
    sys.exit(1)                     					# 1 indicates error

with open(file_name) as myfile:
    lines = myfile.readlines()      					# Returns lines in a list
    
for i in range(len(lines)):         					# Deletes the '\n' from end
	lines[i] = lines[i][:-1]

my_dict = {}
for i in range(0, len(lines), 2):
	if lines[i] not in my_dict:
		my_dict[lines[i]] = [lines[i+1]]
	else:
		my_dict[lines[i]].append(lines[i+1])
		
with open('output_keys.txt', 'w') as file_write:		# Writes to file output_keys.txt, ordered by keys, in the requested format
	for key in sorted(my_dict):
		file_write.write("{}: ".format(int(key)))
		for i in range(len(my_dict[key])):
			if i > 0:
				file_write.write("; {}".format(my_dict[key][i]))
			else:
				file_write.write("{}".format(my_dict[key][i]))
		file_write.write("\n")			

sorted_list = []										# converts the values to a sorted list then write to file!
for key in my_dict:
	for i in range(len(my_dict[key])):
		sorted_list.append(my_dict[key][i])
		
sorted_list.sort();

with open('output_titles.txt', 'w') as sorted_file:
	for i in range(len(sorted_list)):
		sorted_file.write("{}\n".format(sorted_list[i]))

	
