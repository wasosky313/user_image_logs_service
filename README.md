# user_image_logs_service
Create a service to store the logs of user-image-api.


# For run this application

1- Server PostgreSQL and Server RabbitMQ https://github.com/wasosky313/infrastructure

2- git clone https://github.com/wasosky313/user_image_logs_service.git

3- cd user_image_logs_service

4- docker build -t worker .

6- docker run -e DB_HOST='your host database address' -e MQ_CONNECTION='your host RabbitMQ address' -t worker

For Example docker run -e DB_HOST='192.168.1.104' -e MQ_CONNECTION='192.168.1.104' -t worker 
