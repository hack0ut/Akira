import os
import platform


def system():
    if platform.system() == "Windows":
        return f"🖥 {platform.uname().node}"
    else:
        return os.uname()[1]
