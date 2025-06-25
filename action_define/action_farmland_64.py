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

种菜3连 = (大功能键, step_sleep(2)) * 3

下一块地 = (
    {
        "step": "走到下一块地",
        "type": "key",
        "input": "W",
        "delay": 650,
    },
    step_sleep(1),
    *种菜3连,
)


def MyfarmRow(start_position=第1行地初始位置, angle=(544, 280)):
    steps = (
        *发射器,
        *start_position,
        大功能键,
        step_sleep(4),
        *MyView(a=(628, 280)),
        step_sleep(0.5),
        *MyView(a=angle),
        step_sleep(1),
        *种菜3连,
        *下一块地 * 5,
        step_sleep(2),
    )
    return steps


菜地1 = MyfarmRow(start_position=第1行地初始位置)
菜地2 = MyfarmRow(start_position=第2行地初始位置)
菜地3 = MyfarmRow(start_position=第3行地初始位置)
菜地4 = MyfarmRow(start_position=第4行地初始位置, angle=(548, 280))
菜地5 = MyfarmRow(start_position=第5行地初始位置, angle=(548, 280))

菜地1b = MyfarmRow(start_position=第1行地初始位置b)
菜地2b = MyfarmRow(start_position=第2行地初始位置b)
菜地3b = MyfarmRow(start_position=第3行地初始位置b)
菜地4b = MyfarmRow(start_position=第4行地初始位置b, angle=(548, 280))
菜地5b = MyfarmRow(start_position=第5行地初始位置b, angle=(548, 280))

非月卡菜地64 = (
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
