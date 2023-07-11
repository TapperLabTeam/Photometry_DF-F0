# Photometry_Signal_Processor
Calculates DF/F0 from demodulated 465 and 405 nm channels collected from fiber photometry system. Developed for use with Doric Neuroscience Studio 5.4.1.23.

Instructions:
1. Create an "input_folder" and "output_folde"r and update their file paths in "signal_check_wrap.py" to match your directories.
2. Update the file path for "signal_udfs.py" in "signal_check_wrap.py."
3. Copy .csv file from Doric Neuroscience Studio into the "input_folder."
4. The Doric .csv files are structued thusly: row 1 = column titles, column 1 = timestamps, column 2 = 465 nm channel, column 3 = 405 nm channel, column 4 = binary TTL states.
5. Run signal_check_wrap.py to execute the program.

Notes:
Default Filter = 3 Hz lowpass butterworth filter for 465 and 405nm channels. The parameters of this filter should be modified in "signal_check.py" to match your sampling rate.
