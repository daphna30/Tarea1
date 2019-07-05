import re
from mechanize import Browser

br = Browser()
br.open("http://testing-ground.scraping.pro/login")
br.select_form(nr=0)
br["usr"] = "admin"
br["pwd"] = "12345"

print(br.submit())
