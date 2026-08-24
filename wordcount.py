# Word Frequency Counter Python Program

# Prompt the user to insert text in the terminal:
text_content = input('Paste your text:\n')

# Split text by delimiters (, . ? and !)
splitted = text_content.split()

# Remove any leading or trailing punctuation, all words lowercase
trimmed = [ word.strip(',.;:\t?!').casefold() for word in splitted ]

# Arrange text strings using dictionaries
word_frequency_counter = { x: trimmed.count(x) for x in trimmed }

# Sort by frequency
word_freq_sorted = sorted(word_frequency_counter, key=word_frequency_counter.get, reverse=True)

# print the results to the terminal as key-value pairs
for k in word_freq_sorted:
    print(k, word_frequency_counter[k])