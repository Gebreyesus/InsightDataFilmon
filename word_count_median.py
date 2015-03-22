#Author: Filmon H. Gebreyesus
#Insight Data Engineering - Coding Challenge
#Word count and Running median program with Python
#March 21, 2015

#!/usr/bin/python

#os for operating system dependent functionality (getting path to current dir) 
#and numpy is a package used for statistics (median)
import os
import numpy

wordsCount=dict()    #dictionary to count frequency of words
lst=list()           #list to save word count of each line
lineWordsCount=0     #initialized to count word count of each line
punctuation="!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"  #reference used to strip punctuation from each line
fileInputPath=os.path.dirname(os.path.realpath(__file__))+"/wc_input"  #gives path to the current working directory + input directory

files=os.listdir(fileInputPath)   #lists files in the input directory (wc_input)
files=sorted(files)		  #sorts file names in the input directory (wc_input) alphabetically

countOut = open("wc_output/"+"wc_result.txt", "w")    #opens file for writing output to word count result
medianOut = open("wc_output/"+"med_result.txt", "w")  #opens file for writing output to running median result

#for each file in file name lists reads through each one of them
#removes punctuation from that line
#splits each line into words and converts them to lower case
#counts number of words in each line (for running median)
#also counts frequency of each word in dictionary in the format of ('word':1)
#calculates median after each line 
for fileName in files:
	try:
		#open file stream for reading
		fInput = open("wc_input/"+fileName, "r")
	except IOError:
		print "There is an error reading file name", fileName
		sys.exit()
	line=fInput.readline()  #read line
	line=line.translate(None,punctuation) #remove punctuation
	while line:   
		words=line.split()  #split line to words
		for word in words:
			word=word.lower()  #change to lower case
			lineWordsCount+=1  #count number of words in each line
			if word in wordsCount:
				wordsCount[word]+=1  #counts frequency of words
			else:
				wordsCount[word]=1   
		lst.append(lineWordsCount)           #save number of words in each line to list
		lineWordsCount=0		     #reset the word count after saving to list
		medianOut.write(str(numpy.median(numpy.array(lst)))+"\n") #get median of the current list
		line=fInput.readline()   #read more lines in loop
		line=line.translate(None,punctuation)  #remove punctuation

	fInput.close() #close each file in the input directory

sortedWords=sorted(wordsCount)  #sorts words in the dictionary to list
#print sortedWords and its frequency to file
for word in sortedWords:
	countOut.write("{:<16}{:<}\n".format(word,`wordsCount[word]`))

countOut.close()   #close file to word count
medianOut.close()  #close file to running median

