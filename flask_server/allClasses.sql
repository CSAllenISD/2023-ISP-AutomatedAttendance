CREATE TABLE `Period1` (
  `user_id` INTEGER NOT NULL,
  `user_name` TEXT NOT NULL,
  `user_email` TEXT DEFAULT NULL,
  PRIMARY KEY("user_id" AUTOINCREMENT)
);
 
-- (B) DUMMY USERS
INSERT INTO `Period1`
  (`user_name`, `user_email`)
VALUES
  ("Jo Doe", "jo@doe.com"),
  ("Job Doe", "job@doe.com"),
  ("Joe Doe", "joe@doe.com"),
  ("Jog Doe", "jog@doe.com"),
  ("Joi Doe", "joi@doe.com"),
  ("Jol Doe", "jol@doe.com"),
  ("Jon Doe", "jon@doe.com"),
  ("Jos Doe", "jos@doe.com"),
  ("Jou Doe", "jou@doe.com"),
  ("Joy Doe", "joy@doe.com");