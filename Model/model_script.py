import json
from pydantic import BaseModel
from .baseTable import BaseTable


class Model_Script(BaseModel):
    id: int | None = None
    step: str
    type: str
    input: str | None = None
    point: tuple | None = None
    delay: int | None = None
    time: float | None = None
    remark: str | None = None


class DB_Scrpit(BaseTable):
    def __init__(self, table, db="script/db_script.db"):
        super().__init__(table, db)

        self.create_sql = f""" CREATE TABLE IF NOT EXISTS `{self.table}`(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                step TEXT,
                type TEXT,
                input TEXT,
                point TEXT,
                delay INT,
                time REAL,
                remark TEXT
                );
        """

    def format_db_data_into(self, data):
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

    def format_db_data_out(self, data):
        """转换脚本dict数据, 将point的值 json.loads

        Args:
            data (tuple): 脚本

        Returns:
            list: 转换后的脚本
        """
        script = []
        for d in data:
            if d.get("point") is not None:
                d["point"] = json.loads(d.get("point"))
            script.append(d)
        return script


class Model_Code(BaseModel):
    id: int | None = None
    name: str | None = None
    code: str
    team: int
    decode: list | None = None
    uuid: int | None = None
    remark: str | None = None


class DB_CodeList(BaseTable):
    def __init__(self, table="code_list", db="script/db_script.db"):
        super().__init__(table, db)

        self.create_sql = f""" CREATE TABLE IF NOT EXISTS `{self.table}`(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                code TEXT UNIQUE,
                team INT,
                decode TEXT,
                uuid INT,
                remark TEXT
                );
        """
