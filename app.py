from textblob import TextBlob

while True:
	sentence = raw_input("Please enter text: \n")
	text = TextBlob(sentence)
	print "Positivity: %s" % (text.sentiment.polarity)
	print "Objectivity: %s" % (text.sentiment.subjectivity)