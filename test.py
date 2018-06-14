import logging
import test_log

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

n1 = 10
n2 = 5

ar = add(n1, n2)
logger.debug('Add: {} + {} = {}'.format(n1, n2, ar))

mr = multiply(n1, n2)
logger.debug('Mul: {} * {} = {}'.format(n1, n2, mr))