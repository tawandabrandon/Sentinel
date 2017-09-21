import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from textblob import TextBlob

while True:
	sentence = raw_input("Please enter text: \n")
	text = TextBlob(sentence)
	tags = text.noun_phrases
	names = []
	for x in tags:
		names.append(x)

	print "Found names: \n"
	for x in names:
		print x + '\n'