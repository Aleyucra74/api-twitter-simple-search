import stopwords as sw
import tweepy as tt
import json

bearer_token = "Bearer AAAAAAAAAAAAAAAAAAAAAEg0cwEAAAAAYTUZ4ez5f9vePOZy7Wsg%2BJY3oPE%3DyN6ZIrCDGLZkmflL9XlexWXcIqvCDuBxBFsiVgfjMhach51kGz"

dataTwitter = tt.twitter_data(bearer_token,"educacao",10)
tweets = []
tweets_users = []
end_list_tweets = []

for datas in dataTwitter['data']:
    tweets.append(datas)

for datas in dataTwitter['includes']:
    for data_user in dataTwitter['includes']['users']:
        tweets_users.append(data_user)

for number, i in enumerate(tweets):
    if tweets[number]['author_id'] == tweets_users[number]['id']:        
        end_list_tweets.append({
            "tweet":sw.remove_stop_words_text(tweets[number]['text']),
            "name":tweets_users[number]['username'],
            "location":tweets_users[number]['location'] if 'location' in tweets_users[number] else "N"
            })

json_string = json.dumps(end_list_tweets)
with open("data_tweets.json", "w") as i :
   json.dump(json_string, i)