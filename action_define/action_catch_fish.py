from action_define.action_base import *
from action_define.action_fishpond import 走到鱼塘边

炸鱼前 = (
    {
        "step": "点击社交",
        "type": "mouse",
        "input": "click",
        "point": (965, 169),
    },
    step_sleep(1),
    {
        "step": "点击输入栏",
        "type": "mouse",
        "input": "click",
        "point": (694, 537),
    },
    step_sleep(1),
)

炸鱼中 = (
    step_sleep(1),
    {
        "step": "Enter",
        "type": "key",
        "input": "Enter",
        "delay": None,
    },
    step_sleep(0.5),
    {
        "step": "拜访",
        "type": "mouse",
        "input": "click",
        "point": (967, 174),
    },
    step_sleep(0.5),
    弹窗取消,
    step_sleep(12),
    *走到鱼塘边,
    大功能键,
    step_sleep(2),
    大功能键,
    step_sleep(2),
    大功能键,
    step_sleep(2),
    大功能键,
    step_sleep(2),
    大功能键,
    step_sleep(2),
    大功能键,
    step_sleep(2),
    大功能键,
    step_sleep(2),
    大功能键,
    step_sleep(2),
    大功能键,
    step_sleep(2),
    大功能键,
    step_sleep(2),
    {
        "step": "回家",
        "type": "mouse",
        "input": "click",
        "point": (909, 30),
    },
    step_sleep(12),
    头像复位,
    step_sleep(1),
    头像复位,
    step_sleep(1),
)

炸鱼 = {"炸鱼前": 炸鱼前, "炸鱼中": 炸鱼中}
