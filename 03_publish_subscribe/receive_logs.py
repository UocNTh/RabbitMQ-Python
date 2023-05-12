import pika , sys, os 

def main() : 
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) 

    channel = connection.channel() 

    channel.exchange_declare(exchange='03_logs', exchange_type='fanout')

    # khi để queue='' và exexclusive=True thì sẽ tạo ra một queue mới, rỗng
    queue = channel.queue_declare(queue = '',exclusive=True)
    
    # lấy tên queue 
    queue_name = queue.method.queue 
    
    # gửi tin nhắn đến tất cả các queue mà exchange biết (exchange_type='fanout')
    # tạo một ràng buộc 
    # một ràng buộc là mội mối quan hệ giữa exchange và queue 
    channel.queue_bind(exchange='03_logs', queue=queue_name)

    print('Waiting. To exit press CRTL+C')

    def callback(ch , method, properties, body) : 
        print("Receive %r" % body) 


    channel.basic_consume(queue=queue_name,on_message_callback=callback, auto_ack=True) 

    channel.start_consuming()


if __name__ == '__main__' : 
    try : 
        main() 

    except KeyboardInterrupt : 
        try : 
            sys.exit(0)

        except: 
            os._exit(0) 