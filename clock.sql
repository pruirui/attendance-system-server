CREATE DATABASE  IF NOT EXISTS `clock` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `clock`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: clock
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `HRname` varchar(45) DEFAULT NULL,
  `createTime` datetime DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `departmentName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'lee','2023-03-12 15:13:59','待审核','无描述','ikun'),(2,'lee','2023-03-12 15:16:23','待审核','该部门成立于312，是一所基于ai驱动的A轮融资大公司','ikun');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sysconfigs`
--

DROP TABLE IF EXISTS `sysconfigs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sysconfigs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `departmentName` varchar(45) DEFAULT NULL,
  `clockInTime` time DEFAULT NULL,
  `clockOutTime` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sysconfigs`
--

LOCK TABLES `sysconfigs` WRITE;
/*!40000 ALTER TABLE `sysconfigs` DISABLE KEYS */;
INSERT INTO `sysconfigs` VALUES (1,'ikun','06:00:00','21:00:00'),(2,'ikun','06:00:00','21:00:00'),(3,'ikun','06:00:00','21:00:00');
/*!40000 ALTER TABLE `sysconfigs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_applications`
--

DROP TABLE IF EXISTS `user_applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_applications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int DEFAULT NULL,
  `applyTime` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `content` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_applications`
--

LOCK TABLES `user_applications` WRITE;
/*!40000 ALTER TABLE `user_applications` DISABLE KEYS */;
INSERT INTO `user_applications` VALUES (1,1,'2023-03-13 21:25:29','未处理','请假'),(2,1,'2023-03-13 21:28:55','未处理','请假'),(3,1,'2023-03-13 21:31:36','未处理','加班'),(4,1,'2023-03-13 21:32:19','未处理','补打卡');
/*!40000 ALTER TABLE `user_applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_clocks`
--

DROP TABLE IF EXISTS `user_clocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_clocks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int DEFAULT NULL,
  `clockTime` datetime DEFAULT NULL,
  `note` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_clocks`
--

LOCK TABLES `user_clocks` WRITE;
/*!40000 ALTER TABLE `user_clocks` DISABLE KEYS */;
INSERT INTO `user_clocks` VALUES (6,1,'2023-03-13 20:22:40','签到'),(7,1,'2023-03-13 20:29:34','签到'),(8,1,'2023-03-13 21:15:20','签退');
/*!40000 ALTER TABLE `user_clocks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userfaces`
--

DROP TABLE IF EXISTS `userfaces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userfaces` (
  `id` int NOT NULL,
  `username` varchar(45) DEFAULT NULL,
  `userFacePath` varchar(45) DEFAULT NULL,
  `faceEmbedding` varchar(145) DEFAULT NULL,
  `createTime` datetime DEFAULT NULL,
  `updateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userfaces`
--

LOCK TABLES `userfaces` WRITE;
/*!40000 ALTER TABLE `userfaces` DISABLE KEYS */;
INSERT INTO `userfaces` VALUES (1,'lee','/images','999999','2023-03-13 13:16:41','2023-03-13 13:16:41'),(2,'lee','/images','999999','2023-03-13 13:21:42','2023-03-13 13:21:42'),(3,'lee','/images','999999','2023-03-13 14:09:49','2023-03-13 14:09:49'),(4,'lee','./images/lee.jpg','999999','2023-03-13 14:10:53','2023-03-13 14:10:53'),(5,NULL,'./images/5.jpg','999999','2023-03-13 17:42:02','2023-03-13 17:42:02'),(6,NULL,'./images/6.jpg','','2023-03-13 17:47:29','2023-03-13 17:47:29');
/*!40000 ALTER TABLE `userfaces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `motto` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `home` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Lee','111111','17365691811','江苏 苏州','2000-08-11','自信即巅峰','男','陕西 西安'),(2,'liyuanhang','111111','15651659977',NULL,NULL,NULL,NULL,NULL),(3,'admin','111111','00000000000',NULL,NULL,NULL,NULL,NULL),(4,'lee1','111111','11111111111',NULL,NULL,NULL,NULL,NULL),(5,'lee11','111111','22222222222',NULL,NULL,NULL,NULL,NULL),(6,NULL,'111111','17365691822',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-13 22:54:08
