from py2neo import Graph, Node, Relationship
graph = Graph()
fouzia = Node("Person", name = "Fouzia4")
graph.create(fouzia)
meriem = Node("Person", name = "Meriem4")
graph.create(meriem)

graph.create(Relationship(fouzia, "FRIENDS4", meriem))

'''def upload_tweets(tweets):
	graph = Graph()

	for t in tweets:
		u = t['user']
		e = t['entities']

		tweet = graph.merge_one("Tweet", "id", t['id'])
		tweet.properties['text']=t['text']
		tweet.push()

		user = graph.merge_one("User", "username", u['screen_name'])
		graph.create(Relationship(user, "POSTS", tweet))

		for h in e.get('hashtags', []):
			hashtag = graph.merge_one("Hashtag", "name", h['text'].lower())
			graph.create(Relationship(hashtag, "TAGS", tweet))

		for m in e.get('user_mentions', []):
			mention = graph.merge_one("User", "username", m['screen_name'])
			graph.create(Relationship(tweet, "MENTIONS", mention))

		reply = t.get('in_reply_to_status_id') 
		if reply : 
			reply_tweet = graph.merge_one("Tweet", "id", reply)
			graph.create(Relationship(tweet, "REPLY_TO", reply_tweet))

		r = t.get('retweeted_status', {})
		r = r.get('id')

		if r:
			retweet= graph.merge_one("Tweet", "id", r)
			graph.create(Relationship(tweet, "RETWEETS", retweet)) '''
