import webbrowser
import pyautogui
import time
import argparse

# 안전모드 설정하기. 잘못되었을 경우 탈출구
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
parser = argparse.ArgumentParser()
parser.add_argument('--auto',help='auto download argument',type=bool,default=False)
args = parser.parse_args()
auto = args.auto

while(True):
    url = input("ICAMPUS URL : ")
    url_split = url.split('"')

    src_idx = url_split.index(" src=")
    https_idx = src_idx+1
    https = url_split[https_idx]
    https_split = https.split('/')

    result = "https://lcms.skku.edu"
    for i in range(3, len(https_split)):
        result += "/"
        result += https_split[i]
    print()
    print(result)
    print()

    webbrowser.open(result)
    if auto:
        # ctrl + s 해서 다른이름으로 저장하기.
        time.sleep(1)
        pyautogui.hotkey('ctrl','s')
        time.sleep(0.5)
        pyautogui.press('enter')
        


