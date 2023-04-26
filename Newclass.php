<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $className = $_POST['class-name'];
  $classPeriod = $_POST['period'];

  // Connect to the database
  $db = new SQLite3('Usertest.db');

  // Prepare the SQL statement to insert the new class
  $stmt = $db->prepare('INSERT INTO classes (name, period) VALUES (:name, :period)');
  $stmt->bindValue(':name', $className);
  $stmt->bindValue(':period', $classPeriod);

  // Execute the SQL statement
  $stmt->execute();

  // Close the database connection
  $db->close();

  // Redirect to the classes page
  header('Location: classes.html');
  exit();
}
?>
