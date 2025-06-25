from action_define.action_base import *
from action_define.action_fishpond import 走到鱼塘边
from action_define.action_animal_64 import 非月卡牧场64
from action_define.action_farmland_64 import 非月卡菜地64

去小红狐家 = (
    点击社交,
    step_sleep(1),
    点击输入栏,
    step_sleep(1),
    {
        "step": "键入好友昵称",
        "type": "insert",
        "input": "小红狐",
        "delay": None,
    },
    step_sleep(1),
    Enter键位,
    step_sleep(0.5),
    点击拜访,
    step_sleep(0.5),
    弹窗取消,
    step_sleep(15),
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

_小红狐牧场 = (*非月卡牧场64,)
_小红狐菜地 = (*非月卡菜地64,)
_小红狐鱼塘 = (
    *走到鱼塘边,
    *[大功能键, step_sleep(2)] * 10,
)


小红狐全部 = (*去小红狐家, *_小红狐菜地, *_小红狐牧场, *_小红狐鱼塘, *回家)
小红狐菜地 = (*去小红狐家, *_小红狐菜地, *回家)
小红狐牧场 = (*去小红狐家, *_小红狐牧场, *回家)
小红狐鱼塘 = (*去小红狐家, *_小红狐鱼塘, *回家)
