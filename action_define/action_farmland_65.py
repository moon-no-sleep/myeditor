from action_define.action_base import *

第1行地初始位置 = MyView(a=(504, 280))
第2行地初始位置 = MyView(a=(491, 288))
第3行地初始位置 = MyView(a=(469, 297))
第4行地初始位置 = MyView(a=(438, 308))
第5行地初始位置 = MyView(a=(405, 320))
第6行地初始位置 = MyView(a=(364, 324))
种菜视角1 = MyView_fine(a=(440, 280), b=(384, 280))
种菜视角2 = MyView_fine(a=(440, 280), b=(386, 280))
种菜视角3 = MyView_fine(a=(440, 280), b=(388, 280))
种菜视角4 = MyView_fine(a=(440, 280), b=(391, 280))
种菜视角5 = MyView_fine(a=(440, 280), b=(393, 280))
种菜视角6 = MyView_fine(a=(440, 280), b=(395, 280))


下一块地 = (
    {
        "step": "走到下一块地",
        "type": "key",
        "input": "A",
        "delay": 1100,
    },
    step_sleep(3),
)


def MyfarmRow(start_position=第2行地初始位置, farm_view=种菜视角1):
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
        # *farm_view,
        *下一块地,
        *下一块地,
        *下一块地,
        *下一块地,
        step_sleep(2),
    )
    return steps


#  -----分割线-----
菜地1 = (
    *发射器小车,
    *第1行地初始位置,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
    },
    step_sleep(6),
    *下一块地,
    *下一块地,
    *下一块地,
    {
        "step": "微调位置",
        "type": "key",
        "input": "W",
        "delay": 300,
    },
    step_sleep(3),
    *下一块地,
    step_sleep(2),
)


# 菜地1 = MyfarmRow(start_position=第1行地初始位置, farm_view=种菜视角1)
菜地2 = MyfarmRow(start_position=第2行地初始位置, farm_view=种菜视角2)
菜地3 = MyfarmRow(start_position=第3行地初始位置, farm_view=种菜视角3)
菜地4 = MyfarmRow(start_position=第4行地初始位置, farm_view=种菜视角4)
菜地5 = MyfarmRow(start_position=第5行地初始位置, farm_view=种菜视角5)
菜地6 = MyfarmRow(start_position=第6行地初始位置, farm_view=种菜视角6)


非月卡菜地 = (
    *菜地1,
    *菜地2,
    *菜地3,
    *菜地4,
    *菜地5,
    *菜地6,
    step_sleep(1),
    复位鼠标,
)