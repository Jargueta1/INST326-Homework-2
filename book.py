"""book.py for Homework 2  
Author: Jorge Argueta
Assignment: Homework 2
Date created: 10_14_21
Date updated:10_14_21
"""
import re 

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
        with open(path,'r') as f:
            content = f.readlines
            for line in contents:
                for w in line:    
                    words.append(remove_punctuation(w))    
            
        self.words = words ## needs to change this to only include alphabetical 
        
    def remove_punctuation(word):
        """
        Goal:
            removes all punctuation from the a string 
        Args:
            words(String): words with punctuation
        Returns:
            (string): same word without punctuation and lower case 
            """
        word = re.sub(r'[^a-zA-Z]', '', word)
        return word.lower()

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
        