# 1. Write a Python program that finds the longest word in a list of strings. Use
# map() to calculate the length of each word, and filter() to get the word with the
# maximum length.

def function():
    words = ['python', 'functional', 'programming', 'is', 'powerful']
    word_lengths = list(map(len, words))
    max_length = max(word_lengths)
    long_word = list(filter(lambda word: len(word) == max_length , words))
    print(f"the longest word is : {long_word}, size of word = {max_length}")


function()