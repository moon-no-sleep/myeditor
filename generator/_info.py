from Model.infoTable import InfoTable


info = [
    "version: 5.3.0",
    "本表 _info 说明: 本表_info 的内容不会影响app, 只作为说明.",
    "app调用本表时, 携带数据格式比如 code=None, team=1, text=None, pieces=None",
    "code为代码名称(关键参数), team为类别, text为文本(如好友昵称), pieces为数值(如钓鱼次数).",
    "app执行时, 先到表code_list 根据code查找对应的code.",
    "code 的team为1时, 直接查找对应的表.",
    "code 的team为4时, 解析decode, 直到team为1, 查找对应的表.",
]
info2 = [{"detail": i} for i in info]


def write_info():
    data = info2
    table = "_info"

    db = InfoTable(table)
    db.create_table()
    db.write_db(data)
    db.close_db()
