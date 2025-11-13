from action_define.action_base import *


def MyView_magic_farm(a=(491, 288)):
    # 拉视角2
    return (
        {
            "step": "拉动视角1",
            "type": "mouse",
            "input": "move",
            "point": (504, 280),
        },
        step_sleep(0.5),
        {
            "step": "拉动视角2",
            "type": "mouse",
            "input": "down",
            "point": None,
        },
        step_sleep(0.5),
        {
            "step": "拉动视角3",
            "type": "mouse",
            "input": "move",
            "point": (a[0], a[1]),
            "delay": 20,
        },
        step_sleep(0.5),
        {
            "step": "拉动视角4",
            "type": "mouse",
            "input": "up",
            "point": None,
        },
        step_sleep(0.5),
    )


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
        "delay": 600,
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
收菜_手工_v1 = [
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
            "delay": 15000,
        }
    ]
    * 4,
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
            "delay": 15000,
        }
    ]
    * 4,
    step_sleep(1),
    复位鼠标,
    step_sleep(1),
    {
        "step": "往前走1",
        "type": "key",
        "input": "W",
        "delay": 5000,
    },
    *MyView_magic_farm(a=[720, 280]),
    step_sleep(1),
    *[
        {
            "step": "Q键位置",
            "type": "key",
            "input": "Q",
            "delay": 15000,
        }
    ]
    * 4,
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


买种子 = [
    复位鼠标,
    step_sleep(1),
    Q键位置,
    step_sleep(1),
    {
        "step": "种子商店",
        "type": "mouse",
        "input": "click",
        "point": (884, 47),
    },
    step_sleep(8),
    Q键位置,
    step_sleep(1),
    {
        "step": "批量购买",
        "type": "mouse",
        "input": "click",
        "point": (668, 515),
    },
    step_sleep(1),
    {
        "step": "勾选全部",
        "type": "mouse",
        "input": "click",
        "point": (632, 519),
    },
    step_sleep(1),
    {
        "step": "结算",
        "type": "mouse",
        "input": "click",
        "point": (921, 519),
    },
    step_sleep(1),
    {
        "step": "购买确认",
        "type": "mouse",
        "input": "click",
        "point": (506, 408),
    },
    step_sleep(1),
    头像复位,
    step_sleep(1),
    头像复位,
    step_sleep(1),
    复位鼠标,
    step_sleep(1),
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
    step_sleep(1),
    左侧复位,
    step_sleep(15),
    头像复位,
    step_sleep(1),
    头像复位,
    step_sleep(1),
]

奇迹农场_无人机 = [*去奇迹农场, *收菜_无人机, *奇迹农场_卖菜, *买种子, *离开奇迹农场]

奇迹农场_手动 = [*去奇迹农场, *收菜_手工, *奇迹农场_卖菜, *买种子, *离开奇迹农场]
