import tweepy
import time
from logger_case import logger
from config import create_api
from translate import translate_text

def check_mentions(api, since_id):
    logger.info('Retrieving mentions')
    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id,).items():
        new_since_id = max(tweet.id, new_since_id)
        logger.info(tweet.user.screen_name)

        if tweet.in_reply_to_status_id is not None:
            continue
        api.update_status(
            status = translate_text(tweet.user.screen_name, tweet.text),
            in_reply_to_status_id=tweet.id,
        )

    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()