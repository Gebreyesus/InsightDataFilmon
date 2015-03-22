#Author: Filmon H. Gebreyesus
#Insight Data Engineering - Coding Challenge
#shell script to set proper permissions, load dependencies and run python
#March 21, 2015

#!/usr/bin/env bash

#loading dependency used for calculating median
sudo apt-get install python-numpy

#making sure all my python programs have proper permissions
chmod a+x word_count_median.py

#Execute my python program that does Word count and Running median
python word_count_median.py 


