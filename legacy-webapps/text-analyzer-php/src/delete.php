<?php
include "utility.php";
$fname=$_GET['name'];
$uploadDir="MplPlots/";
$fileDir="uploads/";
$absPath = "/var/www/html";

$mdhash = md5($fileDir . $fname);

if(unlink($fileDir . $fname) != 1) {
	echo ParagraphWrap("Error removing" . $fileDir . $fname . " ... ");
} else {
	echo ParagraphWrap("Removed " . $fileDir . $fname . " successfully.");
}
if(unlink($uploadDir . $mdhash . "_fig43D.jpg") != 1) { 
	echo ParagraphWrap("Error removing " . $uploadDir . $mdhash . "_fig43D.jpg" . " ... ");
} else {
	echo ParagraphWrap("Removed " . $uploadDir . $mdhash . "_fig43D.jpg" . " successfully.");
}
if(unlink($uploadDir . $mdhash . "_fig3.jpg") != 1) {
	echo ParagraphWrap("Error removing " . $uploadDir . $mdhash . "_fig3.jpg" . " ... ");
} else {
	echo ParagraphWrap("Removed " . $uploadDir . $mdhash . "_fig3.jpg" . " successfully.");
}
if(unlink($uploadDir . $mdhash . "_fig2.jpg") != 1) {
	echo ParagraphWrap("Error removing " . $uploadDir . $mdhash . "_fig2.jpg" . " ... ");
} else {
	echo ParagraphWrap("Removed " . $uploadDir . $mdhash . "_fig2.jpg" . " successfully.");
}
if(unlink($uploadDir . $mdhash . "_fig1.jpg") != 1) {
	echo ParagraphWrap("Error removing " . $uploadDir . $mdhash . "_fig1.jpg" . " ... ");
} else {
	echo ParagraphWrap("Removed " . $uploadDir . $mdhash . "_fig1.jpg" . " successfully.");
}

echo "<a href='/'>Back</a>";

?>
