from functools import wraps
import time


class Throttle:
    def __init__(self, func, period):
        self.func = func
        self.period = period
        self.lastRun = 0

    def __call__(self, *args, **kwargs):
        now = time.time()
        if now - self.lastRun < self.period:
            raise Exception("Try after {} time".format(self.lastRun + self.period - now))
        else:
            self.lastRun = now
            return self.func(*args, **kwargs)


def throttle(period):
    def apply_decoration(func):
        obj = Throttle(func, period)
        return wraps(func)(obj)
    return apply_decoration


@throttle(period=2)
def call_api():
    print("API Called")


if __name__ == '__main__':
    for i in range(10):
        try:
            call_api()
        except Exception as e:
            print(e)
            time.sleep(1)
