<!DOCTYPE html>
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
          <form action="/rate" method="post">
                  &nbsp &nbsp &nbsp &nbsp &nbsp  Url : <input type="text" name="articleurl" size="80"> 
          <input type="submit" name="watsonquery" value="Submit">
          </form>
        </div>
      </body>
</html>