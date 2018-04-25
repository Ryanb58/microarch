from kafka import KafkaProducer


server = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=server)
print("sending 100 messages to kafka (topic: test)")
for num in range(100):
    message = "Message Number: {}".format(num)
    producer.send('test', value=bytes(message, 'utf-8'))

print("done")

print("Metrics:")
print(producer.metrics())
