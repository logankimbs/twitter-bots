# automatically likes and retweets tweets that match a certain criteria
import tweepy
from config import create_api


class FavRetweetListener(tweepy.Stream):
    def on_status(self, status):
        print(status.text)


def main(keywords):
    api = create_api()
    tweet_listener = FavRetweetListener(
        api.auth.consumer_key, api.auth.consumer_secret,
        api.auth.access_token, api.auth.access_token_secret
    )

    tweet_listener.filter(track=keywords, languages=["en"])


if __name__ == '__main__':
    main(["Python"])
