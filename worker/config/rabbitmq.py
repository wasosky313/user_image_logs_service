import pika
from loguru import logger
from pika.exceptions import AMQPConnectionError

from worker.config import MQ_CONNECTION

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(MQ_CONNECTION))
    channel = connection.channel()
    channel.queue_declare(queue='user_image_api_logg')
except AMQPConnectionError:
    logger.error("SERVER IS DOWN")
