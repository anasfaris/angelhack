from bs4 import BeautifulSoup, SoupStrainer
import urllib2

# returns the whole article as a single string
def get_article_from_plist(p_list):
	article = ""
	for p in p_list:
		# p = p.encode('utf-8')
		p = p.extract().string
		if p is not None:
			# print type(p)
			p = p.encode('utf-8')
			# print type(p)
			article += p

	# print "article:\n\n"
	print article
	return article

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
		get_number_of_p_in_div(div)

	return div_list

# div has to be bs4.element.tag
def get_number_of_p_in_div(div):
	p_list = div.find_all('p')
	num_of_p = len(p_list)
	# print "num_of_p:"
	# print num_of_p
	return num_of_p

def get_div_highest_p(div_list):
	# print "in func get_div_highest_p"
	# find div with highest number of p's
	max_p_number = 0
	max_div = None
	for div in div_list:
		p_number = get_number_of_p_in_div(div)
		# print "p_number"
		# print p_number
		if p_number > max_p_number:
			max_p_number = p_number
			max_div = div

	# print "max_div:"
	# print max_div
	return max_div

def get_all_p_from_div(div):
	 p_list = div.find_all('p')
	 return p_list

def remove_p_tag(p_tag_element):
	p = p_tag_element.strip('<p>')
	p = p.strip('</p>')
	p = p.strip('/>')

	return p


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
	'http://www.themalaysianinsider.com/opinion/ooi-kok-hin/article/from-spm-straight-to-varsity-degree-a-proposal'
	,'http://www.harakahdaily.net/index.php/headline-english/35863-muktamar-never-fails-to-draw-crowds'
	,'http://www.themalaysianinsider.com/opinion/rash-behari-battacharjee/article/will-we-answer-the-call-to-reinvent-malaysia'
	,'https://blog.growth.supply/how-quitting-my-corporate-job-for-my-startup-dream-f-cked-my-life-up-3b6b3e29b318'
	,'https://medium.com/on-coding/you-can-already-code-you-just-dont-know-it-yet-862044601a5a'
]

# test
for url in test_urls:

	page_soup = get_page(url)
	# get list of all divs in page_soup
	div_list = get_divs(page_soup)
	# get div with highest number of p in it
	div_max_p = get_div_highest_p(div_list)
	# get all p's in div_max	_p
	p_list = get_all_p_from_div(div_max_p)
	article = get_article_from_plist(p_list)
