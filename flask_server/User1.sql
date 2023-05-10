CREATE TABLE `Period1` (
  `stu_id` INTEGER NOT NULL,
  `stu_name` TEXT NOT NULL,
  `stu_attendance` TEXT NOT NULL
);
CREATE TABLE `Period2` (
  `stu_id` INTEGER NOT NULL,
  `stu_name` TEXT NOT NULL,
  `stu_attendance` TEXT DEFAULT NULL
);
CREATE TABLE `Period3` (
  `stu_id` INTEGER NOT NULL,
  `stu_name` TEXT NOT NULL,
  `stu_attendance` TEXT DEFAULT NULL
);
CREATE TABLE `Period4` (
  `stu_id` INTEGER NOT NULL,
  `stu_name` TEXT NOT NULL,
  `stu_attendance` TEXT DEFAULT NULL
);
CREATE TABLE `Period8` (
  `stu_id` INTEGER NOT NULL,
  `stu_name` TEXT NOT NULL,
  `stu_attendance` TEXT DEFAULT NULL
);
-- (B) DUMMY USERS
INSERT INTO `Period1` (`stu_id`, `stu_name`, `stu_attendance`)
VALUES ("320123", "Connor Church", "Absent"),
  ("242837", "William Clymire", "Absent"),
  ("512323", "Cameron Farley", "Absent"),
  ("123141", "Oliver Hankins", "Absent"),
  ("987654", "Joshua Lee", "Absent");
INSERT INTO `Period2` (`stu_id`, `stu_name`, `stu_attendance`)
VALUES ("242837", "William Clymire", "Absent");
INSERT INTO `Period3` (`stu_id`, `stu_name`, `stu_attendance`)
VALUES ("123141", "Oliver Hankins", "Absent");
INSERT INTO `Period4` (`stu_id`, `stu_name`, `stu_attendance`)
VALUES ("320123", "Connor Church", "Absent"),
  ("512323", "Cameron Farley", "Absent"),
  ("123141", "Oliver Hankins", "Absent"),
  ("987654", "Joshua Lee", "Absent");
INSERT INTO `Period8` (`stu_id`, `stu_name`, `stu_attendance`)
VALUES ("242837", "William Clymire", "Absent"),
  ("123141", "Oliver Hankins", "Absent");
--  ("320123", "Connor Church", "Absent")
--  ("242837", "William Clymire", "Absent")
--  ("512323", "Cameron Farley", "Absent")
--  ("123141", "Oliver Hankins", "Absent")
--  ("987654"), "Joshua Lee", "Absent")