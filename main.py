# watson
from server import *

#Gevent Server
import sys
if 'threading' in sys.modules:
    del sys.modules['threading']
# from gevent import monkey; monkey.patch_all()

#Bottle Framework
from bottle import *
import bottle
import os

# get article
from imran import get_page, get_article, test_urls, get_title

#specifying the path for the files
@route('/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='.')

@error(404)
def error404(error):
    return 'URL does not exist'



@route('/rate', methods=['POST'])
def main():
	get_url = request.forms.get('articleurl')
	print(request.forms.get('articleurl'))
	page = get_page(get_url)
	# article = get_article(get_url)
	title = get_title(get_url)
	# print(page)
	# print(article)
	print(title)
	return template('index.php')
	
@route('/rate', method="POST")
def rate():
	# print request.forms.post('watsonquery')
	print request.forms.post('watsonquery')
	return template('index.php')

@route('/watson', method="POST")
def watson():
	print request.forms.get('watsonquery')
	# print request.forms.post('watsonquery')
	# print request.query.watsonquery
	# url = raw_input("give url> ")

	# page_soup = get_page(url)
	# div_list = get_divs(page_soup)
	# # get div with highest number of p in it
	# div_max_p = get_div_highest_p(div_list)
	# # get all p's in div_max	_p
	# p_list = get_all_p_from_div(div_max_p)
	# article = get_article_from_plist(p_list)
	# print "article:"
	# print article
	
	url = request.query.articleurl
	return template('url: {{url}}', url=url)

# get articles
# @route('/get_article/<>')


run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
