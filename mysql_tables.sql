-- engagements table: storage of user data extracted from engaged posts.

CREATE TABLE `engagements` (
	`ID` INT(11) NOT NULL AUTO_INCREMENT,
	`hastag` VARCHAR(100),
	`username` VARCHAR(100),
	`profile` VARCHAR(100),
	`url` VARCHAR(100),
	`date` VARCHAR(100),
	`time` VARCHAR(100),
	PRIMARY KEY (`ID`)
) ENGINE=MyISAM;