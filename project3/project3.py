import twitter, os

#Call Twitter API, autheticate with env variables
api = twitter.Api(consumer_key=os.getenv('API_ConsumerKey'),
                  consumer_secret=os.getenv('API_ConsumerSecret'),
                  access_token_key=os.getenv('API_AccessTokenKey'),
                  access_token_secret=os.getenv('API_AccessTokenSecret'))

statuses = api.GetUserTimeline(25073877)
#print([s.text for s in statuses])