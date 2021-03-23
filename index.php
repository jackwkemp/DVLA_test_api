<?php 

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://uat.driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, "{\n  \"registrationNumber\": \"XXXXXXXX\"\n}");
curl_setopt($ch, CURLOPT_POST, 1);

$headers = array();
$headers[] = 'Content-Type: application/json';
$headers[] = 'Accept: application/json';
$headers[] = 'X-Api-Key: INSERT API KEY HERE';
$headers[] = 'X-Correlation-Id: INSERT COMPANY NAME HERE';
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$result = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);

}

curl_close ($ch);

?> 

<!--
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>MOT API</title>
 </head>
 <body>
<form action="">
    <input type="text" name="registrationNumber"/>

    <button type="submit">submit</button>
</form>

 </body>
</html>
 -->


<!-- 
curl -X POST  -d '{
  "registrationNumber": "XXXXXXXX"
}' https://uat.driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles \
 -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'x-api-key: INSERT API KEY HERE' -H 'X-Correlation-Id: INSERT COMPANY NAME HERE'

 -->

