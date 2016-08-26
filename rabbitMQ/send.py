import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()

channel.queue_declare(queue='hello')

def body():
  return "body"

class Test:
  a = 3;
  b = 4;

t = Test()
import pickle
result = pickle.dumps(t)

def invoke():
  channel.basic_publish(exchange='',
      routing_key='hello',
      body='halo world')
  print("[x] send 'halo world'")

import time 
for _ in range(100):
  time.sleep(1)
  invoke()



conn.close()
