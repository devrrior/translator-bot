import tweepy
from logger_case import logger
from credentials import CREDENTIALS

def create_api():
    consumer_key = CREDENTIALS['CONSUMER_KEY']
    consumer_secret = CREDENTIALS['CONSUMER_SECRET']
    access_token = CREDENTIALS['ACCESS_TOKEN']
    access_secret = CREDENTIALS['ACCESS_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API")
        raise e
    logger.info("API created")
    return api

if __name__ == '__main__':
    create_api()