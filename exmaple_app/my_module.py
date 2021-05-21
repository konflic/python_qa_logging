import logging
import sys

# Passing name to logger with __name__ variable

# logging.basicConfig(level="ERROR", filename="test.log")

logger = logging.getLogger(__name__)
f = logging.FileHandler(__name__)
logger.addHandler(f)
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
