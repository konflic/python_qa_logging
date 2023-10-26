import logging
import sys

# Passing name to logger with __name__ variable
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def list_to_dict(l: list):
    res = {}

    logger.error('This is example error')
    logger.info('Creating dict from list {}'.format(l))

    for el in l:

        logger.debug('Adding {} as a key to dict'.format(str(el)))
        res[str(el)] = el
        logger.debug('Current dict is {}'.format(res))

    logger.info('Creating dict finished'.format(l))

    return res


if __name__ == "__main__":
    print(list_to_dict([1, 2, 3]))
