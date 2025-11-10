import json
from Model.model_script import DB_CodeList, Model_Code


r1 = [
    {"name": "无人机", "code": "无人机", "uuid": 101, "team": 1, "remark": "1直接调用"},
    {"name": "解锁鱼塘", "code": "开鱼塘", "uuid": 102, "team": 1},
    {"name": "收鱼缸", "code": "收鱼缸", "uuid": 103, "team": 1},
    {"name": "泡温泉", "code": "泡温泉", "uuid": 104, "team": 1},
    {"name": "泡+喝咖啡", "code": "喝咖啡", "uuid": 105, "team": 1},
    {"name": "神像:许愿金币", "code": "许愿金币", "uuid": 106, "team": 1},
    {"name": "神像:许愿经验", "code": "许愿经验", "uuid": 107, "team": 1},
    {"name": "摸小狗", "code": "摸小狗", "uuid": 108, "team": 1},
    {"name": "投喂小狗", "code": "投喂小狗", "uuid": 109, "team": 1},
]

r2 = [
    {"name": "非月卡菜地<65", "code": "非月卡菜地64", "uuid": 201, "team": 1},
    {"name": "非月卡牧场<65", "code": "非月卡牧场64", "uuid": 202, "team": 1},
    {
        "name": "非月卡鱼塘<65",
        "code": "非月卡鱼塘64",
        "decode": ["走到鱼塘边", "钓鱼3连 * pieces", "钓鱼后复位"],
        "uuid": 208,
        "team": 4,
    },
    {"name": "非月卡菜地>=65", "code": "非月卡菜地65", "uuid": 203, "team": 1},
    {"name": "非月卡牧场>=65", "code": "非月卡牧场65", "uuid": 204, "team": 1},
    {
        "name": "非月卡鱼塘>=65",
        "code": "非月卡鱼塘65",
        "decode": ["走到鱼塘边65", "钓鱼3连65 * pieces", "钓鱼后复位65"],
        "uuid": 205,
        "team": 4,
    },
    {"name": "非月卡加工器", "code": "非月卡加工器", "uuid": 206, "team": 1},
    {"name": "非月卡餐厅", "code": "非月卡餐厅", "uuid": 207, "team": 1},
]

r3 = (
    {
        "name": "去好友家炸鱼",
        "code": "炸鱼",
        "decode": ["炸鱼前", "输入好友名称?text", "炸鱼中"],
        "uuid": 301,
        "team": 4,
        "remark": "3炸鱼专用",
    },
)

r4 = [
    {
        "name": "编号1",
        "uuid": 401,
        "code": "去好友家泡温泉",
        "decode": ["炸鱼前", "输入好友名称2?text", "喝咖啡", "回家"],
        "team": 4,
        "remark": "4组合脚本: text为关键字",
    },
    {
        "name": "编号2",
        "uuid": 402,
        "code": "非月卡鱼塘2",
        "decode": ["走到鱼塘边", "钓鱼3连 * 7", "钓鱼后复位"],
        "team": 4,
        "remark": "4组合脚本: 演示, 重复",
    },
    {
        "name": "编号3",
        "uuid": 403,
        "code": "炸鱼2",
        "decode": ["炸鱼前", "输入好友名称2?这是我名字", "炸鱼中"],
        "team": 4,
        "remark": "4组合脚本: 演示, 好友名称",
    },
    {"name": "非月卡餐厅", "code": "非月卡餐厅_前台SW", "uuid": 404, "team": 1},
    {
        "name": "非月卡鱼塘>=65",
        "code": "非月卡鱼塘old",
        "decode": ["走到鱼塘边65", "钓鱼3连65 * 16", "钓鱼后复位65"],
        "uuid": 205,
        "team": 4,
        "remark": "兼容旧版本",
    },
]


def g_default_codeList():
    db = DB_CodeList()
    db.create_table()
    r = [*r1, *r2, *r3, *r4]
    data = []
    for i in r:
        a = Model_Code.model_validate(i)
        d = a.model_dump()
        if d["decode"] is not None:
            d["decode"] = json.dumps(d["decode"], ensure_ascii=False)
        data.append(d)
    db.write_db(data)
