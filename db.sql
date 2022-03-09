CREATE DATABASE dev2qa;

USE dev2qa;

CREATE TABLE article (
  id int NOT NULL AUTO_INCREMENT,
  articleName varchar(45) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY id_UNIQUE (id),
  UNIQUE KEY artcleName_UNIQUE (articleName)
); 

INSERT INTO article (articleName) VALUES ("article1");
INSERT INTO article (articleName) VALUES ("article2");
INSERT INTO article (articleName) VALUES ("article3");
INSERT INTO article (articleName) VALUES ("article4");


CREATE TABLE articleTopic (
  articleId int NOT NULL,
  topicId int NOT NULL,
  PRIMARY KEY (topicId,articleId)
);
INSERT INTO articleTopic (articleId,topicId) VALUES (1,1);
INSERT INTO articleTopic (articleId,topicId) VALUES (1,3);
INSERT INTO articleTopic (articleId,topicId) VALUES (2,3);
INSERT INTO articleTopic (articleId,topicId) VALUES (3,1);
INSERT INTO articleTopic (articleId,topicId) VALUES (3,4);
INSERT INTO articleTopic (articleId,topicId) VALUES (4,2);


CREATE TABLE topic (
  id int NOT NULL AUTO_INCREMENT,
  topicName varchar(45) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY id_UNIQUE (id),
  UNIQUE KEY topicName_UNIQUE (topicName)
);

INSERT INTO topic (topicName) VALUES ("topic1");
INSERT INTO topic (topicName) VALUES ("topic2");
INSERT INTO topic (topicName) VALUES ("topic3");
INSERT INTO topic (topicName) VALUES ("topic4");


