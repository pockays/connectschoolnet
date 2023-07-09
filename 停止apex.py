import win32con
from selenium.common import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import subprocess
import win32gui
import time
# import psutil


# 连接网络
connect_cmd = f'netsh wlan connect name="wifi_ltu"'
subprocess.run(connect_cmd, capture_output=True, text=True)

# def get_chrome_urls():
#     urls = []
#     for process in psutil.process_iter(['pid', 'name']):
#         if process.info['name'] == 'chrome.exe':
#             for conn in process.connections(kind='inet'):
#                 if conn.laddr.port > 0:
#                     urls.append(conn.laddr.ip + ':' + str(conn.laddr.port))
#     return urls


# # chrome_urls = get_chrome_urls()
# print("已打开的 Chrome 浏览器实例的 URL:", chrome_urls)

hwnd = 0
title = "辽宁工程技术大学"


def enum_windows_callback(handle, _):
    global hwnd
    window_title = win32gui.GetWindowText(handle)
    if title in window_title:
        print("找到窗口:", title)
        hwnd = handle


timeout = 10  # 设置超时时间为10秒
start_time = time.time()  # 记录开始时间
while hwnd == 0:
    time.sleep(1)
    win32gui.EnumWindows(enum_windows_callback, None)
    elapsed_time = time.time() - start_time
    if elapsed_time > timeout:
        print("已登录或超时")
        break

# 找到认证网页
if hwnd != 0:
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    #     edit_hwnd = win32gui.FindWindowEx(hwnd, None, 'Chrome_RenderWidgetHostHWND', None)
    #     url = win32gui.GetWindowText(edit_hwnd)
    #     print(url)
    options = Options()
    options.add_argument(
        "--headless")
    driver = webdriver.Chrome(options=options)
    driver.get('http://10.11.22.1/index_4.html')
    # 登录
    try:
        username = driver.find_element(By.ID, 'username')
        username.send_keys('2120010108@hcmcc')
        password = driver.find_element(By.ID, 'password')
        password.send_keys('113611')
        login = driver.find_element(By.ID, 'login')
        login.click()
    except ElementNotInteractableException:
        print("已登录")
    finally:
        driver.quit()
input("输入任意键结束")
