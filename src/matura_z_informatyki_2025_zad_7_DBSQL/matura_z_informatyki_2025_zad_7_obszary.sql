-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: matura_z_informatyki_2025_zad_7
-- ------------------------------------------------------
-- Server version	9.5.0

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '674a0b36-dea6-11f0-89d3-581122aed039:1-1466';

--
-- Table structure for table `obszary`
--

DROP TABLE IF EXISTS `obszary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `obszary` (
  `kod_obszaru` varchar(255) NOT NULL,
  `nazwa_obszaru` varchar(255) NOT NULL,
  PRIMARY KEY (`kod_obszaru`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `obszary`
--

LOCK TABLES `obszary` WRITE;
/*!40000 ALTER TABLE `obszary` DISABLE KEYS */;
INSERT INTO `obszary` VALUES ('MC-01','Mare Boreum'),('MC-02','Diacria'),('MC-03','Arcadia'),('MC-04','Mare Acidalium'),('MC-05','Ismenius Lacus'),('MC-06','Casius'),('MC-07','Cebrenia'),('MC-08','Amazonis'),('MC-09','Tharsis'),('MC-10','Lunae Palus'),('MC-11','Oxia Palus'),('MC-12','Arabia'),('MC-13','Syrtis Major'),('MC-14','Amenthes'),('MC-15','Elysium'),('MC-16','Memnonia'),('MC-17','Phoenicis Lacus'),('MC-18','Coprates'),('MC-19','Margaritifer Sinus'),('MC-20','Sinus Sabaeus'),('MC-21','Iapygia'),('MC-22','Mare Tyrrhenum'),('MC-23','Aeolis'),('MC-24','Phaethontis'),('MC-25','Thaumasia'),('MC-26','Argyre'),('MC-27','Noachis'),('MC-28','Hellas'),('MC-29','Eridania'),('MC-30','Mare Australe');
/*!40000 ALTER TABLE `obszary` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-13 19:24:06
