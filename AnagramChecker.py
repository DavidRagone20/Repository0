# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:51:08 2021

An anagram is a word or phrase with the same 
letters as another word or phrase in a different order,
resulting in a different word or phrase, i.e. debit 
card and bad credit or dirty room and dormitory. Write 
a function that determines if two string inputs are 
anagrams of each other

@author: dragone1
"""

def anagramPrepandCheck(): # formats strings for anagram analysis then checks
    words1 = input("type your first possible anagram here: ")
    words2 = input("type the corresponding possible anagram here: ")
    punctuation = ' .,;:"'
    for character in punctuation:
        words1 = words1.replace(character, '')
        words2 = words2.replace(character, '')
        words1 = words1.lower()
        words2 = words2.lower()
    anagramBool = True
    if sorted(words1) == sorted(words2):
        return True
    else:
        return False
    return anagramBool
    print(words1)
    print(words2)
    print("anagramBool=", anagramBool)
anagramOutcome = anagramPrepandCheck()
print("The outcome for the possible anagram is:", anagramOutcome)