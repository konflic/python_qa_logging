import logging
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("-l", "--log", type=str, default="WARNING")
# parser.add_argument("-f", "--file", default=None)
# args = parser.parse_args()
#
# # Если не указываем файл передаем в stdout
logging.basicConfig(level=logging.DEBUG, filename="example.log", format='%(asctime)s %(levelname)s %(filename)s %(message)s')

# Уровень по умолчанию WARNING
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
