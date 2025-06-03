def step_sleep(t):
    # 延迟
    return {
        "step": "延迟",
        "type": "sleep",
        "time": t,
    }


激活界面 = {
    "step": "点击",
    "type": "mouse",
    "input": "click",
    "point": (960, 512),
}


复位鼠标 = {
    "step": "复位",
    "type": "mouse",
    "input": "click",
    "point": (960, 512),
}
头像复位 = {
    "step": "头像复位",
    "type": "mouse",
    "input": "click",
    "point": (40, 50),
}

左侧复位 = {
    "step": "左侧复位",
    "type": "mouse",
    "input": "click",
    "point": (100, 470),
}

# (883, 452) 中心点有鼠标形状挡住, 稍微偏一点
大功能键 = {
    "step": "大功能键",
    "type": "mouse",
    "input": "click",
    "point": (850, 449), 
}


E键位置 = {
    "step": "E键位置",
    "type": "mouse",
    "input": "click",
    "point": (867, 318),  
}

Q键位置 = {
    "step": "Q键位置",
    "type": "key",
    "input": "Q",
    "delay": None,
}

跳跃键 = {
    "step": "跳跃键",
    "type": "mouse",
    "input": "click",
    "point": (742, 446),  
}

A键按下 = {
    "step": "移动到无人机旁",
    "type": "down",
    "input": "A",
    "delay": None,
}
A键松开 = {
    "step": "移动到无人机旁",
    "type": "up",
    "input": "A",
    "delay": None,
}
D键按下 = {
    "step": "移动到无人机旁",
    "type": "down",
    "input": "D",
    "delay": None,
}
D键松开 = {
    "step": "移动到无人机旁",
    "type": "up",
    "input": "D",
    "delay": None,
}

弹窗取消 = {
    "step": "弹窗取消",
    "type": "mouse",
    "input": "click",
    "point": (405, 355),
}

确认解锁 = {
    "step": "确认解锁",
    "type": "mouse",
    "input": "click",
    "point": (605, 360),
}

发射器 = (
    激活界面,
    step_sleep(1),
    复位鼠标,
    step_sleep(1),
    弹窗取消,
    step_sleep(0.5),
    {
        "step": "去发射器处",
        "type": "key",
        "input": "D",
        "delay": 900,
    },
    step_sleep(0.5),
    {
        "step": "微调位置",
        "type": "key",
        "input": "W",
        "delay": 200,
    },
    step_sleep(0.5),
    {
        "step": "激活发射器",
        "type": "key",
        "input": "Q",
        "delay": None,
    },
    step_sleep(1),
)

发射器小车 = (
    激活界面,
    step_sleep(1),
    复位鼠标,
    step_sleep(0.5),
    弹窗取消,
    step_sleep(0.5),
    {
        "step": "去发射器处",
        "type": "key",
        "input": "D",
        "delay": 900,
    },
    step_sleep(0.5),
    {
        "step": "微调位置",
        "type": "key",
        "input": "W",
        "delay": 200,
    },
    step_sleep(0.5),
    E键位置,
    step_sleep(0.5),
)

神像 = (
    激活界面,
    step_sleep(1),
    复位鼠标,
    step_sleep(1),
    {
        "step": "去神像处",
        "type": "key",
        "input": "S",
        "delay": 2000,
    },
    step_sleep(0.5),
)

def MyView_fine(a=(380, 230), b=(383, 280)):
    # 拉视角1
    return (
        {
            "step": "拉动视角1",
            "type": "mouse",
            "input": "move",
            "point": (504, 280),
        },
        step_sleep(0.5),
        {
            "step": "拉动视角2",
            "type": "mouse",
            "input": "down",
            "point": None,
        },
        step_sleep(0.5),
        {
            "step": "拉动视角3-1",
            "type": "mouse",
            "input": "move",
            "point": (a[0], a[1]),
        },
        step_sleep(0.5),
        {
            "step": "拉动视角3-2",
            "type": "mouse",
            "input": "move",
            "point": (b[0], b[1]),
        },
        step_sleep(0.5),
        {
            "step": "拉动视角4",
            "type": "mouse",
            "input": "up",
            "point": None,
        },
        step_sleep(0.5),
    )


def MyView(a=(491, 288)):
    # 拉视角2
    return (
        {
            "step": "拉动视角1",
            "type": "mouse",
            "input": "move",
            "point": (504, 280),
        },
        step_sleep(0.5),
        {
            "step": "拉动视角2",
            "type": "mouse",
            "input": "down",
            "point": None,
        },
        step_sleep(0.5),
        {
            "step": "拉动视角3",
            "type": "mouse",
            "input": "move",
            "point": (a[0], a[1]),
        },
        step_sleep(0.5),
        {
            "step": "拉动视角4",
            "type": "mouse",
            "input": "up",
            "point": None,
        },
        step_sleep(0.5),
    )
