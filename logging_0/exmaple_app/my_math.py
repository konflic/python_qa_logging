import logging

# Giving module custom name
logger = logging.getLogger(__name__)

# Add custom file handler
f = logging.FileHandler(filename="my_math.log")
logger.addHandler(f)
logger.setLevel(logging.DEBUG)


def super_sum(a, b):
    if b == 0:
        logger.warning("Never pass second variable as 0!")
    logger.info('Calculating super sum for arguments: {} and {}'.format(a, b))
    result = (a + b) * (a / b)
    logger.debug('Super sum is: {}'.format(result))
    return result
