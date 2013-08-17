# Mikael Trieb 2013-08-15

import os
import sys

# Description: 
# This script reads a text file with names, one name per row. 
# For each row, a function is called with the name as input argument.
# A parameter 'number_of_rows_to_process' specifies how any rows should be processed
# each time the script is called. 
# The last processed row is written to a file to be able to start processing on right place next time. 
# To start from beginning, write the number 0 on the first row in the file 'last_row_index.txt'

# Specify the number of row to process each time this script is called
number_of_rows_to_process = 2;

# Open file to read last row index 
f_last = open(r'last_row_index.txt','r')
last_row_string = f_last.readline()
f_last.close()

# Initialize counters
last_row    = int(last_row_string)
current_row = 1
count       = 0   # Related to number_of_rows_to_process
	

def collect_tweets(user):
	# Do something clever with the user.. call twitter API etc.. 
	print 'Processing user: %s' %user
	# 1) Get tweets
	# 2) Save to file
	

# Open file with user users
f_names = open(r'names.txt','r')
for user in f_names:
	# current_row is a help variable to hold the index in the list
	if current_row > last_row:
		# Do something with the current user:
		collect_tweets(user)
		# Increase the counter that counts processed rows 
		count = count + 1  
		# Check if number_of_rows_to_process have been reached.  
		if count == number_of_rows_to_process:
			break
	current_row = current_row + 1

f_names.close()

# Increase last_row 
last_row = int(last_row_string) + count
print 'Last row was: %s' % last_row


# Open file to write back last row index
f_last = open(r'last_row_index.txt','w')
last_row_string = '%s' % last_row
f_last.write(last_row_string)
f_last.close()