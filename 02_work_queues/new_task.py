import pika, sys 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) 

channel = connection.channel() 

# khai báo một queue 
channel.queue_declare(queue='task' ,durable=True) 

message = ' '.join(sys.argv[1:]) or 'Hello World!' 

# thực hiện gửi message
# delivrty_mode được sử dụng để xác định cách thức gửi messages
# pika.spec.PERSISTENT_DELIVERY_MODE trong trường hợp rabbitmq bị
# mất thì message không bị mất

channel.basic_publish(exchange='',
                      routing_key='task',
                      body=message, 
                      properties=pika.BasicProperties(
                        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      )) 

print('Sent') 

connection.close() 