
# parse trump tweets for word bank
# Choose random word to start tweets
# using RNN guess next words in sequence
# output completed tweets
import re
import markovify
import textstat
# Get raw text as string.
with open("trump fake news.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)

array = []
for i in range(30):
  generatedTweet = text_model.make_sentence()
  if generatedTweet == None:
    break
  array.append(generatedTweet)




regex = r"(\\.*?)[a-eg-zA-Z 0]"
for tweet in array:
  count = 0
  matches = re.finditer(regex, tweet, re.MULTILINE)
  for matchNum, match in enumerate(matches, start=1):
    # print(tweet)

    start = match.start()
    end = match.end()
    match = match.group()    
    # print(matchNum)
    # print( start)
    # print( end)
    # print(count)
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum , start = start , end = end, match = tweet[start:end]))
    tweet = tweet[: start - count] + tweet[end - count - 1:]
    count += end - start - 1 
  if (textstat.flesch_reading_ease(tweet) > 100):
    print(tweet + "\n textstat reading ease {} \n".format(textstat.flesch_reading_ease(tweet)))

 



  