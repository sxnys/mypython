'''
自动播放网易云音乐（win10版）
'''

import pyautogui
import pyperclip

# 启用win10搜索打开网易云音乐
# PyAutoGUI中文输入需要用粘贴实现
pyautogui.hotkey('win', 'q')
pyperclip.copy('网易云音乐')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# 移动鼠标到搜索按钮位置
wy = pyautogui.getWindow('网易云音乐')
tl_x, tl_y, *_ = wy.get_position()
search_pos = tl_x + 30, tl_y + 100
pyautogui.PAUSE = 1
pyautogui.moveTo(search_pos)
pyautogui.PAUSE = 0.2
pyautogui.click()

# 移动鼠标到搜索框位置
pyautogui.moveTo(tl_x + 400, tl_y + 60)
pyautogui.click()

# 输入想听的歌进行搜索
song = '浪人琵琶'
pyperclip.copy(song)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# 移动鼠标到 "专辑" 按钮位置（因为单曲里面位置不好确定，不固定）
pyautogui.moveTo(tl_x + 350, tl_y + 120)
pyautogui.click()
pyautogui.moveTo(tl_x + 350, tl_y + 170)
pyautogui.click()
pyautogui.moveTo(tl_x + 350, tl_y + 380)
pyautogui.click(clicks=2)