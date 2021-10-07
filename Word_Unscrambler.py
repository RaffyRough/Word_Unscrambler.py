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

def find_word_suffixes(s, *args):
    """
    This function will use find_best_word func to generate a list of valid words
    The *args will represent suffixes available in game, which when our selection is appended to the front makes
     a valid word.  A list of valid words built from the combination of 's' and 'args' is then returned.

    :param s: str
    :param args: str
    :return: list[str]
    """
    output = []
    for wrd in find_best_word(s):
        for arg in args:
            if my_dict.check(wrd+arg):
                output.append(wrd+arg)
    return output

def find_word_prefixes(s, *args):
    """
     This function will use find_best_word func to generate a list of valid words
    The *args will represent suffixes available in game, which when our selection is appended to the back makes
     a valid word.  A list of valid words built from the combination of 's' and 'args' is then returned.
    :param s: str
    :param args: str
    :return: list[str]
    """
    output = []
    for wrd in find_best_word(s):
        for arg in args:
            if my_dict.check(arg + wrd):
                output.append(arg + wrd)
    return output



def find_all_valid_words(s, *args):
    """
    This func will use find word prefix and suffix functions as helper functions.
    A list of valid words from both these functions is then returned
    :param s:
    :param args:
    :return: list[str]
    """
    output = set()
    for wrd in find_word_prefixes(s, *args):
        output.add(wrd)
    for wor in find_word_suffixes(s, *args):
        output.add(wor)
    return output

def new_best_word(word, *nodes):
    cont = set()
    output = set()
    for node in nodes:
        cont.add(word+node)
    for string in cont:
        for x in (find_best_word(string)):
            output.add(x)
    return output


if __name__ == '__main__':
    start = time.time()
    for word in find_best_word('firaoec'):
        if len(word) >= 3:

            print(word)



    print(time.time()-start)


