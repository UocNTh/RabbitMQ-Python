import pika, os, sys 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) 

channel = connection.channel()

channel.exchange_declare(exchange='emit_logs_direct',exchange_type='direct') 

queue = channel.queue_declare( queue='', exclusive=True)

queue_name = queue.method.queue 

characteristics = sys.argv[1:]

for characteristic in characteristics : 
    channel.queue_bind(queue=queue_name, exchange='emit_logs_direct', routing_key=characteristic) 

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % ( method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()