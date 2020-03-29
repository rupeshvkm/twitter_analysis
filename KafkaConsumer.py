from kafka import KafkaConsumer

consumer = KafkaConsumer("tweet_topic",
                         bootstrap_servers='localhost:9092',
                         group_id=None,
                         enable_auto_commit=False,
                         #auto_offset_reset='earliest'
                         )

for message in consumer:
    print(message.value)