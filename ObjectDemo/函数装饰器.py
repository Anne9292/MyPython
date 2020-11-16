#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-11 15:41
# filename: MyPython-装饰器

import time
import logging
from functools import wraps

FORMAT = '%(asctime)s--%(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

# 装饰的增强函数：无参数
def use_logging2(func):
    def wrapper():
        logging.info('%s is running--------' % func.__name__)
        return func()
    return wrapper

@use_logging2
def func_3():
    print('this is func_3')


# 装饰的增强函数：两个参数
def event_log(server_id):
    def server_name(event_id, user_id):
        logging.info('%s is recalled...' % server_id.__name__)
        return server_id(event_id, user_id)
    return server_name

@event_log
def lottery(event_id, user_id):
    print('event_id is {}!\tuser_id is {}!'.format(event_id, user_id))


# 装饰的增强函数：多个参数
def log_time(server_id):
    # print('log_time running..............')
    @wraps(server_id)
    def server_name(*args, **kwargs):
        before = time.time()
        print('函数执行前：{}'.format(before))
        server_id(*args, **kwargs)
        after = time.time()
        print('函数执行后：{}'.format(after))
        run_time = after - before
        logging.info('%s运行时间是：%dms' % (server_id.__name__, run_time))
        return run_time
    return server_name

@log_time
def trade(*args, **kwargs):
    for i in range(2):
        print('第%i次运行...' % i)
        print("{} like: {}".format(args, kwargs))
        time.sleep(1)

# 装饰器：多个参数
def event_logging(level):   # 装饰器的函数，参数是装饰器需要接收的
    # print('event_logging running.............')
    def decorator(server_name):    #  装饰的函数，参数是被装饰的增强函数的名称
        @wraps(server_name)     # 装饰器实现时，被装饰的函数已经是另外一个函数了，函数名等函数属性会发生改变，使用wraps(函数名)保留被装饰函数的属性
        def wrapper(*args, **kwargs):   # 增强函数，参数是业务函数的需要接收的
            if level == 'warn':
                logging.warning('%s is running by warning' % server_name.__name__)
            elif level == 'info':
                logging.info('%s is running by info' % server_name.__name__)
            return server_name(*args, **kwargs)
        # print('@@@@@@@@@')
        return wrapper
    return decorator

"""多个装饰器，先执行内层，再执行外层"""
@log_time
@event_logging(level='warn')
def wallet_warn(*args, **kwargs):
    """\ntest wallet_warn!!!"""
    print("{} want to {} ----warn".format(args, kwargs))

@event_logging(level='info')
def wallet_info(*args, **kwargs):
    print("{} want to {} ----info".format(args, kwargs))


if __name__ == '__main__':

    # lottery('lottery', '10086')
    args = ['anne', 20, 'female']
    dict = {'fruit': 'apple', 'sport': 'tennis', 'hobby': 'music'}
    trade(*args, **dict)
    wallet_warn(*args, **dict)
    # print(wallet_warn.__name__, wallet_warn.__doc__)
