#!/bin/python3

#importing
print("Importing is important: ")

import sys #system functions and parameters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #importing with an alias
print(dt.now())


def new_line():
    print('\n')

new_line()

#Advanced strings 
print("Advanced Strings: ")
my_name = "Ethan"
print(my_name[0]) #first initial
print(my_name[-1]) #last initial 

sentence = "This is a sentence"

print(sentence[:4]) #First word
print(sentence[-9:-1]) #Last word

print(sentence.split(" "))

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

quoteception =  "I said, 'give me all the money!'"
print(quoteception)

quoteception2 = "I said,  \"give me all the money\""
print(quoteception2) 

print("A" in "Apple")

letter = "A"
word = "Apple"

print(letter in word)
print(letter.lower() in word.lower()) #Improved, case insensitive 

word_two = "Bingo"

print(letter.lower() in word.lower()) and not (letter.lower() in word_two.lower())
print("finished")
#http://localhost:8000/


#Steps to use ftp:
# python -m pyftpdlib -p 21 w
#Then go to 
#ftp://192.168.1.248/