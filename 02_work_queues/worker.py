import pika, sys , os 
import time
import random


def main() : 

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel = connection.channel()

    # khai báo một queue 

    # durable độ bền chặt, nếu giả sử rabbitmq bị dừng lại
    # thì message vẫn không bị mất
    channel.queue_declare(queue='task', durable=True ) 

    # khi nhận được message thì hàm callback sẽ được gọi bởi 
    # thư viện pika

    # hàm callback là chuỗi hành động xử lý khi nhận được message
  
    def callback(ch, method, properties, body) : 
        random_time = random.randint(1,10) 
        time.sleep(random_time)
        print(" [x] Received %r" % body)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    # gỉa sử khi có 2 worker đang hoạt động, messages lẻ nặng, và 
    # các messages chẵn nhẹ, điều này dẫn đến 1 worker làm việc
    # bận rộn và worker còn lại thì không có gì làm

    # giải pháp là sử dụng channel.basic_qos(prefetch_count=1): chỉ 
    # gửi không quá 1 messages cho 1 worker, nếu worker này bận thì
    # gửi sang worker còn lại

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task',on_message_callback=callback) 

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

