import matplotlib.pyplot as plt
import numpy as np

from cipher_shift import find_shift
from decipher import decipher, text_to_list
from words_info import top_20, word_length, words_each_line
from plotting import top_20_words_bar, word_length_distn_hist, words_per_line_scatter

# Initialising variables

scrambled_text = "text/scrambled_play.txt"


user_number = 506

total = 0 # Initial value of the sum

# Make string for upper and lower case alphabet - converting it to a list

alpha_var = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

alpha_list = list(alpha_var)

# Make dictionary for punctuation, as it isn't encoded in text

punctuation = {' ':' ', '[':'[', ']':']', '(':'(', ')':')', '{':'{',
               '}':'}', ',':',', '.':'.', ':':':', ';':';', '-':'-',
               "'":"'", '!':'!', '?':'?', '&':'&', '\n':'\n'}


shift_value = find_shift(user_number)

temp_text = decipher(shift_value, alpha_list, punctuation, scrambled_text)

text_list = text_to_list(temp_text, punctuation) # This is the translated text as a list 

# Top 20 words in script

top_20_words = top_20(text_list)


# Bar chart of top 20 words longer than 3 letters

top_20_words_bar(top_20_words)

# Looking at word distribution in general

length_of_words = word_length(text_list)

# Histogram of word length distribution

word_length_distn_hist(length_of_words)

# Looking at words in each line

words_in_line = words_each_line(text_list, temp_text)

# Scatter plot of words per line

words_per_line_scatter(words_in_line)
