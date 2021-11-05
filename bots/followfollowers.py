# automatically follows anyone who follows me
import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def follow_followers(api):
    logger.info('Retrieving and following followers')

    for follower in tweepy.Cursor(api.get_followers).items():
        if not follower.following:
            logger.info(f'Following {follower.name}')
            follower.follow()


def main():
    api = create_api()

    while True:
        follow_followers(api)
        logger.info('Waiting for accounts to follow...')
        time.sleep(60)


if __name__ == '__main__':
    main()
