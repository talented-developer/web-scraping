import mechanicalsoup
browser=mechanicalsoup.Browser()
url="http://olympus.realpython.org/login"
login_page=browser.get(url)
login_html=login_page.soup

form=login_html.select("form")[0]
login_name="zeus"
login_password="ThunderDude"
login_html.select("input")[0]["value"]=login_name
login_html.select("input")[1]["value"]=login_password
profile_page=browser.submit(form,login_page.url)
profile_html=profile_page.soup
print(profile_html.select("title")[0])
