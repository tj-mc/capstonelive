CREATE TABLE `posts` (
  `postid` int(255) NOT NULL AUTO_INCREMENT,
  `datetime` datetime(6) NOT NULL,
  `contents` varchar(3000) NOT NULL,
  PRIMARY KEY (`postid`)
) ENGINE=InnoDB AUTO_INCREMENT=1154 DEFAULT CHARSET=utf8

CREATE TABLE `ttshold` (
  `id` int(255) DEFAULT NULL,
  `text` varchar(4000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8


