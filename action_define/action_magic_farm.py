from action_define.action_base import *


去奇迹农场 = [
    复位鼠标,
    step_sleep(0.5),
    复位鼠标,
    step_sleep(1),
    {
        "step": "去奇迹农场1",
        "type": "key",
        "input": "S",
        "delay": 600,
    },
    step_sleep(1),
    {
        "step": "去奇迹农场2",
        "type": "key",
        "input": "D",
        "delay": 2000,
    },
    step_sleep(1),
    大功能键,
    step_sleep(1),
    确认解锁,
    step_sleep(1),
    大功能键,
    step_sleep(15),
]


收菜_无人机 = [
    复位鼠标,
    step_sleep(1),
    {
        "step": "无人机1",
        "type": "key",
        "input": "W",
        "delay": 200,
    },
    step_sleep(1),
    {
        "step": "无人机2",
        "type": "key",
        "input": "A",
        "delay": 1200,
    },
    step_sleep(1),
    Q键位置,
    step_sleep(1),
    确认解锁,
    step_sleep(1),
]
收菜_手工 = [
    复位鼠标,
    step_sleep(1),
    {
        "step": "往前走1",
        "type": "key",
        "input": "W",
        "delay": 1200,
    },
    step_sleep(1),
    {
        "step": "往前走2",
        "type": "key",
        "input": "A",
        "delay": 1200,
    },
    step_sleep(1),
    *[
        {
            "step": "Q键位置",
            "type": "key",
            "input": "Q",
            "delay": 5000,
        }
        * 12
    ],
    step_sleep(1),
]

奇迹农场_卖菜 = [
    复位鼠标,
    step_sleep(1),
    {
        "step": "仓库",
        "type": "mouse",
        "input": "click",
        "point": (956, 96),
    },
    step_sleep(1),
    {
        "step": "果实",
        "type": "mouse",
        "input": "click",
        "point": (975, 157),
    },
    step_sleep(1),
    {
        "step": "批量出售",
        "type": "mouse",
        "input": "click",
        "point": (750, 517),
    },
    step_sleep(1),
    {
        "step": "出售",
        "type": "mouse",
        "input": "click",
        "point": (828, 512),
    },
    step_sleep(1),
    左侧复位,
    step_sleep(1),
    左侧复位,
]

离开奇迹农场 = [
    复位鼠标,
    step_sleep(1),
    {
        "step": "离开奇迹农场1",
        "type": "key",
        "input": "D",
        "delay": 1500,
    },
    step_sleep(1),
    {
        "step": "离开奇迹农场2",
        "type": "key",
        "input": "W",
        "delay": 600,
    },
    step_sleep(1),
    大功能键,
    step_sleep(15),
    头像复位,
    step_sleep(1),
    头像复位,
    step_sleep(1),
]

奇迹农场_无人机 = [*去奇迹农场, *收菜_无人机, *奇迹农场_卖菜, *离开奇迹农场]

奇迹农场_手动 = [*去奇迹农场, *收菜_手工, *奇迹农场_卖菜, *离开奇迹农场]
