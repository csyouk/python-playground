import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = conn.channel()

import pickle

def cb(ch, method, properties, body):
  print(" [x] Received %r" % body)


channel.basic_consume(cb, queue='hello',
    no_ack=True)

print(' [*] Waiting for messages, To exit press CTRL+C')

channel.start_consuming()
