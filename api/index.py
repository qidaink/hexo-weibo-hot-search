# coding=utf-8
# @Instruction:Python获取微博热搜榜
# @Author    : qidaink
# @Date      : 2022/2/24
# @Attention : 全局变量若想在函数中被修改，需要加上global声明

# =======================所需模块============================
import json                    # 处理 json 文件用
import requests                # 请求网址用
import datetime                # 获取时间
# from bs4 import BeautifulSoup  # 解析网页用
from http.server import BaseHTTPRequestHandler

# =======================全局变量============================
# hot_top_url = "https://s.weibo.com/top/summary/"     # 热搜榜链接
hot_json_url = "https://weibo.com/ajax/side/hotSearch"  # 热搜榜 JSON 文件链接


# ========================函数==============================
def GetJsonData():
    ''' GetJsonData()\n
    @Instruction : 微博热搜榜获取\n
    @para : 无 \n
    @Args : params (dict): {} \n
    @Returns : json: {rank: 顺序, title: 标题, url: 地址, num: 热度数值, hot: 热搜等级}
    '''
    now_time = datetime.datetime.now().strftime("%F %A %H:%M:%S") + "\n"  # 获取当前时间
    data = []
    response = requests.get(hot_json_url)
    data_json = response.json()["data"]["realtime"]
    label = {
        "电影": "影",
        "剧集": "剧",
        "综艺": "综",
        "音乐": "音"
    }
    print(now_time)
    for data_item in data_json:
        hot = ""
        # 如果是广告，则不添加
        if "is_ad" in data_item:
            continue
        if "flag_desc" in data_item:
            hot = label.get(data_item["flag_desc"])
        if "is_boom" in data_item:
            hot = "爆"
        if "is_hot" in data_item:
            hot = "热"
        if "is_fei" in data_item:
            hot = "沸"
        if "is_new" in data_item:
            hot = "新"

        dic = {
            "rank": data_item["rank"] + 1,   # 数值
            "title": data_item["note"],  # 字符串
            "url": "https://s.weibo.com/weibo?q=%23" + data_item["word"] + "%23",  # 字符串
            "num": data_item["num"],     # 数值
            "hot": hot                   # 数值
        }
        data.append(dic)
    return data


# =========================类===============================
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = GetJsonData()
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return


if __name__ == '__main__':
    res = GetJsonData()
    for temp in range(0, len(res), 1):
        print("="*80)
        print("|{0:^{len0}d}|{1:^{len1}s}|{2:<{len2}s}|{3:<{len3}s}|{4:^{len4}d}|".format(
            res[temp]['rank'], res[temp]['hot'], res[temp]['title'], res[temp]['url'], res[temp]['num'],
            len0=2,
            len1=4 - len(res[temp]['hot'].encode("GBK")) + len(res[temp]['hot']),
            len2=45 - len(res[temp]['title'].encode("GBK")) + len(res[temp]['title']),
            len3=80 - len(res[temp]['url'].encode("GBK")) + len(res[temp]['url']),
            len4=7,
            ))
    # print(res)
