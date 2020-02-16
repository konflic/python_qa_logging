import logging

# https://docs.python.org/3/library/logging.html#logrecord-attributes

logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')

logging.basicConfig(format='%(filename)s %(filename)s')
logging.warning('is when this event was logged.')