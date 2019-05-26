#!/usr/bin/env python3


import sys
import json
import re

for line in sys.stdin:
	if len(line.strip()) != 1:#checking for empty line with or without whitespaces
		try:
			#reading in the given json file
			tweet_line = json.loads(line)
		except:
			continue
		#declaring pronouns list
		pronoun_list = {'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'}
		if not tweet_line['retweeted']:#check for retweets
			text = tweet_line['text'].lower()#converting tweets to lower case
			for eachword in pronoun_list:#looping through pronouns list 
				if re.search(eachword,text):#searching for each pronoun in tweet text
					print('%s\t%s' % (eachword, 1))
			print('%s\t%s' % ('unique tweets count',1))
