"""def digit_sum(n):
    total = 0
    total_list = []
    for i in str(n): # convert to a string and append to a list
        total_list.append(int(i))
    print(total_list)
    for x in total_list: # iterate through the list and add totals...return totals
        total = total + x
    return total

print(digit_sum())"""

"""def factorial(x):#next step is to combine anf refactor
  num = []
  factor = 1
  while x > 0:  #loop while x is > 0, append each number to list, decrement by 1
    num.append(x)
    x -= 1
  print (num)
  for n in num: #iterate through the list and multiply them
    factor *= n
  return factor


print (factorial(7))"""

#Program to see if the number is prime
'''def is_prime(x):
    if x > 1:
        for n in range(1, x):
            if x % n == 0:
                return False
            else:
                return True
    else:
        return False


print (is_prime(1))'''


#program to reverse the word passed to it
'''def reverse1(text):#put into a list
    word = []
    new_word = ''
    for i in text:
        word.append(i)
    print(word)
    print(len(word))
    for d in range(len(word)-1,-1,-1):
        new_word += word[d]
    return (new_word)
    #create a string from the list, but read it backwards

print (reverse1("sting"))'''
""".
Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!". Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels."""
# Program that removes vowels
# Iterate through list 1, one letter at a time
# Iterate through list 2, and compare to the letter in list 1, to find a match (use lower)
# Add each non-vowel letter to a new string
# Take the vowel out of the argument that is present in vowel list

"""This is a cool way of doing things but I was looking for the algorithm behind intersection o I can understand 
x = set(vowels)
  y = set(word)
  for item in y.intersection(x):
    y.remove(item)"""

"""def anti_vowel(text):
  new_text = ""
  word = []
  vowels = ['a','e','i','o','u',"A","E","I","O","U"]
  for i in text:
    word.append(i)
  for item in word:
    if item not in vowels:
      new_text += item
  return new_text

print (anti_vowel("respect"))"""


"""Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter (we'll leave out the double and triple letter and word scores for now).

To the right is a dictionary containing all of the letters in the alphabet with their corresponding Scrabble point values.

For example: the word "Helix" would score 15 points due to the sum of the letters: 4 + 1 + 1 + 1 + 8.
Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.

Assume your input is only one word containing no spaces or punctuation.
As mentioned, no need to worry about score multipliers!
Your function should work even if the letters you get are uppercase, lowercase, or a mix.
Assume that you're only given non-empty strings"""

"""def scrabble_score(word):
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
  word_score = 0
  for item in word.lower():
    if item in score:
      word_score += score[item]
      print (word_score)
  return word_score

print(scrabble_score("durell"))"""



# Find a match for the entire word
# Then go to the beginning of the word in the text
# Change each letter in the text to an "*"
def censor(text, word):
  new_list = []
  new_text = ""
  #initiate what I need for the problem
  i = 0
  j = 0
  n = len(text)
  m = len(word)
  #Str=immutable, create list instead
  for item in text:
    new_list += item
    while i < n: # total limit this loop will run
      if text[j] == word[i]:
        if j == m-1:# Perfect match if num value at j is equal to len of word
          #the text equivalent of word[0] needs to be changed to "*" then iterate to end of
  return new_list
      

print(censor("this hack is wack hack", "hack"))

"""

def censor(text, word):
  new_text = text.replace(word,"*",2)
  return new_text

print(censor("this hack is wack hack", "hack"))"""





















