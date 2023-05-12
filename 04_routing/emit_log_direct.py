import pika, sys 
import random 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) 

channel = connection.channel() 

channel.exchange_declare(exchange='emit_logs_direct', exchange_type='direct') 

number = random.randint(1,100) 

message = str(number)

if number % 2 == 0 :  
    characteristic = 'odd' 
else : 
    characteristic = 'even' 


channel.basic_publish(exchange='emit_logs_direct',routing_key=characteristic,body=message)

print('Sent') 

channel.close() 