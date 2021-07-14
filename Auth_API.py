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