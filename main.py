print "let us get started!"
spy_name =raw_input("Provide your name here: ")
if len(spy_name)> 0:
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_salutation = raw_input("What should we call you Me. or Ms?")
    spy_age = int(raw_input("Enter your age here: "))
    if spy_age > 12 and spy_age < 60:
        print "You are good to go."
        spy_rating = raw_input("Enter your rating here: ")
        if spy_rating > 4.5:
            print "good"
        elif spy_rating > 3.5 and spy_rating <=4.5:
            print "excellent"
        elif spy_rating >=2.5 and spy_rating <=3.5:
            print "you can do better"
        else:
            print "need improvement"
        spy_is_online = True
        print "Authentication Completed. Welcome" + spy_name + "age:" + str(spy_age ) + "and rating of: " + str(spy_rating) + "proud to have you."

    else:
        print "You are not a valid user."

    spy_name = spy_salutation +  " " + spy_name
    print 'Welcome' + spy_name + ' Glad to have you back with us. '
    print  "Alright " + spy_name + " I would like to know more about you. "
else:
    print "A spy needs to have valid name.Try again. "
