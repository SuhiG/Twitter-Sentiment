import tweepy #importing tweepy
from textblob import TextBlob #importing textblob
import csv #importing csv

# f=open("twitter.txt","w",newline="\n") #opening the 

consumer_key=#"enter your consumer key"
consumer_secret=#"enter your consumer secret key"


access_token=#'enter your access token'

access_token_secret=#'enter your access token secret'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret) #authenticating the consumer key and the consumer secret key using tweepy
auth.set_access_token(access_token,access_token_secret) #setting up the access token

api=tweepy.API(auth) #creating an API 

#searching for a specific word or phrase
public_tweets=api.search#("word or phrase") 

with open("twitter.csv","w",newline="\n") as twitterfile: #opening the csv file
	writer=csv.DictWriter(twitterfile,fieldnames=["tweet","sentiment"]) #entering the names for the columns
	writer.writeheader() #writing the headers
	for tweet in public_tweets: #for loop for tweet search
		analysis=TextBlob(tweet.text)
		text=tweet.text # making the results .text for printing it on the csv file
		# =analysis.sentiment
		sentiment=analysis.sentiment.polarity #writing a statement to identify the polarity of each test result

		if (sentiment>0): # considering the polarity of each test result by an if statement

			p="Positive"
			

		else:
			p="Negative"

		text.encode('utf-8') #solving the unicode charactor error
		text.encode('cp932', "ignore")#solving the unicode charactor error
		writer.writerow({"tweet": text,"sentiment":p}) #printing the final result on the twitter.csv file

	
twitterfile.close()
