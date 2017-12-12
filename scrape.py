from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

all_articles = soup.find_all('article')
for article in all_articles:
	head_line = article.h2.a.text
	summary = article.find('div', class_="entry-content").p.text

	try:
		yt_source = article.find('iframe')["src"].split('/')[4]
		yt_source = yt_source.split('?')[0]
		yt_link = f'https://youtube.com/watch?v={yt_source}'
		print(yt_link)

	except Exception as e:
		yt_link = None



# Scrape Testing Website (./index.html)
# with open('index.html','r') as html_file:
# 	soup = BeautifulSoup(html_file, 'lxml')
# 	headTitle = soup.title.text
# 	footer = soup.find('div', id='footer')
# 	article = soup.find('div', class_='article')
# 	article1 = article.h1.a.text
# 	all_articles = soup.find_all('div', class_="article")
# 	all_summaries = soup.find_all('p', class_="summary")
#
# 	for article in all_articles:
# 		head_line = article.h1.a.text
# 		print(head_line)
#
# 	for summary in all_summaries:
# 		sum_text = summary.text
# 		print(sum_text)
