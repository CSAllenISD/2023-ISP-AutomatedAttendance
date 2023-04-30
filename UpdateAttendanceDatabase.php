<?php
$db = new PDO('sqlite:Usertest.db');

$class = $_POST['class'];
$date = $_POST['date'];

foreach($_POST['attendance'] as $student_id => $attendance) {
    $stmt = $db->prepare("UPDATE attendance SET status = :attendance WHERE class = :class AND date = :date AND student_id = :student_id");
    $stmt->bindParam(':attendance', $attendance);
    $stmt->bindParam(':class', $class);
    $stmt->bindParam(':date', $date);
    $stmt->bindParam(':student_id', $student_id);
    $stmt->execute();
}

header("Location: AttendanceReport.html");
exit();
?>
