import eel
import requests

@eel.expose
def post(url,data):
    """
    Args:
        url (Str):URL
        data (Object):送信するデータ
    """
    #httpリクエスト
    res = requests.post(url,data)
    print(res.status_code)
    print(res.text)
    callable(res.text)
    eel.showRes(res.text)

def gui():
    eel.init("gui")
    eel.start("main.html",size=(400,400),port=8080)
gui()