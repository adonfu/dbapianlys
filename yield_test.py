# -*- coding: utf-8 -*-
import contextlib
import time


def func1():
    for idx in range(10):
        print "idx=%s" % idx


def func2():

    try:
        for idx in range(10):
            print("before {} times".format(idx))
            yield idx * idx
            print("after {} times".format(idx))
    finally:
        print "generator done executed!"


@contextlib.contextmanager
def timely(procName):
    now = time.time()
    try:
        yield
    finally:
        total = time.time() - now
        print "%s execute done, total second: %f!" % (procName, total)


def func3(ctx):
    with ctx("async proc"):
        for idx in range(10):
            yield idx
            print "times: %s" % idx


if __name__ == '__main__':
    # func1()

    # generator = func2()
    # data = generator.next()
    # print "data=%s" % data
    #
    # data = generator.next()
    # print "data=%s" % data

    # func3(timely)

    generator = func3(timely)
    data = generator.next()
    print "data=%s" % data
    data = generator.next()
    print "data=%s" % data
