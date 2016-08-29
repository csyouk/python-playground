import time

def cb(ch, method, properties, body):
  print(" [x] Received %r" % body)
  time.sleep(body.count(b'.'))
  print(" [x] Done")


print(" [*] Waiting for messages. To exit press CTRL+C")
