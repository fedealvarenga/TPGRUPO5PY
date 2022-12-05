CREATE DATABASE  IF NOT EXISTS `Proyecto` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Proyecto`;
-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: Proyecto
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.22.04.1

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
-- Table structure for table `Entradas`
--

DROP TABLE IF EXISTS `Entradas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Entradas` (
  `id_Entrada` int NOT NULL AUTO_INCREMENT,
  `FK_Tipo_Entrada` int NOT NULL,
  `FK_Parque` int NOT NULL,
  `FK_Factura` int NOT NULL,
  `FK_Usuario` int NOT NULL,
  `Fecha` date DEFAULT NULL,
  `Precio` float DEFAULT NULL,
  PRIMARY KEY (`id_Entrada`),
  KEY `fk_Entradas_Tipo_Entrada1_idx` (`FK_Tipo_Entrada`),
  KEY `fk_Entradas_Parques1_idx` (`FK_Parque`),
  KEY `fk_Entradas_Factura1_idx` (`FK_Factura`),
  KEY `fk_Entradas_Usuarios1_idx` (`FK_Usuario`),
  CONSTRAINT `fk_Entradas_Factura1` FOREIGN KEY (`FK_Factura`) REFERENCES `Factura` (`id_Factura`),
  CONSTRAINT `fk_Entradas_Parques1` FOREIGN KEY (`FK_Parque`) REFERENCES `Parques` (`id_Parque`),
  CONSTRAINT `fk_Entradas_Tipo_Entrada1` FOREIGN KEY (`FK_Tipo_Entrada`) REFERENCES `Tipo_Entrada` (`id_Tipo_Entrada`),
  CONSTRAINT `fk_Entradas_Usuarios1` FOREIGN KEY (`FK_Usuario`) REFERENCES `Usuarios` (`id_Usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Entradas`
--

LOCK TABLES `Entradas` WRITE;
/*!40000 ALTER TABLE `Entradas` DISABLE KEYS */;
INSERT INTO `Entradas` VALUES (9,1,1,2,1,'2022-12-06',500),(10,2,1,2,1,'2022-12-06',1000),(11,1,1,3,1,'2022-12-06',500),(12,2,1,3,1,'2022-12-06',1000),(13,2,1,3,1,'2022-12-06',1000),(14,2,1,3,1,'2022-12-06',1000);
/*!40000 ALTER TABLE `Entradas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Factura`
--

DROP TABLE IF EXISTS `Factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Factura` (
  `id_Factura` int NOT NULL AUTO_INCREMENT,
  `FK_Usuario` int NOT NULL,
  `Facturacol` datetime NOT NULL,
  `Total` float DEFAULT NULL,
  PRIMARY KEY (`id_Factura`),
  KEY `fk_Factura_Usuarios1_idx` (`FK_Usuario`),
  CONSTRAINT `fk_Factura_Usuarios1` FOREIGN KEY (`FK_Usuario`) REFERENCES `Usuarios` (`id_Usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Factura`
--

LOCK TABLES `Factura` WRITE;
/*!40000 ALTER TABLE `Factura` DISABLE KEYS */;
INSERT INTO `Factura` VALUES (1,1,'2022-12-05 03:33:42',1000),(2,1,'2022-12-05 03:48:45',1500),(3,1,'2022-12-05 03:50:27',3500);
/*!40000 ALTER TABLE `Factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Parques`
--

DROP TABLE IF EXISTS `Parques`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Parques` (
  `id_Parque` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Ubicacion` varchar(45) DEFAULT NULL,
  `Capacidad_fastpass` int DEFAULT NULL,
  `Capacidad_normal` int DEFAULT NULL,
  PRIMARY KEY (`id_Parque`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Parques`
--

LOCK TABLES `Parques` WRITE;
/*!40000 ALTER TABLE `Parques` DISABLE KEYS */;
INSERT INTO `Parques` VALUES (1,'Magic Kingdom','Florida',5,10),(2,'Animal Kingdom','Florida',5,10),(3,'EPCOT','Florida',5,10),(4,'Hollywood Studios','Florida',5,10);
/*!40000 ALTER TABLE `Parques` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tipo_Entrada`
--

DROP TABLE IF EXISTS `Tipo_Entrada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Entrada` (
  `id_Tipo_Entrada` int NOT NULL AUTO_INCREMENT,
  `Tipo` varchar(45) DEFAULT NULL,
  `Descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_Tipo_Entrada`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Entrada`
--

LOCK TABLES `Tipo_Entrada` WRITE;
/*!40000 ALTER TABLE `Tipo_Entrada` DISABLE KEYS */;
INSERT INTO `Tipo_Entrada` VALUES (1,'normal','normal'),(2,'fast','fast');
/*!40000 ALTER TABLE `Tipo_Entrada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuarios`
--

DROP TABLE IF EXISTS `Usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuarios` (
  `id_Usuario` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Apellido` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Password` varchar(45) DEFAULT NULL,
  `Usuario` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_Usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuarios`
--

LOCK TABLES `Usuarios` WRITE;
/*!40000 ALTER TABLE `Usuarios` DISABLE KEYS */;
INSERT INTO `Usuarios` VALUES (1,'fede','rico','asd@da.com','fede',1),(2,'user1','test','test@test.com','test',1);
/*!40000 ALTER TABLE `Usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-05  1:38:07
