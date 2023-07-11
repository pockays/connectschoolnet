import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 获取所有正在运行的进程列表
processes = psutil.process_iter()

# 遍历进程列表
for process in processes:
    try:
        # 判断进程的名称是否包含浏览器关键词（如chrome、firefox等）
        if 'chrome' in process.name().lower():
            # 获取浏览器进程的PID
            pid = process.pid

            # 使用selenium控制浏览器
            options = Options()
            options.add_experimental_option("debuggerAddress", f"localhost:{pid}")
            driver = webdriver.Chrome(options=options)
            url = driver.current_url
            # 连接到正在运行的浏览器进程
            print(url)
            # 关闭浏览器
            driver.quit()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

