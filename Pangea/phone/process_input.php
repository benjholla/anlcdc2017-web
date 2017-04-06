<?php

echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";

date_default_timezone_set('UTC');
//$str = md5(date('Y-m-d H:i'));
$str = md5(date('Y-m-d H'));

$strlen = strlen($str);
$seed = 1526;
for($i = 0; $i <= $strlen; $i++) {
    $char = substr( $str, $i, 1 );
    $seed = $seed + ord($char);
}

// not really a OTP, but whatever...
$formattedOTP = implode(' ',str_split($seed)); 


if(isset($_REQUEST['Digits']) && strlen($_REQUEST['Digits'])==8){
	// Frank Castle
	if(strcmp(substr($_REQUEST['Digits'], 0, 4), "4421") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "8203") == 0){
		echo "<Response><Say>Hi Frank. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	} 
	
	// Lisa Delrose
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "8723") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "7351") == 0){
		echo "<Response><Say>Hi Lisa. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}
		
	// Chuck Wheeler
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "3637") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "6221") == 0){
		echo "<Response><Say>Hi Chuck. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// James Hoyt
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "5345") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "4914") == 0){
		echo "<Response><Say>Hi James. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	//Sandra Wilhelm
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "6365") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "9361") == 0){
		echo "<Response><Say>Hi Sandra. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// Patricia Emerson
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "8373") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "5101") == 0){
		echo "<Response><Say>Hi Patricia. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// Piotre Luther
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "2383") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "6628") == 0){
		echo "<Response><Say>Hi Piotre. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// Karen Holms
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "1122") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "8819") == 0){
		echo "<Response><Say>Hi Karen. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// Simon Smith
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "9923") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "2315") == 0){
		echo "<Response><Say>Hi Simon. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// Ted Fritz
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "9121") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "4918") == 0){
		echo "<Response><Say>Hi Ted. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// Crystal Licht
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "2287") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "1029") == 0){
		echo "<Response><Say>Hi Crystal. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// Holly Peterson
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "2342") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "7384") == 0){
		echo "<Response><Say>Hi Holly. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// Brad Wells
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "1022") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "1946") == 0){
		echo "<Response><Say>Hi Brad. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// Susan Taylor
	else if(strcmp(substr($_REQUEST['Digits'], 0, 4), "3234") == 0 && strcmp(substr($_REQUEST['Digits'], 4, 7), "1082") == 0){
		echo "<Response><Say>Hi Susan. Your HMI one time password is " . $formattedOTP . ". Goodbye.</Say></Response>";
	}	
	
	// invalid credentials
	else {
		echo "<Response><Say>Your credentials were incorrect. If you believe this is an error, please come onsite to the Pangea offices and we will assist you. Goodbye.</Say></Response>";
	}
} else {
	echo "<Response><Say>Invalid input. If you believe this is an error, please come onsite to the Pangea offices and we will assist you. Goodbye.</Say></Response>";
}

?>