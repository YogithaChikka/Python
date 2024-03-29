#finalcode

#Hangman

import random

# can be used when importing from same module
# from handman_art import logo, stages

#Update the word list to use the 'word_list' from hangman_words.py
# import hangman_words

# {Another method of writing import}
from hangman_words import word_list 
chosen_word = random.choice(word_list)

# chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art 
print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#Use a while loop to let the user guess again. 
#The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
#Then you can tell the user they've won.
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        
        # Loop through each position in the chosen_word;
        # #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        # #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        #If guess is not a letter in the chosen_word,
        #Then reduce 'lives' by 1.
        lives -= 1
        print("Lives left: " , lives)
        
        #If lives goes down to 0 then the game should stop and it should print "You lose."
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word is: {chosen_word}.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    #The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
    #Then you can tell the user they've won.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py and make this error go away.
    import hangman_art 
    print(hangman_art.stages[lives])

