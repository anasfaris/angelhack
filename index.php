<?php 
//this code is tested locally
require_once 'cps_api.php';

// Connect to clusterpoint
$connectionStrings = array(
  'tcp://cloud-us-0.clusterpoint.com:9007',
  'tcp://cloud-us-1.clusterpoint.com:9007',
  'tcp://cloud-us-2.clusterpoint.com:9007',
  'tcp://cloud-us-3.clusterpoint.com:9007'
);

$cpsConn = new CPS_Connection(
  new CPS_LoadBalancer($connectionStrings),
  'TruArticle',
  'jimmyasyraf',
  '12345',
  'document',
  '//document/id',
  array('account' => 100491)
);

$submit = @$_POST['watsonquery'];
if ($submit) {
  exec("python watson.py someparams");
}

// Debug
//$cpsConn->setDebug(true);

?>

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
             <h2 id="introspeech">TruArticle</h2>
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