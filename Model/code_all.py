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
    {"name": "非月卡菜地<65", "code": "非月卡菜地64", "uuid": 111, "team": 1},
    {"name": "非月卡牧场<65", "code": "非月卡牧场64", "uuid": 112, "team": 1},
    {"name": "非月卡菜地>=65", "code": "非月卡菜地65", "uuid": 113, "team": 1},
    {"name": "非月卡牧场>=65", "code": "非月卡牧场65", "uuid": 114, "team": 1},
    {
        "name": "非月卡鱼塘",
        "code": "非月卡鱼塘",
        "uuid": 205,
        "team": 2,
        "remark": "2传入pieces",
    },
    {"name": "非月卡加工器", "code": "非月卡加工器", "uuid": 116, "team": 1},
    {"name": "非月卡餐厅", "code": "非月卡餐厅", "uuid": 117, "team": 1},
]

r3 = (
    {
        "name": "去好友家炸鱼",
        "code": "炸鱼",
        "uuid": 301,
        "team": 3,
        "remark": "3传入text",
    },
    {
        "name": "输入好友UID/昵称",
        "code": "输入好友名称",
        "uuid": 302,
        "team": 3,
        "remark": "3传入text",
    },
)

r4 = [
    {
        "name": "编号1",
        "uuid": 401,
        "code": "去好友家泡温泉",
        "decode": ["炸鱼前", "输入好友名称", "喝咖啡", "回家"],
        "team": 4,
        "remark": "4组合脚本",
    },
    {"name": "编号2", "uuid": 402, "code": "自定义2", "team": 4},
    {"name": "编号3", "uuid": 403, "code": "自定义3", "team": 4},
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
