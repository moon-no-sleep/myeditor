from action_define.action_base import *


第1行地初始位置 = MyView(a=(367, 319))
第2行地初始位置 = MyView(a=(354, 304))
第3行地初始位置 = MyView(a=(348, 288))
第4行地初始位置 = MyView(a=(339, 280))
第5行地初始位置 = MyView(a=(336, 270))

第1行地初始位置b = MyView(a=(367, 321))
第2行地初始位置b = MyView(a=(354, 305))
第3行地初始位置b = MyView(a=(348, 290))
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


def MyfarmRow(start_position=第1行地初始位置, n=1):
    steps = (
        *发射器小车,
        *start_position,
        {
            "step": "发射",
            "type": "mouse",
            "input": "click",
            "point": (880, 450),
            "remark": "第" + str(n) + "行",
        },
        step_sleep(6),
        *下一块地 * 5,
        step_sleep(2),
    )
    return steps


菜地1 = (
    *发射器小车,
    *第1行地初始位置,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
        "remark": "第1行",
    },
    step_sleep(6),
    *下一块地 * 4,
    {"step": "走到下一块地", "type": "key", "input": "D", "delay": 1100},
    step_sleep(1),
    {"step": "微调", "type": "key", "input": "A", "delay": 200, "remark": "这块地微调"},
    step_sleep(3.5),
)
# 菜地1 = MyfarmRow(start_position=第1行地初始位置, n=1)
菜地2 = MyfarmRow(start_position=第2行地初始位置, n=2)
菜地3 = MyfarmRow(start_position=第3行地初始位置, n=3)
菜地4 = MyfarmRow(start_position=第4行地初始位置, n=4)
菜地5 = MyfarmRow(start_position=第5行地初始位置, n=5)

菜地1b = (
    *发射器小车,
    *第1行地初始位置b,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
        "remark": "第1行",
    },
    step_sleep(6),
    *下一块地 * 4,
    {"step": "走到下一块地", "type": "key", "input": "D", "delay": 1100},
    step_sleep(1),
    {"step": "微调", "type": "key", "input": "A", "delay": 200, "remark": "这块地微调"},
    step_sleep(3.5),
)
# 菜地1b = MyfarmRow(start_position=第1行地初始位置b, n=1)
菜地2b = MyfarmRow(start_position=第2行地初始位置b, n=2)
菜地3b = MyfarmRow(start_position=第3行地初始位置b, n=3)
菜地4b = MyfarmRow(start_position=第4行地初始位置b, n=4)
菜地5b = MyfarmRow(start_position=第5行地初始位置b, n=5)

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
