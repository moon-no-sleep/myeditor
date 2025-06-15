import os
import yaml

from action_define.config import *
from action_define.action_base import *
from action_define.action_farmland_65 import 非月卡菜地
from action_define.action_animal import 非月卡牧场
from action_define.action_fishpond import 非月卡鱼塘
from action_define.action_catch_fish import 炸鱼
from action_define.action_processor import 非月卡加工器
from action_define.action_general import *
from action_define.action_restaurant import 非月卡餐厅, 非月卡餐厅_发射器
from action_define.action_farmland_less65 import 非月卡菜地小于65级
from action_define.action_red_fox import 小红狐全部, 小红狐菜地, 小红狐牧场, 小红狐鱼塘

actions_tree = {
    "无人机": 无人机v2,
    "非月卡菜地": 非月卡菜地,
    "非月卡牧场": 非月卡牧场,
    "非月卡鱼塘": 非月卡鱼塘,
    "开鱼塘": 开鱼塘,
    "收鱼缸": 收鱼缸,
    "泡温泉": 泡温泉,
    "喝咖啡": 喝咖啡,
    "许愿经验": 许愿经验,
    "许愿金币": 许愿金币,
    "摸小狗": 摸小狗,
    "投喂小狗": 投喂小狗,
    "炸鱼": 炸鱼,
    "非月卡加工器": 非月卡加工器,
    "非月卡餐厅": 非月卡餐厅,
}

current_path = os.path.dirname(os.path.abspath(__file__))
if 切换有摇杆_无摇杆:
    path_folder = os.path.join(current_path, f"script/script_not_wasd")
    print("无摇杆路径")
else:
    path_folder = os.path.join(current_path, f"script/script_default")
    print("有摇杆路径")


def write_script(i):
    """写入文件

    Args:
        i (str): 指定文件
    """
    path_action_tree = os.path.join(path_folder, f"{i}.yaml")
    with open(path_action_tree, "w", encoding="utf-8") as f:
        yaml.dump(actions_tree[i], f, allow_unicode=True, sort_keys=False)


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
        "非月卡菜地64": 非月卡菜地小于65级,
        "小红狐全部": 小红狐全部,
        "小红狐菜地": 小红狐菜地,
        "小红狐牧场": 小红狐牧场,
        "小红狐鱼塘": 小红狐鱼塘,
        "非月卡餐厅biu": 非月卡餐厅_发射器,
    }
    for i in actions_tree:
        path_action_tree = os.path.join(path_folder, f"custom/{i}.yaml")
        with open(path_action_tree, "w", encoding="utf-8") as f:
            yaml.dump(actions_tree[i], f, allow_unicode=True, sort_keys=False)
    print("自定义脚本已生成")


if __name__ == "__main__":
    # 请先在config.py中设置有摇杆或无摇杆模式
    print("有摇杆模式: ", not 切换有摇杆_无摇杆)

    main_script("all")  # 更新所有脚本
    # main_script("非月卡菜地小于65")  # 单点更新指定脚本

    custom_script()

    print("更新完成")
