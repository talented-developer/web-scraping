from urllib.request import urlopen
import re
url = "https://github.com/search?q=%40gmail.com&type=issues&p=2"
page = urlopen(url)
html_bytes =  page.read()
html = html_bytes.decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)

