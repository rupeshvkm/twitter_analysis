import tweepy
from datetime import datetime,timedelta

auth = tweepy.OAuthHandler("JpvjnTn6SEC50OiFjYfTkRqFl","WIudFHDtQzKPJtYMy95n8XS5e1S6CFbJsNfsoM0uQPssYSGaxI")
auth.set_access_token("182743223-egRe2H0SsnnYPdPae5vImLr3XRMDguBfHkny8ppD","WHGekA93XasB4oN3QdwlQ24R9I4UY8Qn361o6HSk6siCG")

api = tweepy.API(auth,wait_on_rate_limit=True)

#user_tweets = api.user_timeline(screen_name = 'ssrajamouli',count = 5)

#home_tweets = api.home_timeline(count = 5)

now = datetime.now()
end = now
start = now - timedelta(hours=48)

tweets = []
str = ""
for c in start.__str__():
    if c.isalnum():
        str += c

f = open("data/"+str+".txt",'w+',encoding="utf-8")
trend_tweets = api.search(q = ["corona"], lang = 'en',count = 100000)

for t in trend_tweets:
    if (t.created_at >= start) :
        msg = t.text
        tweets.append(msg)
        f.writelines(msg.__str__())


print(tweets)