# Photometry_Signal_Processor
Calculates DF/F0 from demodulated 465 and 405 nm channels collected from fiber photometry system.

Notes:
Run signal_check_wrap.py to execute the program.
You must create an input_folder and output_folder and update their file paths in signal_check_wrap.py.
You must update the file path to signal_udfs.py in signal_check_wrap.py

Default Filter: The code is set to apply a 3 Hz lowpass butterworth filter to 465 and 405nm channels. The parameters of this filter should be modified in signal_check.py to fit your data.
