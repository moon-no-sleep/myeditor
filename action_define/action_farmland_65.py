from action_define.action_base import *

第1行地初始位置 = MyView(a=(364, 324))
第2行地初始位置 = MyView(a=(352, 306))
第3行地初始位置 = MyView(a=(345, 294))
第4行地初始位置 = MyView(a=(339, 281))
第5行地初始位置 = MyView(a=(336, 271))

第1行地初始位置b = MyView(a=(367, 322))
第2行地初始位置b = MyView(a=(354, 304))
第3行地初始位置b = MyView(a=(348, 289))
第4行地初始位置b = MyView(a=(339, 281))
第5行地初始位置b = MyView(a=(336, 271))

下一块地 = (
    {
        "step": "走到下一块地",
        "type": "key",
        "input": "D",
        "delay": 1100,
    },
    step_sleep(3),
)


def MyfarmRow(start_position=第1行地初始位置):
    steps = (
        *发射器小车,
        *start_position,
        {
            "step": "发射",
            "type": "mouse",
            "input": "click",
            "point": (880, 450),
        },
        step_sleep(6),
        *下一块地 * 5,
        step_sleep(2),
    )
    return steps


菜地1 = MyfarmRow(start_position=第1行地初始位置)
菜地2 = MyfarmRow(start_position=第2行地初始位置)
菜地3 = MyfarmRow(start_position=第3行地初始位置)
菜地4 = MyfarmRow(start_position=第4行地初始位置)
菜地5 = MyfarmRow(start_position=第5行地初始位置)

菜地1b = MyfarmRow(start_position=第1行地初始位置b)
菜地2b = MyfarmRow(start_position=第2行地初始位置b)
菜地3b = MyfarmRow(start_position=第3行地初始位置b)
菜地4b = MyfarmRow(start_position=第4行地初始位置b)
菜地5b = MyfarmRow(start_position=第5行地初始位置b)

非月卡菜地65 = (
    *菜地1,
    *菜地2,
    *菜地3,
    *菜地4,
    *菜地5,
    step_sleep(1),
    复位鼠标,
    *菜地1b,
    *菜地2b,
    *菜地3b,
    *菜地4b,
    *菜地5b,
    step_sleep(1),
    复位鼠标,
)
