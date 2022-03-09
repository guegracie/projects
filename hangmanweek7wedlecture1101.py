  #create hangman game 
  #store answer in a variable 
  #import regular expression library.. 
import re

answer_characters = "What's up? Doc"; 
#capitalize the answer
answer_characters = answer_characters.upper(); 


#KEEP TRACK OF WHAT LETTERS HAVE BEEN GUESSED 
answer_guesses = []

#create a for loop to reiterate through guess list 
#always end for loop with a colon.. and indent every line inside the for loop
#first argument will be an exponent and end with a dollar sign.. in between those two symbols
#you'll have what you want to look through
#second argument will be current_answer_characters
for current_answer_characters in answer_characters:
    if re.search("^[A-Z]$",current_answer_characters):
        
        answer_guesses.append(False) #false and true have to be capitalized 
    else:
        answer_guesses.append(True)
 #make sure you're outside the for loop, so no more indentations 
 #logic of playing game.. as long as the user hasnt guessed all LETTERS, user should keep playing
 #we can have max amount of trials, keep track of incorrect guesses, and keep track if theyve guessed the word 
numOfIncorrectGuesses = 0 
lettersthatwereguessed = []

#create a loop to ask user what letter they want to guess.. should be a while loop 
# keep playing game as long as max guesses hasnt been reached and theres letters to be guessed
while numOfIncorrectGuesses < 5 and False in answer_guesses:
    #ask user what letter they'd like to guess and cin guess
    #create array to output letters that have been guessed 
    #output number of incorrect guesses allowed.. decrement every guess 
    #output the actual answer _ _ _ _ E _ _ 
    #ask user for another guess 
    print("--------------------------------")
    #tells python to not create a new line and output everything in the same line
    print("Guessed Letters: ", sep = " ")  
    #create for loop to go through array of letters that were guessed
    for current_lettersthatwereguessed in lettersthatwereguessed:
        print(lettersthatwereguessed , end = " ")
    print() #end the line and create a new line 
    print("---------------------------------")
    #tell user number of guesses remaining 
    print(f"Number of guesses remaining: {5 - numOfIncorrectGuesses}")
    #blank line for organization purposes 
    print()
    #create index 
    for answer_index in range(len(answer_characters)):
        if answer_guesses[answer_index]:
            print(answer_characters[answer_index], end = " ")
        else: 
            print("_", end = " ")
    print()
    #ask user for their guess
    letter = input("Enter a letter: ")
    #if letter entered is lower case, make it upper case 
    letter = letter.upper()
    #if letter has not been guessed before then lets continue, make sure oly one letter has been passed, and that a letter has been passed not a NUMBER
    if letter not in lettersthatwereguessed and len(letter) == 1 and re.search("^[A-Z]$", letter):
        #temporary place holder 
        guessed_letters_insert_index = 0
        for current_guessed_letter in lettersthatwereguessed:
            if letter > current_guessed_letter:
                break; 
            guessed_letters_insert_index = 0

        lettersthatwereguessed.insert(guessed_letters_insert_index, letter)
        if letter in answer_characters: 
            #letter is in the puzzle and replace the underscores with the letters
            for current_answer_index in range(len(answer_characters)):
                if letter == answer_characters[current_answer_index]: 
                    answer_guesses[current_answer_index] = True
        else:
            numOfIncorrectGuesses += 1; 
    #pass in guessed letter into guessed letters array 

#GAME IS OVER OUTSIDE OF WHILE LOOP 
if numOfIncorrectGuesses < 5:
    print("Congratulations, you solved the puzzle")
else: 
    print("Sorry, you ran out of guesses.")

print(f"{answer_characters} is the answer to the puzzle. ")