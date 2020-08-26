tweets = open('tweets.txt', 'r')
resulting_data = open('resulting_data.csv', 'w')



# get rid of these characters
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = ['yes']
### Strip out useless characters
def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s = s.replace(i, "")
    return s

# count positives 
def get_pos(sentence):
    count_pos = 0
    sentence = strip_punctuation(sentence.lower())
    words = list(sentence.split(" "))
    for w in words:
        if w in positive_words:
            count_pos +=1
    return count_pos  

# count negatives 
negative_words = ['no']
def get_neg(sentence):
    count_neg = 0
    sentence = strip_punctuation(sentence.lower())
    words = list(sentence.split(" "))
    for w in words:
        if w in negative_words:
            count_neg += 1
    return count_neg     

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

# x = resulting_data.readlines()
# for l in x:
#   print (l)
