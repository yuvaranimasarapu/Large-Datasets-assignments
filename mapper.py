#!/usr/bin/env python3


import sys
import json

for line in sys.stdin:
	#removing leading and trailing whitespaces
	line = line.strip()
	#checking if the line is blank before loading it as json
	if not line:continue #reading in the given json file 
		tweet = json.loads(line)
		if not tweet.get('text'):continue
			word_list = {'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'}
			word_count = {}
			if not tweet['retweeted']:
				text = tweet['text'].lower()
				for eachword in word_list:
					if eachword in text:
						print('%s\t%s' % (eachword, 1))
				print('%s\t%s' % ('unique',1))