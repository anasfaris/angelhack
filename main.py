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

@route('/rate')
def main():
	return ''' <!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="static/stylesheets/stylesheet.css">
	<title>TruArticle</title>
  <script src="js/main.js" type="text/javascript" ></script>
	<link rel="icon" type="image/png">
</head>
<body>
      <div id="headerbar">
        <div id="logo">
             <h2 id="introspeech">ReadSmart</h2>
             <h5 id="description">Check if the article is realible or not. Paste the link below!</h5>
      	</div>
      </div>
      <div id="searchbox">
          <form action="/rate" method="POST">
                  &nbsp &nbsp &nbsp &nbsp &nbsp  Url : <input type="text" name="articleurl" size="80"> 
          <input type="submit" name="watsonquery" value="Submit">
          </form>
        </div>
      </body>
</html> '''

@route('/rate', methods=['POST'])
def do_main():
	get_url = request.forms.get('articleurl')
	print(request.forms.get('articleurl'))
	page = get_page(get_url)
	# article = get_article(get_url)
	title = get_title(get_url)
	# print(page)
	# print(article)
	print(title)
	return template('index.php')
	

# get articles
# @route('/get_article/<>')

url = test_urls[0]
# beautiful_page = get_page(url)
print "url:"
print url
print "beautiful page:"
# print beautiful_page

run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
