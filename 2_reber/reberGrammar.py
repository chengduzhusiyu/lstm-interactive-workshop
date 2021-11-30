#!/usr/bin/python

import numpy as np

chars='BTSXPVE'

graph = [[(1,5),('T','P')] , [(1,2),('S','X')], \
           [(3,5),('S','X')], [(6,),('E')], \
           [(3,2),('V','P')], [(4,5),('V','T')] ]


def in_grammar(word):
    if word[0] != 'B':
        return False
    node = 0
    for c in word[1:]:
        transitions = graph[node]
        try:
            node = transitions[0][transitions[1].index(c)]
        except ValueError: # using exceptions for flow control in python is common
            return False
    return True

def sequenceToWord(sequence):
    """
    converts a sequence (one-hot) in a reber string
    """
    reberString = ''
    for s in sequence:
        index = np.where(s==1.)[0][0]
        reberString += chars[index]
    return reberString

def generateSequences(minLength):
    while True:
        inchars = ['B']
        node = 0
        outchars = []
        while node != 6:
            transitions = graph[node]
            i = np.random.randint(0, 