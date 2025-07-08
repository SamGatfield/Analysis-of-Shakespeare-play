import matplotlib.pyplot as plt
import numpy as np

def top_20(text_list):
    long_words = {} #Empty dictionary for words > 3 letters

    for t in text_list:
        if len(t) > 3:
            if t in long_words:
                long_words[t] += 1
            else:
                long_words[t] = 1
        else:
            continue

    list_of_long_words = sorted(long_words.items(), 
                                key = lambda x:x[1],
                                reverse = True)

    top_20_words = list_of_long_words[:20]

    return top_20_words



def word_length(text_list):
    all_words = {} #Empty dictionary for all words

    for t in text_list:
        if t in all_words:
            all_words[t] += 1
        else:
            all_words[t] = 1

    list_of_all_words = sorted(all_words.items(), 
                            key = lambda x:x[1])

    length_of_words = [] #Create an empty list for the lengths - 
                        #to be passed into the histogram

    for i in range(0,len(list_of_all_words)):
        length_of_words.append(len(list_of_all_words[i][0]))

    return length_of_words


def words_each_line(text_list, temp_text):
    text_list = temp_text.split('\n')

    words_in_line = []

    for line in text_list:
        words_in_line.append(len(line.split()))

    return words_in_line

