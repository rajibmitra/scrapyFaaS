import lxml
from lxml import etree
import urllib2
class webCrawler(object):
	self.urlStack = set() #Set to avoid duplicates in the list
	def __init__(self,baseURL):
		"""The init function(can do database connection setup here)"""
		self.urlStack.add(baseURL)

	def checkURL(self,url):
		"""Check if the url already exists in the database and return True or False"""
	def db_call(self,url,html):
		"""Insert into the db/disk the URL and the html content of the URL"""
	
	def crawl(self,url):
		try:
			html = urllib2.urlopen(url).read()
		except:
			print "Unable to retrieve HTML"
			if len(self.urlStack)>;0:
				self.crawl(self.urlStack.pop())
		href_xpath = "//a/@href"
		self.db_call(url,html)
		tree = lxml.etree.HTML(html)
		hrefs = tree.xpath(href_xpath)
		for each in hrefs:
			if each.find("openfaas.com")<=0 or (self.checkURL(url)):
				hrefs.remove(each)
		for each in hrefs:
			self.urlStack.add(each)
		if len(self.urlStack)>;0:
			self.crawl(self.urlStack.pop())
