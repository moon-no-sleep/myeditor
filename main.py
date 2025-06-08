import os
import yaml

from action_define.action_base import *
from action_define.action_farmland_65 import 非月卡菜地
from action_define.action_animal import 非月卡牧场
from action_define.action_fishpond import 非月卡鱼塘
from action_define.action_catch_fish import 炸鱼
from action_define.action_processor import 非月卡加工器
from action_define.action_general import *
from action_define.action_restaurant import 非月卡餐厅


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


def write_script(i):
    """写入文件

    Args:
        i (str): 指定文件
    """
    current_path = os.path.dirname(os.path.abspath(__file__))
    path_action_tree = os.path.join(current_path, f"script/{i}.yaml")
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


if __name__ == "__main__":
    main_script("all")  # 更新所有脚本
    # main_script("非月卡餐厅")  # 单点更新指定脚本

    print("更新完成")
