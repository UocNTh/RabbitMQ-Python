Trong thư mục Hello_World

- Giả sử mở 1 terminal send.py và 2 terminal receive.py 

- Khi thực hiện gửi một message đến thì 2 terminal sẽ thay phiên nhau lấy message và xử lý 

- Nếu giả sử trong trường hợp một task mất thời gian để xử lý, trong thời gian xử lý mà terminal đang xử lý bị tắt mất sẽ dẫn đến hậu quả là message sẽ bị mất. 

![m](https://github.com/UocNTh/Thuc_tap_VCCorp/blob/main/RabbitMQ/Images/Screenshot%20from%202023-04-25%2016-47-28.png?raw=true)


- Khi xử lý một task mất nhiều thời gian, khi rabbitmq chuyển message đến customer, nó đánh dấu để xóa ngay lập tức. Vì vậy khi dừng một worker, mà worker đó đang trong quá trình xử lý message thì message sẽ bị mất. (```auto_ack = True``` trong channel.basic_consume() (ack : acknowledgement )) 

--> Nếu một worker bị dừng, mà không muốn mất message ???? 


Khi không sử dụng auto_ack thì cần gửi ack tới rabbitmq sau khi xử lý message để đảm báo rabbitmq sẽ xóa message khởi queue. Nếu không message sẽ không được xóa khởi queue và sẽ được xử lý tại worker khác. Cần thiết lập một ```basic_ack```





---

**Work Queues** hướng dẫn phân phối đến tin nhắn đến cho các worker xử lý 