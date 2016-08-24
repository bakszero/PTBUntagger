
from __future__ import print_function
import sys, re

with open(sys.argv[1], "r") as filestream:
	for line in filestream:
		array = re.findall('[\bA-Za-z,0-9\.]+/', line)
		for word in array:
			final=re.findall('[A-Za-z,0-9\.]+', word)
			for token in final:
				print (token, end=' ')

print ()
