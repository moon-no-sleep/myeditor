import os
import yaml

from action_define.action_base import *
from action_define.action_farmland_65 import 非月卡菜地
from action_define.action_animal import 非月卡牧场
from action_define.action_fishpond import 非月卡鱼塘
from action_define.action_catch_fish import 炸鱼
from action_define.action_processor import 非月卡加工器
from action_define.action_general import *


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
}

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))

    # # 全部更新
    # for i in actions_tree:
    #     path_action_tree = os.path.join(current_path, f"script/{i}.yaml")
    #     with open(path_action_tree, "w", encoding="utf-8") as f:
    #         yaml.dump(actions_tree[i], f, allow_unicode=True, sort_keys=False)

    # 单点更新
    i ="喝咖啡"
    path_action_tree = os.path.join(current_path, f"script/{i}.yaml")
    with open(path_action_tree, "w", encoding="utf-8") as f:
        yaml.dump(actions_tree[i], f, allow_unicode=True, sort_keys=False)
