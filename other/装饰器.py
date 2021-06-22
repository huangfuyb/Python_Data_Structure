import time


def display_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2 - t1)
    return wrapper


def display_time_re(func):
    def wrapper():
        t1 = time.time()
        c = func()
        t2 = time.time()
        print(t2 - t1)
        return c  #返回计数
    return wrapper


def display_time_re_with_args(func):
    def wrapper(*args):  # 被装饰函数的参数
        t1 = time.time()
        c = func(*args) # 被装饰的函数
        t2 = time.time()
        print(t2 - t1)
        return c   # 返回计数
    return wrapper


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i ==0:
                return False
        return True


@display_time
def prime_nums():

    # t1 = time.time()
    for i in range(2, 10000):
        if is_prime(i):
            print(i)
    # t2 = time.time()
    # print(t2-t1)


# @display_time
@display_time_re
def count_prime_nums():
    count = 0
    # t1 = time.time()
    for i in range(2, 10000):
        if is_prime(i):
            count += 1
    return count
    # t2 = time.time()
    # print(t2-t1)


@display_time_re_with_args
def count_prime_nums_with_args(max_num):
    count = 0
    # t1 = time.time()
    for i in range(2, max_num):
        if is_prime(i):
            count += 1
    return count


if __name__ == '__main__':
    '''1，带有装饰器的函数'''
    # prime_nums()

    '''2，当函数有返回值时，调用之前的装饰器，发现返回None,这是因为wrapper函数仅运行了time计时，但没有返回值'''
    # c = count_prime_nums()
    # print(c)
    '''3,当函数有参数时，需要在wrapper函数加上参数，否则报错'''
    c = count_prime_nums_with_args(10000)
    print(c)

