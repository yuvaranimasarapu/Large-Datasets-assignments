#!/usr/bin/env python3


import sys
import json

for line in sys.stdin:
	if len(line) != 1:
		try:
			line = line.strip()
			tweets = json.loads(line)
		except:
			continue
		check_word = {'DEN', 'DET', 'DENNA', 'DENNE', 'HAN', 'HON', 'HEN'}
		tweets_text = tweets['text']
		if not tweets['retweeted']:
			for word in check_word:
				if word in tweets_text.upper():
					print('%s\t%s' % (word, 1))
			print('%s\t%s' % ('unique_count',1))
