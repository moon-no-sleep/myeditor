from action_define.action_base import *

餐厅初始位置 = MyView(a=(204, 248))
# 餐厅拉视角1 = MyView(a=(265, 284))

# 发射器进入餐厅
进入餐厅 = (
    *发射器,
    *餐厅初始位置,
    大功能键,
    step_sleep(3.5),
    # *餐厅拉视角1,
    {
        "step": "进入餐厅",
        "type": "key",
        "input": "W",
        "delay": 1000,
    },
    step_sleep(0.5),
    大功能键,
    step_sleep(0.5),
    {
        "step": "门口位置",
        "type": "key",
        "input": "D",
        "delay": 200,
    },
    step_sleep(0.5),
    大功能键,
    step_sleep(0.5),
    {
        "step": "进入餐厅",
        "type": "key",
        "input": "W",
        "delay": 300,
    },
    step_sleep(1),
    大功能键,
    step_sleep(12),
)

# 步行去餐厅门口, 鼠标模拟按键
去餐厅门口v2 = (
    激活界面,
    step_sleep(1),
    复位鼠标,
    step_sleep(1),
    弹窗取消,
    step_sleep(0.5),
    *mouse_WASD(90),
    step_sleep(1),
    鼠标左键松开,
    *mouse_WASD(165),
    step_sleep(5),
    鼠标左键松开,
    step_sleep(1),
    {
        "step": "往前走",
        "type": "key",
        "input": "A",
        "delay": 600,
    },
    step_sleep(1),
)
# 步行进餐厅
进入餐厅v2 = (
    *去餐厅门口v2,
    大功能键,
    step_sleep(0.5),
    {
        "step": "进入餐厅",
        "type": "key",
        "input": "A",
        "delay": 600,
    },
    大功能键,
    step_sleep(12),
)

# 步行去餐厅门口, WASD方式
去餐厅门口v3 = (
    激活界面,
    step_sleep(1),
    复位鼠标,
    step_sleep(1),
    弹窗取消,
    step_sleep(0.5),
    {
        "step": "往前走",
        "type": "key",
        "input": "W",
        "delay": 1100,
    },
    step_sleep(1),
    {
        "step": "往前走",
        "type": "key",
        "input": "A",
        "delay": 2500,
    },
    step_sleep(1),
    {
        "step": "往前走",
        "type": "key",
        "input": "W",
        "delay": 1500,
    },
    step_sleep(1),
    {
        "step": "往前走",
        "type": "key",
        "input": "A",
        "delay": 2500,
    },
    step_sleep(1),
    {
        "step": "往前走",
        "type": "key",
        "input": "W",
        "delay": 200,
    },
)

# 步行进餐厅
进入餐厅v3 = (
    *去餐厅门口v3,
    大功能键,
    step_sleep(0.5),
    {
        "step": "进入餐厅",
        "type": "key",
        "input": "A",
        "delay": 1000,
    },
    大功能键,
    step_sleep(12),
)

招待顾客 = (
    左侧复位,
    step_sleep(0.5),
    复位鼠标,
    step_sleep(0.5),
    复位鼠标,
    step_sleep(1),
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
    *(
        [
            Q键位置,
            step_sleep(0.5),
            Q键位置,
            step_sleep(0.5),
            Q键位置,
            step_sleep(3),
        ]
        * 8  # 重复8pcs
    ),
    step_sleep(1),
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
    左侧复位,
    step_sleep(0.5),
    复位鼠标,
    step_sleep(1),
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
        "delay": 1500,
    },
    大功能键,
    step_sleep(12),
    {
        "step": "往南走",
        "type": "key",
        "input": "D",
        "delay": 800,
    },
    step_sleep(1),
    头像复位,
    step_sleep(1),
    头像复位,
    step_sleep(1),
    左侧复位,
    step_sleep(1),
    复位鼠标,
)
非月卡餐厅_发射器 = (*进入餐厅, *补充食材, *招待顾客, *预约顾客, *离开餐厅)
非月卡餐厅 = (*进入餐厅v2, *补充食材, *招待顾客, *预约顾客, *离开餐厅)
非月卡餐厅_notWASD = (*进入餐厅v3, *补充食材, *招待顾客, *预约顾客, *离开餐厅)
