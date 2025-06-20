from action_define.action_base import *
from action_define.action_fishpond import 走到鱼塘边


炸鱼前 = (
    点击社交,
    step_sleep(1),
    点击输入栏,
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
    *[大功能键, step_sleep(2)] * 10,
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

炸鱼 = {"炸鱼前": 炸鱼前, "炸鱼中": 炸鱼中}
