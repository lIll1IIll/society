import pymysql

class DB:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self, id, pw, db, host='localhost', port=3306):
        self.conn = pymysql.connect(host=host, port=port, user=id, password=pw, db=db, charset='utf8')
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()
        self.conn = None
        self.cursor = None

    def execute(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchmany(self, size=1):
        return self.cursor.fetchmany(size)

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def __del__(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None