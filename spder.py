from selenium import webdriver
import re
import json
from pymongo import MongoClient
class NationalDaySpider:
    baseUrl = "http://index.sogou.com/index/searchHeat"

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.zfdb = self.client.zfdb
        self.zfdb.authenticate("user", "password")
        self.browser = webdriver.Chrome()

    addresss = [
        "布达拉宫", "稻城亚丁", "故宫", "张家界", "九寨沟", "丽江古城", "雅鲁藏布江大峡谷", "乐山大佛", "万里长城", "宏村", "鼓浪屿", "婺源", "纳木错", "外滩", "三清山",        "三亚",        "乌镇", "凤凰古城", "峨眉山", "青海湖", "黄山", "洱海", "元阳梯田", "长白山天池", "周庄", "桂林", "长江三峡", "呼伦贝尔", "月牙泉", "颐和园", "黄果树瀑布",        "华山",        "阿坝", "壶口瀑布", "龙脊梯田", "维多利亚港", "香格里拉", "泸沽湖", "鸟巢", "可可西里", "秦始皇兵马俑", "西双版纳", "趵突泉", "大连", "中山陵", "大兴安岭", "大雁塔",        "丹霞山", "都江堰", "贺兰山",        "夫子庙", "龙虎山", "恒山", "衡山",        "黄帝陵", "黄龙景区", "晋祠", "井冈山", "喀纳斯", "海口", "楼兰古城",        "景德镇", "庐山", "罗平", "莫高窟", "帕米尔高原", "平遥古城", "普陀山", "千户苗寨", "曲阜三孔", "日月潭", "三峡大坝", "三星堆遗址", "沙坡头",        "神农架",        "瘦西湖", "苏州园林", "泰山", "避暑山庄", "太湖", "滕王阁", "五大连池", "武当山", "西湖", "阳朔西街", "西塘", "西夏王陵", "雁荡山", "殷墟", "玉龙雪山",        "云冈石窟",        "千岛湖", "朱家角", "北戴河", "自贡恐龙博物馆",    ]
    urlList = []
    baseUrl = "http://index.sogou.com/index/searchHeat"

    # 拼接 url
    def get_url(self):
        for index, address in enumerate(self.addresss):
            if index % 5 == 0:
                self.urlList.append(
                    self.baseUrl + "?kwdNamesStr=" + address + "," + self.addresss[index + 1] + "," + self.addresss[
                        index + 2] + "," +
                    self.addresss[index + 3] + "," + self.addresss[
                        index + 4] + "&timePeriodType=MONTH&dataType=SEARCH_ALL&queryType=INPUT")
        return self.urlList

# 获取指数信息
def get_index_data(self):
    try:
        for url in self.get_url():
            print("当前地址为：" + url)
            self.browser.get(url)
            self.browser.implicitly_wait(10)
            ret = re.findall(r'root.SG.data = (.*)}]};', self.browser.page_source)
            totalJson = json.loads(ret[0] + "}]}")
            topPvDataList = totalJson["topPvDataList"]
            infoList = totalJson["infoList"]
            pvList = totalJson["pvList"]
            for index, info in enumerate(infoList):
                for pvDate in pvList[index]:
                    print("index => "+str(index)+"地址 => "+info["kwdName"] + "日期 => " + str(pvDate["date"]) + " => " + str(pvDate["pv"]) + " => " + str(
                        info["avgWapPv"]) + " => " + str(info["kwdSumPv"]["sumPv"]) + " => ")
                    self.zfdb.national_day_index.insert({
                        "address": info["kwdName"],  # 地名
                        "date": pvDate["date"],  # 日期
                        "day_pv": pvDate["pv"],  # 日访问量
                    })
                self.zfdb.national_month_index.insert({
                    "address": info["kwdName"],  # 地名
                    "day_avg_pv": info["avgWapPv"],  # 平均访问量
                    "sum_pv": info["kwdSumPv"]["sumPv"],  # 总访问量
                })
    except :
        print("exception")


national_day_spider = NationalDaySpider()
national_day_spider.get_index_data()