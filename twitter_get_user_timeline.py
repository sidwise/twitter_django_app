import sys
import json
import time
from tweepy import Cursor 
from twitter_client import get_twitter_client
from py2neo import Graph, Node, Relationship


if __name__ == '__main__':
	user = sys.argv[1]
	client = get_twitter_client()

	fname = "user_timeline_{}.json1".format(user)

	with open(fname, 'w') as f:
		for page in Cursor(client.user_timeline, screen_name= user, count=200).pages(16):
			for status in page:
				f.write(json.dumps(status._json)+"\n")
print(sys.argv)

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
			graph.create(Relationship(tweet, "RETWEETS", retweet)) 

	def constraint(label, property):
		graph = Graph()
		schema = graph.schema
		if property not in schema.get_uniqueness_constraints(label):
			schema.get_uniqueness_constraints(label, property)

	constraint("Tweet", "id")
	constraint("User", "username")
	constraint("Hashtag", "name")

	since_id = -1

	while true:
		try:
			tweets= find_tweets(sys.argv[1], since_id=since_id)
			since_id= tweets[0].get('id')
			upload_tweets(tweets)
			time.sleep(60)

		except Exception as e:
			print(e)
			time.sleep(60)
			continue'''



