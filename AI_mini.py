def AI():
    name = input ("Type In Your Name In Quotation Marks")
    print "Well, Hello "  +  name 
    lastname = input ("Type In Your Last Name In Quotation Marks")
    print "Hello, "  +  name    +  "  "  +   lastname
    goodsosobad = input ("How Are You Today,Please type Good Or Bad Or Soso please print in lowercase letters and quotation marks!")
    if goodsosobad == "good":
        print "I am happy too!" 
    elif goodsosobad == "soso":
        print "At Least That's Better Than Bad!"
    elif goodsosobad == "bad":
        print "I Hope You Will Have Fun Next Time!"
    else:
        print  "Huh, "  +   name  +  " I don't understand!"
    sadhappy = input ("Are You Sad Or Happy, please type sad or happy. Please print in lowercase letters and quotation marks!")
    if sadhappy == "sad":
        print ("I am sad that you are sad " + name + " WAAAWAAAWAAA!")
    elif sadhappy == "happy":
        "I am happy that you are happy " + name
    else:
         print  "Huh, "  +   name  +  " I don't understand
