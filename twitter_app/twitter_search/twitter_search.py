from twython import Twython
import json

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
    print tweet['text'], '\n'
    print tweet['retweet_count'], '\n'
    print tweet['favorite_count']

    print "################### mentions"
    # user mentions
    for user_t in tweet['entities']['user_mentions']:
        if tweet['user']['screen_name'] != user_t['screen_name']:
            user = t.show_user(screen_name=user_t['screen_name'])
            print user['name']
            print user['screen_name']
            print user['location']
            print user['favourites_count']
            print user['followers_count']
            print user['friends_count']
            print user['lang']
            print user['geo_enabled']
            print user['description']
    print "################### user infor"
    # user info
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

    # import TwitterSearch as ts

    # try:
    #     tso = ts.TwitterSearchOrder()
    #     # create a TwitterSearchOrder object
    #     tso.set_keywords(['Trump'])
    #     # let's define all words we would like to have a look for
    #     tso.set_language('en')
    #     # we want to see English tweets only
    #     tso.set_include_entities(False)
    #     # and don't give us all those entity information # it's about time to
    #     # create a TwitterSearch object with our secret tokens
    #     print "Tessstttttttt"
    #     ts = ts.TwitterSearch(
    #         consumer_key='z0JO1aunGAWu0xgxtpOMiw2qx',
    #         consumer_secret='8vwUONvjOAfBcnNU9X1mtg9YJGPvDLjGZsZnbgs0CWhbOxYZDc',
    #         access_token='3021210887-iKtdExGlsNC6JNGqsgKdSTgjaKVjyTDLMDLiXKM',
    #         access_token_secret='GdeRJ504DoANMZqDuE02vO4XFPJcux4pUzzqTCa3Gg6Oj'
    #     )

    #     # this is where the fun actually starts :
    #     for tweet in ts.search_tweets_iterable(tso):
    #         print('@%s tweeted: %s' % (
    #             tweet['user']['screen_name'],
    #             tweet['text']))
    #         # print tweet

    # except ts.TwitterSearchException as e:
    #     # take care of all those ugly errors if there are some
    #     print(e)
