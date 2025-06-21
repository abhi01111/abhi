#  Write a function filter_long_words() that takes a list of words and an integer len and returns the list of words that are longer than len.


def filter_long_words(words, length):
    return [word for word in words if len(word) > length]

word_list = ["market" , "is" , "closed" , "today" , "what" , "happened"]
length_word = 5
filter_words = filter_long_words(word_list , length_word)
print(f"filter words are = {filter_words}")