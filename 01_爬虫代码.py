import requests
from lxml import etree
from openpyxl import Workbook
import time

def get_douban_top250():
    # 基础配置
    base_url = 'https://movie.douban.com/top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
        'Referer': 'https://movie.douban.com/top250',
    }

    # 创建Excel + 设置列表头
    wb = Workbook()
    ws = wb.active
    ws.title = '豆瓣Top250'
    # 🔥 最终表头：排名、电影名、评分、评价人数、导演、年份、国家、类型、主演
    ws.append(['排名', '电影名', '评分', '评价人数', '导演', '年份','国家', '类型', '主演'])

    # 爬取10页
    for page in range(0, 250, 25):
        url = f'{base_url}?start={page}&filter='
        try:
            response = requests.get(url, headers=headers, timeout=10)
            print(f'第{page//25+1}页 请求成功')
            
            if response.status_code == 200:
                html = etree.HTML(response.text)
                items = html.xpath('//div[@class="item"]')
                
                for item in items:
                    # 原有核心字段（数字格式）
                    index = int(item.xpath('.//em/text()')[0])
                    title = item.xpath('.//span[@class="title"][1]/text()')[0]
                    score = float(item.xpath('.//span[@class="rating_num"]/text()')[0])
                    comment_num = int(item.xpath('.//span[4]/text()')[0].strip('()人评价'))

                    # ======================
                    # 提取 导演、年份、国家、类型、主演
                    # ======================
                    info_text = item.xpath('.//div[@class="bd"]/p[1]/text()')[0].strip()
                    director = ""
                    year = ""
                    country = ""  
                    movie_type = ""
                    actor = ""

                    # 1. 提取导演
                    if "导演:" in info_text:
                        director = info_text.split("导演:")[1].split("主演:")[0].strip()
                    # 2. 提取主演
                    if "主演:" in info_text:
                        actor = info_text.split("主演:")[1].strip()

                    # 🔥 核心：拆分 年份、国家、类型（豆瓣固定格式：/ 年份 / 国家 / 类型）
                    detail_part = item.xpath('normalize-space(.//div[@class="bd"]/p[1]/text()[last()])')
                    if detail_part:
                        parts = [p.strip() for p in detail_part.split("/") if p.strip()]
                        # 按位置提取：倒数3=年份，倒数2=国家，倒数1=类型
                        if len(parts) >= 3:
                            year = int(parts[-3]) if parts[-3].isdigit() else parts[-3]
                            country = parts[-2]  
                            movie_type = parts[-1]

                    # 写入Excel
                    ws.append([index, title, score, comment_num, director, year, country, movie_type, actor])

            time.sleep(1)
        except Exception as e:
            print(f'第{page//25+1}页 处理失败：{str(e)}')

    # 保存文件
    wb.save(r"C:\Users\桃花林\Desktop\数据分析\实战项目\豆瓣Top250\豆瓣Top250.xlsx")
    print('✅ 数据爬取完成！包含：排名、片名、评分、人数、导演、年份、国家、类型、主演')

if __name__ == '__main__':
    get_douban_top250()