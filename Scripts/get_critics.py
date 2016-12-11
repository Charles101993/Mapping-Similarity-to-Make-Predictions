import urllib2
from bs4 import BeautifulSoup as bsoup
import csv
import pandas
from scrape_funcs import *
import time


link = "http://www.metacritic.com/browse/movies/critic/popular?page="
rows = [["critic links"]]

headers = {'User-Agent': 'Mozilla/5.0', 'content-type':'text/html'}

for page in range (0,33):
	print "\nPAGE "+str(page)
	
	link2 = link + str(page)
	
	request = urllib2.Request(link2, headers=headers)
	response = urllib2.urlopen(request)
	html = response.read()
	
	soup = bsoup(html, "html.parser").find("div", { "class" : "browse_list_wrapper one" })
	critics = soup.findAll("div", { "class" : "title" })
	
	for critic in critics:
		rows.append([critic.a["href"]])
	time.sleep(10) 

with open("critics2.csv", 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(rows)