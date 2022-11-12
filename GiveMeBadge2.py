import json
import ctypes
import urllib3
import webbrowser
import win32gui, win32con
from time import sleep
from threading import Thread

#Rick Roll
YouTube = "https://youtu.be/dQw4w9WgXcQ"

http = urllib3.PoolManager()
api = 'https://teamkuso.xyz/GiveMeBadge2/msg.json'
r = http.request('GET', api)
l = json.loads(r.data.decode('utf-8'))

# buttons
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000

# icons
ICON_EXCLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10

apititle = l["Title"]
apitext = l["Text"]
apistyle = l["Style"]

def Hide():
    win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_HIDE)

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def Noti():
    sleep(5)
    Mbox(apititle, apitext, apistyle)
    SystemExit

def RickRoll():
    webbrowser.open(YouTube, new=1)

if __name__ == "__main__":
    Thread(target=Hide).start()
    Thread(target=RickRoll).start()
    Thread(target=Noti).start()