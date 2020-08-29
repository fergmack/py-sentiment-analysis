
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

projectTwitterDataFile = open("project_twitter_data.csv","r")
resultingDataFile = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences= strSentences.split()
    
    count=0
    for word in listStrSentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count+=1
    return count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

            
def get_neg(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()
    
    count=0
    for word in listStrSentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count+=1
    return count

    
def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord


def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF =  projectTwitterDataFile.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")

        

writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()


// my code 




# Postive words
positive_words = []
# Opening the positive words file
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        # Some of the comments in the postive file has ; at the start. 
        # Remove these along with the \n
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
# Negative words
negative_words = []

with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            


# Remove punctuation
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(tweet_word):
    for charPunc in punctuation_chars:
        cleanTweet = tweet_word.replace(charPunc, '')
        return cleanTweet
        
# Count Positive words
def get_pos(sentences):
    sentence = strip_punctuation(sentences)
    sentenceList = sentence.split()
    count = 0 
    for word in sentenceList:
        for postiveWord in positive_words:
            if word == postiveWord:
                count += 1
        return count

# Count Negative words
def get_neg(sentences):
    sentence = strip_punctuation(sentences)
    sentenceList = sentence.split()
    count = 0 
    for word in sentenceList:
        for negativeWord in negative_words:
            if word == negativeWord:
                count += 1
        return count

### Do analysis 
# Get Tweets            
twitterData = open('project_twitter_data.csv', 'r')
# Creates a new file (as resutling data csv does not yet exist)
resultingDataFile = open('resulting_data.csv', 'w')

def resultingData(resultingDataFile):
    # Write header
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")
    twitterDataLines = twitterData.readlines()
    dropHeader = twitterDataLines.pop(0)
    
    for lines in twitterDataLines:
        linesList = lines.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}".format(
            linesList[1], linesList[2], get_pos(linesList[0]), 
            get_neg(linesList[0]), 
            (get_pos(linesList[0]) - get_neg(linesList[0])
        )))
            
resultingData(resultingDataFile)

    
            
