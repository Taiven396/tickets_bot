from loguru import logger


def create_logs():
    logger.add('logs/bot.log',
               rotation='100MB',
               enqueue=True)
