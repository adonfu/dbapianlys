

import tornado.ioloop
import asynctorndb
import random
import cProfile
import StringIO
import contextlib
import pstats
from tornado.gen import coroutine
import torndb
import time
import pymysql


def get_sql():
    offset = random.randint(0, 300)
    limit = random.randint(offset, 300) - offset
    sql = "SELECT * FROM userinfo limit %s, %s" % (offset, limit)
    return sql


@contextlib.contextmanager
def profiled(api):
    pr = cProfile.Profile()
    pr.enable()
    yield
    pr.disable()
    pr.dump_stats("profile.stats")
    s = StringIO.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print "API:  %s" % api
    print s.getvalue()


@contextlib.contextmanager
def timeonly(api):
    now = time.time()
    try:
        yield
    finally:
        total = time.time() - now
        print "API:  %s, total seconds %f" % (api, total)


def torndb_test(ctx, count=500):
    conn = torndb.Connection(host="localhost:3306", user="root", password="root", database="test")
    with ctx('torndb'):
        for i in range(count):
            conn.query(get_sql())
            # res = conn.query(get_sql())
            # print "time: %s, res=[%s]" % (i, res)


def pymysql_test(ctx, count=500):
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", database="test")
    with ctx('pymysql'):
        for i in range(count):
            with conn as cursor:
                cursor.execute(get_sql())


def asynctorndb_test(ctx, count=500):
    conn = asynctorndb.Connect(host="localhost", port=3306, user="root", passwd="root", database="test")
    with ctx('asynctorndb'):
        @coroutine
        def get():
            yield conn.connect()
            # print "programmer return now!"
            # return
            for i in range(count):
                yield conn.query(get_sql())
                # res = yield conn.query(get_sql())
                # print "time: %s, res=[%s]" % (i, res)
        tornado.ioloop.IOLoop.current().run_sync(get)


if __name__ == "__main__":
    # torndb_test(timeonly)
    # pymysql_test(timeonly)
    # asynctorndb_test(timeonly)

    torndb_test(profiled, 500)
    pymysql_test(profiled, 500)
    asynctorndb_test(profiled, 500)
