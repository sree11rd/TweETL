# Twitter API authentication

import tweepy

api_key = 'Ov33fDXpasxzUK9ViTF3mY8go'
api_secret_key = 'dzarGrhP5vSWOwFHPfGZkiwY9isJYbuMU3YSHgQk2Upfy0TjDw'
access_token =  '102939965-5Cl4miAvHjrQzLuUhCVJxrgKcwKuB3E2L7ZLc1lO'
access_token_secret =  'xWC9Nt3RsUITlSQxr8eMbv9UWZhrfbenH6myKEP8lqOBg'

# authorize the API Key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the api
api = tweepy.API(authentication)

# Streaming tweets from home timeline

public_tweet = api.home_timeline(count=5)

for tweet in public_tweet:
    print("-->",tweet.text)

# Streaming tweets from user timeline

user = "ziabolas"
public_tweet = api.user_timeline(id=user,count=5)

for tweet in public_tweet:
    print("-->",tweet.text)

# Retrieve tweets
result = api.search(['covid','Covid-19','COVID-19'], lang='en', count=10)

# JSON keys
print(result[0]._json.keys())
