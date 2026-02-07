import asyncio

from src.config import settings
from src.infrastructure.logger.impl import logger
from src.infrastructure.messaging.consumer import KafkaConsumer
from src.infrastructure.messaging.kafka_router import KafkaMessageRouter
from src.infrastructure.uow.impl import get_uow


async def start_app():
    logger.info('Start app...')
    await KafkaMessageRouter(get_uow(), KafkaConsumer(settings), logger).run()


if __name__ == '__main__':
    try:
        asyncio.run(start_app())
    except Exception:
        raise
    finally:
        logger.info('App shutdown')
