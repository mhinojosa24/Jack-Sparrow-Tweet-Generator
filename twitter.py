import os
import dotenv


# dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env")) # Of course, replace by your correct path
# os.environ.update(dotenv)
from requests_oauthlib import OAuth1Session
print("dotenv should be shown here: ", dir(dotenv))
dotenv.load_dotenv('.env')

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


session = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)


# The URL endpoint to update a status (i.e. tweet)
url = 'https://api.twitter.com/1.1/statuses/update.json'

def tweet(status):
    # status = 'If you are reading this on Twitter, the API request worked!'
    resp = session.post(url, { 'status': status })
    # print("response ==> ", resp.text)
    return resp.text
