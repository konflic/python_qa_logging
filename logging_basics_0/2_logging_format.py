import logging

# Format attributes for logger messages
# https://docs.python.org/3/library/logging.html#logrecord-attributes

logging.basicConfig(format='%(asctime)s %(message)s')  # disable first
logging.warning('This when first event was logged.')  # disable second

logging.basicConfig(format='%(asctime)s %(levelname)s %(filename)s %(message)s')
logging.warning('This is when second event was logged.')
