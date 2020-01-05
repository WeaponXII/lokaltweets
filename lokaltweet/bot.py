
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:

    api.verify_credentials()

    print("Authentication OK")

except:

    print("Error during authentication")
public_tweets = api.home_timeline()
for tweet in public_tweets:
    api.retweet
