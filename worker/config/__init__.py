import os

TITLE = "Worker for User Image System logs"
DESCRIPTION = "Service to store the logs of user-image-api,"
VERSION = "1.0.0"

# DATABASE
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "user_image_db")
DB_USER = os.environ.get("DB_USER", "user_image")
DB_PASS = os.environ.get("DB_PASS", "user_image_2021")
DB_SCHEMA = "user_system_image"

# RabbitMQ
MQ_CONNECTION = os.environ.get("MQ_CONNECTION", "localhost")
MQ_TIMESLEEP = os.environ.get("MQ_TIMESLEEP", 0.5)
