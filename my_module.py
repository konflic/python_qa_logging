import logging

logger = logging.getLogger(__name__)

def super_sum(a, b):
    logger.info('Calculating super sum for arguments: {} and {}'.format(a, b))
    result = (a + b) * (a / b)
    logger.debug('Super sum is: {}'.format(result))
    return result


def list_to_dict(l: list):
    res = {}
    logger.info('Creating dict from list {}'.format(l))
    for el in l:
        logger.debug('Adding {} as a key to dict'.format(str(el)))
        res[str(el)] = el
        logger.debug('Current dict is {}'.format(res))
    logger.info('Creating dict finished'.format(l))
    return res
