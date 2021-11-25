from math import inf
from module.DB import DB
from module.tester import *
from module.data import data_generator
from module.encrypt.hash import sha256, md5, original

repeat = 10
data_cnt = 250

db_user = ""
db_pass = ""
db_host = ""
db_name = ""
db_port = 3306

db = DB()
db.connect(db_user, db_pass, db_name, db_host, db_port)

data = data_generator(data_cnt)

for test_func in [insert_tester, query_tester]:
    test = test_func.__name__.replace("_tester", "")
    times = {
        "original": {"max": 0, "min": inf, "tot": 0},
        "sha256": {"max": 0, "min": inf, "tot": 0},
        "md5": {"max": 0, "min": inf, "tot": 0}
    }

    for i in range(repeat):
        print(f"{test} {i + 1} times")
        for func in [original, sha256, md5]:
            if test_func == insert_tester:
                db_clear(db, func.__name__)
            t = test_func(db, data, func, func.__name__)
            if t > times[func.__name__]["max"]:
                times[func.__name__]["max"] = t
            if t < times[func.__name__]["min"]:
                times[func.__name__]["min"] = t
            times[func.__name__]["tot"] += t
            print(f'{func.__name__}: {t}')
        print()

    print(f"{test} average")
    for v in times:
        print(v)
        print("min:", times[v]["min"])
        print("max:", times[v]["max"])
        print("avg:", times[v]["tot"] / repeat)
        print()