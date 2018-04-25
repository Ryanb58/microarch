from kafka import KafkaConsumer

server = 'localhost:9092'

consumer = KafkaConsumer(
    'test',
    bootstrap_servers=server)

try:
    for msg in consumer:
        print (msg)
except KeyboardInterrupt:
    print("Metrics:")
    print(consumer.metrics())
