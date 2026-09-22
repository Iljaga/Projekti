-- --------------------------------------------------------
-- Verkkotietokone:              127.0.0.1
-- Palvelinversio:               12.3.3-MariaDB - MariaDB Server
-- Server OS:                    Win64
-- HeidiSQL Versio:              12.20.0.7320
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for flight_game
DROP DATABASE IF EXISTS `flight_game`;
CREATE DATABASE IF NOT EXISTS `flight_game` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci */;
USE `flight_game`;

-- Dumping structure for taulu flight_game.airport
DROP TABLE IF EXISTS `airport`;
CREATE TABLE IF NOT EXISTS `airport` (
  `id` int(11) NOT NULL,
  `ident` varchar(40) NOT NULL,
  `type` varchar(40) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `latitude_deg` double DEFAULT NULL,
  `longitude_deg` double DEFAULT NULL,
  `elevation_ft` int(11) DEFAULT NULL,
  `continent` varchar(40) DEFAULT NULL,
  `iso_country` varchar(40) DEFAULT NULL,
  `iso_region` varchar(40) DEFAULT NULL,
  `municipality` varchar(40) DEFAULT NULL,
  `scheduled_service` varchar(40) DEFAULT NULL,
  `gps_code` varchar(40) DEFAULT NULL,
  `iata_code` varchar(40) DEFAULT NULL,
  `local_code` varchar(40) DEFAULT NULL,
  `home_link` varchar(40) DEFAULT NULL,
  `wikipedia_link` varchar(40) DEFAULT NULL,
  `keywords` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ident`),
  KEY `iso_country` (`iso_country`),
  CONSTRAINT `airport_ibfk_1` FOREIGN KEY (`iso_country`) REFERENCES `country` (`iso_country`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.country
DROP TABLE IF EXISTS `country`;
CREATE TABLE IF NOT EXISTS `country` (
  `iso_country` varchar(40) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `continent` varchar(40) DEFAULT NULL,
  `wikipedia_link` varchar(40) DEFAULT NULL,
  `keywords` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`iso_country`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.game
DROP TABLE IF EXISTS `game`;
CREATE TABLE IF NOT EXISTS `game` (
  `id` varchar(40) NOT NULL,
  `co2_consumed` int(8) DEFAULT NULL,
  `co2_budget` int(8) DEFAULT NULL,
  `location` varchar(10) DEFAULT NULL,
  `screen_name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `location` (`location`),
  CONSTRAINT `game_ibfk_1` FOREIGN KEY (`location`) REFERENCES `airport` (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.goal
DROP TABLE IF EXISTS `goal`;
CREATE TABLE IF NOT EXISTS `goal` (
  `id` int(11) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `icon` varchar(8) DEFAULT NULL,
  `target` varchar(40) DEFAULT NULL,
  `target_minvalue` decimal(8,2) DEFAULT NULL,
  `target_maxvalue` decimal(8,2) DEFAULT NULL,
  `target_text` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.goal_reached
DROP TABLE IF EXISTS `goal_reached`;
CREATE TABLE IF NOT EXISTS `goal_reached` (
  `game_id` varchar(40) NOT NULL,
  `goal_id` int(11) NOT NULL,
  PRIMARY KEY (`game_id`,`goal_id`),
  KEY `goalid` (`goal_id`),
  CONSTRAINT `goal_reached_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `goal_reached_ibfk_2` FOREIGN KEY (`goal_id`) REFERENCES `goal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
