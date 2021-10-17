"""bookshelf.py for Homework 2  
Author: Jorge Argueta
Assignment: Homework 2
Date created: 10_14_21
Date updated:10_14_21
"""
import book as b
from argparse import ArgumentParser
import sys

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

def main(libray): 
    """
    Goal:
        Create an instance of bookshelf. 
        Use each path in the library list
        invoke the add_books method on that bookshelf instance. 
	    Invoke find_popularity() 
    Args:
        Library(list): list that contains paths to works 
    Returns:
        result(tuple): 
            The index attribute of your bookshelf
	        Length of the index of your bookshelf
	        Popularity_index attribute of your bookshelf 
    """
    
    shelf = Bookshleft()
    for filename in libray:
        shelf.addBooks(filename)

    shelf.find_popularity()
    
    return shelf.index, len(shelf.index),shelf.popularity_index


def parse_args(args_list):
    """
    Goal:
        create an instance of an ArgumentParser object
        assign one argument to it named books. 
	    
    Args:
        args_list(list): A list of command line arguments. Can be of any length 
    Returns:
        ArgumentParser Object 
            """
    parser = ArgumentParser()
    parser.add_argument("books", nargs='+', default=[])
    args = parser.parse_args(args_list)
    return args

    

if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
        main(args.books)
    except ValueError as e:
        sys.exit(str(e))