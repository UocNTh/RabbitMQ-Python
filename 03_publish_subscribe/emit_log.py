import pika, sys
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel() 

# fanout: phát ra tất cả các tin nhắn mà nó nhận được 
# đến tất cả hàng đợi mà nó biết

channel.exchange_declare(exchange='03_logs', exchange_type='fanout')

number = random.randint(1,100) 

message = ' '.join(sys.argv[1:]) or str(number)

channel.basic_publish(exchange='03_logs', routing_key='', body=message)
 
print('Sent')

connection.close() 