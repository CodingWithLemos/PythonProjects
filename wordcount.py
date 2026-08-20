# Word Frequency Counter Python Program

# Import sys module
#import sys

# Read text content of sys.argv
#text_content = sys.argv[1]

text_content = input('Type your phrase:\n')

# Split text by delimiters (, . ? and !)
splitted = text_content.split()

# Remove any leading or trailing punctuation
trimmed = [ word.strip(',.;:\t?!').casefold() for word in splitted ]

# Sort text strings by occurrence using dictionaries
word_frequency_counter = { x: trimmed.count(x) for x in trimmed }

# print the results to the terminal as key-value pairs
for k, v in word_frequency_counter.items():
    print (k , v)