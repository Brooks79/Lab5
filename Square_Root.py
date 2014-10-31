__author__ = 'Ray'

#after the class i realized this is not what you wanted, and yes I know using to the power of .5 is the same thing as
#square root, but the amount of time I spent trying to get this to work is far more than you probably think I should be
#spending.
while True:
    Q1 = raw_input("Please choose a number that you would like to know the square root of: ")
    print ("\n")
    x = float(Q1)

    if x >= 0.0:

        y = (x **(0.5))

        print "The answer is: ",y
        print ("\n")
    else:
        y = (abs(x) **(0.5))

        print "The answer is:",y,"i"
        print ("\n")
