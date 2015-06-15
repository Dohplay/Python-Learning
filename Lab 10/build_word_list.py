"""
SYSC 1005 A Fall 2014 - Case Study: Using Lists and Sets
"""
import string

# For information about the string module, type help(string) at the shell 
# prompt, or browse the Library Reference, Section 6.1, in the Python 3.4.1 
# documentation (available @ python.org).

def build_word_list(filename):
    """ Return a list of all the words in the specified file,
    sorted in ascending order.
    
    Example:
    >>> word_list = build_word_list('sons_of_martha.txt')
    >>> word_list
    >>> len(word_list)  # How many different words are in the file?
    """
    infile = open(filename, "r")
    word_set = set()

    for line in infile:

        # Split each line into a list of words.
        # The split method removes the whitespace from around each word.
        word_list = line.split()

        # For each word, remove any punctuation marks immediately
        # before and after the word, then convert it to lower case.
        
        for word in word_list:
            w = word.strip(string.punctuation).lower()
            
            # or, 
            # w = word.strip(string.punctuation)
            # w = w.lower()

            # Don't save any empty strings created when the punctuation marks
            # are removed. For example, if w is bound to a hyphen, '-',
            # w.strip(string.punctuation) yields the empty string, ''.
            
            if w != '':
                # Storing the words in a set removes any duplicates.
                word_set.add(w)

    # Now build the list of words.
    
    word_list = list(word_set)
    
    # or,
    # word_list = []
    # for word in word_set:
    #    word_list.append(word)

    # Sort the list into ascending order.
    word_list.sort()
    return word_list
