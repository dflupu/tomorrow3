import time
from tomorrow3 import threads

DELAY = 0.5
N = 5


def test_throwing_func():

    @threads(10, queue_max=20)
    def throws():
        raise Exception('test exception')

    throws()
    throws.wait()
    assert 1


def test_decorator():

    def slow_add(x, y):
        time.sleep(DELAY)
        return x + y

    @threads(N)
    def async_add(x, y):
        time.sleep(DELAY)
        return x + y

    x, y = 2, 2

    start = time.time()

    results = []
    for i in range(N * 2):
        results.append(async_add(x, y))

    checkpoint = time.time()

    for future in results:
        future.result()

    end = time.time()
    assert (checkpoint - start) < DELAY * 2
    assert DELAY < (end - start) < (DELAY * N * 2)


def test_future_function():

    @threads(N)
    def returns_function():

        def f():
            return True

        return f

    true = returns_function().result()
    assert true()
