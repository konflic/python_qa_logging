import os


def __get_path_to(driver_name):
    return os.path.expanduser("~") + os.sep + "Downloads" + os.sep + "drivers" + os.sep + driver_name


def chromedriver():
    return __get_path_to("chromedriver")


def geckodriver():
    return __get_path_to("geckodriver")
