import json
from urllib.parse import unquote
import requests


def decode(origin_stok):
    origin_stok = origin_stok.replace('%28', '(')
    origin_stok = origin_stok.replace('%29', ')')
    origin_stok = origin_stok.replace('%21', '!')
    return origin_stok


def get_hostInfo():
    login_url = 'http://192.168.1.1/'
    login_data = {
        "method": "do",
        "login": {
            "password": "RK3V5X4H9TefbwK"
        }
    }
    ds_data = {
        "system": {
            "name": ["sys"]
        },
        "hosts_info": {
            "table": "host_info"
        },
        "network": {
            "name": "iface_mac"
        },
        "function": {
            "name": "new_module_spec"
        },
        "method": "get"
    }
    # 登陆获取stok
    response = requests.post(login_url, json=login_data)
    origin_stok = response.text.split('"stok":')[1][1:-2]
    # 需要一次自定义解码
    stok = decode(origin_stok)
    ds_url = 'http://192.168.1.1/stok=' + stok + '/ds'
    # 请求ds数据
    response_ds = requests.post(ds_url, json=ds_data)
    data = json.loads(response_ds.text)
    hosts_info = data['hosts_info']['host_info']
    return hosts_info


def outputInfo(hosts_info):
    for index, host_info in enumerate(hosts_info):
        host_code = 'host_info_' + str(index)
        # 解码hostname
        host_info[host_code]['hostname'] = unquote(host_info[host_code]['hostname'])
        if host_info[host_code]:
            print()
        print(host_info[host_code])
        # print(i[host_code]['hostname'])
