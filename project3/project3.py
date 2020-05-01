#A script that gets the text & date of the last 5 public statuses from a Twitter user.
import twitter, os

#Authenticate with API using environment variables
api = twitter.Api(consumer_key=os.getenv('API_ConsumerKey'),
                  consumer_secret=os.getenv('API_ConsumerSecret'),
                  access_token_key=os.getenv('API_AccessTokenKey'),
                  access_token_secret=os.getenv('API_AccessTokenSecret'))

#ask user what they want
print('What user did you want to check?')
name = input()


#Call API
statuses = api.GetUserTimeline(screen_name=name, count=5)


print(statuses[0])



for i in range(0, 5):
    iPlusOne = i + 1
    print('Status %s:' % (iPlusOne))
    print('=========')
    print(statuses[i].created_at)
    print(statuses[i].text)
    print()
