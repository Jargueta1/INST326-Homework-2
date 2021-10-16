"""bookshelf.py for Homework 2  
Author: Jorge Argueta
Assignment: Homework 2
Date created: 10_14_21
Date updated:10_14_21
"""

from os import PRIO_PGRP
import book as b

class Bookshleft:

    def __init__(self):
        """
        Goal:
            initializes attributes and sets them to empty dic
        Args:
            
        Returns:
            None
        """
        self.index = {}
        self.popularity_index = {}
    
    def addBooks(self,text):
        """
        Goal:
            Cretes new book object and from text name that is passsed
            adds words returned from unique_words func. into index
        Args:
            self
            text(string): path
        Returns:
            None
        """
        book = b.Book(text)

        for w in book.unique_words():
            if w not in  self.index:
                self.index[w] = []
        
            self.index[w].append(text)

    def find_popularity(self):
        """
        Goal:
            resets the popularity index 
            populate it by iterating over the items of the index attribute 
            index where the keys are integers that represent how many books a word is found in and the values are the words that correspond to that count 
        Args:
            self
        Returns:
            None
        """
        self.popularity_index = {}
        
        for key in self.index:
            self.popularity_index[key] = len([count for count in self.index[key] ])

    def _test(self):
        max = 0
        for value in self.popularity_index:
            new = self.popularity_index[value]

            if new > max:
                max = new
        print(max)
            