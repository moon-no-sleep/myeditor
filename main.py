from Model.code_all import g_default_codeList
from config.config import read_mode, set_mode
from config import config
from generator._info import write_info


def main(a=True):
    set_mode(有摇杆=a)
    config.有摇杆 = read_mode()["有摇杆"]
    print("有摇杆模式: ", config.有摇杆)

    from generator.generate_sqlite import main_script

    main_script("all")  # 更新所有脚本
    # main_script("非月卡菜地64")  # 单点更新指定脚本

    print("更新完成")


def code_list():
    g_default_codeList()
    print("更新完成")


if __name__ == "__main__":
    write_info()
    # 请先设置有摇杆或无摇杆模式
    main(True)
    # main(False)
    code_list()

    print("结束")
