### DB client
torndb、pymysql、asynctorndb访问MySQL数据库耗时及性能比较

#### AsyncTorndb:
```
git@github.com:mayflaver/AsyncTorndb.git
```


#### Time consuming (osx 10.10)
```
API:  torndb, total seconds 0.056177
API:  pymysql, total seconds 0.295820
API:  asynctorndb, total seconds 0.982185
```

#### Profiled (osx 10.10)
```
API:  torndb
         27050 function calls in 0.072 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      500    0.002    0.000    0.067    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/torndb.py:145(query)
      500    0.001    0.000    0.056    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/torndb.py:247(_execute)
      500    0.002    0.000    0.056    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:164(execute)
      500    0.001    0.000    0.051    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:353(_query)
      500    0.001    0.000    0.048    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:315(_do_query)
      500    0.040    0.000    0.040    0.000 {method 'query' of '_mysql.connection' objects}
      500    0.003    0.000    0.006    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:142(_do_get_result)
      500    0.001    0.000    0.005    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/torndb.py:243(_cursor)
      500    0.001    0.000    0.004    0.000 test.py:16(get_sql)
      500    0.001    0.000    0.003    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/connections.py:245(cursor)
     1000    0.001    0.000    0.003    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py:238(randint)
      500    0.003    0.000    0.003    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:75(__init__)
     1000    0.001    0.000    0.003    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:97(close)
      500    0.001    0.000    0.003    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:358(_post_get_result)
     1000    0.002    0.000    0.002    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py:175(randrange)
      500    0.001    0.000    0.002    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:351(_get_result)
      500    0.002    0.000    0.002    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:107(_warning_check)
      500    0.001    0.000    0.002    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:122(nextset)
      500    0.000    0.000    0.002    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:324(_fetch_row)
      500    0.002    0.000    0.002    0.000 {method 'store_result' of '_mysql.connection' objects}
      500    0.000    0.000    0.001    0.000 {built-in method fetch_row}
      382    0.000    0.000    0.001    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/connections.py:212(string_decoder)
      500    0.001    0.000    0.001    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/torndb.py:232(_ensure_connected)
      500    0.001    0.000    0.001    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:409(__iter__)
      500    0.001    0.000    0.001    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:380(fetchall)
      382    0.000    0.000    0.001    0.000 {method 'decode' of 'str' objects}
     2500    0.001    0.000    0.001    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:159(_get_db)
      500    0.001    0.000    0.001    0.000 {built-in method describe}
     1002    0.001    0.000    0.001    0.000 {isinstance}
      500    0.000    0.000    0.000    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:92(__del__)
      382    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/encodings/utf_8.py:15(decode)
     1000    0.000    0.000    0.000    0.000 build/bdist.macosx-10.13-intel/egg/MySQLdb/cursors.py:103(_check_executed)
      382    0.000    0.000    0.000    0.000 {_codecs.utf_8_decode}
      500    0.000    0.000    0.000    0.000 {method 'next_result' of '_mysql.connection' objects}
     1000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
     1000    0.000    0.000    0.000    0.000 {time.time}
      500    0.000    0.000    0.000    0.000 {built-in method field_flags}
      500    0.000    0.000    0.000    0.000 {_weakref.proxy}
      500    0.000    0.000    0.000    0.000 {iter}
      500    0.000    0.000    0.000    0.000 {method 'affected_rows' of '_mysql.connection' objects}
      500    0.000    0.000    0.000    0.000 {method 'insert_id' of '_mysql.connection' objects}
      500    0.000    0.000    0.000    0.000 {method 'info' of '_mysql.connection' objects}
      500    0.000    0.000    0.000    0.000 {method 'warning_count' of '_mysql.connection' objects}
      500    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/encodings/__init__.py:71(search_function)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/encodings/utf_8.py:33(getregentry)
        1    0.000    0.000    0.000    0.000 {range}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/encodings/__init__.py:49(normalize_encoding)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/codecs.py:83(__new__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py:21(__exit__)
        1    0.000    0.000    0.000    0.000 test.py:23(profiled)
        1    0.000    0.000    0.000    0.000 {__import__}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pkg_resources/extern/__init__.py:23(find_module)
        2    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x7fff993d0498}
        1    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pkg_resources/_vendor/six.py:184(find_module)
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'translate' of 'str' objects}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/six.py:184(find_module)



API:  pymysql
         247934 function calls in 0.382 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      500    0.001    0.000    0.288    0.001 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:151(execute)
     4111    0.020    0.000    0.286    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:647(_read_packet)
      500    0.001    0.000    0.283    0.001 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:324(_query)
      500    0.001    0.000    0.279    0.001 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:507(query)
      500    0.002    0.000    0.262    0.001 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:715(_read_query_result)
      500    0.002    0.000    0.260    0.001 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:1064(read)
     8222    0.023    0.000    0.185    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:686(_read_bytes)
      500    0.002    0.000    0.169    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:1140(_read_result_packet)
      500    0.010    0.000    0.146    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:1204(_get_descriptions)
     8222    0.021    0.000    0.126    0.000 {method 'read' of '_io.BufferedReader' objects}
     1000    0.005    0.000    0.105    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/_socketio.py:45(readinto)
     1000    0.094    0.000    0.094    0.000 {method 'recv_into' of '_socket.socket' objects}
      500    0.000    0.000    0.086    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:499(__exit__)
      500    0.002    0.000    0.085    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:414(commit)
     2000    0.003    0.000    0.073    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:233(__init__)
     2000    0.011    0.000    0.069    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:237(_parse_field_descriptor)
      500    0.001    0.000    0.069    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:395(_read_ok_packet)
    10222    0.010    0.000    0.055    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py:227(meth)
    12444    0.009    0.000    0.034    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:168(read_length_coded_string)
     1000    0.004    0.000    0.030    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:739(_execute_command)
     9222    0.029    0.000    0.029    0.000 {method 'settimeout' of '_socket.socket' objects}
     1000    0.003    0.000    0.024    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:705(_write_bytes)
      500    0.002    0.000    0.020    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:1173(_read_rowdata_packet)
     8000    0.007    0.000    0.018    0.000 {method 'decode' of 'str' objects}
    13944    0.007    0.000    0.017    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:150(read_length_encoded_integer)
     1000    0.014    0.000    0.014    0.000 {method 'sendall' of '_socket.socket' objects}
     8000    0.004    0.000    0.012    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/encodings/utf_8.py:15(decode)
     3000    0.008    0.000    0.011    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:180(read_struct)
    13944    0.009    0.000    0.010    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:112(read_uint8)
    12440    0.009    0.000    0.010    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:63(read)
      500    0.004    0.000    0.010    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:283(__init__)
     8000    0.008    0.000    0.008    0.000 {_codecs.utf_8_decode}
     2000    0.003    0.000    0.007    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:253(description)
      500    0.002    0.000    0.006    0.000 test.py:16(get_sql)
      611    0.001    0.000    0.005    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:1128(_check_packet_is_eof)
     4111    0.003    0.000    0.005    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:214(check_error)
     1000    0.001    0.000    0.004    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py:238(randint)
     4000    0.003    0.000    0.004    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:264(get_column_length)
     1000    0.002    0.000    0.004    0.000 {method '_checkReadable' of '_io._IOBase' objects}
     1000    0.003    0.000    0.003    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py:175(randrange)
      500    0.001    0.000    0.003    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:308(__init__)
    25162    0.003    0.000    0.003    0.000 {len}
     3000    0.003    0.000    0.003    0.000 {method 'unpack_from' of 'Struct' objects}
    10722    0.003    0.000    0.003    0.000 {getattr}
      500    0.001    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:135(mogrify)
      500    0.001    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:341(_do_get_result)
     4111    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:56(__init__)
      500    0.000    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:495(__enter__)
     1000    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/_socketio.py:87(readable)
     4111    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:211(is_error_packet)
     1000    0.002    0.000    0.002    0.000 {method '_checkClosed' of '_io._IOBase' objects}
     4111    0.002    0.000    0.002    0.000 {_struct.unpack}
      111    0.000    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:1186(_read_row_from_packet)
      500    0.001    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:483(cursor)
    13944    0.001    0.000    0.001    0.000 {ord}
      500    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:109(_ensure_bytes)
     2500    0.001    0.000    0.001    0.000 {isinstance}
      500    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:1044(__init__)
     1611    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:190(is_eof_packet)
      500    0.000    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:106(nextset)
     6555    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
     1000    0.001    0.000    0.001    0.000 {_struct.pack}
     1500    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:186(is_ok_packet)
     6000    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
      500    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:40(__init__)
     2000    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:71(_get_db)
     1000    0.001    0.000    0.001    0.000 {min}
      500    0.000    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:89(_nextset)
      500    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:355(_show_warnings)
      500    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:86(advance)
      500    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:297(__getattr__)
      500    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/cursors.py:332(_clear_result)
      500    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:77(read_all)
      499    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/connections.py:1060(__del__)
     1000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
      500    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pymysql/protocol.py:208(is_load_local_packet)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py:21(__exit__)
        1    0.000    0.000    0.000    0.000 {range}
        1    0.000    0.000    0.000    0.000 test.py:23(profiled)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



API:  asynctorndb
         1408459 function calls (1341840 primitive calls) in 1.516 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.516    1.516 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:513(run_sync)
        1    0.051    0.051    1.516    1.516 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:935(start)
    15091    0.050    0.000    1.439    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:752(_run_callback)
    15182    0.018    0.000    1.273    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/stack_context.py:296(null_wrapper)
      788    0.002    0.000    1.228    0.002 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:1230(inner)
13183/788    0.105    0.000    1.226    0.002 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:1115(run)
20784/1377    0.011    0.000    1.195    0.001 {method 'send' of 'generator' objects}
13008/590    0.057    0.000    1.188    0.002 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:295(wrapper)
13010/680    0.007    0.000    1.142    0.002 {next}
      502    0.001    0.000    1.051    0.002 test.py:67(get)
13008/2942    0.062    0.000    1.042    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:1061(__init__)
     1000    0.004    0.000    1.011    0.001 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:746(query)
     1000    0.004    0.000    0.981    0.001 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:105(execute)
     1000    0.003    0.000    0.954    0.001 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:276(_query)
     1500    0.004    0.000    0.913    0.001 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1203(read)
     1500    0.002    0.000    0.911    0.001 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:845(execute_query)
     1000    0.004    0.000    0.801    0.001 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:984(_read_query_result)
     1500    0.002    0.000    0.758    0.001 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1251(_read_result_packet)
     3000    0.009    0.000    0.631    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1343(_get_descriptions)
     6000    0.014    0.000    0.576    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:953(_read_packet)
     4000    0.006    0.000    0.312    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:403(recv_packet)
    33793    0.036    0.000    0.223    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/singledispatch.py:209(wrapper)
    20784    0.052    0.000    0.195    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:1183(handle_yield)
     7274    0.014    0.000    0.161    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:407(read_bytes)
     9006    0.015    0.000    0.159    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:260(recv_packet)
   174172    0.073    0.000    0.145    0.000 {isinstance}
    33793    0.056    0.000    0.141    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:1337(convert_yielded)
    14299    0.045    0.000    0.124    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:282(add_done_callback)
     7274    0.013    0.000    0.105    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:898(_try_inline_read)
     2000    0.021    0.000    0.090    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:408(__parse_field_descriptor)
    15090    0.039    0.000    0.081    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:1121(add_callback)
    33292    0.043    0.000    0.072    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/abc.py:128(__instancecheck__)
     7274    0.008    0.000    0.063    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:985(_read_from_buffer)
    13008    0.019    0.000    0.057    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:186(_create_future)
     7274    0.016    0.000    0.055    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:869(_run_read_callback)
     1000    0.004    0.000    0.054    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1008(_execute_command)
    13008    0.005    0.000    0.047    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/backports_abc.py:195(isawaitable)
    33793    0.030    0.000    0.047    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/singledispatch.py:173(dispatch)
      501    0.004    0.000    0.046    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:544(write)
    20786    0.045    0.000    0.045    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:191(__init__)
    20786    0.013    0.000    0.043    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:296(set_result)
    12540    0.010    0.000    0.042    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:353(read_length_coded_string)
    15883    0.027    0.000    0.040    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/stack_context.py:278(wrap)
    13008    0.039    0.000    0.039    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:171(_value_from_stopiteration)
     1770    0.005    0.000    0.039    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1287(_read_rowdata_packet)
    13008    0.013    0.000    0.039    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:618(future_set_result_unless_cancelled)
      502    0.005    0.000    0.032    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1045(_handle_write)
    20784    0.015    0.000    0.031    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:707(_contains_yieldpoint)
    36569    0.027    0.000    0.030    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:287(read)
    20786    0.016    0.000    0.030    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:345(_set_done)
    20786    0.017    0.000    0.026    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:248(result)
    73109    0.025    0.000    0.025    0.000 {getattr}
    26613    0.018    0.000    0.024    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:253(current)
    34585    0.013    0.000    0.024    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:379(is_future)
     7274    0.010    0.000    0.024    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:858(_set_read_callback)
    13040    0.010    0.000    0.023    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:335(read_length_encoded_integer)
    46303    0.023    0.000    0.023    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/_weakrefset.py:70(__contains__)
     7274    0.019    0.000    0.021    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1091(_consume)
      589    0.003    0.000    0.019    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:783(_read_to_buffer_loop)
    33793    0.016    0.000    0.016    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/weakref.py:314(__getitem__)
     2000    0.008    0.000    0.016    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:430(description)
      589    0.008    0.000    0.015    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:931(_read_to_buffer)
    15890    0.014    0.000    0.014    0.000 {hasattr}
     1589    0.004    0.000    0.012    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/platform/kqueue.py:64(poll)
     7638    0.007    0.000    0.012    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/util.py:3(byte2int)
      501    0.001    0.000    0.012    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1247(write_to_fd)
        4    0.000    0.000    0.011    0.003 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:895(connect)
     8001    0.011    0.000    0.011    0.000 {method 'decode' of 'str' objects}
        3    0.000    0.000    0.011    0.004 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:186(connect)
      501    0.011    0.000    0.011    0.000 {method 'send' of '_socket.socket' objects}
        1    0.000    0.000    0.011    0.011 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:545(run)
     7775    0.009    0.000    0.010    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1114(_maybe_add_error_listener)
     5502    0.010    0.000    0.010    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:398(__init__)
        2    0.000    0.000    0.010    0.005 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/netutil.py:375(resolve)
        1    0.001    0.001    0.010    0.010 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:721(run_in_executor)
     7863    0.007    0.000    0.010    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:995(_find_read_pos)
     1767    0.009    0.000    0.009    0.000 {method 'control' of 'select.kqueue' objects}
       89    0.001    0.000    0.009    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:695(_handle_events)
        1    0.000    0.000    0.008    0.008 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/process.py:59(cpu_count)
        1    0.000    0.000    0.008    0.008 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/multiprocessing/__init__.py:109(cpu_count)
    42361    0.007    0.000    0.007    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:238(done)
        5    0.007    0.001    0.007    0.001 {method 'read' of 'file' objects}
      589    0.002    0.000    0.007    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1236(read_from_fd)
    21287    0.007    0.000    0.007    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:242(_clear_tb_log)
    49447    0.007    0.000    0.007    0.000 {len}
      500    0.002    0.000    0.007    0.000 test.py:16(get_sql)
      635    0.001    0.000    0.006    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1243(_check_packet_is_eof)
      176    0.001    0.000    0.006    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:912(update_handler)
    18318    0.006    0.000    0.006    0.000 {_struct.unpack}
      791    0.001    0.000    0.006    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:705(add_future)
     4000    0.005    0.000    0.005    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:448(get_column_length)
      589    0.005    0.000    0.005    0.000 {method 'recv_into' of '_socket.socket' objects}
       88    0.000    0.000    0.005    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:843(_handle_read)
     1000    0.001    0.000    0.005    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py:238(randint)
       88    0.000    0.000    0.005    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1130(_add_io_state)
      500    0.002    0.000    0.004    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:493(__init__)
      176    0.000    0.000    0.004    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/platform/kqueue.py:43(modify)
    20856    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
     7776    0.004    0.000    0.004    0.000 {min}
     3002    0.002    0.000    0.004    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:381(check_error)
    13008    0.004    0.000    0.004    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:1252(_deactivate_stack_context)
     1000    0.003    0.000    0.004    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py:175(randrange)
     2000    0.003    0.000    0.004    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:400(__init__)
     4500    0.003    0.000    0.004    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:310(advance)
      790    0.001    0.000    0.004    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:719(<lambda>)
      353    0.002    0.000    0.003    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/platform/kqueue.py:51(_control)
      135    0.001    0.000    0.003    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1319(_read_row_from_packet)
      501    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:180(advance)
    13008    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:347(<lambda>)
    13009    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:226(cancelled)
      501    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:141(append)
    16093    0.002    0.000    0.002    0.000 {method 'append' of 'collections.deque' objects}
     9811    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:676(closed)
     7274    0.002    0.000    0.002    0.000 {method 'tobytes' of 'memoryview' objects}
      500    0.002    0.000    0.002    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:95(_escape_args)
     1591    0.002    0.000    0.002    0.000 {method 'update' of 'dict' objects}
      177    0.000    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/platform/kqueue.py:37(register)
     7776    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:977(_run_streaming_callback)
    15112    0.002    0.000    0.002    0.000 {thread.get_ident}
     9008    0.002    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:341(_check_done)
     3637    0.002    0.000    0.002    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:253(__init__)
    16093    0.002    0.000    0.002    0.000 {method 'popleft' of 'collections.deque' objects}
      176    0.001    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/platform/kqueue.py:47(unregister)
      792    0.001    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:646(future_add_done_callback)
      500    0.001    0.000    0.002    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:728(cursor)
     1636    0.002    0.000    0.002    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:368(is_eof_packet)
     3002    0.002    0.000    0.002    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:378(is_error_packet)
     1000    0.001    0.000    0.002    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:52(close)
      500    0.001    0.000    0.002    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:284(_do_get_result)
      501    0.000    0.000    0.002    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:584(<lambda>)
    13040    0.001    0.000    0.001    0.000 {ord}
      635    0.001    0.000    0.001    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:232(fetchone)
      500    0.001    0.000    0.001    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1186(__init__)
      177    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:803(split_fd)
     1000    0.001    0.000    0.001    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:83(nextset)
     1029    0.001    0.000    0.001    0.000 {_struct.pack}
      501    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:267(exception)
     1591    0.001    0.000    0.001    0.000 {range}
     1002    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1110(_check_closed)
      501    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:163(peek)
      500    0.001    0.000    0.001    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:32(__init__)
     4627    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
     2500    0.001    0.000    0.001    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:65(_get_db)
        1    0.001    0.001    0.001    0.001 {posix.popen}
      505    0.000    0.000    0.001    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/util.py:9(int2byte)
      181    0.000    0.000    0.001    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py:227(meth)
      500    0.000    0.000    0.001    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:295(__iter__)
      500    0.000    0.000    0.001    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:116(ensure_bytes)
     2095    0.001    0.000    0.001    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:134(__len__)
      500    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:46(__del__)
      500    0.000    0.000    0.000    0.000 {map}
        3    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1043(_request_authentication)
     1000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
     1589    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
      500    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:365(is_ok_packet)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/thread.py:121(submit)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:86(start)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/thread.py:134(_adjust_thread_count)
       89    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:672(writing)
      635    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:70(_check_executed)
        2    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1122(_get_server_information)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:93(try_connect)
      499    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:1199(__del__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:245(_create_stream)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:726(start)
      635    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:257(set_data)
      501    0.000    0.000    0.000    0.000 {iter}
      135    0.000    0.000    0.000    0.000 {zip}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:484(_setup_logging)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:603(wait)
      500    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/cursors.py:97(<genexpr>)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:309(wait)
       15    0.000    0.000    0.000    0.000 {method 'acquire' of 'thread.lock' objects}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1255(connect)
      4/3    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/abc.py:148(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/process.py:18(<module>)
      177    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1224(fileno)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/thread.py:98(__init__)
        2    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/singledispatch.py:132(_find_impl)
      178    0.000    0.000    0.000    0.000 {method 'fileno' of '_socket.socket' objects}
      529    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/converters.py:299(through)
        2    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/singledispatch.py:91(_compose_mro)
      176    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:242(Condition)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:1505(basicConfig)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:157(_scramble)
        3    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:1565(getLogger)
       90    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:668(reading)
        6    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:260(__init__)
        2    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:1023(getLogger)
      4/2    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/singledispatch.py:46(_c3_mro)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:135(set_timeout)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/Queue.py:26(__init__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:593(add_timeout)
        1    0.000    0.000    0.000    0.000 {method 'connect' of '_socket.socket' objects}
        2    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:875(<lambda>)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:599(copy)
        2    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/platform/posix.py:58(consume)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:825(__init__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:656(__init__)
        1    0.000    0.000    0.000    0.000 {thread.start_new_thread}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:170(_my_crypt)
        6    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/_weakrefset.py:58(__iter__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:742(<lambda>)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1219(__init__)
       10    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:147(acquire)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/concurrent.py:587(chain_future)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:109(on_connect_done)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:907(add_handler)
       91    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:663(__init__)
        2    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/_base.py:400(done)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:243(coroutine)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:174(__init__)
        5    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:211(_acquireLock)
       10    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:187(release)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:1412(_handle_connect)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py:189(__init__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/gen.py:282(_make_coroutine_wrapper)
        4    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/singledispatch.py:19(_c3_merge)
        3    0.000    0.000    0.000    0.000 {issubclass}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/util.py:295(__new__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:229(__init__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:54(__init__)
        5    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:285(__enter__)
        5    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:220(_releaseLock)
        2    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/platform/posix.py:52(wake)
        5    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:288(__exit__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/charset.py:36(by_name)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/_base.py:318(__init__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:542(Event)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/Queue.py:107(put)
        2    0.000    0.000    0.000    0.000 {method 'write' of 'file' objects}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:1104(call_at)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/platform/posix.py:26(set_close_exec)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:560(<lambda>)
        2    0.000    0.000    0.000    0.000 {signal.set_wakeup_fd}
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:561(__init__)
        5    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:215(__exit__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/functools.py:17(update_wrapper)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:1096(stop)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:644(_addHandlerRef)
        4    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/_weakrefset.py:26(__exit__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/_base.py:499(exception)
        2    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:114(RLock)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:692(createLock)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/_base.py:418(add_done_callback)
        3    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/hashlib.py:119(__hash_new)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/_base.py:435(result)
        4    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/_weakrefset.py:83(add)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/_base.py:466(exception_info)
        2    0.000    0.000    0.000    0.000 {fcntl.fcntl}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/util.py:360(configured_class)
        2    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:132(__init__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:709(_set_daemon)
       23    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:64(_note)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:1125(__init__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:1093(_fixupChildren)
        3    0.000    0.000    0.000    0.000 {_hashlib.new}
        4    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/_weakrefset.py:36(__init__)
        2    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:300(_is_owned)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:1296(addHandler)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py:21(__exit__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:373(notify)
        3    0.000    0.000    0.000    0.000 {method 'digest' of '_hashlib.HASH' objects}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/process.py:189(Subprocess)
        4    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:1101(time)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:1148(__init__)
        4    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/_weakrefset.py:20(__enter__)
       10    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:59(__init__)
        7    0.000    0.000    0.000    0.000 {thread.allocate_lock}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:157(clear_timeouts)
        3    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/weakref.py:320(__setitem__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:1069(_fixupParents)
        1    0.000    0.000    0.000    0.000 {method 'setblocking' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 {method 'getsockopt' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pkg_resources/extern/__init__.py:23(find_module)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/functools.py:39(wraps)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/Queue.py:197(_init)
        1    0.000    0.000    0.000    0.000 test.py:23(profiled)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:1152(currentThread)
        2    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:183(_checkLevel)
        4    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/_weakrefset.py:16(__init__)
        1    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/backports_abc.py:158(__subclasshook__)
        4    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/_weakrefset.py:52(_commit_removals)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/backports_abc.py:102(__subclasshook__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:294(_release_save)
        2    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:585(__init__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:127(__init__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:66(split)
        9    0.000    0.000    0.000    0.000 {setattr}
        1    0.000    0.000    0.000    0.000 {method 'encode' of 'str' objects}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/ioloop.py:1112(remove_timeout)
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dictproxy' objects}
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/Queue.py:204(_put)
       11    0.000    0.000    0.000    0.000 {method 'release' of 'thread.lock' objects}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/stack_context.py:244(__enter__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:297(_acquire_restore)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:397(__init__)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:1024(daemon)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/thread.py:52(__init__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/platform/posix.py:49(write_fileno)
        3    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/netutil.py:316(configurable_base)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/util.py:219(errno_from_exception)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging/__init__.py:762(setFormatter)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/tcpclient.py:163(close_streams)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/concurrent/futures/_base.py:405(__get_result)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:231(pack_int24)
        1    0.000    0.000    0.000    0.000 {_heapq.heappush}
        2    0.000    0.000    0.000    0.000 {method '__subclasshook__' of 'object' objects}
        2    0.000    0.000    0.000    0.000 {max}
        4    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/charset.py:33(by_id)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/netutil.py:320(configurable_default)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/stack_context.py:248(__exit__)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/iostream.py:638(_maybe_run_close_callback)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/six.py:184(find_module)
        1    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'unicode' objects}
        1    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        2    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/singledispatch.py:100(is_related)
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/pkg_resources/_vendor/six.py:184(find_module)
        1    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:1008(daemon)
        1    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'fileno' of 'file' objects}
        1    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        2    0.000    0.000    0.000    0.000 {method 'update' of '_hashlib.HASH' objects}
        1    0.000    0.000    0.000    0.000 {posix.getpid}
        2    0.000    0.000    0.000    0.000 {method '__subclasses__' of 'type' objects}
        1    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {any}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/tornado/util.py:333(initialize)
        2    0.000    0.000    0.000    0.000 /Users/fuyadong/.virtualenvs/vending/lib/python2.7/site-packages/backports_abc.py:24(get_mro)
        4    0.000    0.000    0.000    0.000 {time.time}
        1    0.000    0.000    0.000    0.000 {_heapq.heappop}
        2    0.000    0.000    0.000    0.000 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py:570(isSet)
        1    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x7fff993d0498}
        1    0.000    0.000    0.000    0.000 /Users/fuyadong/Desktop/AsyncTorndb-master/asynctorndb/connection.py:284(get_all_data)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

函数调用次数
```
API:  torndb
    27050 function calls in 0.072 seconds
API:  pymysql
    247934 function calls in 0.382 seconds
API:  asynctorndb
    1408459 function calls (1341840 primitive calls) in 1.516 seconds
```