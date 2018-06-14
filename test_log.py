# # # import logging
# # #
# # # logger = logging.getLogger(__name__)
# # # logger.setLevel(logging.INFO)
# # #
# # # formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
# # #
# # # file_handler = logging.FileHandler('test_log.log')
# # # file_handler.setFormatter(formatter)
# # # logger.addHandler(file_handler)
# # #
# # #
# # #
# # #
# # # class Employee(object):
# # #
# # #     def __init__(self, f, l):
# # #         self.first = f
# # #         self.last = l
# # #         # print('Created Employee: {} - {}'.format(self.fullname, self.email))
# # #
# # #         logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))
# # #
# # #     @property
# # #     def email(self):
# # #         return '{}.{}@email.com'.format(self.first, self.last)
# # #
# # #     @property
# # #     def fullname(self):
# # #         return '{} {}'.format(self.first, self.last)
# # #
# # # e1 = Employee('John', 'Smith')
# # # e2 = Employee('Corey', 'Schafer')
# # # e3 = Employee('Jane', 'Doe')
# # #
# #
# # import logging
# #
# # def console_out(title):
# #
# #     logging.basicConfig(
# #         level=logging.DEBUG,
# #         format="%(asctime)s - [%(levelname)s] -  %(name)s GET %(message)s",
# #         datefmt="%Y-%b-%d %a %H:%M:%S",
# #         filename=title + '.log'
# #     )
# #
# #     console = logging.StreamHandler()
# #     console.setLevel(logging.INFO)
# #     formatter = logging.Formatter(
# #         "%(asctime)s [%(levelname)s] -> %(name)s GET %(message)s"
# #     )
# #     console.setFormatter(formatter)
# #     logging.getLogger().addHandler(console)
# #
# #     logging.debug('hello debut')
# #     logging.info('hello info')
# #
# # if __name__ == '__main__':
# #     console_out('Summary')
#
# import logging
#
# logging.basicConfig(filename='test_log.log', level=logging.DEBUG)
#
#
#
# a = {"a": 1, "b\u2122": "B"}
# print(a)
# a.__repr__()
# a.__str__()
# print(a.__str__().encode("utf-8"))
# logging.warning(a)
# logging.error(a)
#
#

import redis
import os

os.popen(r'D:\ASoft\Reids\redis-server.exe D:\ASoft\Reids\redis.windows.conf')

r = redis.Redis()

a = {'a':1, 'B':'b'}
r.hmset('dict', a)
r.shutdown()



