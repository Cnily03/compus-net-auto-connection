import sys
from campus_win.cipher import decrypt
from campus_win.logger import Prompter
from campus_win.record import readconf, record, saveconf
from campus_win.restful.net import login


def login_by_record(debug=False):
    info = readconf()
    try:
        if not info == False:
            username, password = decrypt(info)
            login(username, password)
        else:
            username, password = record(save=False)
            if login(username, password) == True:
                saveconf(username, password)
    except KeyboardInterrupt:
        sys.exit()
    except:
        if debug:
            raise
        Prompter.error("未知错误！")


def login_once(debug=False):
    try:
        username, password = record(save=False)
        login(username, password)
    except KeyboardInterrupt:
        sys.exit()
    except:
        if debug:
            raise
        Prompter.warn("未知错误！")
