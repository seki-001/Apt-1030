<?php
function check_login($username, $password) {
    $users = [
        'user1' => 'pass1',
        'user2' => 'pass2'
    ];

    if (isset($users[$username]) && $users[$username] === $password) {
        return true;
    } else {
        return false;
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if (check_login($username, $password)) {
        echo "Login successful!";
    } else {
        echo "Invalid username or password.";
    }
}
?>
