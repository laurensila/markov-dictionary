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



    # random_key = choice(chains.keys())


    # if random_key in chains.keys():
    #     print random_key
    #     print chains[random_key]

    #     random_value = choice(chains[random_key])

    #     brand_new_key = ()
    # return " ".join()

    key = choice(chains.keys())
    words = [key[0], key[1]]

    while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text)
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        word = choice(chains[key])
        words.append(word)
        key = (key[1], word)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
