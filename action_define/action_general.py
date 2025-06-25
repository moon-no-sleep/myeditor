from action_define.action_base import *


无人机v2 = (
    激活界面,
    step_sleep(1),
    复位鼠标,
    step_sleep(0.5),
    弹窗取消,
    step_sleep(0.5),
    A键按下,
    跳跃键,
    step_sleep(1.5),
    A键松开,
    step_sleep(0.5),
    {
        "step": "执行无人机",
        "type": "key",
        "input": "Q",
        "delay": None,
    },
    step_sleep(1),
)


开鱼塘 = (
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
        "delay": 1900,
    },
    step_sleep(1),
    点击普通鱼塘解锁,
    step_sleep(1),
    确认解锁,
    点击金彩鱼塘解锁,
    step_sleep(1),
    确认解锁,
    step_sleep(1),
)

收鱼缸 = (
    *发射器,
    *MyView(a=(459, 212)),
    大功能键,
    step_sleep(3.5),
    {
        "step": "收取金币",
        "type": "mouse",
        "input": "click",
        "point": (868, 313),
    },
    step_sleep(3),
    复位鼠标,
    step_sleep(1),
    复位鼠标,
    step_sleep(1),
)

温泉 = (
    *发射器,
    *MyView(a=(605, 140)),
    {
        "step": "发射",
        "type": "mouse",
        "input": "click",
        "point": (880, 450),
    },
    大功能键,
    step_sleep(4),
    {
        "step": "往回走",
        "type": "key",
        "input": "S",
        "delay": 400,
    },
    step_sleep(1),
)
泡温泉 = (*温泉, 大功能键, step_sleep(17), 复位鼠标, step_sleep(1))

喝咖啡 = (
    *温泉,
    大功能键,
    step_sleep(0.5),
    Q键位置,
    step_sleep(1),
    {
        "step": "咖啡确认",
        "type": "mouse",
        "input": "click",
        "point": (602, 362),
    },
    step_sleep(17),
    复位鼠标,
    step_sleep(1),
)


神像许愿 = (
    *神像,
    {
        "step": "点击祈福",
        "type": "key",
        "input": "E",
        "delay": None,
    },
    step_sleep(0.5),
)
许愿确认 = (
    {
        "step": "许愿确认",
        "type": "mouse",
        "input": "click",
        "point": (788, 498),
    },
    step_sleep(1),
)
许愿经验 = (
    *神像许愿,
    {
        "step": "选择金币",
        "type": "mouse",
        "input": "click",
        "point": (867, 315),  # E键位置
    },
    step_sleep(1),
    *许愿确认,
    左侧复位,
    左侧复位,
    复位鼠标,
)
许愿金币 = (
    *神像许愿,
    {
        "step": "选择金币",
        "type": "mouse",
        "input": "click",
        "point": (715, 336),
    },
    step_sleep(1),
    *许愿确认,
    step_sleep(2),
    左侧复位,
    step_sleep(2),
    左侧复位,
    step_sleep(2),
    复位鼠标,
)

小狗坐标 = (
    *MyView(a=(569, 275)),
    大功能键,
    step_sleep(4),
)
投喂小狗 = (
    *发射器,
    *小狗坐标,
    大功能键,
    step_sleep(3.5),
    复位鼠标,
    step_sleep(1),
    左侧复位,
    step_sleep(1),
)
摸小狗 = (
    *发射器,
    *小狗坐标,
    E键位置,
    step_sleep(1),
    {
        "step": "离开狗窝",
        "type": "key",
        "input": "S",
        "delay": 1000,
    },
    step_sleep(9),
    {
        "step": "Q按键",
        "type": "key",
        "input": "Q",
        "delay": None,
    },
    step_sleep(0.5),
    {
        "step": "摸小狗",
        "type": "mouse",
        "input": "click",
        "point": (810, 233),  # E键位置
    },
    step_sleep(6),
    头像复位,
    step_sleep(1),
    头像复位,
    step_sleep(1),
    左侧复位,
    step_sleep(0.5),
    复位鼠标,
    step_sleep(1),
    左侧复位,
    step_sleep(1),
)
