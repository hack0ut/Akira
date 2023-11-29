import os


def shutdown_system():
    os.system("shutdown /s /t 1")
    return "Успешно!"


def hibernate_system():
    os.system("rundll32.exe powrprof.dll,SetSuspendState Hibernate")
    return "Успешно!"


def block_system():
    os.system("Rundll32.exe user32.dll,LockWorkStation")
    return "Успешно!"
