import json
import time

from loguru import logger
from pika.exceptions import AMQPConnectionError

from worker.config import MQ_TIMESLEEP
from worker.data.database import add_logged
from worker.process.consumer import start_consuming


def start():
    try:
        while True:
            message = start_consuming()
            if message:
                json_logger = json.loads(message)
                add_logged(json_logger)
                logger.info(f"SAVING LOGGER IN DATABASE: {json_logger}")
            logger.info(f"WORKER RUNNING AT {time.time()}")

            time.sleep(MQ_TIMESLEEP)
    except AMQPConnectionError:
        logger.error("QUEUE SERVER CONNEXION: IS DOWN")
