CREATE DATABASE  IF NOT EXISTS `municipiostcc` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `municipiostcc`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: municipiostcc
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.33-MariaDB

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
-- Temporary view structure for view `matematico`
--

DROP TABLE IF EXISTS `matematico`;
/*!50001 DROP VIEW IF EXISTS `matematico`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `matematico` AS SELECT 
 1 AS `NomeM`,
 1 AS `POP_2010`,
 1 AS `POP_2013`,
 1 AS `POP_2014`,
 1 AS `POP_2015`,
 1 AS `POP_2016`,
 1 AS `QTD_IES`,
 1 AS `IDH_2010`,
 1 AS `GINI_2010`,
 1 AS `PIB_2010`,
 1 AS `PERCAPITA_2010`,
 1 AS `SiglaUF`,
 1 AS `NomeR`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `matematico`
--

/*!50001 DROP VIEW IF EXISTS `matematico`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `matematico` AS select `m`.`NomeM` AS `NomeM`,`m`.`POP_2010` AS `POP_2010`,`m`.`POP_2013` AS `POP_2013`,`m`.`POP_2014` AS `POP_2014`,`m`.`POP_2015` AS `POP_2015`,`m`.`POP_2016` AS `POP_2016`,`m`.`QTD_IES` AS `QTD_IES`,`m`.`IDH_2010` AS `IDH_2010`,`m`.`GINI_2010` AS `GINI_2010`,`m`.`PIB_2010` AS `PIB_2010`,`m`.`PERCAPITA_2010` AS `PERCAPITA_2010`,`u`.`SiglaUF` AS `SiglaUF`,`r`.`NomeR` AS `NomeR` from ((`municipio` `m` join `uf` `u` on((`m`.`UF_idUF` = `u`.`idUF`))) join `regiao` `r` on((`u`.`REGIAO_idREGIAO` = `r`.`idREGIAO`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Dumping events for database 'municipiostcc'
--

--
-- Dumping routines for database 'municipiostcc'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-22 17:34:43
