from action_define.action_base import *

加工操作 = (
    大功能键,
    step_sleep(2),
    左侧复位,
    step_sleep(1),
    大功能键,
    step_sleep(2),
    左侧复位,
    step_sleep(0.5),
)

加工北 = (
    {
        "step": "向北走",
        "type": "key",
        "input": "W",
        "delay": 280,
    },
    step_sleep(1),
    *加工操作,
)

加工北2 = (
    {
        "step": "向北走2",
        "type": "key",
        "input": "W",
        "delay": 285,
    },
    step_sleep(1),
    *加工操作,
)
加工器视角 = MyView(a=(370, 247))
非月卡加工器 = (
    *发射器,
    *加工器视角,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
    },
    step_sleep(3),
    {
        "step": "走进小屋",
        "type": "key",
        "input": "A",
        "delay": 1500,
    },
    step_sleep(12),
    复位鼠标,
    step_sleep(1),
    {
        "step": "向北走点",
        "type": "key",
        "input": "W",
        "delay": 225,
    },
    step_sleep(0.5),
    {
        "step": "东拐到底",
        "type": "key",
        "input": "D",
        "delay": 2000,
    },
    *加工操作,
    *加工北 * 5,
    复位鼠标,
    step_sleep(1),
    {
        "step": "向北走点",
        "type": "key",
        "input": "W",
        "delay": 225,
    },
    step_sleep(0.5),
    {
        "step": "东拐到底",
        "type": "key",
        "input": "D",
        "delay": 2000,
    },
    step_sleep(1),
    *加工操作,
    *加工北2 * 5,
    复位鼠标,
    step_sleep(1),
    {
        "step": "走出小屋",
        "type": "key",
        "input": "S",
        "delay": 1200,
    },
    step_sleep(1),
    {
        "step": "确认不捡物品",
        "type": "mouse",
        "input": "click",
        "point": (609, 353),
    },
    step_sleep(1),
    {
        "step": "走出小屋",
        "type": "key",
        "input": "S",
        "delay": 1500,
    },
    大功能键,
    step_sleep(12),
    {
        "step": "走出小屋",
        "type": "key",
        "input": "S",
        "delay": 200,
    },
    复位鼠标,
)
