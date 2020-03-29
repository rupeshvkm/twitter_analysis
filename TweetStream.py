import tweepy
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


auth = tweepy.OAuthHandler("JpvjnTn6SEC50OiFjYfTkRqFl","WIudFHDtQzKPJtYMy95n8XS5e1S6CFbJsNfsoM0uQPssYSGaxI")
auth.set_access_token("182743223-egRe2H0SsnnYPdPae5vImLr3XRMDguBfHkny8ppD","WHGekA93XasB4oN3QdwlQ24R9I4UY8Qn361o6HSk6siCG")

api = tweepy.API(auth,wait_on_rate_limit=True)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

ts = myStream.filter(track=['#MannKiBaat'], is_async=True)

spark = SparkSession.builder.master("local[*]").appName("tweet_stream").getOrCreate()
sc = spark.sparkContext

ssc = StreamingContext(sc,5)
