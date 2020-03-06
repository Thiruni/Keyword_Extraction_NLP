import GetOldTweets3 as got
from datetime import datetime, timedelta
import tweepy
import traceback
data_set = []

def get_data_tweepy(user_name):
    consumer_key = ''
    consumer_secret_key = ''
    access_token = ''
    access_token_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    user = api.get_user(user_name)
    u_data = str(user.screen_name) + ' | ' + str(user.created_at) + ' | ' + str(user.followers_count) + ' | ' + \
             str(user.verified) + ' | ' + str(user.listed_count) + ' | ' + str(user.default_profile) + ' | ' + \
             str(user.statuses_count) + ' | ' + str(user.friends_count) + ' | ' + str(user.favourites_count) + ' | ' +\
             str(user.location) + ' | ' + str(user.description) + ' | ' +  str(user.url) + ' | ' + str(user.lang)
    return u_data


def getTweets(keyword_list):

    querySearchTerm = ''
    endDate = datetime.today().strftime('%Y-%m-%d')
    startDate = (datetime.today() - timedelta(days = 2000)).strftime('%Y-%m-%d')
    global counter
    tweetLimit = 200

    try:
        for elem in keyword_list:
            querySearchTerm = elem
            # print("querySearchTerm", querySearchTerm)
            tweetCriteria = got.manager.TweetCriteria().setQuerySearch(querySearchTerm) \
                .setSince(startDate) \
                .setUntil(endDate) \
                .setMaxTweets(tweetLimit)

            for index, x in enumerate(got.manager.TweetManager.getTweets(tweetCriteria)):
                datestring = str(x.date)
                user_data_tweepy = get_data_tweepy(x.username)
                type = datestring + ' | ' + str(x.id) + ' | ' + str(x.username) + ' | ' + x.text + ' | ' + str(x.retweets) + \
                       ' | ' + str(x.favorites) + ' | '+ str(x.geo) + user_data_tweepy
                print(type)
                data_set.append(type)
            print("done for ", elem)
    except Exception:
        traceback.print_exc()
        print("Something went wrong")
    finally:
        write_file(data_set)


def write_file(data_list):
    try:
        print("Started writing file")
        f = open("collected_tweetsT2.txt", "w+", encoding="utf-8")
        f.write("date | id | username | text | retweets | favorites | geo | screen_name | created_at | followers_count |"
                " verified | listed_count | default_profile | statuses_count | friends_count | favorites_count | location "
                "| description | url | lang\n")
        for i in range(len(data_list)):
            record = str(data_list[i])
            f.write("%s\n" % record)
    except Exception:
        traceback.print_exc()
        print("Something went wrong when writing file ")
    finally:
        f.close()
