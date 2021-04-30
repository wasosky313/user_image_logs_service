from loguru import logger
from pika.exceptions import AMQPConnectionError

from worker import start

try:
    start()
except AMQPConnectionError:
    logger.error("QUEUE SERVER CONNEXION IS DOWN")
