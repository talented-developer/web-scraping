from urllib.request import urlopen
import re
import time
import urllib
import csv

url = "https://github.com/search?q=%40gmail.com&type=issues&p="
gmails = []
end = True
for page_no in range(1,100):
    end=True
    while end:
        try:
            print(page_no)
            page = urlopen(url+str(page_no))
            time.sleep(3)  # wait for 1 second
            html_bytes =  page.read()
            html = html_bytes.decode("utf-8")
            datas = re.findall("<span class=\"Text__StyledText-sc-17v1xeu-0 cWNlgR search-match\">.*?<em>.*?</span>",html)
            for data in datas:
                gmails.append(re.sub("<.*?>","",data))
            time.sleep(1)  # wait for 1 second
            end=False
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("No more pages")
                break
            elif e.code == 429:
                print("Too many requests")
                time.sleep(0.1)  # wait for 1 minute
                continue
with open('gmails.list', 'w', encoding='utf-8') as f:
    f.write('\n'.join(gmails))
#print(gmails)