import os
import subprocess

#OPTIONS
input_folder = 'C:/Users/Tim/Documents/Python/Signal_Check/input_folder/'
output_folder = 'C:/Users/Tim/Documents/Python/Signal_Check/output_folder/'
udf_path = 'C:/Users/Tim/Documents/Python/UDFs'

#Collect list of file names for processing
input_files = []
for file_name in os.listdir(input_folder):
	input_files.append(file_name)
	
#Main processing loop
for file_name in input_files:
	input_handle = input_folder + file_name
	output_handle = output_folder + file_name
	print('Processing: ' + file_name  + '...')
	subprocess.call(['python', 'signal_check.py', input_handle, output_handle, udf_path])
	
print('Done')
