from __future__ import unicode_literals

# from django.db import models
from neo4django.db import models
from neo4django import Property
# Create your models here.


class User(models.NodeModel):
    name = models.StringProperty()
    screen_name = models.StringProperty()
    location = models.StringProperty()
    lang = models.StringProperty()
    favourites_count = models.IntegerProperty()
    followers_count = models.IntegerProperty()
    friends_count = models.IntegerProperty()
    description = models.StringProperty()


class Tweet(models.NodeModel):
    text = models.StringProperty()
    retweet_count = models.IntegerProperty()
    favourites_count = models.IntegerProperty()
    date = models.DateTimeProperty()
    user_id = models.Relationship(User,
                                  rel_type='sends',
                                  single=True,
                                  related_name='tweets'
                                  )

    mention_ids = models.Relationship(User,
                                      rel_type='received',
                                      related_name='tweets_received'
                                      )
    arousal = models.FloatProperty()
    valence = models.FloatProperty()


class FloatProperty(Property):

    def get_default(self):
        return 0.0

    def to_neo(self, value):
        return float(value)
