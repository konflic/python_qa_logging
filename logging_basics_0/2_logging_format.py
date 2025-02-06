import logging

# Format attributes for logger messages
# https://docs.python.org/3/library/logging.html#logrecord-attributes

print("code")

logger1 = logging.getLogger("logger1")

logging.basicConfig(format='%(message)s')  # disable first
logging.warning('This when first event was logged.')  # disable second

print("code2")

logger2 = logging.getLogger("logger2")

logging.basicConfig(format='%(asctime)s %(levelname)s %(filename)s %(message)s')
logging.warning('This is when second event was logged.')

print("code3")