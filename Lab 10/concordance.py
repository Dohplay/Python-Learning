import string
from random import *

def concord(filename):
    line_num = 0
    dictionary = {}
    file = open(filename, "r")
    number = set()
    
    for line in file:
        line_num += 1
        word_list = line.split()
        
        for word in word_list:   
            w = word.strip(string.punctuation).lower()
            if w != '':
                if w not in dictionary:
                    dictionary[w] = []
                    dictionary[w].append(line_num)
                else:
                    dictionary[w].append(line_num)
                        
    for key in sorted(dictionary):
        print ("%s: %s" % (key, dictionary[key]))  
        
def words_in_text(filename):
    file = open (filename,"r")
    dictionary = {}
    for line in file:
        word_list = line.split()
        for word in word_list:
            w = word.strip(string.punctuation).lower()
        if w != "":
            if w not in dictionary:
                dictionary[w] = 1
            else:
                dictionary[w] += 1
    
    highest_value = 0
    output = []
    for key in dictionary:
        if dictionary[key] >= highest_value:
            highest_value = dictionary[key]
    
    for key in dictionary: 
        if dictionary[key]>= highest_value:
            output.append(key)
    print ("The following list of words: \n %s \n was seen %i times" \
           % (output, highest_value))
    
def craps():
    done = False
    while done == False:
        die1 = randint(1,6)
        die2 = randint(1,6)
        dice_sum = die1 + die2        
        if dice_sum == 7 or dice_sum == 11:
            print("Congratulations you won")
            done = True
            return 1
        elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
            print("Sorry! You lost the game")
            done = True
            return 0
        else:
            print("Try again!")
            
