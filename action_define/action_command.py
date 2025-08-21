from action_define.action_base import step_sleep


IOS账号登录 = {
    "step": "IOS账号登录",
    "type": "mouse",
    "input": "click",
    "point": (616, 400),
}
安卓账号登录 = {
    "step": "安卓账号登录",
    "type": "mouse",
    "input": "click",
    "point": (823, 400),
}

登录账号 = (
    IOS账号登录,
    step_sleep(1),
    {
        "step": "账号信息授权登录",
        "type": "mouse",
        "input": "click",
        "point": (507, 320),
    },
    step_sleep(1),
    {
        "step": "授权登录",
        "type": "mouse",
        "input": "click",
        "point": (503, 372),
    },
    step_sleep(8),
)
进入游戏 = (
    {
        "step": "点击任意位置开始游戏",
        "type": "mouse",
        "input": "click",
        "point": (510, 390),
    },
    step_sleep(5),
    *[
        {
            "step": "关闭广告",
            "type": "mouse",
            "input": "click",
            "point": (88, 450),
        },
        step_sleep(1),
    ]
    * 10,
    {
        "step": "星宝农场",
        "type": "mouse",
        "input": "click",
        "point": (641, 393),
    },
    step_sleep(10),
)
下载资源包 = (
    {
        "step": "确定",
        "type": "mouse",
        "input": "click",
        "point": (605, 375),
    },
    step_sleep(1),
    {
        "step": "全部继续",
        "type": "mouse",
        "input": "click",
        "point": (882, 518),
    },
    step_sleep(15),
    {
        "step": "星宝农场",
        "type": "mouse",
        "input": "click",
        "point": (641, 393),
    },
    step_sleep(10),
)

# 登录界面
登录游戏账号 = (*登录账号, *进入游戏, *下载资源包)
登录游戏任意 = (*进入游戏, *下载资源包)

# 消费界面
