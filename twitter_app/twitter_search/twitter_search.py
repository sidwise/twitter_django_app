import TwitterSearch as ts

try:
    tso = ts.TwitterSearchOrder()
    # create a TwitterSearchOrder object
    tso.set_keywords(['Trump'])
    # let's define all words we would like to have a look for
    tso.set_language('en')
    # we want to see English tweets only
    tso.set_include_entities(False)
    # and don't give us all those entity information # it's about time to
    # create a TwitterSearch object with our secret tokens
    print "Tessstttttttt"
    ts = ts.TwitterSearch(
        consumer_key='z0JO1aunGAWu0xgxtpOMiw2qx',
        consumer_secret='8vwUONvjOAfBcnNU9X1mtg9YJGPvDLjGZsZnbgs0CWhbOxYZDc',
        access_token='3021210887-iKtdExGlsNC6JNGqsgKdSTgjaKVjyTDLMDLiXKM',
        access_token_secret='GdeRJ504DoANMZqDuE02vO4XFPJcux4pUzzqTCa3Gg6Oj'
    )

    # this is where the fun actually starts :
    for tweet in ts.search_tweets_iterable(tso):
        # print('@%s tweeted: %s' % (
        #     tweet['user']['screen_name'],
        #     tweet['text']))
        print tweet

except ts.TwitterSearchException as e:
    # take care of all those ugly errors if there are some
    print(e)
