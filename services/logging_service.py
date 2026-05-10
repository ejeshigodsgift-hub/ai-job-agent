import logging

logging.basicConfig(
    filename='storage/logs/system.log',
    level=logging.INFO
)


def log_activity(message):
    logging.info(message)