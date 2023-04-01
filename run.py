import os
import requests

ip_url = 'https://raw.githubusercontent.com/QiuSimons/Chnroute/master/dist/chnroute/chnroute.txt'
list_url = 'https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/direct-list.txt'

def getChnroute(ip_url):
    try:
        response = requests.get(ip_url, timeout=5)
    except requests.exceptions.Timeout:
        print("IP Time Out!!!")
    else:
        data = response.text
        lines = data.split('\n')
        new_lines = []

        for line in lines:
            if not line.startswith('17.'):
                new_line = 'IP-CIDR,' + line + ',Direct,no-resolve'
                new_lines.append(new_line)
        del new_lines[-1]
        new_lines.append('\n')

        with open('./head.txt', 'a', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))

def getChnlist(list_url):
    try:
        response = requests.get(list_url, timeout=5)
    except requests.exceptions.Timeout:
        print("List Time Out!!!")
    else:
        data = response.text
        lines = data.split('\n')
        new_lines = []

        for line in lines:
            if not line.startswith('regexp:'):
                if line.startswith('full:'):
                    line = line.strip('full:')
                    new_line = 'DOMAIN-SUFFIX,' + line + ',Direct'
                    new_lines.append(new_line)
                else:
                    new_line = 'DOMAIN-SUFFIX,' + line + ',Direct'
                    new_lines.append(new_line)
        del new_lines[-1]
        new_lines.append('\n')

        with open('./head.txt', 'a', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
def merge():
    with open("./head.txt","a") as head, open("./tail.txt","r") as tail:
        for line in tail:
            head.write(line)
    os.rename('./head.txt', './Rocket.conf')

getChnlist(list_url)
getChnroute(ip_url)
merge()
