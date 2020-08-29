# 1) Remove punctuation
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s = s.replace(i, "")
    return s
# 2) Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s = s.replace(i, "")
    return s
                        
def get_pos(sentence):
    count_pos = 0
    sentence = strip_punctuation(sentence.lower())
    words = list(sentence.split(" "))
    for w in words:
        if w in positive_words:
            count_pos +=1
    return count_pos

# 3) Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s = s.replace(i, "")
    return s
            
def get_neg(sentence):
    count_neg = 0
    sentence = strip_punctuation(sentence.lower())
    words = list(sentence.split(" "))
    for w in words:
        if w in negative_words:
            count_neg += 1
    return count_neg

## final code 
# Open list of positive/negative words
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
# remove unwanted characters
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']  
def strip_punctuation(word):
    for punctChar in punctuation_chars:
        word = word.replace(punctChar, '')
    return word
# Count pos/neg
def get_pos(sentences):
    sentences = strip_punctuation(sentences)
    sentenceList = sentences.split()
    count = 0 
    for word in sentenceList:
        for posWord in positive_words:
            if word == posWord:
                count +=1
    return count

def get_neg(sentences):
    sentences = strip_punctuation(sentences)
    sentenceList = sentences.split()
    count = 0
    for word in sentenceList:
        for negWord in negative_words:
            if word == negWord:
                count += 1
    return count


twitterDataFile = open("project_twitter_data.csv","r")
resultingDataFile = open("resulting_data.csv","w")


# perform analysis 
def twitterResults(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF =  twitterDataFile.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")

        

twitterResults(resultingDataFile)
twitterDataFile.close()
resultingDataFile.close()
