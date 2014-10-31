__author__ = 'Ray'

#I got so into this trying to figure out the averagae word count per sentence I didn't realize until Bryan mentioned it
#avgerage character length.... Anyways here is what I have thus far.

count = []
with open("C:\Users\Ray\Desktop\School\python\Lab5\shunned_house.txt") as r:
    text = r.read()
    sentences = text.split(".")
    for sent in sentences:
        words = sent.split(" ")
        count.append(len(words))

        average = (sum(count)/len(count))

    #print "The number of words per sentence is: ",count
    print "The avaerage number of words per sentence is: ",average
    print words

raw_input("press enter:")