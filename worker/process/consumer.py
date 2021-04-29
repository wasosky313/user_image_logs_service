import pika

from worker.config import MQ_CONNECTION

connection = pika.BlockingConnection(pika.ConnectionParameters(host=MQ_CONNECTION))
channel = connection.channel()


def start_consuming():
    method_frame, header_frame, body = channel.basic_get('user_image_api_logg')
    if method_frame:
        channel.basic_ack(method_frame.delivery_tag)
    return body

