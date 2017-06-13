# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

user_input = raw_input("Enter a word: ")
pal = True
p_word = []
for letter in user_input:
    p_word.append(letter)

while p_word:
    if  p_word[0] == p_word [-1]:
        p_word = p_word [1:-1]
    else:
        pal = False
        print "This is not a palindrome."
        break
if pal == True:
    print "This is a palindrome."




