youguess = False
numtries = 0
correct = 0
ccorrect = 0
print ("Welcome to the movie guessing game!")
print ("You will attempt to guess the IMDB rating of 3 different popular movies.")
print ("It will be out of 10 stars but you have to get it right to the decimal!")
print ("There will be 3 movies and 3 guesses for each.")
print ("Ready, Begin!")
print ("First, The 2017 IT Movie")
while youguess == False:
    numtries = numtries + 1 
    correct = 7.4 
    print("Guess a number between 0.0-10.0") 
    guess = input("Example: 6.9: ")
    numguess = float(guess)
    if (numguess == correct):
        ccorrect = ccorrect + 1
        str_tries =  str(numtries) 
        print("Well done!")
        print("You have guessed correctly in " + str_tries + " tries.") 
        youguess = True 
    else:
        str_tries = str(numtries)
        if (numtries > 2):
            print("You couldn't complete the Challenge in 3 turns, You Lose!")
            youguess = True
        else:
            if (numguess > correct): 
                print("Wrong! Too high.")
            else:
                print("Wrong! Too low.")
youguess = False
numtries = 0
print ("Next let's see how you do with adventure movies!")
print ("What is the IMDB rating for Jumanji: Welcome to the Jungle")
while youguess == False:
    numtries = numtries + 1 
    correct = 6.9 
    print("Guess a number between 0.0-10.0") 
    guess = input("Example: 6.9: ")
    numguess = float(guess) 
    if (numguess == correct):
        ccorrect = ccorrect + 1
        str_tries =  str(numtries) 
        print("Well done!")
        print("You have guessed correctly in " + str_tries + " tries.") 
        youguess = True 
    else:
        str_tries = str(numtries)
        if (numtries > 2):
            print("You couldn't complete the Challenge in 3 turns, You Lose!")
            youguess = True
        else:
            if (numguess > correct):
                
                print("Wrong! Too high.")
            else:
                print("Wrong! Too low.")
youguess = False
numtries = 0
print ("Lastly, Let's see how you fair with anime titles")
print ("What is the IMDB rating for Your Name?")
while youguess == False:
    numtries = numtries + 1 
    correct = 8.4
    print("Guess a number between 0.0-10.0") 
    guess = input("Example: 6.9: ")
    numguess = float(guess) 
    if (numguess == correct):
        ccorrect = ccorrect + 1
        str_tries =  str(numtries) 
        print("Well done!")
        print("You have guessed correctly in " + str_tries + " tries.") 
        youguess = True 
    else:
        str_tries = str(numtries)
        if (numtries > 2):
            print("You couldn't complete the Challenge in 3 turns, You Lose!")
            youguess = True
        else:
            if (numguess > correct): 
                print("Wrong! Too high.")
            else:
                print("Wrong! Too low.")
str_ccorrect = str(ccorrect)
print ("you got" + str_ccorrect + "right out of 3!")
