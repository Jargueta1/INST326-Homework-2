"""bookshelf.py for Homework 2  
Author: Jorge Argueta
Assignment: Homework 2
Date created: 10_14_21
Date updated:10_14_21
"""
import re 
import Book from book 
import Bookshelf from bookshelf

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
    book_one = Book("/dataTry/try1.txt")
    print(book_one.words)
    
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
    
"""
            if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
         sys.exit(str(e))
"""

main("this")