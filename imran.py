from bs4 import BeautifulSoup, SoupStrainer
import urllib2

# returns page as a soup type
def get_page(article_url):

	# is url correct?

	# get page as html
	page = urllib2.urlopen(article_url).read()
	# get only div
	div_only = SoupStrainer('div')
	# get page as soup
	page_soup = BeautifulSoup(page)
	# encode to utf-8 to avoid charmap error
	# page_soup = page_soup
	# print type(page_soup)
	# print type(page_soup.prettify())

	# test 
	# print "page_soup div_only:"
	# print page_soup
	# print "page_soup.prettify():"
	# print page_soup.prettify()

	# for div in page_soup:
	# 	print "page_soup div:"
	# 	print div

	# print "soup.stripped_strings:"
	# stripped_strings = page_soup.stripped_strings
	# print stripped_strings
	# for i in stripped_strings:
	# 	print "i"
	# 	print i
		# print 'stripped_strings[i]'
		# print stripped_strings[i]

	return page_soup

def get_article(article_url):

	article = ""

	# get page as soup
	page_soup = get_page(article_url)

	# look for element with longest string

	return article

def get_title(article_url):
	page_html = urllib2.urlopen(article_url)
	page_soup= BeautifulSoup(page_html)
	# page_soup = get_page(article_url)
	print "in get_title"
	title_tag = page_soup.title

	title = "not available"
	if title_tag != None:
		print "title_tag works"
		title = page_soup.title.string
		print title
		return title
	# get title with differenet algo
	return title

# helper functions for get_article
# def get_all_string(page_soup):

def get_divs(page_soup):

	div_list = page_soup.find_all('div')

	# test
	for div in div_list:
		print "div"
		print div
		print "type(div)"
		print type(div)
		get_number_of_p_in_div(div)

	return div_list

# div has to be bs4.element.tag
def get_number_of_p_in_div(div):
	p_list = div.find_all('p')
	num_of_p = len(p_list)
	print "num_of_p:"
	print num_of_p
	return num_of_p

def get_div_highest_p(div_list):
	print "in func get_div_highest_p"
	# find div with highest number of p's
	max_p_number = 0
	max_div = None
	for div in div_list:
		p_number = get_number_of_p_in_div(div)
		print "p_number"
		print p_number
		if p_number > max_p_number:
			max_p_number = p_number
			max_div = div

	print "max_div:"
	print max_div
	return max_div

# find article by p
def get_article_p(article_url):
	page_html = urllib2.urlopen(article_url).read()
	page_soup= BeautifulSoup(page_html)

	p_list = page_soup.find_all('p')
	for p in p_list:
		print 'p:'
		print p
		print type(p)

test_urls = [
	# 'http://www.themalaysianinsider.com/opinion/ooi-kok-hin/article/from-spm-straight-to-varsity-degree-a-proposal'
	'http://www.harakahdaily.net/index.php/headline-english/35863-muktamar-never-fails-to-draw-crowds'
	,'http://www.themalaysianinsider.com/opinion/rash-behari-battacharjee/article/will-we-answer-the-call-to-reinvent-malaysia'
	,'https://blog.growth.supply/how-quitting-my-corporate-job-for-my-startup-dream-f-cked-my-life-up-3b6b3e29b318'
	,'https://medium.com/on-coding/you-can-already-code-you-just-dont-know-it-yet-862044601a5a'
]

# test
# for url in test_urls:
# 	print "url:"
# 	print url
# 	page_soup = get_page(url)
# 	print "page_soup.prettify()"
# 	# encode to utf-8 to avoid charmap error
# 	print page_soup.encode('utf-8').prettify()
# 	print "\n"
	# get_title(url)
# get_article_p(test_urls[1])
page_soup = get_page(test_urls[1])
div_list = get_divs(page_soup)
get_div_highest_p(div_list)
# article_url = test_urls[1]
# get_div_highest_p(article_url)
# url = test_urls[0]
# page_soup = get_page(url)
# get_title(url)