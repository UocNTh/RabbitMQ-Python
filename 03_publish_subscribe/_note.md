
Gửi một tin nhắn đến nhiều customer 


Để minh hoạ, xây dựng một hệ thống ghi nhật lý.


Gồm 2 chương trình: 
- phát ra tin nhắn thông điệp  
- nhận và in 


---

Exchanges 

A producer : gửi messages

A queue 

A consumer : nhận message 


---

Một producer sẽ không gửi trực tiếp một message đến queue, và producer dũng không thể biết message đã được gửi đến một queue hay chưa.

Producer sẽ gửi message đến một exchange. Một exchange nhận message và đẩy message vào queue 

Một exchange sẽ biết chính xác phải làm gì với message (Gửi đến một queue???, Gửi đến nhiều queue??? Hoặc bỏ đi??? ) --> Những luật này được xác định trong exchange_type 


![m](https://raw.githubusercontent.com/UocNTh/Thuc_tap_VCCorp/9b58954fd6cd3755fbd08131aff294256adbe08b/RabbitMQ/Images/Screenshot%20from%202023-04-26%2009-36-54.png)




----
**Publish/Subscribe** gửi tin nhắn đến các customer trong cùng một lúc 



![m](https://github.com/UocNTh/Thuc_tap_VCCorp/blob/main/RabbitMQ/Images/Screenshot%20from%202023-04-26%2011-08-49.png?raw=true)
