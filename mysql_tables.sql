-- engagements_hasgtag table: storage of user data extracted from engaged posts by hashtag.

CREATE TABLE `engagements_hashtag` (
	`ID` INT(11) NOT NULL AUTO_INCREMENT,
	`hastag` VARCHAR(100),
	`username` VARCHAR(100),
	`profile` VARCHAR(100),
	`url` VARCHAR(100),
	`date` VARCHAR(100),
	`time` VARCHAR(100),
	PRIMARY KEY (`ID`)
) ENGINE=MyISAM;

-- engagements_explore table: storage of user data extracted from engaged posts by explore.

CREATE TABLE `engagements_explore` (
	`ID` INT(11) NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(100),
	`profile` VARCHAR(100),
	`url` VARCHAR(100),
	`date` VARCHAR(100),
	`time` VARCHAR(100),
	PRIMARY KEY (`ID`)
) ENGINE=MyISAM;