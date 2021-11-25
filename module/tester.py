import time
from module.DB import DB

def db_clear(db: DB, db_name: str):
    db.execute(f"DELETE FROM {db_name}")
    db.execute(f"ALTER TABLE {db_name} AUTO_INCREMENT = 1")

def insert_tester(db: DB, data: tuple, hash_func: callable, db_name: str):
    start = time.time()
    for i in data:
        name, age, address, phone, pw = i
        pw = hash_func(pw)
        sql = f"INSERT INTO {db_name}(name, age, address, phone, pw) VALUES('{name}', {age}, '{address}', '{phone}', '{pw}')"
        db.execute(sql)
    end = time.time()
    return end - start

def query_tester(db: DB, data: tuple, hash_func: callable, db_name: str):
    start = time.time()
    for i in data:
        name, age, address, phone, pw = i
        pw = hash_func(pw)
        sql = f"SELECT * FROM {db_name} WHERE name='{name}' AND pw='{pw}'"
        db.execute(sql)
        db.fetchall()
    end = time.time()
    return end - start