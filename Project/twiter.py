import matplotlib.pyplot as plt
import numpy as np
from Twiter_API import TwitterClient

# Main Program Start
if __name__ == "__main__":
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query='CA Technology', count=100000)
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    # print("Total tweets percentage: {}".format(100 * len(tweets)))
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    # print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    # percentage of neutral tweets
    # print("Neutral tweets percentage: {} %".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))
    ps = len(ptweets) / len(tweets)
    ns = len(ntweets) / len(tweets)
    nn = (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)
    tt = len(tweets)

    # Ploting into bar graph
    titles = ("+Ve","-Ve","Neutral")
    weights = [ps,ns,nn]
    y_pos = np.arange(len(titles))

    plt.bar(y_pos,weights, align="center", alpha=0.5)
    plt.xticks(y_pos,titles)
    plt.ylabel("% of feedbacks")
    plt.title("Sentiment anylysis Result")
    plt.show()




















