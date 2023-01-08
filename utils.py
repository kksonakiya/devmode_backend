from apps.devmode_backend.filepath import SearchFile
from apps.devmode_backend.telegram_utils import telegram_bot

import json, traceback, os
from requests import Response

def developer_status(request):
    path_info = request.url.split("//")
    try:
        localhost = path_info[1].split(":")[0]
        return True if localhost == "127.0.0.1" else False
    except IndexError:
        return False


def read_devinfo(find):
    devinfo = SearchFile("devinfo.json").completePath()
    with open(devinfo, "r") as file:
        devinfo_data = json.load(file)
    return devinfo_data.get(f"{find}")


def error_reporter(func):
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            return val
        except Exception:
            traceback_msg = f"""Project Name : {read_devinfo('project')}
            {traceback.format_exc()}"""
            telegram_bot.msgTelegram(traceback_msg)
            if read_devinfo("base") == "flask":
                return Response(
                        """ Application has encountered an error. Please contact the admin.
                     Back to Homepage
    <a href="/">Home</a>
                    """
                    )
                
            else:
                return "Error: Please contact the admin."

    return wrapper
