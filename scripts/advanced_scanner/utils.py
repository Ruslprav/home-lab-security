import os
import platform

def get_system_info():
    """Сбор базовой информации об ОС."""
    return {
        "os": platform.system(),
        "release": platform.release(),
        "user": os.getlogin()
    }
