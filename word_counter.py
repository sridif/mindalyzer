#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
mindalyzer.py

Initiated by a lazy programmer and  Mattias Östmar.
"""


import re
import csv

def load_tweet_archive(csvfile):
	"""Load a CSV-formatted tweet-archive file (see: https://blog.twitter.com/2012/your-twitter-archive) into the mindalyzer for analysis.""" 
	mytweettext = []
	fil1 = 'beige.ordlista'
	fil2 = 'purple.ordlista'
	fil3 = 'red.ordlista'
	fil4 = 'blue.ordlista'
	fil5 = 'orange.ordlista'
	fil6 = 'green.ordlista'
	dictofwlsets = {fil1: makeset(fil1), fil2: makeset(fil2), fil3: makeset(fil3), fil4: makeset(fil4), fil5: makeset(fil5), fil6: makeset(fil6)}

	counters = {}	
	with open(csvfile, 'r') as f:
		csvdata = csv.reader(f, delimiter=",")
		for row in csvdata:
			mytweettext = row[7]
			counters = countwords(mytweettext, dictofwlsets, counters)
	return counters

def load_aggregated_tsv_file(tsvfile):
        """Load a TSV-formatted tweetfile with from_user, to_user and tweet text"""
        mytweettext = []
        fil1 = 'beige.ordlista'
        fil2 = 'orange.ordlista'
        fil3 = 'green.ordlista'
        dictofwlsets = {fil1: makeset(fil1), fil2: makeset(fil2), fil3: makeset(fil3)}

        counters = {}
        with open(tsvfile, 'r') as f:
                tsvdata = csv.reader(f, delimiter="\t")
                for row in tsvdata:
                        mytweettext = row[2]
                        counters = countwords(mytweettext, dictofwlsets, counters)
        return counters
	

def makeset(filename):
    """Load list of words and phrases from a file."""

    ourlist = []
    with open(filename, 'r') as f:
        for line in f:
            ourlist.append(line.strip().lower())
    return set(ourlist)        



def phrasecombinations(words):
	"""Make phrase combinations of the list of words, that includes single words also"""

	if len(words) < 2:
		return words

	phrases = []
	for startwordnum in range(0, len(words)):
		for numofwordsincombo in range(1, len(words) - startwordnum + 1):
			#print words[startwordnum:startwordnum + numofwordsincombo]
			thesentence = listofwordstosentence(words[startwordnum:startwordnum + numofwordsincombo])
			phrases.append(thesentence)
	return phrases

def listofwordstosentence(words):
	"""Conver a list of strings to a string, strip the result."""
	mystr = ""
	for w in words:
		mystr = mystr + ' ' + w
	return mystr.strip()

def splitwords(text):
	"""Split text into words. strip !#€ and others, allow 0-9, make lower case, ok?"""

	splitted = re.split('[^a-zA-ZåäöÅÄÖ0-9]+', text)
	words = []
	for w in splitted:
		if re.match('^[a-zA-ZåäöÅÄÖ0-9]+$', w):
			words.append(w.lower())			
	return words
	

def countwords(text, wordlistsdict, counters):
	"""Any word/phrase matching wordlistsets, give an empty dict {} as counters unless you want to add prev results"""
	words = phrasecombinations(splitwords(text))
	# @todo:remember use the phrasecombiner!!! also.
	wlkeys = wordlistsdict.keys()

	for w in words:        
		for wlistkey in wlkeys:
			print("checking: \"" + w + "\" " + wlistkey)
			if w in wordlistsdict[wlistkey]:
				print("dbg hit: " + w + ", in " + wlistkey)
				if wlistkey in counters:
					print("dbg hit in if: \"" + w + "\", in " + wlistkey)
					counters[wlistkey] = counters[wlistkey] + 1
				else:
					print("dbg hit in else: \"" + w + "\", in " + wlistkey)
					counters[wlistkey] = 1
	return counters



def main():
	fil1 = 'beige.ordlista'
        fil2 = 'purple.ordlista'
        fil3 = 'red.ordlista'
        fil4 = 'blue.ordlista'
        fil5 = 'orange.ordlista'
        fil6 = 'green.ordlista'
        dictofwlsets = {fil1: makeset(fil1), fil2: makeset(fil2), fil3: makeset(fil3), fil4: makeset(fil4), fil5: makeset(fil5), fil6: makeset(fil6)}
	counters = {}
	
### mytweettext = "David Hall is a very nice guy. svenska ord: grymt snäll och kunnig."
	results = countwords(mytweettext, dictofwlsets, counters)
	
	print(results)
	

    
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()
