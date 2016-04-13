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

    for index in range(len(words)-2):
        keys = words[index], words[index + 1]
        value = words[index + 2]

        if keys in chains:
            chains[keys].append(value)
        else: 
            chains[keys] = [value]
    

    print chains
    return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    import random

    random_key = random.choice(chains.keys())


    if random_key in chains.keys():
        print random_key
        print chains[random_key]

    random_value = random.choice(random_key)
    print random_value


    #random_value = random.choice(chains.value())

        

    # print new_key

    #ex:
    #current_key = ('in', 'a') : [ 'house?', 'box']
    #chosen_word = 'house?'
    #new_key = ('a', 'chosen_word')


    #variable new_key = key[1] + random value

    # return text





input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
