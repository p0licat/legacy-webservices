<?php
include "utility.php";
$target_dir = "/var/www/html/uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
$uplimit = 500000;
echo ParagraphWrap("Trying to upload: " . $target_file);

if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        echo ParagraphWrap("File is an image - " . $check["mime"] . ".");
	$uploadOk = 1;
    } else {
        $uploadOk = 0;
    }
    if($imageFileType == "txt"){
		$uploadOk = 1;
		echo ParagraphWrap("File is text.");
    }
}

if(file_exists($target_file)) {
    echo ParagraphWrap("File already exists.");
    $uploadOk = 0;
}

if($_FILES["fileToUpload"]["size"] > $uplimit) {
    echo ParagraphWrap("Sorry, larger than up limit: " . $uplimit . "bytes.");
    $uploadOk = 0;
}

if($imageFileType != "txt" && $imageFileType != "png" && $imageFileType != "jpg" && $imageFileType != "gif") {
    echo ParagraphWrap("Sorry, file type not allowed.");
    $uploadOk = 0;
}

if($uploadOk == 0){
    echo ParagraphWrap("Upload parameters not ok...");
} else {
	echo ParagraphWrap("Upload parameters ok.");
	echo " " . $_FILES["fileToUpload"]["tmp_name"] . "<br> ";
	echo " " . $_FILES["fileToUpload"]["name"] . "<br> ";
	if(is_uploaded_file($_FILES["fileToUpload"]["tmp_name"])){
		echo ParagraphWrap("Server received file...");
	} else {
		echo ParagraphWrap("Failed to upload to server.");
	}
	try {
    if(move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo ParagraphWrap("The file ". basename($_FILES["fileToUpload"]["name"]). " has been uploaded.");
	} else {	
        echo ParagraphWrap("Upload failed...");
	}
	} catch (RuntimeException $e) {
		echo $e->getMessage();
	}
}
echo "<a href='/'>Go back.</a>";
?>

