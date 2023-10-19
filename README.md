# Aivesa自动签到/askopenai.cn
Aivesa自动多账号自动化签到程序

## 功能
该程序是一个使用Selenium库编写的自动化程序，用于给Aivesa内测版进行签到操作。

![image-20231020014626117](D:\Code\Selenium\Aivesa-----askopenai.cn\assets\image-20231020014626117.png)

## 注意事项
在使用该程序之前，请注意以下事项：
- 确保已安装Python3.6以上版本和Selenium库`pip install selenium`。
- 需要安装Chrome浏览器。Chrome 114以上版本一般无需配置ChromeDriver，如果无法运行请自行下载并配置ChromeDriver路径。
- 根据实际情况修改参数配置部分的内容，包括`AIVESA_URL`、`USERS`、`LOADING_TIMEOUT`等。
- 确保提供的用户名和密码组合正确无误。
- 确保指定的网站能够正常访问。

## 使用方法
1. 克隆或下载该程序到本地。
2. 根据需要修改参数配置部分的内容。
3. 运行`python AutoAivesa.py`。
4. (可选) 增加一个任务计划，触发时间为当用户登录时，并设置推迟1分钟，这样可以实现每次开机自动签到。

## 使用截图

![image-20231020015530153](D:\Code\Selenium\Aivesa-----askopenai.cn\assets\image-20231020015530153.png)

## 联系方式

如果您有任何问题或建议，请随时联系作者：
- 作者：Renard Amano
- 邮箱：AmanoRenard@foxmail.com
