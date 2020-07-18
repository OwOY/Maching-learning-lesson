import requests
from lxml import etree
import json
import jieba
from jieba.analyse import extract_tags

jieba.set_dictionary('..\VS\practice\dict.txt.big.txt')

requests = requests.Session()

p = requests.get(
    'https://tw.appledaily.com/pf/api/v3/content/fetch/query-feed?query=%7B%22feedOffset%22%3A0%2C%22feedQuery%22%3A%22type%253Astory%2520AND%2520taxonomy.primary_section._id%253A%252F%255C%252Frealtime.*%252F%22%2C%22feedSize%22%3A%22100%22%2C%22sort%22%3A%22display_date%3Adesc%22%7D&d=107&_website=tw-appledaily',
    headers = {
                'Host': 'tw.appledaily.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Accept': '*/*',
                'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'https://tw.appledaily.com/realtime/new/',
                'DNT': '1',
                'Connection': 'keep-alive',
                'If-Modified-Since': 'Fri, 17 Jul 2020 07:58:56 GMT',
                # If-None-Match: W/"1fcab4-djwnsLgIaHFy9lQXgcmJ6Buxe1A"
                'Cache-Control': 'max-age=0'
    }
    )
a = json.loads(p.text)
b = a['content_elements']
for c in b:
    d = c['content_elements']
    print('-----------------------------'+c['headlines']['basic']+'-----------------------------'+'\n')   #新聞標題
    for e in d:
        try:
            Article =  e['content'].replace('<div style="font-size:32px;color:red">即起免費看《蘋果新聞網》　歡迎分享</div><hr><div style="color:blue;font-size:32px">在APP內訂閱　看新聞無廣告　<a href="https://tw.adai.ly/e/W24W5UV825" target="_blank">按此了解更多</a></div><hr>','').replace('<br />','').replace('&nbsp;','').replace('<wbr>','').replace('<br>','').replace('</strong>','').replace('<strong>','').replace('</span>','').replace('<span style="color:','')
        except:
            continue
        if '／' in Article :
            for ARTICLE in Article.split('／')[:-1]:
                print(ARTICLE+'）')
                print(extract_tags(ARTICLE))
        else:
            print(Article)
            print(extract_tags(Article))