'''
apa_record.py

Active-passive asynchronous method means that a voice sample is recorded
actively and then passively, and one of these modes is asynchronous.

In this case, we call a previous script aa_record.py with pa_record.py
to get the weather asynchronously and then record passively.

Note just one of these scripts needs to be asynchronous for the APA 
mode to take effect. Both can also be asynchronous and it would still
be an APA mode. 
'''
import os

# APA CONFIG 1 (AA → PA)
os.system('python3 aa_record.py')
os.system('python3 pa_record.py')

# APA CONFIG 2 (AS→ PA)
# os.system('python3 as_record.py')
# os.system('python3 pa_record.py')

# APA CONFIG 3 (AA→ PS)
# os.system('python3 aa_record.py')
# os.system('python3 ps_record.py')
