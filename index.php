<%
import pycps

con = pycps.Connection('tcp://cloud-us-0.clusterpoint.com:9007', 'TruArticle', 'jimmyasyraf@gmail.com', '12345', '100491')

response = con.search(term('TruArticle'), docs=3, offset=1)


// Debug
//$cpsConn->setDebug(true);

%>

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
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
          <form action="index.php" method="post">
                  &nbsp &nbsp &nbsp &nbsp &nbsp  Url : <input type="text" name="articleurl" size="80"> 
          <input type="submit" name="watsonquery" value="Submit">
          </form>
        </div>
      </body>
</html>