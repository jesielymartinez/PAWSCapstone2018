<?php
//connect.php
$host = "localhost"; 
$user = "postgres"; 
$pass = "pass"; 
$db = "Forum";
	//Database connection
    $db_connection = pg_connect("host=$host dbname=$db user=$user password=$pass");

    //test database connection
    if($db_connection)
    {
    	echo "connected\n</br>";
    	$query ="SELECT distinct utype from users LIMIT 2";
    	$result = pg_query($db_connection, $query) or die("Cannot execute query: $query\n");

    	while ($row = pg_fetch_row($result)) {
  		echo "$row[0] \n";
		}
    }
    	else{
    		echo 'Not connected';
    	}
    pg_close()
?>
