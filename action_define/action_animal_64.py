from action_define.action_base import *


第1行地初始位置 = MyView(a=(612, 285))
第2行地初始位置 = MyView(a=(605, 300))
第3行地初始位置 = MyView(a=(604, 320))
第4行地初始位置 = MyView(a=(596, 349))
第5行地初始位置 = MyView(a=(586, 385))


种菜2连 = (
    大功能键,
    step_sleep(2),
    {
        "step": "左侧复位",
        "type": "mouse",
        "input": "click",
        "point": (100, 470),
    },
    step_sleep(0.5),
    大功能键,
    step_sleep(2),
    {
        "step": "左侧复位",
        "type": "mouse",
        "input": "click",
        "point": (100, 470),
    },
    step_sleep(0.5),
)
下一块地 = (
    D键按下,
    跳跃键,
    step_sleep(0.72),
    D键松开,
    step_sleep(1),
    *种菜2连,
)


def MyfarmRow(start_position=第2行地初始位置):
    return (
        *发射器,
        *start_position,
        {
            "step": "发射",
            "type": "mouse",
            "input": "click",
            "point": (880, 450),
        },
        step_sleep(2.5),
        *种菜2连,
        *下一块地,
        *下一块地,
    )


#  -----分割线-----
牧场1 = MyfarmRow(start_position=第1行地初始位置)
牧场2 = MyfarmRow(start_position=第2行地初始位置)
牧场3 = MyfarmRow(start_position=第3行地初始位置)
牧场4 = MyfarmRow(start_position=第4行地初始位置)
牧场5 = MyfarmRow(start_position=第5行地初始位置)


非月卡牧场64 = (
    *[
        *牧场1,
        *牧场2,
        *牧场3,
        *牧场4,
        *牧场5,
    ]
    * 2,
    复位鼠标,
)
