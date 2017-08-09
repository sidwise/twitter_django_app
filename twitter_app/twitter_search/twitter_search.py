from twython import Twython
# import json
#

TWITTER_APP_KEY = 'z0JO1aunGAWu0xgxtpOMiw2qx'  # supply the appropriate value
TWITTER_APP_KEY_SECRET = '8vwUONvjOAfBcnNU9X1mtg9YJGPvDLjGZsZnbgs0CWhbOxYZDc'
TWITTER_ACCESS_TOKEN = '3021210887-iKtdExGlsNC6JNGqsgKdSTgjaKVjyTDLMDLiXKM'
TWITTER_ACCESS_TOKEN_SECRET = 'GdeRJ504DoANMZqDuE02vO4XFPJcux4pUzzqTCa3Gg6Oj'

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.cursor(t.search, q='#trump',
                  # **supply whatever query you want here**
                  count=15000, lang='en')

# tweets = search['statuses']

for tweet in search:
    # print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
    # print tweet
    # with open('data.txt', 'w') as outfile:
    #     json.dump(tweet, outfile)

    # tweet description
    tweet = {
        'text': tweet['text'],
        'retweet_count': tweet['retweet_count'],
        'favorite_count': tweet['favourite_count'],
        'created_at': tweet['created_at']
    }
    # print tweet['text'], '\n'
    # print tweet['retweet_count'], '\n'
    # print tweet['favorite_count']
    # print tweet['created_at']
    print "################### mentions"
    # user mentions
    mentions = []
    for user_t in tweet['entities']['user_mentions']:
        if tweet['user']['screen_name'] != user_t['screen_name']:
            user = t.show_user(screen_name=user_t['screen_name'])
            receiver = {
                'name': user['name'],
                'screen_name': user['screen_name'],
                'location': user['location'],
                'favourites_count': user['favourites_count'],
                'followers_count': user['followers_count'],
                'friends_count': user['friends_count'],
                'lang': user['lang'],
                'geo_enabled': user['geo_enabled'],
                'description': user['description'],
            }

            # print user['name']
            # print user['screen_name']
            # print user['location']
            # print user['favourites_count']
            # print user['followers_count']
            # print user['friends_count']
            # print user['lang']
            # print user['geo_enabled']
            # print user['description']
            mentions.append(receiver)

    print "################### user infor"
    # user info
    sender = {
        'name': tweet['user']['name'],
        'screen_name': tweet['user']['screen_name'],
        'location': tweet['user']['location'],
        'favourites_count': tweet['user']['favourites_count'],
        'followers_count': tweet['user']['followers_count'],
        'friends_count': tweet['user']['friends_count'],
        'lang': tweet['user']['lang'],
        'geo_enabled': tweet['user']['geo_enabled'],
        'description': tweet['user']['description'],
    }
    print tweet['user']['name']
    print tweet['user']['screen_name']
    print tweet['user']['location']
    print tweet['user']['favourites_count']
    print tweet['user']['followers_count']
    print tweet['user']['friends_count']
    print tweet['user']['lang']
    print tweet['user']['geo_enabled']
    print tweet['user']['description']
    # is reply
    if tweet['in_reply_to_status_id']:
        user = t.show_user(screen_name=user_t['in_reply_to_screen_name'])
        print user['name']
        print user['screen_name']
        print user['location']
        print user['favourites_count']
        print user['followers_count']
        print user['friends_count']
        print user['lang']
        print user['geo_enabled']
        print user['description']
        status = t.showStatus(id=tweet['in_reply_to_status_id'])
        print status['text'], '\n'
        print status['retweet_count'], '\n'
        print status['favorite_count']
