"""bookshelf.py for Homework 2  
Author: Jorge Argueta
Assignment: Homework 2
Date created: 10_14_21
Date updated:10_14_21
"""
from argparse import ArgumentParser
import re
import sys
import bookshelf as bs 

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
    
    shelf = bs.Bookshleft()
    for filename in libray:
        shelf.addBooks(filename)

    shelf.find_popularity()
    shelf._test()



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
    parser.add_argument("books", type = str)
    args = parser.parse_args(args_list)
    return args

    

if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
        
    except ValueError as e:
        sys.exit(str(e))
    print("this")
    print(args.books)
    main(args.books)