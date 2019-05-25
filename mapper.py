#!/usr/bin/env python3


import sys
import json

for line in sys.stdin:
	line = line.strip(); #removing leading and trailing whitespaces
    if not line:continue #checking if the line is blank before loading it as json
        tweet = json.loads(line) #reading in the given json file
		if not tweet.get('text'):continue
        word_list = {'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'}
        word_count = {}
        if not tweet['retweeted']:
            text = tweet['text'].lower()
            for eachword in word_list:
                if eachword in text:
                    print('%s\t%s' % (eachword, 1))
            print('%s\t%s' % ('unique',1))
