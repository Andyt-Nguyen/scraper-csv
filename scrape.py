from bs4 import BeautifulSoup
import requests

with open('index.html','r') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')
	headTitle = soup.title.text
	footer = soup.find('div', id='footer')
	article = soup.find('div', class_='article')
	article1 = article.h1.a.text
	all_articles = soup.find_all('div', class_="article")
	all_summaries = soup.find_all('p', class_="summary")

	# for article in all_articles:
	# 	head_line = article.h1.a.text
	# 	print(head_line)

	# for summary in all_summaries:
	# 	sum_text = summary.text
	# 	print(sum_text)
