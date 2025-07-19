import os
import sqlite3
from env import current_path


class BaseTable:
    def __init__(self, table, db="Users/db_myfarm.db"):
        path = os.path.join(current_path, db)
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

        self.table = table
        self.columns = self.get_columns()

        self.create_sql = f""" CREATE TABLE IF NOT EXISTS `{self.table}`(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                checked INT,
                text TEXT,
                value INT,
                unit TEXT,
                trigger TEXT,
                category TEXT,
                code INT ,
                uuid INT UNIQUE,
                mode TEXT,
                page TEXT,
                groups TEXT,
                remark TEXT
                );
        """

    def create_table(self):

        try:
            self.cur.execute(self.create_sql)
        except Exception as e:
            print(e)
        self.con.commit()

    def write_db(self, data: list):
        columns = ", ".join([f"`{s}`" for s in data[0].keys()])
        placeholders = ", ".join("?" * len(data[0]))
        sql = f"""INSERT OR REPLACE INTO `{self.table}` ({columns})VALUES({placeholders})"""

        for i in data:
            self.cur.execute(
                sql,
                list(i.values()),
            )
        self.con.commit()

    def update_db(self, data):
        columns = "= ? , ".join(data[0].keys())

        sql = f"""UPDATE {self.table} SET ({columns}) WHERE uuid = {i['uuid']}"""

        for i in data:
            self.cur.execute(
                sql,
                list(i.values()),
            )
        self.con.commit()

    def read_db(self) -> list:
        data = []
        sql = f"""   SELECT * FROM {self.table}; """
        self.cur.execute(sql)
        r = self.cur.fetchall()
        for i in r:
            result = dict(zip(self.columns, i))
            data.append(result)
        return data

    def read_db_latest(self) -> list:
        data = []
        sql = f"""   SELECT * FROM {self.table} WHERE id = (SELECT MAX(id) from {self.table}  ); """
        self.cur.execute(sql)
        r = self.cur.fetchall()
        for i in r:
            result = dict(zip(self.columns, i))
            data.append(result)
        return data

    def read_db_checked(self) -> list:
        data = []
        sql = f"""   SELECT * FROM {self.table} WHERE checked=1; """
        self.cur.execute(sql)
        r = self.cur.fetchall()
        for i in r:
            result = dict(zip(self.columns, i))
            data.append(result)
        return data

    def get_columns(self):

        self.cur.execute(f"""PRAGMA table_info({self.table});""")
        r = self.cur.fetchall()
        columns = [i[1] for i in r]
        return columns

    def close_db(self):
        """关闭数据库"""
        self.con.close()
