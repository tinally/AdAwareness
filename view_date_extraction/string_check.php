
<!-- #!/usr/bin/php -->

<?php

$json = '{"video_id":"tO0L-7lkhPM","views":"437728","published_date":"2015-12-17T14:36:07.000Z","title":"IT\u2019S ALL ABOUT THE PIKE IN ONTARIO"}';


$jsonData = json_decode($json);
$views = $jsonData->title;

echo $views;


?>