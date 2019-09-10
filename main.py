# -*- coding: utf-8 -*-
import urllib.request
import json

# 天気クラス
class Weather:
    def __init__(self, data):
        # 日付
        self.date = data["date"]

        # テロップ
        self.telop = data["telop"]

        # 最高気温
        if data["temperature"]["max"] is not None:
            self.temperature_max = "{0}℃".format(data["temperature"]["max"]["celsius"])
        else:
            self.temperature_max = "--"

        # 最低気温
        if data["temperature"]["min"] is not None:
            self.temperature_min = "{0}℃".format(data["temperature"]["min"]["celsius"])
        else:
            self.temperature_min = "--"

    def print(self):
        print(self.date)
        print("  " + self.telop)
        print("  最低気温：{0}".format(self.temperature_min))
        print("  最高気温：{0}".format(self.temperature_max))

# Weather Hacks URL
URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city={0}"

# 町コード：横浜市
ID = 140010

# リクエスト実行
req = urllib.request.Request(URL.format(ID))
with urllib.request.urlopen(req) as res:
    # レスポンス結果
    data = json.load(res)
    print(data["title"])

    # 天気結果の取得
    weathers = []
    for forecast in data["forecasts"]:
        weathers.append(Weather(forecast))

    # 天気結果の出力
    for item in weathers:
        item.print()
