import logging

# Giving module custom name
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def super_sum(a, b):

    if b == 0:
        logger.warning("Never pass second variable as 0!")

    logger.info('Calculating super sum for arguments: {} and {}'.format(a, b))

    result = (a + b) * (a / b)

    logger.debug('Super sum is: {}'.format(result))

    return result
