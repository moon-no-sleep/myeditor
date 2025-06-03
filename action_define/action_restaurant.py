from action_define.action_base import *

餐厅初始位置 = MyView(a=(204, 248))
# 餐厅拉视角1 = MyView(a=(265, 284))

进入餐厅 = (
    *发射器,
    *餐厅初始位置,
    大功能键,
    step_sleep(3.5),
    # *餐厅拉视角1,
    {
        "step": "进入餐厅",
        "type": "key",
        "input": "A",
        "delay": 1000,
    },
    大功能键,
    step_sleep(10),
)

招待顾客 = (
    复位鼠标,
    复位鼠标,
    {
        "step": "往南走",
        "type": "key",
        "input": "S",
        "delay": 200,
    },
    step_sleep(1.5),
    {
        "step": "往西走",
        "type": "key",
        "input": "A",
        "delay": 300,
    },
    step_sleep(1),
    Q键位置,
    step_sleep(1),
    Q键位置,
    step_sleep(4),
    Q键位置,
    step_sleep(1),
    Q键位置,
    step_sleep(4),
    Q键位置,
    step_sleep(1),
    Q键位置,
    step_sleep(4),
    Q键位置,
    step_sleep(1),
    Q键位置,
    step_sleep(3),
)
预约顾客 = (
    大功能键,
    step_sleep(1),
    {
        "step": "接收预约",
        "type": "mouse",
        "input": "click",
        "point": (920, 214),
    },
    step_sleep(1),
    左侧复位,
    step_sleep(1),
)

拉视角 = (
    *MyView(a=(627, 268)),
    *MyView(a=(627, 268)),
)
补充食材 = (
    复位鼠标,
    {
        "step": "往北走",
        "type": "down",
        "input": "W",
        "delay": None,
    },
    step_sleep(1),
    跳跃键,
    step_sleep(1),
    跳跃键,
    step_sleep(1),
    跳跃键,
    step_sleep(1),
    跳跃键,
    step_sleep(1),
    跳跃键,
    step_sleep(1),
    跳跃键,
    step_sleep(1),
    {
        "step": "松开按键",
        "type": "up",
        "input": "W",
        "delay": None,
    },
    step_sleep(1),
    *拉视角,
    step_sleep(1),
    {
        "step": "往前走",
        "type": "key",
        "input": "W",
        "delay": 3000,
    },
    step_sleep(3),
    大功能键,
    step_sleep(1),
    {
        "step": "补充原料",
        "type": "mouse",
        "input": "click",
        "point": (800, 522),
    },
    step_sleep(1),
    确认解锁,
    step_sleep(1),
    左侧复位,
    step_sleep(2),
)
离开餐厅 = (
    复位鼠标,
    step_sleep(1),
    {
        "step": "往南走",
        "type": "key",
        "input": "S",
        "delay": 1200,
    },
    step_sleep(10),
    复位鼠标,
)
非月卡餐厅 = (*进入餐厅, *补充食材, *招待顾客, *预约顾客, *离开餐厅)

