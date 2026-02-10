import logging

# Format attributes for logger messages
# https://docs.python.org/3/library/logging.html#logrecord-attributes

print("code")

logger1 = logging.getLogger("logger1")

logger1.warning("This when first event was logged.")  # disable second

print("code2")

logger2 = logging.getLogger("logger2")

# logger2.basicConfig(format='%(asctime)s %(levelname)s %(filename)s %(message)s')
logger2.warning("This is when second event was logged.")

print("code3")
