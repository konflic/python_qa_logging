import logging
import my_module

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('====== Started ======')
my_module.super_sum(10, 50)
my_module.list_to_dict(['1', 10, None])
logger.info('====== Finished ======')
