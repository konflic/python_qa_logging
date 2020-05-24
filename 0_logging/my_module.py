import logging

# Хорошей практикой является указание на то что именно мы логгируем
logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)


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


if __name__ == "__main__":
    a = super_sum(1, 5)
    r = list_to_dict([1, 2, 3])
    print(a)
