import logging
from . import my_module

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('compose_logger_example')

logger.info('====== Started ======')
print(my_module.super_sum(10, 50))
print(my_module.list_to_dict(['1', 10, None]))
logger.info('====== Finished ======')
