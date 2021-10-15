"""bookshelf.py for Homework 2  
Author: Jorge Argueta
Assignment: Homework 2
Date created: 10_14_21
Date updated:10_14_21
"""

Class Bookshleft:

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