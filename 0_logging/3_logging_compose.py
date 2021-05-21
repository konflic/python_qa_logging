import logging
import time

from exmaple_app import my_module, my_math

# logging.basicConfig(level=logging.INFO) #  Control output
logger = logging.getLogger(__name__)

f = logging.FileHandler('compose_logger_example.log')
logger.addHandler(f)
logger.setLevel(logging.DEBUG)

logger.info('====== Started: {} ======'.format(int(time.time())))

my_math.super_sum(10, 20)
time.sleep(0.5)
my_module.list_to_dict(['1', 10, None])

logger.info('====== Finished: {} ======'.format(int(time.time())))
