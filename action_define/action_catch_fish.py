from action_define.action_base import *
from action_define.action_fishpond import 走到鱼塘边


开鱼塘 = (
    *发射器,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
    },
    step_sleep(2.5),
    {
        "step": "走到鱼塘边",
        "type": "key",
        "input": "W",
        "delay": 1900,
    },
    step_sleep(1),
    点击普通鱼塘解锁,
    step_sleep(1),
    确认解锁,
    点击金彩鱼塘解锁,
    step_sleep(1),
    确认解锁,
    step_sleep(1),
)

开鱼塘2 = (
    step_sleep(1),
    点击普通鱼塘解锁,
    step_sleep(1),
    确认解锁,
    点击金彩鱼塘解锁,
    step_sleep(1),
    确认解锁,
    step_sleep(1),
)


炸鱼前 = (
    点击社交,
    step_sleep(1),
    点击输入栏,
    step_sleep(1),
)
回家 = (
    点击回家,
    step_sleep(1),
    确认解锁,
    step_sleep(15),
    头像复位,
    step_sleep(1),
    头像复位,
    step_sleep(1),
    左侧复位,
    step_sleep(1),
)
炸鱼中 = (
    step_sleep(1),
    Enter键位,
    step_sleep(0.5),
    点击拜访,
    step_sleep(0.5),
    弹窗取消,
    step_sleep(15),
    *走到鱼塘边,
    *[大功能键, step_sleep(1)] * 30,
    *回家,
)

炸鱼 = {"炸鱼前": 炸鱼前, "炸鱼中": 炸鱼中}

输入好友名称2 = [
    {
        "step": "键入好友昵称",
        "type": "insert",
        "input": "好友昵称/UID",
        "delay": None,
    },
    step_sleep(1),
    Enter键位,
    step_sleep(0.5),
    点击拜访,
    step_sleep(0.5),
    弹窗取消,
    step_sleep(15),
]

输入好友名称 = [
    {
        "step": "键入好友昵称",
        "type": "insert",
        "input": "好友昵称/UID",
        "delay": None,
    },
]
