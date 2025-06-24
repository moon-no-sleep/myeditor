from action_define.action_base import *


第1行地初始位置 = MyView(a=(504, 280))
第2行地初始位置 = MyView(a=(491, 288))
第3行地初始位置 = MyView(a=(469, 297))
第4行地初始位置 = MyView(a=(438, 308))
第5行地初始位置 = MyView(a=(405, 320))
第6行地初始位置 = MyView(a=(364, 324))


下一块地 = (
    {
        "step": "走到下一块地",
        "type": "key",
        "input": "W",
        "delay": 650,
    },
    step_sleep(1),
    *[
        大功能键,
        step_sleep(2),
    ]
    * 3,
)


def MyfarmRow(start_position=第1行地初始位置):
    steps = (
        *发射器,
        *start_position,
        {
            "step": "发射",
            "type": "mouse",
            "input": "click",
            "point": (880, 450),
        },
        step_sleep(4),
        *MyView(a=(378, 280)) * 2,
        *[
            大功能键,
            step_sleep(2),
        ]
        * 3,
        *下一块地,
        *下一块地,
        *下一块地,
        *下一块地,
        step_sleep(1),
    )
    return steps


#  -----分割线-----
菜地1 = MyfarmRow(start_position=第1行地初始位置)
菜地2 = MyfarmRow(start_position=第2行地初始位置)
菜地3 = MyfarmRow(start_position=第3行地初始位置)
菜地4 = MyfarmRow(start_position=第4行地初始位置)
菜地5 = MyfarmRow(start_position=第5行地初始位置)
菜地6 = MyfarmRow(start_position=第6行地初始位置)


非月卡菜地64 = (
    *菜地1,
    *菜地2,
    *菜地3,
    *菜地4,
    *菜地5,
    *菜地6,
    step_sleep(1),
    复位鼠标,
)
