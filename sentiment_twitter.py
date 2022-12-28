import tweepy, json, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()

twitter_access_token = []
twitter_access_token_secret = []
twitter_consumer_key = []
twitter_consumer_secret = []

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

news_sources = ("@BBC", "@ctvnews", "@CNN", "@FoxNews", "@dawn_com")

array_sentiments = []

for user in news_sources:
    count_tweet = 100
    print("Poczatek wiadomosci z %s" % user)
    for x in range(5):
        public_tweets = api.user_timeline(user, page=x)
        for tweet in public_tweets:
            compound = analyzer.polarity_scores(tweet["text"])["compound"]
            pos = analyzer.polarity_scores(tweet["text"])["pos"]
            neu = analyzer.polarity_scores(tweet["text"])["neu"]
            neg = analyzer.polarity_scores(tweet["text"])["neg"]

            array_sentiments.append({"Media": user,
                                     "Tweet Text": tweet["text"],
                                     "Positive": pos,
                                     "Negative": neg,
                                     "Neutral": neu,
                                     "Date": tweet["created_at"],
                                     "Tweets Ago": count_tweet})
            count_tweet -= 1
            print("Koniec pobierania tweetow")

for media in source:
    mydf = sentiments_df[sentiments_df["Media"] == media]
    plt.scatter(mydf["Tweets Ago"], mydf["Compound"], marker="o", linewidth=0, aplha=0.8, label=media,
                facecolors=mydf.Media.map({"BBC": "pink", "ctvnews": "purple", "CNN": "red",
                                           "FoxNews": "blue", "dawn_com": "green"}))

plt.legend(bbox_to_anchor=(1, 1), title="Media Sources")
plt.title("Sentiment Analysis of Media Tweets (%s)" % (time.strftime("%s")), fontsize=14)
plt.xlabel("Tweets Ago")
plt.ylabel("Tweet Polarity")
plt.xlim(101, 0)
plt.ylim(-1, 1)
plt.grid(True)
plt.savefig("Output/Sentiment Analysis of Media Tweets.png", bbox_inches='tight')
plt.show()

means_media_trends = sentiments_df.groupby("Media").mean()["Compound"].to_frame()
means_media_trends.reset_index(inplace=True)
print(means_media_trends)
