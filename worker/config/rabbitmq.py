import pika

from worker.config import MQ_CONNECTION

# fazer tratamiento de error connect fila con logoru
connection = pika.BlockingConnection(pika.ConnectionParameters(MQ_CONNECTION))
channel = connection.channel()
channel.queue_declare(queue='user_image_api_logg')
