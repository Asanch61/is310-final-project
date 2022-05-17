import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

my_url= "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=ps5&_sacat=0"

client= uReq(my_url)
client 

page_html = client.read()
page_html
