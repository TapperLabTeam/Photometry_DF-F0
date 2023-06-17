import sys
import numpy as np
sys.path.append(sys.argv[3])
from signal_udfs import lowpass
import matplotlib.pyplot as plt
import pickle

input_file = sys.argv[1]
output_handle = sys.argv[2]

#Import photometry data from Doric .csv file
time = []
gcamp_channel = []
control_channel = []
ttl_channel = []

for line_num, line in enumerate(open(input_file)):
	line = line.strip().split(',')
	if line_num >= 2 and line[1] != '':
		time.append(float(line[0]))
		gcamp_channel.append(float(line[1]))
		control_channel.append(float(line[2]))
		if line[4] == '0.5': #Sometimes TTL from fear chamber reads 0.5 in the ON state.
			ttl_channel.append(1)
		else:
			ttl_channel.append(int(line[4]))

#3 Hz Butterwort lowpass filter channels
gcamp_channel_filt = lowpass(gcamp_channel, 3, 234, 2)
control_channel_filt = lowpass(control_channel, 3, 234, 2)

#Fit the control channel to the gcamp channel
line_fit = np.polyfit(control_channel_filt, gcamp_channel_filt, 1)

a = line_fit[0]
b = line_fit[1]

control_fit = a * control_channel_filt + b

#Calculate DF/F0
norm_dat = (gcamp_channel_filt - control_fit) / control_fit
norm_dat = norm_dat * 100

#Output block
df_f_output = open(output_handle + '_df-f0.csv','w')
title_line = ['Time (s)', '465nm', '405nm', '405nm Fitted', 'DF/F0', 'TTL']

df_f_output.write(','.join(title_line)+'\n')

for item_num, item in enumerate(time):
	current_line = []
	current_line.append(str(item))
	current_line.append(str(gcamp_channel_filt[item_num]))
	current_line.append(str(control_channel_filt[item_num]))
	current_line.append(str(control_fit[item_num]))
	current_line.append(str(norm_dat[item_num]))
	current_line.append(str(ttl_channel[item_num]))
	df_f_output.write(','.join(current_line) + '\n')
	
#Plot DF/F0 and save figure
plt.plot(time,norm_dat)
plt.xlabel('Time (s)')
plt.ylabel('DF/F0')
plt.savefig(output_handle[:-4] + '_df-f0.png')
plt.close()

#Plot and save 465nm and fitted 405nm channels
plt.plot(time, control_fit, label = '405nm Fit')
plt.plot(time, gcamp_channel_filt, label = '465nm')
plt.xlabel('Time (s)')
plt.ylabel('Volts')
plt.legend(bbox_to_anchor=(1.02,1), loc="upper left")
plt.savefig(output_handle[:-4] + '_channels.png', bbox_inches = 'tight')
plt.close()

#Pickle base data
pickle.dump(time,open('time.pkl','wb'))
pickle.dump(norm_dat,open('df-f.pkl','wb'))
pickle.dump(ttl_channel,open('ttl.pkl','wb'))
