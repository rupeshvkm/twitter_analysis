import tweepy
import KafkaProducer as kp

auth = tweepy.OAuthHandler("JpvjnTn6SEC50OiFjYfTkRqFl","WIudFHDtQzKPJtYMy95n8XS5e1S6CFbJsNfsoM0uQPssYSGaxI")
auth.set_access_token("182743223-egRe2H0SsnnYPdPae5vImLr3XRMDguBfHkny8ppD","WHGekA93XasB4oN3QdwlQ24R9I4UY8Qn361o6HSk6siCG")

api = tweepy.API(auth)

user_tweets = api.user_timeline(screen_name = 'ssrajamouli',count = 5)

home_tweets = api.home_timeline(count = 5)

trend_tweets = api.search(q = ["#BheemforRamaraju"], lang = 'en',count = 5)


#kp.publish(msg,"tweet_topic")

for t in trend_tweets:
    #t.user.id,
    msg = t.text
    print(msg)
    kp.publish(msg,"tweet_topic")
