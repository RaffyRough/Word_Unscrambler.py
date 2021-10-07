# A program that will take letters available to me in Words with Friends and show best words that can be made
# Author O. Raphael Mapp

from itertools import permutations, combinations
import enchant
import time


# Instantiate an enchant dictionary object.
my_dict = enchant.Dict('en_GB')



def find_best_word(word):
    """:arg word: -> A string to be searched for all real words
       :return: -> A list of all the words found in the argument"""
    real_words = set()
    container = set()
    letters = [x.lower() for x in word]    # Make every letter in our string a lower case
    for x in range(4, len(letters)+1):    # each x in the loop represents the lengths of the words
        for words in set(permutations(letters, x)):  # we put the permutations in a set to avoid duplicates
            container.add(''.join(words))
    for wrd in container:        # For every word we have appended to the container
        if my_dict.check(wrd):   # If it is a real word, then append it to the real_words list
            real_words.add(wrd)
    # Finally we return real_words
    return real_words


