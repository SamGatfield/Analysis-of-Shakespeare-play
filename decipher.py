import matplotlib.pyplot as plt
import numpy as np

def decipher(shift, alpha_list, punctuation, scrambled_text):
    #Can use the offset to de-cipher the text in the file
    shifted_alpha = alpha_list[-shift:] + alpha_list[:-shift]

    t_alpha = {} #Dictionary which will contain every character

    alpha_length = len(alpha_list)

    t_alpha = {alpha_list[y]:shifted_alpha[y] 
                        for y in range(alpha_length)}


    t_alpha.update(punctuation)


    with open(scrambled_text,'r') as ciphered_text:    #Using 'with' closes the file when outside of the indent
        play_text = ''.join(ciphered_text.readlines())


    plain_text = [t_alpha[l] for l in play_text] #Un-ciphered text as a list


    temp_text = ''.join(plain_text) #Turns plain_text from a list to a string

    return temp_text


def text_to_list(temp_text, punctuation):
    text = temp_text #Variable for the play text without punctuation


    #Loop that replaces each piece of punctuation with a space

    for key in punctuation.keys():
        text = text.replace(punctuation[key],' ')
    
        
    text_list = text.lower().split(' ')
    return text_list

