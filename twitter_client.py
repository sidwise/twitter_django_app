import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():

	try:
		consumer_key = "z0JO1aunGAWu0xgxtpOMiw2qx"
		consumer_secret = "8vwUONvjOAfBcnNU9X1mtg9YJGPvDLjGZsZnbgs0CWhbOxYZDc"
		access_token = "3021210887-iKtdExGlsNC6JNGqsgKdSTgjaKVjyTDLMDLiXKM"
		access_secret = "GdeRJ504DoANMZqDuE02vO4XFPJcux4pUzzqTCa3Gg6Oj"

	except KeyError:
		sys.stderr.write("TWITTER_* environment variables not set \n")
		sys.exit(1)
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	return auth 

def get_twitter_client():

	auth = get_twitter_auth()
	client = API(auth)
	return client

	