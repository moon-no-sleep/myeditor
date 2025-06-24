from config.config import set_mode

if __name__ == "__main__":
    # 请先设置有摇杆或无摇杆模式
    set_mode(有摇杆=True)

    from action_define.action_base import 有摇杆
    print("有摇杆模式: ", 有摇杆)

    from result.generate_yaml import main_script, custom_script
    # main_script("all")  # 更新所有脚本
    # # main_script("非月卡菜地小于65")  # 单点更新指定脚本

    custom_script() #更新自定义模块脚本

    print("更新完成")
