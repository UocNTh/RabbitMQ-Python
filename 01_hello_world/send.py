# thư viện pika dùng để tạo và quản lý đến rabbitmq 

import pika 

# send.py là chương trình gửi message đến queue 
# tạo một kết nối đồng bộ đến rabbitmq


# ConnectionParameters đại hiện cho các thông tin 
# cấu hình rabbitmq gồm tên host và các 
# thông số kết nối khác vd tên, mật khẩu

# BlockingConnection dùng để tạo một kết nối đồng bộ 
# đến rabbitmq sử dụng các thông tin của CoonectionParagrameters
# để cấu hình

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) 

channel = connection.channel() 

# khai báo một queue 
channel.queue_declare(queue='hello_world')

# thực hiện gửi message
channel.basic_publish(exchange='',
                      routing_key='hello_world',
                      body='Hello World') 

print('Sent') 

connection.close() 