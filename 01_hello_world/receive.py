import pika, sys , os 
import time


def main() : 
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel = connection.channel()

    # khai báo một queue 
    channel.queue_declare(queue='hello_world') 

    # khi nhận được message thì hàm callback sẽ được gọi bởi 
    # thư viện pika

    # hàm callback là chuỗi hành động xử lý khi nhận được message
    def callback(ch, method, properties, body) : 
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello_world',on_message_callback=callback, auto_ack=True) 

    print('Waiting. To exit press CTRL+C') 

    channel.start_consuming() 


if __name__ == '__main__' : 
    try: 
        main() 
    except KeyboardInterrupt : 
        try: 
            sys.exit(0)
        except SystemExit : 
            os._exit(0) 

