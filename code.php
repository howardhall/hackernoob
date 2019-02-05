<?php
session_start();
if(!isset($_POST['code'])){
	die("what the fuck");
}
$name = md5(uniqid());
$code = $_POST['code'];
$format = $_POST['format'];
$file = fopen("submissions/$name.txt","w");
$time = time();
fwrite($file,$code);
fclose($file);
chmod("submissions/$name.txt",0644);
$db = new SQLite3("db.sqlite3");
$db->exec("INSERT INTO uploads VALUES ('$name','$format',$time, 0, null)");
die("success");
