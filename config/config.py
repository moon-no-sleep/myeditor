import tomli_w
import tomllib


def set_mode(有摇杆=True):
    doc = {"有摇杆": 有摇杆}
    with open("config/conf.toml", "wb") as f:
        tomli_w.dump(doc, f)


def read_mode():
    """读取摇杆摸式

    Returns:
        dict: 摇杆模式
    """
    with open("config/conf.toml", "rb") as f:
        data = tomllib.load(f)
    return data


有摇杆 = read_mode()["有摇杆"]
