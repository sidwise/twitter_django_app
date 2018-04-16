from twython import Twython


TWITTER_APP_KEY = 'z0JO1aunGAWu0xgxtpOMiw2qx'  # supply the appropriate value
TWITTER_APP_KEY_SECRET = '8vwUONvjOAfBcnNU9X1mtg9YJGPvDLjGZsZnbgs0CWhbOxYZDc'
TWITTER_ACCESS_TOKEN = '3021210887-iKtdExGlsNC6JNGqsgKdSTgjaKVjyTDLMDLiXKM'
TWITTER_ACCESS_TOKEN_SECRET = 'GdeRJ504DoANMZqDuE02vO4XFPJcux4pUzzqTCa3Gg6Oj'

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)