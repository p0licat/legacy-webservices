<?php

$dir='/var/www/html/uploads';
$files1=scandir($dir);

$count=1;
echo "<div class=\"box\">" . "<p>";
foreach ($files1 as $ent) {
	if($ent != '.' && $ent != '..') {
			/*
			$form_start = "<form method=\"get\" action=\"";
			$form_start2 = "render.php?name=" . $ent . "\">";
			$btnt_start = "<button ";
			$btnt_end = ">X</button></form>";
			$btnt_mid = "type=\"submit\"";
			$btnt = $form_start . $form_start2 . $btnt_start . $btnt_mid . $btnt_end;
			 */
			$nlink = "<a href=\"render.html?name=" . $ent . "\">X</a>";
			$dlink = "<a href=\"delete.html?name=" . $ent . "\">D</a>";

			//echo $ent . $ent;

			echo ""  . ""  . $count . ": " . $ent . " " . $nlink . " " . $dlink . "<br>";
			$count = $count + 1;
	} else {
		continue;
	}
}
echo "</p>" . "</div>";
?>
