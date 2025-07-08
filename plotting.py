import matplotlib.pyplot as plt
import numpy as np



def top_20_words_bar(top_20_words):
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

    plt.savefig("images/top_20_words_bar.png")
    plt.close()

    print("The most common word over 3 characters is 'that'. \n")

def word_length_distn_hist(length_of_words):
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

    plt.savefig("images/word_length_distn_hist.png")
    plt.close()

    print("The most common word length is between 6 and 7 letters.")
    print("This looks roughly like a Normal Distribution \n")

def words_per_line_scatter(words_in_line):
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

    plt.savefig("images/words_per_line_scatter.png")
    plt.close()


    print("The largest amount of words per line is just under 400.\n")