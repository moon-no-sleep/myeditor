from action_define.action_base import *

钓鱼3连 = (
    大功能键,
    step_sleep(3),
    大功能键,
    step_sleep(3),
    大功能键,
    step_sleep(3),
    {
        "step": "钓鱼留白",
        "type": "mouse",
        "input": "click",
        "point": (100, 512),  # 点击左侧, 翻页鱼卡
    },
    step_sleep(0.5),
    Q键位置,
    step_sleep(0.5),
)

走到鱼塘边 = (
    *发射器,
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
    },
    step_sleep(2.5),
    {
        "step": "走到鱼塘边",
        "type": "key",
        "input": "W",
        "delay": 1200,
    },
    step_sleep(1),
)
非月卡鱼塘 = (
    *走到鱼塘边,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,    
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,
    *钓鱼3连,  
    *钓鱼3连,
    *钓鱼3连,  
    复位鼠标,
)

