
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 

class TwitterClient(object): 
    
    def __init__(self): 
       
        
        consumer_key = "Zm3yk6NO21n6bSqLk9cRz5VHM"
        consumer_secret = "0k5kfFqNGgmhuAXgqYDhFSW6czoASfQchIzassTisgD0Ixx0py"
        access_token = "1235855507325239297-0qrIDAvSWJApyCIhtlUfA3AUOq1xQR"
        access_token_secret = "qxyoQnxyVoxkZPFQpxKteT3UW6XzhyxlCyXUKL1jrzryb"

        
        try: 
            
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
           
            self.auth.set_access_token(access_token, access_token_secret) 
           
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 

    def clean_tweet(self, tweet): 
        
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())  

    def get_tweet_sentiment(self, tweet): 
        
       
        analysis = TextBlob(self.clean_tweet(tweet)) 
       
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

    def get_tweets(self, query, count = 10): 
        
       
        tweets = [] 

        try: 
           
            fetched_tweets = self.api.search(q = query, count = count) 

           
            for tweet in fetched_tweets: 
               
                parsed_tweet = {} 

               
                parsed_tweet['text'] = tweet.text 
               
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

               
                if tweet.retweet_count > 0: 
                    
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 

            
            return tweets 

        except tweepy.TweepError as e: 
           
            print("Error : " + str(e)) 

def main(): 
   
    api = TwitterClient() 
  
    tweets = api.get_tweets(query = input('enter the query item: '), count = 1000) 

   
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    

    
    
    positive=(100*len(ptweets)/len(tweets))
    negative=(100*len(ntweets)/len(tweets))
    
    if negative==0:
        ratingbase=positive+20
    else:
        ratingbase=positive-negative
    
    
    if ratingbase<0:
        ratingbase=(-1)*ratingbase
    elif ratingbase==0:
        ratingbase=12.5
    else:
        ratingbase=ratingbase
    rating=(ratingbase/50)*100
    
    if rating>0 and rating<20:
        print('** - 2 star')
    elif rating>20 and rating<40:
        print("**' - 2.5 star")
    elif rating>40 and rating<60:
        print('*** - 3 star')
    elif rating>60 and rating<80:
        print('**** - 4 star')
    else:
        print('***** - 5 star')
    
     
   
        
if __name__ == "__main__": 
  
    main() 