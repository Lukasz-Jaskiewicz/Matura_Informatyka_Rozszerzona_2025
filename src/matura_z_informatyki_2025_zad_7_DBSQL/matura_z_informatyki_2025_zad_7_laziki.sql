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
-- Table structure for table `laziki`
--

DROP TABLE IF EXISTS `laziki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `laziki` (
  `nr_lazika` int NOT NULL,
  `nazwa_lazika` varchar(255) NOT NULL,
  `rok_wyslania` int NOT NULL,
  `wsp_lodowania` varchar(45) NOT NULL,
  PRIMARY KEY (`nr_lazika`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laziki`
--

LOCK TABLES `laziki` WRITE;
/*!40000 ALTER TABLE `laziki` DISABLE KEYS */;
INSERT INTO `laziki` VALUES (1,'Mariner 3',2049,'50.51N, 70.01E\r'),(2,'Mariner 6',2050,'11.90N, 119.49E\r'),(3,'Mariner 7',2050,'44.90S, 130.80W\r'),(4,'Mariner 9',2051,'43.20S, 21.89W\r'),(5,'Mariner 10',2051,'4.88N, 63.43E\r'),(6,'Mariner 11',2052,'77.71N, 148.53E\r'),(7,'Mariner 12',2053,'53.29N, 45.78W\r'),(8,'Mariner 13',2053,'57.37S, 25.45E\r'),(9,'Mariner 14',2054,'17.63S, 13.01W\r'),(10,'Mariner 15',2054,'23.79S, 56.97W\r'),(11,'Mariner 16',2055,'59.42S, 15.97W\r'),(12,'Mariner 20',2055,'6.41S, 116.10W\r'),(13,'Viking 2',2052,'60.72N, 122.46E\r'),(14,'Viking 4',2053,'18.71N, 17.14W\r'),(15,'Viking 5',2053,'33.52S, 162.36W\r'),(16,'Viking 7',2054,'47.12S, 102.95W\r'),(17,'Viking 8',2054,'21.27N, 90.13E\r'),(18,'Viking 10',2055,'25.21S, 169.35E\r'),(19,'Viking 13',2056,'47.43N, 160.74E\r'),(20,'Viking 15',2056,'51.10S, 71.36E\r'),(21,'Viking 17',2056,'11.38S, 119.54W\r'),(22,'Phobos 1',2053,'5.89N, 39.91E\r'),(23,'Phobos 2',2053,'23.80S, 156.02W\r'),(24,'Phobos 3',2053,'32.13S, 131.87E\r'),(25,'Phobos 4',2054,'51.58S, 161.55W\r'),(26,'Phobos 5',2054,'48.99S, 67.17E\r'),(27,'Phobos 6',2054,'74.62S, 100.08E\r'),(28,'Deimos 3',2058,'63.27S, 66.46W\r'),(29,'Deimos 4',2058,'33.88S, 148.04W\r'),(30,'Deimos 8',2058,'21.43N, 76.62W\r'),(31,'Deimos 10',2059,'66.67N, 93.37W\r'),(32,'Deimos 11',2059,'39.82S, 96.42W\r'),(33,'Deimos 13',2060,'73.37N, 48.09E\r'),(34,'Deimos 14',2060,'24.45N, 112.91E\r'),(35,'Pathfinder 2',2060,'16.90S, 101.43W\r'),(36,'Pathfinder 3',2061,'5.85N, 156.58W\r'),(37,'Pathfinder 5',2061,'10.83N, 133.81E\r'),(38,'Pathfinder 7',2062,'79.27N, 111.64W\r'),(39,'Pathfinder 9',2062,'59.92S, 179.01W\r'),(40,'Spirit 1',2062,'23.56S, 147.94E\r'),(41,'Spirit 5',2063,'66.19N, 33.82E\r'),(42,'Spirit 6',2063,'27.80N, 160.30E\r'),(43,'Spirit 7',2063,'13.98S, 98.57W\r'),(44,'Spirit 11',2064,'64.61N, 131.25E\r'),(45,'Spirit 12',2064,'0.43S, 61.64E\r'),(46,'Spirit 13',2065,'58.80S, 113.46W\r'),(47,'Spirit 14',2065,'27.30N, 17.48W\r'),(48,'Spirit 15',2066,'55.77N, 134.40E\r'),(49,'Spirit 16',2066,'30.54S, 24.75W\r'),(50,'Opportunity 2',2064,'22.61N, 142.82E\r'),(51,'Opportunity 3',2064,'50.59S, 47.85W\r'),(52,'Opportunity 4',2065,'9.63N, 121.52W\r'),(53,'Opportunity 5',2065,'70.62S, 159.12W\r'),(54,'Opportunity 6',2065,'14.31N, 112.28E\r'),(55,'Opportunity 7',2066,'37.14N, 148.66E\r'),(56,'Opportunity 10',2067,'35.35S, 72.67W\r'),(57,'Opportunity 13',2067,'44.72S, 102.07W\r'),(58,'Opportunity 15',2068,'56.96S, 5.44W\r'),(59,'Opportunity 16',2068,'41.83S, 120.38E\r'),(60,'Opportunity 18',2069,'47.77S, 28.62W\r'),(61,'Opportunity 19',2069,'68.17S, 21.83W\r'),(62,'Rosetta 1',2065,'3.33S, 27.57E\r'),(63,'Rosetta 3',2066,'54.72S, 108.92E\r'),(64,'Rosetta 7',2067,'48.64S, 67.03E\r'),(65,'Rosetta 8',2067,'3.05S, 8.90W\r'),(66,'Rosetta 9',2067,'17.54N, 149.60E\r'),(67,'Rosetta 10',2068,'29.82S, 66.01W\r'),(68,'Rosetta 11',2068,'21.49N, 105.87E\r'),(69,'Rosetta 13',2069,'69.41N, 168.67E\r'),(70,'Rosetta 14',2069,'24.07S, 46.44W\r'),(71,'Rosetta 15',2070,'50.96S, 146.33W\r'),(72,'Rosetta 16',2071,'29.49S, 118.42W\r'),(73,'Rosetta 20',2071,'69.31S, 68.72W\r'),(74,'Rosetta 21',2071,'17.28N, 7.12E\r'),(75,'Rosetta 22',2071,'43.21S, 109.99E\r'),(76,'Rosetta 25',2072,'47.84N, 169.44E\r'),(77,'Rosetta 27',2073,'28.90S, 98.55E\r'),(78,'Rosetta 28',2073,'2.95N, 160.52W\r'),(79,'Rosetta 29',2073,'18.24N, 120.68E\r'),(80,'Phoenix 2',2067,'53.64N, 159.28W\r'),(81,'Phoenix 3',2068,'4.04S, 171.74W\r'),(82,'Phoenix 7',2068,'42.36S, 157.15E\r'),(83,'Phoenix 11',2069,'56.07N, 79.63E\r'),(84,'Phoenix 12',2069,'53.00N, 129.64E\r'),(85,'Phoenix 13',2070,'6.43S, 95.96E\r'),(86,'Phoenix 16',2071,'75.84N, 122.24E\r'),(87,'Phoenix 17',2071,'34.44S, 25.42W\r'),(88,'Phoenix 19',2071,'12.19S, 23.63W\r'),(89,'Phoenix 22',2072,'65.07S, 96.09W\r'),(90,'Phoenix 23',2072,'65.99S, 161.89W\r'),(91,'Phoenix 27',2073,'75.27N, 138.32W\r'),(92,'Phoenix 28',2073,'77.60N, 60.62E\r'),(93,'Dawn 3',2066,'40.73N, 101.92W\r'),(94,'Dawn 4',2066,'46.81S, 143.88E\r'),(95,'Dawn 6',2067,'8.80N, 79.73W\r'),(96,'Dawn 9',2067,'77.71N, 179.82E\r'),(97,'Perseverance 4',2069,'80.24N, 27.18W\r'),(98,'Perseverance 5',2070,'48.97S, 86.32E\r'),(99,'Perseverance 6',2070,'34.38N, 12.41E\r'),(100,'Perseverance 7',2070,'61.39S, 157.42W\r'),(101,'Perseverance 8',2071,'53.93N, 163.34E\r');
/*!40000 ALTER TABLE `laziki` ENABLE KEYS */;
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
