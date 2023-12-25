# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    length =  len(secret_word)
    i = 0
    for s in secret_word:
        if s in letters_guessed:
            i += 1
    if i == length:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ''
    for s in secret_word:
        if s in letters_guessed:
            result += s 
        else:
            result += '_ '
    return result


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = string.ascii_lowercase
    
    for s in letters_guessed:
        result = result.replace(s, '')
    
    return result
    
def count_different_secret_word(secret_word):
    temp = string.ascii_lowercase
    result = 0
    
    for s in secret_word:
        if s in temp:
            temp = temp.replace(s,'')
            result += 1
    return result

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_length = len(secret_word)
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = ''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is %d letters long.' % secret_word_length)
    print('You have 3 warnings left.')
    while(True):
        print('-------------')
        if(guesses_remaining <= 0):
            print('Sorry, you ran out of guesses. The word was %s.' % secret_word)
            break
        if(is_word_guessed(secret_word, letters_guessed)):
            print('Congratulations, you won!')
            print('Your total score for this game is: %d' %(guesses_remaining * count_different_secret_word(secret_word)))
            break
        print('You have %d guesses left.' % guesses_remaining)
        print('Available letters:',get_available_letters(letters_guessed))
        guess_word = input('Please guess a letter:')
        if(guess_word.isalpha()):
            if(guess_word not in letters_guessed and guess_word in secret_word):
                letters_guessed += guess_word    
                print('Good guess:',get_guessed_word(secret_word,list(letters_guessed)))
            elif(guess_word not in letters_guessed and guess_word not in secret_word):
                letters_guessed += guess_word 
                if(guess_word == 'a' or guess_word == 'e' or guess_word == 'i' or guess_word == 'o' or guess_word == 'u'):
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print("Oops! That letter is not in my word.",get_guessed_word(secret_word,list(letters_guessed)))
            else:
                if warnings_remaining >= 1:
                    warnings_remaining -= 1
                    print('Oops! You"ve already guessed that letter. You have %d warnings left :' %warnings_remaining,get_guessed_word(secret_word,list(letters_guessed)))
                else:
                    guesses_remaining -=1
                    print('Oops! You"ve already guessed that letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word,list(letters_guessed)))
        else:
            if warnings_remaining >= 1:
                warnings_remaining -= 1
                print('Oops! That is not a valid letter. You have %d warnings left:' %warnings_remaining,get_guessed_word(secret_word, list(letters_guessed)))
            #else:
             #   print('Oops! That is not a valid letter. You have %d warnings left:' %warnings_remaining,get_guessed_word(secret_word, list(letters_guessed)))
         
        
        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word=''
    for s in my_word:
        if s != ' ':
            word += s
    if(len(word)!= len(other_word)):
        return False
    for i in range(len(word)):
        if word[i] == '_':
            for j in range(len(word)):
                if j != i and other_word[i] == other_word[j] and word[j] != '_':
                    
                    return False
        elif word[i] != other_word[i]:
            return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = []
    for word in wordlist:
        if(match_with_gaps(my_word, word)):
            result.append(word)
    if(len(result) == 0):
        print("No matches found")
    for word in result:
        print("%s" % word,end=" ")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #secret_word = 'egeg'
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
