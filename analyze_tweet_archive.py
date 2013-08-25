#!/usr/bin/env python
#-*- coding: utf-8 -*-

import word_counter
import csv

def analyze_tweet_archive(csvfile):
	"""Load a CSV-formatted tweet-archive file (see: https://blog.twitter.com/2012/your-twitter-archive) into the mindalyzer for analysis.""" 
	fil1 = 'beige.ordlista'
	fil2 = 'purple.ordlista'
	fil3 = 'red.ordlista'
	fil4 = 'blue.ordlista'
	fil5 = 'orange.ordlista'
	fil6 = 'green.ordlista'
	dictofwlsets = {fil1: makeset(fil1), fil2: makeset(fil2), fil3: makeset(fil3), fil4: makeset(fil4), fil5: makeset(fil5), fil6: makeset(fil6)}
	
	mytweettext = []
	
	with open(csvfile, 'r') as f:
		csvdata = csv.reader(f, delimiter=",")
		for row in csvdata:
			mytweettext = row[7]
			counters = countwords(mytweettext, dictofwlsets, counters)
			
			#count up totwords
			for word in mytweettext.split():
				counters['totwords'] += 1
	return counters

def main():
     analyze_tweet_archive(csvfile)
     print(counters)

if __main__ == "__main__":
     main()

