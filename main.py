# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from collections import Counter
def read_file_content(filename):
    
    # [assignment] Add your code here 
    with open(filename) as f:
        return Counter(f.read().split())

#def count_words():
   # text = read_file_content("story.txt")
   # text_lst = set(text.split())
    # [assignment] Add your code here
   # for word in text_lst:
       # word_count = text.count(word)
       # unique_words = (word + ": {}".format(word_count))
       # return unique_words

print(read_file_content('story.txt'))