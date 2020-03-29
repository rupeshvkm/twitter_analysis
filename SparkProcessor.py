from pyspark.sql import SparkSession
import re

spark = SparkSession.builder.appName("tweet_analysis").master("local[*]").getOrCreate()
sc = spark.sparkContext

rdd = sc.textFile("data/")
words = rdd.flatMap(lambda l: re.sub('[^A-Za-z0-9# ]+','',l).split(" "))

tags = words.filter(lambda r: r.startswith('#')).map(lambda r: (r,1)).reduceByKey(lambda a,b : a+b).toDF(("tags","count"))

tags.repartition(1).write.option("header","true").csv("output/"+"coronavirusinindia/")



