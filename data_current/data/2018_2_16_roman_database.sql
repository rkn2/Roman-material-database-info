-- MySQL dump 10.13  Distrib 5.7.19, for osx10.12 (x86_64)
--
-- Host: localhost    Database: treestone
-- ------------------------------------------------------
-- Server version	5.7.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bibliography`
--

DROP TABLE IF EXISTS `bibliography`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bibliography` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bib_no` int(11) DEFAULT NULL,
  `full_citation` longtext,
  `notes` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bibliography`
--

LOCK TABLES `bibliography` WRITE;
/*!40000 ALTER TABLE `bibliography` DISABLE KEYS */;
/*!40000 ALTER TABLE `bibliography` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citation`
--

DROP TABLE IF EXISTS `citation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `citation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bibliography_id` int(11) DEFAULT NULL,
  `page_range` longtext,
  `classical_identifier` longtext,
  `url` longtext,
  `notes` longtext,
  PRIMARY KEY (`id`),
  KEY `fk_bibliography` (`bibliography_id`),
  CONSTRAINT `citation_ibfk_1` FOREIGN KEY (`bibliography_id`) REFERENCES `bibliography` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citation`
--

LOCK TABLES `citation` WRITE;
/*!40000 ALTER TABLE `citation` DISABLE KEYS */;
/*!40000 ALTER TABLE `citation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citation_stone`
--

DROP TABLE IF EXISTS `citation_stone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `citation_stone` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `citation_id` int(11) DEFAULT NULL,
  `stone_id` int(11) DEFAULT NULL,
  `supports` longtext,
  `stone_attribute` varchar(255),
  `notes` longtext,
  PRIMARY KEY (`id`),
  KEY `fk_citation` (`citation_id`),
  KEY `stone_id` (`stone_id`),
  CONSTRAINT `citation_stone_ibfk_1` FOREIGN KEY (`citation_id`) REFERENCES `citation` (`id`),
  CONSTRAINT `citation_stone_ibfk_2` FOREIGN KEY (`stone_id`) REFERENCES `stones` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citation_stone`
--

LOCK TABLES `citation_stone` WRITE;
/*!40000 ALTER TABLE `citation_stone` DISABLE KEYS */;
/*!40000 ALTER TABLE `citation_stone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citation_tree`
--

DROP TABLE IF EXISTS `citation_tree`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `citation_tree` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `citation_id` int(11) DEFAULT NULL,
  `tree_id` int(11) DEFAULT NULL,
  `supports` longtext,
  `tree_attribute` varchar(255),
  `notes` longtext,
  PRIMARY KEY (`id`),
  KEY `fk_citation` (`citation_id`),
  KEY `tree_id` (`tree_id`),
  CONSTRAINT `citation_tree_ibfk_1` FOREIGN KEY (`citation_id`) REFERENCES `citation` (`id`),
  CONSTRAINT `citation_tree_ibfk_2` FOREIGN KEY (`tree_id`) REFERENCES `trees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citation_tree`
--

LOCK TABLES `citation_tree` WRITE;
/*!40000 ALTER TABLE `citation_tree` DISABLE KEYS */;
/*!40000 ALTER TABLE `citation_tree` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stones`
--

DROP TABLE IF EXISTS `stones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext,
  `alternate_name` longtext,
  `petrographic_details` longtext,
  `age` longtext,
  `appearance` longtext,
  `poisson_ratio` float DEFAULT NULL,
  `absorption` float DEFAULT NULL,
  `quarry_location` longtext,
  `archaeological_sources` longtext,
  `primary_sources` longtext,
  `secondary_sources` longtext,
  `shapefile` multipolygon DEFAULT NULL,
  `notes` longtext,
  `dates_of_use` longtext,
  `density_avg` float DEFAULT NULL,
  `density_low` float DEFAULT NULL,
  `density_high` float DEFAULT NULL,
  `elastic_modulus_average` float DEFAULT NULL,
  `elastic_modulus_low` float DEFAULT NULL,
  `elastic_modulus_high` float DEFAULT NULL,
  `image` longblob,
  `rupture_modulus_average` float DEFAULT NULL,
  `rupture_modulus_low` float DEFAULT NULL,
  `rupture_modulus_high` float DEFAULT NULL,
  `compressive_strength_average` float DEFAULT NULL,
  `compressive_strength_low` float DEFAULT NULL,
  `compressive_strength_high` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stones`
--

LOCK TABLES `stones` WRITE;
/*!40000 ALTER TABLE `stones` DISABLE KEYS */;
/*!40000 ALTER TABLE `stones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trees`
--

DROP TABLE IF EXISTS `trees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `common_name` longtext,
  `sci_name` longtext,
  `distribution` longtext,
  `tree_rad_low` int(11) DEFAULT NULL,
  `tree_rad_high` int(11) DEFAULT NULL,
  `density` int(11) DEFAULT NULL,
  `janka_hardness` int(11) DEFAULT NULL,
  `rupture_modulus` int(11) DEFAULT NULL,
  `elastic_modulus` int(11) DEFAULT NULL,
  `crushing_strength` int(11) DEFAULT NULL,
  `shrink_rad` float DEFAULT NULL,
  `shrink_tan` float DEFAULT NULL,
  `shrink_volumetric` float DEFAULT NULL,
  `rot_resistance` longtext,
  `workability` longtext,
  `common_uses` longtext,
  `primary_sources` longtext,
  `archaeological_sources` longtext,
  `shapefile` multipolygon DEFAULT NULL,
  `secondary_sources` longtext,
  `notes` longtext,
  `tree_height_low` float DEFAULT NULL,
  `tree_height_high` float DEFAULT NULL,
  `image` longblob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trees`
--

LOCK TABLES `trees` WRITE;
/*!40000 ALTER TABLE `trees` DISABLE KEYS */;
/*!40000 ALTER TABLE `trees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-30 11:57:32
