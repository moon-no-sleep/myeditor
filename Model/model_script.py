import json
import os
import sqlite3
from pydantic import BaseModel

from env import current_path


def data_model_format(data):
    """转换脚本dict数据, 补充缺失的字段值. 先将json数据转为model格式, 再重新转换为dict

    Args:
        data (tuple): 脚本

    Returns:
        list: 转换后的脚本
    """
    script = []
    for i in data:
        a = Model_Script.model_validate(i)
        d = a.model_dump()
        if d.get("point") is not None:
            d["point"] = json.dumps(d.get("point"))
        script.append(d)
    return script


class Model_Script(BaseModel):
    id: int | None = None
    step: str
    type: str
    input: str | None = None
    point: tuple | None = None
    delay: int | None = None
    time: float | None = None
    remark: str | None = None


class DB_Scrpit:
    def __init__(self, table):
        path = os.path.join(current_path, "script/db_script.db")
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.table = table
        self.columns = list(Model_Script.model_fields.keys())

        self.create_sql = f""" CREATE TABLE IF NOT EXISTS `{self.table}`(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                step TEXT,
                type INT,
                input TEXT,
                point INT,
                delay TEXT,
                time TEXT,
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
        columns = ", ".join([f"`{s}`" for s in self.columns])
        placeholders = ", ".join("?" * len(self.columns))
        sql = f"""INSERT OR REPLACE INTO `{self.table}` ({columns})VALUES({placeholders})"""

        for i in data:
            self.cur.execute(
                sql,
                list(i.values()),
            )
        self.con.commit()

    def update_db(self, data):
        columns = "= ? , ".join(data[0].keys())

        sql = f"""UPDATE {self.table} SET ({columns}) WHERE id = {i['id']}"""

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

    def close_db(self):
        """关闭数据库"""
        self.con.close()
