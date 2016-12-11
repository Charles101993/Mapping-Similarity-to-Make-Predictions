import urllib2
from bs4 import BeautifulSoup as bsoup
import csv
import pandas
from scrape_funcs import *
import time

critics = pandas.read_csv('critics2.csv')

for index, row in critics.iterrows():

	if index > 400: break
	if index < 376: continue

	print "PAGE 0\n-----------"

	link = row[0] + "?filter=movies&num_items=100&sort_options=critic_score&page=0"
	row_headers = [["Critic","Title","Metascore","Critic Score", "Review Text"]]
	
	headers = {'User-Agent': 'Mozilla/5.0', 'content-type':'text/html'}
	request = urllib2.Request(link, headers=headers)
	response = urllib2.urlopen(request)
	html = response.read()

	with open(str(index)+"-0.csv", 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(row_headers + scrape_critic_page(html))
	
	last_page = bsoup(html, "html.parser").find("li", { "class" : "page last_page" })
	if last_page is None:
		continue
		
	last_page = int(last_page.a.getText().encode("utf-8"))
	# loop through pages
	for page in range(1,last_page):
		print "PAGE "+str(page)+"\n-----------"
		link = row[0] + "?filter=movies&num_items=100&sort_options=critic_score&page=" + str(page)
		
		request = urllib2.Request(link, headers=headers)
		try:
			response = urllib2.urlopen(request)
		except urllib2.HTTPError, e:
			if e.code == 429:
				time.sleep(10)
				response = urllib2.urlopen(request)
				
			
		html = response.read()
		
		file_name = str(index)+"-"+str(page)+".csv"
		with open(file_name, 'wb') as f:
			writer = csv.writer(f)
			writer.writerows(row_headers + scrape_critic_page(html))