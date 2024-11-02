import time
import mechanicalsoup
browser=mechanicalsoup.Browser()

for i in range(4):
    url="http://olympus.realpython.org/dice"
    page=browser.get(url)
    tag=page.soup.select("#result")[0]
    print(tag.text)
    time.sleep(10)