import json
from Model.model_script import DB_Scrpit, Model_Script, data_model_format
from config.config import *
from action_define.action_base import *
from action_define.action_general import *
from action_define.action_farmland_64 import 非月卡菜地64
from action_define.action_farmland_65 import 非月卡菜地65
from action_define.action_animal_64 import 非月卡牧场64
from action_define.action_animal_65 import 非月卡牧场65
from action_define.action_fishpond import 非月卡鱼塘, 走到鱼塘边
from action_define.action_catch_fish import 炸鱼前, 炸鱼中
from action_define.action_processor import 非月卡加工器
from action_define.action_restaurant import (
    非月卡餐厅,
    非月卡餐厅_发射器,
    非月卡餐厅_notWASD,
)
from action_define.action_red_fox import 小红狐全部, 小红狐菜地, 小红狐牧场, 小红狐鱼塘


actions_tree = {
    "无人机": 无人机v2,
    "非月卡菜地64": 非月卡菜地64,
    "非月卡菜地65": 非月卡菜地65,
    "非月卡牧场64": 非月卡牧场64,
    "非月卡牧场65": 非月卡牧场65,
    "非月卡鱼塘": 非月卡鱼塘,
    "开鱼塘": 开鱼塘,
    "收鱼缸": 收鱼缸,
    "泡温泉": 泡温泉,
    "喝咖啡": 喝咖啡,
    "许愿经验": 许愿经验,
    "许愿金币": 许愿金币,
    "摸小狗": 摸小狗,
    "投喂小狗": 投喂小狗,
    "非月卡加工器": 非月卡加工器,
    "非月卡餐厅": 非月卡餐厅,
    "走到鱼塘边": 走到鱼塘边,
    "炸鱼前": 炸鱼前,
    "炸鱼中": 炸鱼中,
}


def write_script(i):
    data = actions_tree[i]
    if 有摇杆:
        table = "default_" + i
    else:
        table = "notwasd_" + i

    db_recognition = DB_Scrpit(table)
    db_recognition.create_table()
    db_recognition.write_db(data_model_format(data))


def main_script(x="all"):
    """主程序

    Args:
        x (str, optional): 指定文件. Defaults to "all".
    """

    if x == "all":
        # 全部更新
        for i in actions_tree:
            write_script(i)
    else:
        # 单点更新
        write_script(x)


def custom_script():
    """生成自定义脚本"""
    actions_tree = {
        # "小红狐全部": 小红狐全部,
        # "小红狐菜地": 小红狐菜地,
        # "小红狐牧场": 小红狐牧场,
        # "小红狐鱼塘": 小红狐鱼塘,
        "非月卡餐厅发射器": 非月卡餐厅_发射器,
        "非月卡餐厅notWASD": 非月卡餐厅_notWASD,
    }
    for i in actions_tree:
        data = actions_tree[i]
        table = "custom_" + i
        db_recognition = DB_Scrpit(table)
        db_recognition.create_table()
        db_recognition.write_db(data_model_format(data))
