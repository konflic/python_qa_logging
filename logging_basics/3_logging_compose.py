import logging
import time

from logging_basics.exmaple_app import my_module, my_math

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.info('====== Started: {} ======'.format(int(time.time())))

my_math.super_sum(10, 20)
my_module.list_to_dict(['1', 10, None])
my_math.super_sum(10, 211)

logger.info('====== Finished: {} ======'.format(int(time.time())))
