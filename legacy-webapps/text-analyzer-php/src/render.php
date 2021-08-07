<?php
include "utility.php";
$fname=$_GET['name'];
$dirname="uploads/";
$fileType=strtolower(pathinfo($dirname . $fname, PATHINFO_EXTENSION));

$bbtn="<a href='/'>Back</a>";
$ftagt="";
$brtag="<br>";

echo ParagraphWrap($fname . $brtag);

if($fileType == 'txt'){
	$command = escapeshellcmd('python3 script.py ' . $dirname . $fname);
	$output = shell_exec($command);
	echo $output;

} else {
	$ftagt="<img src='uploads/" . $fname . "'/>";
}

echo $ftagt . $brtag . "\n";
echo $bbtn . "\n";

?>
