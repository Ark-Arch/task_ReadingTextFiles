# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string # imported needed libary

def read_file_content(filename):
    # [assignment] Add your code here

    with open(filename) as fhand:
         file_content = fhand.read()

    return file_content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    word_count = dict()
    text = text.lower() # Eliminate capitalizations

    punctuations = string.punctuation
    ascii_dict = str.maketrans('','',punctuations) 

    text = text.translate(ascii_dict)  # ELiminate punctuations

    text = text.split() # split into words

    for word in text:
        word_count[word] = word_count.get(word, 0) + 1
    
    
    return word_count

print(count_words())