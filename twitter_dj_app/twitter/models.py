# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tweet(models.NodeModel):
    id_str = models.IntegerProperty()
    text = models.StringProperty()
    retweet_count = models.IntegerProperty()
    favourites_count = models.IntegerProperty()
    created_at = models.DateTimeProperty()
    lemm = models.StringProperty()
    valence = models.FloatProperty()
    arousal = models.FloatProperty()
    emotion = models.StringProperty()

	retweets = models.Relationship(Tweet,
                                  rel_type='sends',
                                  single=True,
                                  related_name='retweets'
                                  )

    reply_to = models.Relationship(Tweet,
                                      rel_type='received',
                                      related_name='reply_to'
                                      )
    contains = models.Relationship(Url,
                                      rel_type='received',
                                      related_name='contains'
                                      )
    mentions = models.Relationship(User,
                                      rel_type='received',
                                      related_name='mentions'
                                      )
    using = models.Relationship(Source,
                                      rel_type='received',
                                      related_name='using'
                                      )

    

class User(models.NodeModel):
    name = models.StringProperty()
    screen_name = models.StringProperty()
    location = models.StringProperty()
    lang = models.StringProperty()
    favourites_count = models.IntegerProperty()
    followers_count = models.IntegerProperty()
    friends_count = models.IntegerProperty()
    description = models.StringProperty()
	geo_enabled = Property()
    
	posts = models.Relationship(Tweet,
                                      rel_type='received',
                                      related_name='posts'
                                      )
    
class Hashtag(models.NodeModel):

    hashtag = models.StringProperty()

    tags = models.Relationship(Tweet,
                                      rel_type='received',
                                      related_name='tags'
                                      )

class Source(models.NodeModel):

    name = models.StringProperty()

    

class Url(models.NodeModel):

    tweet_url = models.StringProperty()



    