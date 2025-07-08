import matplotlib.pyplot as plt
import numpy as np

#----------//----------

user_number = 506

total = 0 #Initial value of the sum


def Sum(m): #m is a parameter which gets passed into the function
    total = 0 
    n = 1 
    for i in range(0,m):
        total += n**(-1/5)
        n+=1
    return total


k = 1 #Initial value for the k we need to find


while Sum(k) <= user_number:
    k += 1
    Sum(k)
    
print(f'The value for k such that the sum is > {user_number} is k = {k}')
  

#----------//----------


#Next compute the gcd of k and user_number

max_val = max(k, user_number)
min_val = min(k, user_number)

r = max_val
s = 0 #This is for the multiples of min_val we subtract
while r > 0:
    while r >= min_val:
        r = max_val - s*min_val
        s += 1
        
    max_val = min_val
    min_val = r
    s = 0

gcd = max_val #Offset used to encode the text (and also the GCD)
print(f'The GCD of {k} and {user_number} is {gcd} \n')


#----------//----------


#Make string for upper and lower case alphabet - converting it to a list

alpha_var = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


alpha_list = list(alpha_var)


#Can use the offset to de-cipher the text in the file

shifted_alpha = alpha_list[-gcd:] + alpha_list[:-gcd]


#Make dictionary for punctuation, as it isn't encoded in text

punctuation = {' ':' ', '[':'[', ']':']', '(':'(', ')':')', '{':'{',
               '}':'}', ',':',', '.':'.', ':':':', ';':';', '-':'-',
               "'":"'", '!':'!', '?':'?', '&':'&', '\n':'\n'}

t_alpha = {} #Dictionary which will contain every character

alpha_length = len(alpha_list)

t_alpha = {alpha_list[y]:shifted_alpha[y] 
                    for y in range(alpha_length)}


t_alpha.update(punctuation)


with open('scrambled_play.txt','r') as ciphered_text:    #Using 'with' closes the file when outside of the indent
    play_text = ''.join(ciphered_text.readlines())


plain_text = [t_alpha[l] for l in play_text] #Un-ciphered text as a list


temp_text = ''.join(plain_text) #Turns plain_text from a list to a string


text = temp_text #Variable for the play text without punctuation


#Loop that replaces each piece of punctuation with a space

for key in punctuation.keys():
    text = text.replace(punctuation[key],' ')
   
       
text_list = text.lower().split(' ')



#----------//----------


#Looking at words longer than 3 letters

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



#----------//----------


#Bar chart of top 20 words longer than 3 letters

plt.style.use('ggplot')

fig, ax = plt.subplots()


ax.barh([i for i in range(20,0,-1)],
        [i[1] for i in top_20_words], 
        ec='black')

ax.set_yticks([i for i in range(20,0,-1)],
             labels = [i[0] for i in top_20_words])


#Setting and styling the labels on each axis

ax.set(title = 'Top 20 used words longer than 3 letters',
       xlabel = 'Number of times word appears',
       ylabel = 'Words')


#Styling the labels and title

ax.xaxis.get_label().set_size(10)
ax.xaxis.get_label().set_style('italic')

ax.yaxis.get_label().set_size(10)
ax.yaxis.get_label().set_style('italic')

ax.set_title('Top 20 used words longer than 3 letters')
ax.title.set_weight('bold')


print("The most common word over 3 characters is 'that'. \n")

#----------//----------


#Looking at word distribution in general


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


#----------//----------


#Histogram of word length distribution

fig, ax = plt.subplots()


bins = [i for i in range(1,15)]


ax.hist(length_of_words, 
        bins=bins, 
        ec='black')


ax.set(title = 'Distribution of word length', 
       xlabel = 'Length of words', 
       ylabel = 'Amount of words with given length')


#Styling the labels and title

ax.xaxis.get_label().set_size(10)
ax.xaxis.get_label().set_style('italic')

ax.yaxis.get_label().set_size(10)
ax.yaxis.get_label().set_style('italic')

ax.title.set_weight('bold')


print("The most common word length is between 6 and 7 letters.")
print("This looks roughly like a Normal Distribution \n")

#----------//----------


#Looking at words in each line


text_list = temp_text.split('\n')


words_in_line = []

for line in text_list:
    words_in_line.append(len(line.split()))


#Scatter plot of words per line

fig, ax = plt.subplots()

x = np.array([i for i in range(0,len(words_in_line))])
y = np.array(words_in_line)

plt.scatter(x,y)


ax.set(title = 'Scatter plot of Words per Line', 
       xlabel = 'Line number', 
       ylabel = 'Words per Line')



#Styling the labels and title

ax.xaxis.get_label().set_size(10)
ax.xaxis.get_label().set_style('italic')

ax.yaxis.get_label().set_size(10)
ax.yaxis.get_label().set_style('italic')

ax.title.set_weight('bold')


print("The largest amount of words per line is just under 400.\n")

#----------//----------


#Character Speeches


lines = temp_text.splitlines()

speeches = {}


#Making the character names the key, and the lines spoken by the 
#character the value in the dictionary

for i in range(0,len(lines)):
    if ':' in lines[i]:
        character_line = lines[i].split(':',1) #Splits each line by the first colon
        speeches.update({character_line[0]: character_line[1]})
    else:
        continue



#Finding the amount of words per speech for each character


words_in_speech = []


speech_list = list(speeches.values())

for s in speech_list:
    words_in_speech.append(len(s.split()))


#Plot graph of character names against speech length



#----------//----------

#Dialogue in scenes

scenes = {}

for i in range(0,len(lines)):
    if lines[i].startswith('[[SCENE'):
        pass
        #Need to add every proceeding element to 'scenes' dictionary 
        #with the scene number being the key until a line starts with 
        #'[[SCENE' again
        
#Make a plot of each scene against number of lines in each scene
