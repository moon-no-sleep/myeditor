from action_define.action_base import *


神像仙术 = (
    *神像,
    {
        "step": "激活仙术",
        "type": "key",
        "input": "Q",
        "delay": None,
    },
    step_sleep(0.5),
    {
        "step": "选择时光跳跃",
        "type": "mouse",
        "input": "click",
        "point": (390, 215),
    },
    step_sleep(0.5),
)

仙术植物 = (
    *神像仙术,
    {
        "step": "查看植物",
        "type": "mouse",
        "input": "click",
        "point": (418, 441),
    },
    step_sleep(0.5),
)
仙术动物 = (
    *神像仙术,
    {
        "step": "查看动物",
        "type": "mouse",
        "input": "click",
        "point": (519, 444),
    },
    step_sleep(0.5),
)
仙术鱼塘 = (
    *神像仙术,
    {
        "step": "查看鱼塘",
        "type": "mouse",
        "input": "click",
        "point": (631, 442),
    },
    step_sleep(0.5),
)
仙术加工器 = (
    *神像仙术,
    {
        "step": "查看加工器",
        "type": "mouse",
        "input": "click",
        "point": (734, 438),
    },
    step_sleep(0.5),
)
菜地时间 = 发射器
动物时间 = (
    *发射器,
    *MyView(a=(605, 140)),
)
鱼塘时间 = (*发射器, *MyView(a=(605, 140)))

加工器时间 = (*发射器, *MyView(a=(605, 140)))
