#!/usr/bin/php

<?php


$videoID = $argv[1]; // view id here 

$json = file_get_contents("https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" . $videoID . "&key=AIzaSyCPuVtaXg9TQuUnTUnoCZ5ryP3c7n4fm9Q");


$jsonData = json_decode($json);
$viewCount = $jsonData->items[0]->statistics->viewCount;
$likeCount = $jsonData->items[0]->statistics->likeCount;
$dislikeCount = $jsonData->items[0]->statistics->dislikeCount;
$favoriteCount = $jsonData->items[0]->statistics->favoriteCount;
$commentCount = $jsonData->items[0]->statistics->commentCount;

$json = file_get_contents("https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" . $videoID . "&key=AIzaSyCPuVtaXg9TQuUnTUnoCZ5ryP3c7n4fm9Q");

$jsonData = json_decode($json);

$published_date = $jsonData->items[0]->snippet->publishedAt;
$title = $jsonData->items[0]->snippet->title;
$description = $jsonData->items[0]->snippet->description;
$categoryId = $jsonData->items[0]->snippet->categoryId;


// $views = $jsonData->items[0]->statistics->viewCount;

if (isset($viewCount)) {
	$result = array('video_id' => $videoID,
    'viewCount' => $viewCount,
    'likeCount' => $likeCount,
    'dislikeCount' => $dislikeCount,
    'favoriteCount' => $favoriteCount,
    'commentCount' => $commentCount,
    'published_date' => $published_date,
	'title' => $title, 
	'description' => $description, 
	'categoryId' => $categoryId
);

	$resultJSON = json_encode($result);

	echo $resultJSON;

}

?>