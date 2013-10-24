import sys
import json
import operator

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  scores = {} # initialize an empty dictionary
  for line in sent_file:
   term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
   scores[term] = int(score) # Convert the score to an integer.

  happiness={} #pair state, sentiment

  for line in tweet_file:
       #convert the line from file into a json object
       mystr = json.loads(line)
       #check "place"->"country_code" key in response, it should be in US
       if 'place' in mystr.keys() and mystr["place"] is not None and mystr["place"]["country_code"]=='US':
            #get "user"->"location" parameter, it should be two characters representing the state
            if 'user' in mystr.keys() and mystr["user"] is not None and mystr["user"]["location"] is not None:
                 location=mystr["user"]["location"].split(' ')
                 if len(location)==2 and len(location[1])==2:
                      if 'text' in mystr.keys():
                           resscore=0
                           #split the tweet into a list of words
                           words = mystr["text"].split()
                           for word in words:
                                #if the current word exists in our dictionary, add its value to the total
                                if word in scores:
                                     resscore+=scores[word]
                           #convert to float
                           resscore+=0.0
                           #store states happiness
                           if location[1] not in happiness:
                                happiness[location[1]]=resscore
                           else:
                                happiness[location[1]]+=resscore
  #get the happiest if dict is not null!
  if len(happiness.keys())>0:
       happiest=happiness.iteritems()
       print happiness
  else:
       print 'US'

if __name__ == '__main__':
  main()
