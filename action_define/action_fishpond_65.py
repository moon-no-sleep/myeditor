from action_define.action_base import *

钓鱼3连65 = [
    *[
        {
            "step": "钓鱼留白",
            "type": "mouse",
            "input": "click",
            "point": (100, 512),  # 点击左侧, 翻页鱼卡
        },
        step_sleep(0.5),
    ]
    * 4,
    step_sleep(0.5),
]

走到鱼塘边65 = (
    *发射器小车,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
    },
    step_sleep(5),
    {
        "step": "走到鱼塘边",
        "type": "key",
        "input": "W",
        "delay": 2500,
    },
    step_sleep(4),
)

钓鱼后65 = (
    step_sleep(6),
    Q键位置,
    step_sleep(1),
    头像复位,
    step_sleep(1),
    头像复位,
    step_sleep(1),
    左侧复位,
    step_sleep(1),
    复位鼠标,
)
非月卡鱼塘65 = (*走到鱼塘边65, *钓鱼3连65 * 16, *钓鱼后65)
