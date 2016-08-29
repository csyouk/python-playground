import sys
import pika

msg = ' '.join(sys.argv[1:]) or "Hello world!"

channel.basic_publish(exchange='',
    routing_key='task_queue',
    body=msg,
    properties=pika.BasicProperties(
      delivery_mode = 2,
      ))

print(" [x] Send %r" % msg)


