from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    return contents 

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """


    words = text_string.split() #splitting text string into indiviual word strings

    chains = {}    
    # tuples_of_keys = [] 
    list_of_values = []

    for index in range(len(words)-2):
        tuples_of_keys = (words[index], words[index + 1])
        values = words[index + 2]

        chains[tuples_of_keys] = values

        if values not in list_of_values:
            list_of_values.append(values)
        else: 
            print "blah"
    
    

    print list_of_values


    print chains



    
    # return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
