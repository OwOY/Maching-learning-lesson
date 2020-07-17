'''
運用jieba結合extract_tags與lcut，判斷巴哈前30頁Key_word
'''
import requests
from lxml import etree
import jieba
from jieba.analyse import set_stop_words
from jieba.analyse import extract_tags
from jieba.analyse import set_stop_words
requests = requests.Session()

Total = []
count = {}
for i in range(1,30):
    p = requests.get(
        'https://forum.gamer.com.tw/B.php?page={0}&bsn=60076'.format(i),
        headers = {
                'Host': 'forum.gamer.com.tw',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0'
        }
    )
    HTML = etree.HTML(p.text)
    Title = HTML.xpath('//p[@class="b-list__main__title"]//text()')
    for T in Title:
        try:
            Total.append(T.split('】')[1])
        except:
            Total.append(T)
Article = ('').join(Total)
jieba.set_dictionary('..\VS\practice\dict.txt.big.txt')
jieba.analyse.set_stop_words('..\VS\practice\stop_word.txt')
Article_cut = jieba.lcut(Article)
Tags = extract_tags(Article, topK=30, withWeight=True)
Tags_list = []
for T in Tags:
    print(T)
    Tags_list.append(T[0])
for word in Article_cut:
    if len(word) <= 1:
        continue
    else:
        count[word] = count.get(word, 0)+1
item = list(count.items())
item.sort(key=lambda x:x[1], reverse=True)
for i in range(30):
    word, count = item[i]
    if word in Tags_list:
        print(word, count)