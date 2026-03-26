import logging
from logging.handlers import RotatingFileHandler, QueueHandler, QueueListener
from queue import Queue

def setup_logging(app):
    log_queue = Queue(-1)

    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=10_000_000,
        backupCount=5
    )

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s pid=%(process)d %(message)s"
    )
    file_handler.setFormatter(formatter)

    queue_handler = QueueHandler(log_queue)
    listener = QueueListener(log_queue, file_handler)
    listener.start()

    app.logger.handlers.clear()
    app.logger.addHandler(queue_handler)
    app.logger.setLevel(logging.INFO)
