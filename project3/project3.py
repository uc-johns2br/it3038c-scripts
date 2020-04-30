from routes import app
import twitter, os, requests

from routes import app

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
    

#Call Twitter API, autheticate with env variables
#api = twitter.Api(consumer_key=os.getenv('API_ConsumerKey'),
#                  consumer_secret=os.getenv('API_ConsumerSecret'),
#                  access_token_key=os.getenv('API_AccessTokenKey'),
#                  access_token_secret=os.getenv('API_AccessTokenSecret'))


#statuses = api.GetUserTimeline(user_id=25073877, count=5)

#print([s.text for s in statuses])