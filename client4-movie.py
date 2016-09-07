#! /usr/bin/env python
#! encoding = utf-8

import requests
import codecs
from bs4 import  BeautifulSoup

#要爬取的地址
DOWNLOAD_URL='http://movie.douban.com/top250'

#user-agent，模仿浏览器，防止被目标网站反爬
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}

#下载页面
def download_page(url):
#请求页面，获取要爬取的页面内容
	data = requests.get(url,headers=HEADERS).content
	return data


def parse_html(html):
  #使用bs解析(获取的页面)，
  #测试是可以使用print soup.pretiffy()打印查看获得的页面
	soup= BeautifulSoup(html)

  #根据css获得要爬取的页面信息
	movie_list_soup = soup.find('ol',attrs={'class':'grid_view'})

	movie_name_list=[]

    #遍历页面中有关的信息
	for movie_li  in movie_list_soup.find_all('li'):
    #找到电影描述
		detail = movie_li.find('div',attrs={'class':'hd'})
    #电影名字
		movie_name=detail.find('span',attrs={'class':'title'}).getText()
    #添加到list
		movie_name_list.append(movie_name)
  #找到下一页
	next_page = soup.find('span',attrs={'class':'next'}).find('a')

  #拼接下一页的url，继续爬取下一页
	if next_page:
		return movie_name_list,DOWNLOAD_URL+next_page['href']
		
  #返回电影名称的list
	return movie_name_list,None


def main():
	url=DOWNLOAD_URL
  #打开文件，使用utf-8编码
	with codecs.open('movies','wb',encoding='utf-8') as fp:
		while url:
      #获取页面
			html = download_page(url)
      #分析页面获取信息
			movies,url=parse_html(html)
      #将获得的信息写入文件
			fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
			#fp.write(u'{url}\n'.format(url='\n'.join(url)))


if __name__=='__main__':
	main()
	
	
