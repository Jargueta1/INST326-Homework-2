"""book.py for Homework 2  
Author: Jorge Argueta
Assignment: Homework 2
Date created: 10_14_21
Date updated:10_14_21
"""

Class Book:

    def __init__(self, path):
        """
        Goal:
            gets all the words from book from the path entered and sets them to word
        Args:
            self
            path(string): path containing the file to read
        Returns:
            None
        """
        
        ## Make for each for extracting words and removing punctuation 
        words = [] 
        self.words = words ## needs to change this to only include alphabetical 
        
    def remove_punctuation(word):
        """
        Goal:
            removes all punctuation from the a string 
        Args:
            words(String): words with punctuation
        Returns:
            words_str(string): same word without punctuation
            """
        pass

    def unique_words(self):
        """
        Goal:
            Returns set created from words attribute 
        Args:
            self
        Returns:
            word_attribute(set): contains all the uniques words from the book
        """
        pass
        