from concurrent.futures import ThreadPoolExecutor
import weatherSpider
import csv

headers = ['date', 'week', 'high_temp', 'low_temp', 'weather_condition', 'wind_force']
f_csv = open('weather4.csv', 'a', newline='\n', encoding='utf-8')
writer = csv.writer(f_csv)  # 创建一个写入器
writer.writerow(headers)

with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(weatherSpider.dowload,weatherSpider.url_li)
    htmls = zip(weatherSpider.url_li, results)


with ThreadPoolExecutor(max_workers=3) as pool1:
    for url, html in htmls:
        future = pool1.submit(weatherSpider.parse, html)
        print("正在写入：%s的内容" % url)
        writer.writerows(future.result())

    f_csv.close()