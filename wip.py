tweets = open('project_twitter_data.csv', 'r')
resulting_data = open('resulting_data.csv', 'w')

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = ['yes']
### Strip out useless characters
def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s = s.replace(i, "")
            
            
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
# count positives 
def get_pos(sentence):
    count_pos = 0
    sentence = strip_punctuation(sentence.lower())
    words = list(sentence.split(" "))
    for w in words:
        if w in positive_words:
            count_pos +=1
    return count_pos  

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

negative_words = ['no']
def get_neg(sentence):
    count_neg = 0
    sentence = strip_punctuation(sentence.lower())
    words = list(sentence.split(" "))
    for w in words:
        if w in negative_words:
            count_neg += 1
    return count_neg    

## this is function 
def thisisx(resulting_data):
    tweets_header = tweets.readlines()
# what is happening here. Why is header popped in the for loop?
    tweets_noheader = tweets_header.pop(0)
    resulting_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resulting_data.write('\n')

    # no retweets, replies, score pos, socre neg, net
    for line in tweets_header:
        line_list = line.strip().split(',')
      # print(line_list)r
        resulting_data.write("{}, {}, {}, {}".format(line_list[1], line_list[2],
      get_pos(line_list[0]), get_neg(line_list[0]),   (get_pos(line_list[0])-get_neg(line_list[0]))  )
      )
        resulting_data.write('\n')
