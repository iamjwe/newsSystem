/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50540
Source Host           : localhost:3306
Source Database       : newsdb

Target Server Type    : MYSQL
Target Server Version : 50540
File Encoding         : 65001

Date: 2019-08-07 13:51:06
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `t_news`
-- ----------------------------
DROP TABLE IF EXISTS `t_news`;
CREATE TABLE `t_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `newsid` int(11) NOT NULL,
  `is_release` char(1) NOT NULL DEFAULT '0' COMMENT '0为未发布，1为已发布',
  `browse_count` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_news_detail` (`newsid`),
  CONSTRAINT `fk_news_detail` FOREIGN KEY (`newsid`) REFERENCES `t_news_detail` (`newsid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_news
-- ----------------------------
INSERT INTO t_news VALUES ('1', '1', '1', '100');
INSERT INTO t_news VALUES ('2', '2', '1', '50');
INSERT INTO t_news VALUES ('3', '3', '1', '210');
INSERT INTO t_news VALUES ('16', '17', '0', '0');

-- ----------------------------
-- Table structure for `t_news_detail`
-- ----------------------------
DROP TABLE IF EXISTS `t_news_detail`;
CREATE TABLE `t_news_detail` (
  `newsid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) DEFAULT NULL,
  `content` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`newsid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_news_detail
-- ----------------------------
INSERT INTO t_news_detail VALUES ('1', '杨云峰窗体写的哈呀', '杨云峰确实很强，很强');
INSERT INTO t_news_detail VALUES ('2', '王传鑫强强强啊', '巴拉巴拉巴拉巴拉');
INSERT INTO t_news_detail VALUES ('3', '刘锋代码写得好', '巴拉巴拉，嘿，巴拉巴拉嘿巴拉巴拉');
INSERT INTO t_news_detail VALUES ('17', 'kaihui', 'haode ');

-- ----------------------------
-- Procedure structure for `proc_addnews`
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_addnews`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `proc_addnews`(in tit varchar(30),in cont varchar(1000))
BEGIN
	#Routine body goes here...
	declare c int;
	insert into t_news_detail(title,content) values(tit,cont);
	select last_insert_id() into c;
	insert into t_news(newsid,is_release,browse_count) values(c,0,0);
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for `proc_delete_news`
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_delete_news`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `proc_delete_news`(in v_id int)
BEGIN
	#Routine body goes here...
  declare c int;
	select newsid from t_news where id=v_id into c;
	delete from t_news where id=v_id;
  delete from t_news_detail where newsid = c;
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for `proc_page_news`
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_page_news`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `proc_page_news`(in begin int,in num int)
BEGIN
	#Routine body goes here...
	select * from (select t1.id,t1.is_release,t1.browse_count,t2.title,t2.content
	from t_news t1 inner join t_news_detail t2 on t1.newsid=t2.newsid) as t where is_release='1' limit begin,num;
END
;;
DELIMITER ;
