import stopwords as sw
import tweepy as tt
import json

bearer_token = "Insert bearer token"

dataTwitter = tt.twitter_data(bearer_token,"educacao",30)
tweets = dataTwitter['data']
tweets_users = dataTwitter['includes']['users']
end_list_tweets = []

for tweet in tweets:
    user = ""
    location = ""
    for tweet_user in tweets_users:
        if tweet['author_id'] == tweet_user['id']:    
            user = tweet_user['username']
            location = tweet_user['location'] if 'location' in tweet_user else "N"
            break
    end_list_tweets.append({
        "tweet":sw.remove_stop_words_text(tweet['text']),
        "name":user,
        "location":location
        })

json_string = json.dumps(end_list_tweets)
with open("data_tweets.json", "a") as i :
   json.dump(json_string, i)