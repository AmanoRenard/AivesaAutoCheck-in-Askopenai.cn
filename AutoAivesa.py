# Aivesa 自动签到脚本
# 作者: AmanoRenard / AmanoRenard@foxmail.com

# 参数配置(请根据实际情况修改)：
# Aivesa内测版地址（xxx.aivesa.xxx）：
AIVESA_URL = "c01.aivesa.fun"
# 用户列表：[用户名, 密码]
USERS = [
    ["用户名1", "密码"],
    ["用户名2", "密码"],
    ["用户名3", "密码"],
]
# 页面加载超时时间（秒）
LOADING_TIMEOUT = 180
# ChromeDriver 路径(如果无法运行该程序请填写, 示例: "C:\WebDriver\chromedriver.exe")
# 下载地址: http://chromedriver.storage.googleapis.com/index.html
DIRVER_PATH = None

import sys
import time

print("Aivesa 自动签到脚本 \n作者: AmanoRenard / AmanoRenard@foxmail.com \n 脚本已启动，正在初始化……")

if len(USERS) <1:
    print("无效的用户数量!")
    time.sleep(3)
    sys.exit()
for user in USERS:
    if len(user) != 2:
        print("无效的用户名与密码组合, 请检查格式!")
        time.sleep(3)
        sys.exit()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = Options()
options.add_argument("--headless")
if DIRVER_PATH != None:
    service = Service(DIRVER_PATH)
    dirver = webdriver.Chrome(options=options, service=service)
else:
    dirver = webdriver.Chrome(options=options)
dirver.get(f'https://{AIVESA_URL}/#/web/chat')
print("初始化完成, 等待Aivesa加载……")
try:
    login_btn = WebDriverWait(dirver, LOADING_TIMEOUT).until(
        ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[2]/button[2]'))
    )
except:
    dirver.quit()
    sys.exit()
print("Aivesa加载完成!")
dirver.execute_script("arguments[0].click();", login_btn)
# login_btn.click()
finished = 0
for user_account, user_password in USERS:
    time.sleep(1)
    finished += 1
    print("- 进度 [", finished, "/", len(USERS), "]")
    print("正在为", user_account, "签到……")
    account_input = dirver.find_element(By.XPATH, "//input[@placeholder='请输入用户名/手机号']")
    account_input.send_keys(Keys.CONTROL + Keys.BACK_SPACE)
    account_input.send_keys(user_account)
    password_input = dirver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
    password_input.send_keys(Keys.CONTROL + Keys.BACK_SPACE)
    password_input.send_keys(user_password)
    # dirver.find_element(By.XPATH, "//span[contains(text(), '立即登录')]").click()
    dirver.execute_script("arguments[0].click();", dirver.find_element(By.XPATH, "//span[contains(text(), '立即登录')]"))
    try:
        WebDriverWait(dirver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//div[contains(text(),'登录成功')]"))
        )
    except:
        print(user_account + "登录失败!")
        time.sleep(3)
        dirver.quit()
        sys.exit()
    time.sleep(1)
    # dirver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[2]/button[3]").click()
    dirver.execute_script("arguments[0].click();", dirver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[2]/button[3]"))
    try:
        daily_msg = WebDriverWait(dirver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[contains(text(),'签到') and @class='n-message__content']"))
        )
    except:
        print(user_account + "无法签到!")
        time.sleep(3)
        dirver.quit()
        sys.exit()
    print(user_account, "的签到信息:", daily_msg.text)
    time.sleep(0.5)
    # dirver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[2]/button[1]").click()
    dirver.execute_script("arguments[0].click();", dirver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[2]/button[1]"))
    try:
        # WebDriverWait(dirver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//span[text() = '确定']"))
        # ).click()
        dirver.execute_script("arguments[0].click();", WebDriverWait(dirver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//span[text() = '确定']"))
        ))
    except:
        print(user_account, "退出登录失败!")
        time.sleep(3)
        dirver.quit()
        sys.exit()

dirver.quit()
print("\n- 签到已完成！")
time.sleep(5)