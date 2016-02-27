def happy_birthday():
    print "Good day. What is your name?"
    name = raw_input("Type your name and hit 'Enter'.")
    print "Is today your birthday?"
    answer = raw_input("Type yes or no and hit 'Enter'.").lower()
    if answer == "yes" or answer == "y":
        print "Happy birthday,",name + "!"
    elif answer == "no" or answer == "n":
        print "Have a good day,",name + "!"
    else:
        print "You didn't pick yes or no! Try again."
        happy_birthday()

happy_birthday()

