<?php
$action = (empty($_POST['action'])) ? 'default' : $_POST['action'];

// ternary operator diatas sama seperti statement if/else dibawah ini:
if (empty($_POST['action'])) {
    $action = 'default';
} else {
    $action = $_POST['action'];
}

?>

