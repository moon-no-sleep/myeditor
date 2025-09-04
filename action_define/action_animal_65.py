from action_define.action_base import *


第1行地初始位置 = MyView(a=(586, 385))
第2行地初始位置 = MyView(a=(680, 389))
第3行地初始位置 = MyView(a=(761, 368))


下一块地 = (
    {
        "step": "走到下一块地",
        "type": "key",
        "input": "W",
        "delay": 1300,
    },
    step_sleep(2.5),
)

下一块地3 = (
    {
        "step": "走到下一块地",
        "type": "down",
        "input": "A",
        "delay": None,
    },
    {
        "step": "走到下一块地",
        "type": "key",
        "input": "W",
        "delay": 1300,
    },
    {
        "step": "走到下一块地",
        "type": "up",
        "input": "A",
        "delay": None,
    },
    step_sleep(2.5),
)


#  -----分割线-----
牧场1 = (
    *发射器小车,
    *第1行地初始位置,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
    },
    step_sleep(5),
    {
        "step": "调方向",
        "type": "key",
        "input": "D",
        "delay": 200,
    },
    step_sleep(1),
    *下一块地 * 4,
)

牧场2 = (
    *发射器小车,
    *第2行地初始位置,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
    },
    step_sleep(5),
    {
        "step": "调方向",
        "type": "key",
        "input": "A",
        "delay": 200,
    },
    step_sleep(1),
    *下一块地 * 4,
)

牧场3 = (
    *发射器小车,
    *第3行地初始位置,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
    },
    step_sleep(5),
    *下一块地3 * 4,
    {
        "step": "微调",
        "type": "key",
        "input": "D",
        "delay": 200,
    },
    step_sleep(2.5),
)

非月卡牧场65 = (
    *牧场1,
    *牧场2,
    *牧场3,
    复位鼠标,
)
