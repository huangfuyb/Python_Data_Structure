from threading import Lock
from threading import Thread


class MyThread(Thread):

    def __init__(self, target=None, args=()):
        super(MyThread, self).__init__()
        self.func = target
        self.args = args

    def run(self):
        self.func(*self.args)


class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()

        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        # print('second')
        with self.firstJobDone:
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # print('third')
        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()


def thread_first():
    t1 = Thread(target=print_func1)
    t1.start()


def thread_second():
    t2 = Thread(target=print_func2)
    t2.start()


def thread_third():
    t3 = Thread(target=print_func3)
    t3.start()


def print_func1():
    print('a')


def print_func2():
    print('b')


def print_func3():
    print('c')


if __name__ == '__main__':
    f = Foo()
    # t3 = Thread(target=f.third, args=(print_func3,))
    # t2 = Thread(target=f.second, args=(print_func2,))
    # t1 = Thread(target=f.first, args=(print_func1,))
    # t1.start()
    # t3.start()
    # t2.start()
    '''-------------------------------------------------------------'''
    t2 = MyThread(target=f.second, args=(print_func2,))
    t1 = MyThread(target=f.first, args=(print_func1,))
    t3 = MyThread(target=f.third, args=(print_func3,))
    # f.third(thread_third)
    t1.start()
    t2.start()
    t3.start()


