import pika
from pika.exceptions import AMQPConnectionError, ChannelClosedByBroker, DuplicateGetOkCallback
from loguru import logger

from worker.config import MQ_CONNECTION

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=MQ_CONNECTION))
    channel = connection.channel()
except AMQPConnectionError:
    logger.error("QUEUE SERVER CONNEXION IS DOWN")


def start_consuming():
    try:
        method_frame, header_frame, body = channel.basic_get('user_image_api_logg')
        if method_frame:
            channel.basic_ack(method_frame.delivery_tag)
        return body
    except AMQPConnectionError:
        logger.error("QUEUE SERVER CONNEXION IS DOWN")
    except NameError:
        logger.error("QUEUE SERVER CONNEXION IS DOWN")
    except ChannelClosedByBroker:
        logger.error("QUEUE FOR CONSUMER NO EXIST")
    except DuplicateGetOkCallback:
        logger.error("QUEUE FOR CONSUMER NO EXIST")
