<?php




if (isset(POST='send')) {
	
// the message
$msg = "First line of text\nSecond line of text";

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);

// send email
mail("someone@example.com","My subject",$msg);
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>mail</title>
</head>
<body>
<form method="POST">
	<textarea></textarea>
	<input type="bottum" name="send">
</form>
</body>
</html>