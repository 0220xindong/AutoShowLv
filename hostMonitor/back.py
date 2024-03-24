from urllib.parse import unquote

from flask import Flask, render_template
from service.tpService import get_hostInfo
app = Flask(__name__)

@app.route('/')
def index():
    hosts_info = get_hostInfo()
    for index, host_info in enumerate(hosts_info):
        host_code = 'host_info_' + str(index)
        # 解码hostname
        host_info[host_code]['hostname'] = unquote(host_info[host_code]['hostname'])
        print(host_info)
    return render_template('index.html', host_info=hosts_info)

if __name__ == '__main__':
    app.run()