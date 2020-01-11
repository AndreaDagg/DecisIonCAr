-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Gen 11, 2020 alle 14:38
-- Versione del server: 10.1.36-MariaDB
-- Versione PHP: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cars`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `predictions`
--

CREATE TABLE `predictions` (
  `MARCA` varchar(30) COLLATE utf16_unicode_ci DEFAULT NULL,
  `Q1` varchar(30) COLLATE utf16_unicode_ci DEFAULT NULL,
  `Q2` varchar(30) COLLATE utf16_unicode_ci DEFAULT NULL,
  `Q3` tinyint(1) DEFAULT NULL,
  `Q4` varchar(30) COLLATE utf16_unicode_ci DEFAULT NULL,
  `Q5` varchar(30) COLLATE utf16_unicode_ci DEFAULT NULL,
  `Q6` varchar(30) COLLATE utf16_unicode_ci DEFAULT NULL,
  `TIPO` varchar(20) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dump dei dati per la tabella `predictions`
--

INSERT INTO `predictions` (`MARCA`, `Q1`, `Q2`, `Q3`, `Q4`, `Q5`, `Q6`, `TIPO`) VALUES
('nissan Micra', 'C', 'Three', 0, 'POST', 'DIS', 'euro', 'CITY');

-- --------------------------------------------------------

--
-- Struttura della tabella `tablecars`
--

CREATE TABLE `tablecars` (
  `SYMBOL` varchar(9) DEFAULT NULL,
  `MARCA` varchar(31) DEFAULT NULL,
  `CARBURANTE` varchar(10) DEFAULT NULL,
  `COL 4` varchar(11) DEFAULT NULL,
  `PORTE` varchar(5) DEFAULT NULL,
  `COL 6` varchar(8) DEFAULT NULL,
  `COL 7` varchar(9) DEFAULT NULL,
  `COL 8` varchar(9) DEFAULT NULL,
  `COL 9` varchar(7) DEFAULT NULL,
  `COL 10` varchar(4) DEFAULT NULL,
  `COL 11` varchar(8) DEFAULT NULL,
  `CILINDRATA` varchar(10) DEFAULT NULL,
  `COL 13` varchar(7) DEFAULT NULL,
  `CITTA` varchar(8) DEFAULT NULL,
  `TRIP` varchar(13) DEFAULT NULL,
  `PREZZO` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `tablecars`
--

INSERT INTO `tablecars` (`SYMBOL`, `MARCA`, `CARBURANTE`, `COL 4`, `PORTE`, `COL 6`, `COL 7`, `COL 8`, `COL 9`, `COL 10`, `COL 11`, `CILINDRATA`, `COL 13`, `CITTA`, `TRIP`, `PREZZO`) VALUES
('symboling', 'marca', 'carburante', 'aspirazione', 'porte', 'trazione', 'lunghezza', 'larghezza', 'altezza', 'peso', 'cilindri', 'cilindrata', 'cavalli', 'mpgcitta', 'mpgautostrada', 'prezzo'),
('3', 'alfa-romero Giulia Quadrifoglio', 'gas', 'std', '2', 'rwd', '168.8', '64.1', '48.8', '2548', '8', '200', '120', '21', '27', '86495'),
('3', 'alfa-romero Giulia', 'gas', 'std', '2', 'rwd', '168.8', '64.1', '40.8', '2548', '6', '130', '111', '21', '27', '60500'),
('1', 'alfa-romero Stelvio', 'gas', 'std', '2', 'rwd', '171.2', '65.5', '52.4', '2823', '6', '152', '154', '19', '26', '50500'),
('2', 'audi A5', 'gas', 'std', '4', 'rwd', '176.6', '66.2', '54.3', '2337', '4', '109', '102', '24', '30', '45950'),
('2', 'audi A5', 'gas', 'std', '4', 'rwd', '176.6', '66.4', '54.3', '2824', '5', '136', '115', '18', '22', '45450'),
('2', 'audi A3', 'gas', 'std', '2', 'fwd', '177.3', '66.3', '53.1', '2507', '5', '136', '110', '23', '35', '2550'),
('1', 'audi A6', 'gas', 'std', '4', 'fwd', '182.7', '71.4', '40.7', '2844', '6', '136', '110', '19', '25', '57710'),
('1', 'audi A7', 'gas', 'std', '4', 'rwd', '182.7', '71.4', '55.7', '2954', '6', '136', '110', '19', '25', '68920'),
('1', 'audi TT', 'gas', 'turbo', '2', 'rwd', '162.7', '71.4', '40.9', '3086', '5', '131', '140', '17', '20', '73875'),
('0', 'audi A3', 'gas', 'turbo', '2', 'fwd', '168.2', '67.9', '52', '3053', '5', '131', '160', '26', '31', '21000'),
('2', 'bmw 125', 'gas', 'std', '2', 'rwd', '176.8', '64.8', '40.3', '2395', '4', '108', '101', '23', '31', '26430'),
('0', 'bmw 125', 'gas', 'std', '4', 'rwd', '176.8', '64.8', '40.3', '2395', '4', '108', '101', '23', '31', '26925'),
('0', 'bmw M3', 'gas', 'std', '2', 'rwd', '176.8', '64.8', '54.3', '2710', '6', '164', '121', '21', '28', '40970'),
('0', 'bmw M3', 'gas', 'std', '4', 'rwd', '176.8', '64.8', '54.3', '2765', '6', '164', '121', '21', '28', '38105'),
('1', 'bmw Z7', 'gas', 'std', '4', 'rwd', '189', '66.9', '55.7', '3055', '8', '164', '121', '20', '25', '95565'),
('0', 'bmw M5', 'gas', 'std', '4', 'rwd', '189', '66.9', '55.7', '3230', '6', '209', '182', '16', '22', '100760'),
('0', 'bmw serie 8', 'gas', 'std', '2', 'rwd', '193.8', '67.9', '53.7', '3380', '6', '209', '182', '16', '22', '121315'),
('0', 'bmw serie 8 Coupè', 'gas', 'std', '2', 'rwd', '197', '70.9', '56.3', '3505', '6', '209', '182', '15', '20', '136880'),
('2', 'chevrolet spark', 'gas', 'std', '4', 'fwd', '141.1', '60.3', '53.2', '1488', '3', '61', '48', '27', '33', '7151'),
('1', 'chevrolet captiva', 'gas', 'std', '2', 'fwd', '175.9', '63.6', '57', '1874', '4', '90', '70', '28', '33', '15295'),
('0', 'chevrolet cruze', 'gas', 'std', '4', 'fwd', '158.8', '63.6', '52', '1909', '4', '90', '70', '27', '33', '16575'),
('1', 'dodge VIPER', 'gas', 'std', '2', 'fwd', '147.3', '63.8', '50.8', '1876', '6', '119', '148', '14', '23', '85572'),
('1', 'dodge VIPER', 'gas', 'std', '2', 'fwd', '147.3', '63.8', '50.8', '1876', '6', '1199', '128', '14', '23', '96377'),
('1', 'dodge RAM', 'gas', 'turbo', '2', 'fwd', '167.3', '63.8', '57.8', '2128', '4', '98', '102', '21', '25', '57957'),
('1', 'dodge RAM', 'gas', 'std', '4', 'fwd', '177.3', '63.8', '56.6', '1967', '4', '99', '100', '21', '28', '56229'),
('1', 'dodge RAM', 'gas', 'std', '4', 'fwd', '177.3', '63.8', '57.6', '1989', '4', '94', '100', '21', '26', '56692'),
('1', 'dodge CHARGE', 'gas', 'std', '4', 'fwd', '157.3', '63.8', '50.6', '1989', '6', '110', '118', '16', '23', '77609'),
('1', 'dodge CHARGE', 'gas', 'turbo', '4', 'fwd', '157.3', '63.8', '50.6', '2191', '6', '118', '102', '17', '24', '68558'),
('-1', 'dodge CHARGE', 'gas', 'std', '4', 'fwd', '154.6', '64.6', '52.8', '2535', '6', '122', '110', '20', '26', '48921'),
('3', 'dodge DURANGO', 'gas', 'turbo', '4', 'fwd', '180.2', '66.3', '55.2', '2811', '4', '156', '145', '19', '24', '32964'),
('2', 'honda JAZZ', 'gas', 'std', '2', 'fwd', '144.6', '63.9', '50.8', '1713', '4', '92', '58', '32', '32', '8479'),
('2', 'honda JAZZ', 'gas', 'std', '2', 'fwd', '144.6', '63.9', '50.8', '1819', '4', '92', '76', '31', '38', '9855'),
('1', 'honda JAZZ', 'gas', 'std', '4', 'fwd', '150', '64', '52.6', '1837', '4', '79', '60', '38', '32', '9399'),
('1', 'honda JAZZ', 'gas', 'std', '4', 'fwd', '150', '64', '52.6', '1940', '4', '92', '76', '30', '34', '9529'),
('1', 'honda JAZZ', 'gas', 'std', '4', 'fwd', '150', '64', '52.6', '1956', '4', '92', '76', '30', '34', '9129'),
('0', 'honda CIVIC', 'gas', 'std', '4', 'fwd', '173.4', '64', '54.5', '2010', '4', '92', '76', '27', '32', '27295'),
('0', 'honda CIVIC', 'gas', 'std', '4', 'fwd', '177.1', '63.9', '55.3', '2024', '4', '92', '76', '26', '32', '27295'),
('0', 'honda CIVIC', 'gas', 'std', '2', 'fwd', '169.5', '65.2', '54.3', '2236', '4', '110', '86', '27', '33', '27895'),
('0', 'honda CIVIC', 'gas', 'std', '2', 'fwd', '169.5', '65.2', '54.3', '2289', '4', '110', '86', '27', '33', '29095'),
('0', 'honda CRV', 'gas', 'std', '4', 'fwd', '175.4', '65.2', '55.1', '2304', '4', '110', '86', '27', '33', '28845'),
('0', 'honda CRV', 'gas', 'std', '4', 'fwd', '175.4', '62.5', '55.1', '2372', '4', '110', '86', '27', '33', '29295'),
('0', 'honda CRV', 'gas', 'std', '4', 'fwd', '175.4', '65.2', '55.1', '2465', '4', '110', '95', '24', '28', '22945'),
('1', 'honda CRV', 'gas', 'std', '4', 'fwd', '169.1', '66', '55', '2293', '4', '110', '95', '25', '31', '30345'),
('0', 'isuzu D-Max', 'gas', 'std', '4', 'rwd', '170.7', '61.8', '56.5', '2337', '4', '111', '78', '24', '27', '2785'),
('1', 'isuzu D-Max', 'gas', 'std', '2', 'fwd', '185.9', '63.6', '56', '1874', '4', '90', '70', '24', '27', '21000'),
('0', 'isuzu D-Max', 'gas', 'std', '4', 'fwd', '185.9', '63.6', '56', '1909', '4', '90', '70', '24', '27', '21000'),
('2', 'isuzu D-Max', 'gas', 'std', '2', 'rwd', '172.6', '65.2', '56.4', '2734', '4', '119', '90', '24', '28', '21048'),
('0', 'jaguar XF', 'gas', 'std', '4', 'rwd', '189.6', '69.6', '52.8', '4066', '6', '258', '176', '13', '29', '62250'),
('0', 'jaguar XF', 'gas', 'std', '4', 'rwd', '189.6', '69.6', '52.8', '4066', '6', '258', '176', '13', '26', '65550'),
('0', 'jaguar F-Type', 'gas', 'std', '2', 'rwd', '191.7', '70.6', '47.8', '3950', '8', '326', '262', '13', '27', '66000'),
('1', 'mazda 2', 'gas', 'std', '2', 'fwd', '155.1', '64.2', '54.1', '1890', '4', '91', '68', '25', '28', '15195'),
('1', 'mazda 2', 'gas', 'std', '2', 'fwd', '156.1', '64.2', '54.1', '1900', '4', '91', '68', '25', '28', '16095'),
('1', 'mazda 2', 'gas', 'std', '2', 'fwd', '154.1', '64.2', '54.1', '1905', '4', '91', '68', '25', '28', '16795'),
('1', 'mazda 2', 'gas', 'std', '4', 'fwd', '156.8', '64.2', '54.1', '1945', '4', '91', '68', '25', '28', '16695'),
('1', 'mazda 2', 'gas', 'std', '4', 'fwd', '156.8', '64.2', '54.1', '1950', '4', '91', '68', '25', '28', '17395'),
('3', 'mazda Rx', 'gas', 'std', '2', 'rwd', '169', '65.7', '49.6', '2380', '4', '70', '101', '17', '25', '40945'),
('3', 'mazda Rx', 'gas', 'std', '2', 'rwd', '169', '65.7', '49.6', '2380', '4', '70', '101', '17', '25', '41845'),
('3', 'mazda Rx', 'gas', 'std', '2', 'rwd', '169', '65.7', '49.6', '2385', '4', '70', '101', '17', '25', '43645'),
('3', 'mazda Rx', 'gas', 'std', '2', 'rwd', '169', '65.7', '49.6', '2500', '4', '80', '135', '17', '25', '45645'),
('1', 'mazda 3', 'gas', 'std', '2', 'fwd', '177.8', '66.5', '53.7', '2385', '4', '122', '84', '26', '32', '8845'),
('0', 'mazda 3', 'gas', 'std', '4', 'fwd', '177.8', '66.5', '55.5', '2410', '4', '122', '84', '26', '32', '8495'),
('1', 'mazda 3', 'gas', 'std', '2', 'fwd', '177.8', '66.5', '53.7', '2385', '4', '122', '84', '26', '32', '10595'),
('0', 'mazda 3', 'gas', 'std', '4', 'fwd', '177.8', '66.5', '55.5', '2410', '4', '122', '84', '26', '32', '10245'),
('0', 'mazda 3', 'diesel', 'std', '4', 'fwd', '177.8', '66.5', '55.5', '2443', '4', '122', '64', '36', '42', '10795'),
('0', 'mazda 3', 'gas', 'std', '4', 'fwd', '177.8', '66.5', '55.5', '2425', '4', '122', '84', '26', '32', '11245'),
('0', 'mazda Rx', 'gas', 'std', '4', 'rwd', '175', '66.1', '54.4', '2670', '4', '140', '120', '17', '27', '38280'),
('0', 'mazda 2', 'diesel', 'std', '2', 'rwd', '155', '66.1', '54.4', '2700', '4', '134', '72', '20', '25', '18344'),
('-1', 'mercedes-benz Classe A', 'diesel', 'turbo', '4', 'rwd', '190.9', '70.3', '56.5', '3515', '5', '183', '100', '29', '32', '25552'),
('-1', 'mercedes-benz GLA', 'diesel', 'turbo', '4', 'rwd', '190.9', '70.3', '58.7', '3750', '5', '183', '100', '22', '29', '48248'),
('0', 'mercedes-benz GLA', 'diesel', 'turbo', '4', 'rwd', '187.5', '70.3', '58.9', '3495', '5', '183', '100', '22', '29', '48176'),
('-1', 'mercedes-benz GLA', 'diesel', 'turbo', '4', 'rwd', '202.6', '71.7', '58.3', '3770', '5', '183', '123', '22', '29', '41600'),
('-1', 'mercedes-benz AMG GT', 'gas', 'std', '4', 'rwd', '155.6', '71.7', '56.5', '3740', '8', '234', '155', '17', '25', '104184'),
('3', 'mercedes-benz AMG GT', 'gas', 'std', '2', 'rwd', '115.3', '70.5', '50.8', '3685', '8', '234', '155', '17', '26', '105056'),
('0', 'mercedes-benz AMG GT', 'gas', 'std', '2', 'rwd', '155.1', '71.7', '56.7', '3900', '8', '308', '184', '17', '26', '100960'),
('1', 'mercedes-benz AMG GT', 'gas', 'std', '2', 'rwd', '155.2', '72', '25.4', '3715', '8', '304', '184', '17', '26', '105400'),
('1', 'Fiat Panda', 'gas', 'turbo', '4', 'rwd', '159.4', '68', '55.8', '2910', '4', '140', '90', '29', '32', '9503'),
('2', 'mitsubishi Space', 'gas', 'std', '4', 'fwd', '152.3', '64.4', '52.8', '1918', '4', '70', '68', '26', '32', '9389'),
('2', 'mitsubishi Space', 'gas', 'std', '4', 'fwd', '153.3', '64.4', '52.8', '1944', '4', '70', '68', '26', '32', '9189'),
('2', 'mitsubishi Space', 'gas', 'std', '4', 'fwd', '153.3', '64.4', '53.8', '2004', '4', '70', '68', '26', '32', '9669'),
('1', 'mitsubishi L200', 'gas', 'turbo', '2', 'fwd', '177.3', '63.8', '55.8', '2145', '4', '98', '96', '24', '30', '27689'),
('3', 'mitsubishi L200', 'gas', 'turbo', '2', 'fwd', '173', '65.4', '55.4', '2370', '4', '110', '96', '23', '30', '29959'),
('3', 'mitsubishi L200', 'gas', 'std', '2', 'fwd', '173', '65.4', '55.4', '2328', '4', '122', '97', '25', '32', '28499'),
('3', 'mitsubishi L200', 'gas', 'turbo', '2', 'fwd', '173.2', '66.3', '55.2', '2833', '4', '156', '100', '23', '24', '22629'),
('3', 'mitsubishi L200', 'gas', 'turbo', '2', 'fwd', '173.2', '66.3', '55.2', '2921', '4', '156', '100', '23', '24', '24869'),
('3', 'mitsubishi L200', 'gas', 'turbo', '2', 'fwd', '173.2', '66.3', '55.2', '2926', '4', '156', '100', '23', '24', '24489'),
('1', 'mitsubishi Eclipse', 'gas', 'std', '4', 'fwd', '172.4', '65.4', '55.6', '2365', '4', '122', '88', '25', '32', '26989'),
('1', 'mitsubishi Eclipse', 'gas', 'std', '4', 'fwd', '172.4', '65.4', '55.6', '2405', '4', '122', '88', '25', '32', '28189'),
('1', 'mitsubishi Eclipse', 'gas', 'turbo', '4', 'fwd', '172.4', '65.4', '55.6', '2403', '4', '110', '92', '23', '30', '23279'),
('-1', 'mitsubishi Eclipse', 'gas', 'std', '4', 'fwd', '172.4', '65.4', '55.6', '2403', '4', '110', '92', '23', '30', '23979'),
('1', 'nissan Leaf', 'gas', 'std', '4', 'fwd', '165.3', '63.8', '54.5', '1889', '4', '100', '69', '21', '37', '35499'),
('1', 'nissan Micra', 'diesel', 'std', '2', 'fwd', '155.3', '63.8', '54.5', '2017', '4', '91', '55', '29', '35', '9099'),
('1', 'nissan Micra', 'gas', 'std', '4', 'fwd', '155.3', '63.8', '54.5', '1918', '4', '97', '69', '29', '35', '9649'),
('1', 'nissan Leaf', 'gas', 'std', '4', 'fwd', '165.3', '63.8', '54.5', '1938', '4', '97', '69', '31', '37', '36849'),
('1', 'nissan Qashqai ', 'gas', 'std', '4', 'fwd', '170.2', '63.8', '56.5', '2024', '4', '97', '90', '27', '27', '27349'),
('1', 'nissan Leaf', 'gas', 'std', '4', 'fwd', '165.3', '63.8', '54.5', '1951', '4', '97', '69', '23', '23', '37299'),
('1', 'nissan Leaf', 'gas', 'std', '4', 'fwd', '165.6', '63.8', '53.3', '2028', '4', '97', '69', '23', '23', '37799'),
('1', 'nissan Leaf', 'gas', 'std', '4', 'fwd', '165.3', '63.8', '54.5', '1971', '4', '97', '69', '23', '23', '37499'),
('1', 'nissan Qashqai ', 'gas', 'std', '4', 'fwd', '170.2', '63.8', '56.5', '2037', '4', '97', '90', '25', '27', '27999'),
('2', 'nissan Leaf', 'gas', 'std', '4', 'fwd', '162.4', '63.8', '54', '2008', '4', '97', '69', '23', '23', '38249'),
('0', 'nissan Qashqai ', 'gas', 'std', '4', 'fwd', '173.4', '65.2', '55.7', '2324', '4', '120', '90', '25', '30', '28949'),
('0', 'nissan Qashqai ', 'gas', 'std', '4', 'fwd', '173.4', '65.2', '55.7', '2302', '4', '120', '90', '25', '30', '29549'),
('0', 'nissan X-Trail', 'gas', 'std', '4', 'fwd', '181.7', '66.5', '56.1', '3095', '4', '181', '91', '26', '31', '23499'),
('0', 'nissan X-Trail', 'gas', 'std', '4', 'fwd', '184.6', '66.5', '56.1', '3296', '4', '181', '91', '26', '31', '24399'),
('0', 'nissan X-Trail', 'gas', 'std', '4', 'fwd', '184.6', '66.5', '56.1', '3060', '4', '181', '91', '26', '31', '23499'),
('3', 'nissan Qashqai ', 'gas', 'std', '4', 'rwd', '170.7', '67.9', '55.7', '3071', '4', '181', '90', '25', '31', '21199'),
('3', 'nissan Qashqai ', 'gas', 'turbo', '4', 'rwd', '170.7', '67.9', '56.7', '3139', '4', '181', '90', '25', '31', '21699'),
('1', 'nissan GTR', 'gas', 'std', '2', 'rwd', '168.5', '67.9', '49.7', '3139', '6', '181', '110', '15', '24', '108399'),
('0', 'peugot 208', 'gas', 'std', '4', 'rwd', '166.7', '68.4', '56.7', '3020', '4', '120', '92', '24', '29', '11900'),
('0', 'peugot 3008', 'diesel', 'turbo', '4', 'rwd', '186.7', '68.4', '56.7', '3197', '4', '152', '95', '25', '33', '23200'),
('0', 'peugot 3008', 'gas', 'std', '4', 'rwd', '198.9', '68.4', '58.7', '3230', '4', '120', '97', '25', '24', '22440'),
('0', 'peugot 3008', 'diesel', 'turbo', '4', 'rwd', '198.9', '68.4', '58.7', '3430', '4', '152', '95', '25', '25', '23860'),
('0', 'peugot 508', 'gas', 'std', '4', 'rwd', '186.7', '68.4', '56.7', '3075', '4', '120', '95', '24', '32', '35580'),
('0', 'peugot 508', 'diesel', 'turbo', '4', 'rwd', '186.7', '68.4', '56.7', '3252', '4', '152', '95', '28', '33', '36900'),
('0', 'peugot 3008', 'gas', 'std', '4', 'rwd', '198.9', '68.4', '56.7', '3285', '4', '120', '95', '24', '32', '26695'),
('0', 'peugot 3008', 'diesel', 'turbo', '4', 'rwd', '198.9', '68.4', '58.7', '3485', '4', '152', '95', '25', '25', '27075'),
('0', 'peugot 508', 'gas', 'std', '4', 'rwd', '186.7', '68.4', '56.7', '3075', '4', '120', '97', '24', '24', '36630'),
('0', 'peugot 508', 'diesel', 'turbo', '4', 'rwd', '186.7', '68.4', '56.7', '3252', '4', '152', '95', '28', '33', '37950'),
('0', 'peugot 508', 'gas', 'turbo', '4', 'rwd', '186.7', '68.3', '56', '3130', '4', '134', '92', '28', '33', '38150'),
('3', 'porsche Cayenne', 'gas', 'std', '4', 'rwd', '188.9', '68.3', '56.2', '2778', '4', '151', '143', '17', '28', '92018'),
('3', 'porsche Cayenne', 'gas', 'std', '4', 'rwd', '188.9', '65', '56.6', '2756', '6', '194', '207', '17', '25', '92528'),
('3', 'porsche 911 Coupè', 'gas', 'std', '2', 'rwd', '168.9', '65', '51.6', '2756', '6', '194', '207', '12', '23', '134028'),
('3', 'porsche 911', 'gas', 'std', '2', 'rwd', '168.9', '65', '51.6', '2800', '6', '194', '207', '12', '23', '137028'),
('1', 'porsche 911 S', 'gas', 'std', '2', 'rwd', '165.7', '72.3', '50.5', '3366', '8', '203', '288', '12', '24', '151000'),
('0', 'renault Clio', 'gas', 'std', '4', 'fwd', '161.5', '66.5', '55.2', '2579', '4', '132', '92', '23', '38', '16295'),
('2', 'renault Twingo', 'gas', 'std', '2', 'fwd', '156.8', '66.6', '50.5', '2460', '4', '132', '64', '30', '33', '10895'),
('3', 'saab 9-3', 'gas', 'std', '2', 'fwd', '166.6', '66.5', '56.1', '2658', '4', '121', '110', '21', '28', '11850'),
('2', 'saab 9-3', 'gas', 'std', '4', 'fwd', '166.6', '66.5', '56.1', '2695', '4', '121', '110', '21', '28', '12170'),
('3', 'saab 9-5', 'gas', 'std', '2', 'fwd', '186.6', '66.5', '56.1', '2707', '4', '121', '110', '21', '28', '25040'),
('2', 'saab 9-5W', 'gas', 'std', '4', 'fwd', '186.6', '66.5', '56.1', '2758', '6', '121', '110', '21', '28', '25510'),
('3', 'saab 9-4X', 'gas', 'turbo', '2', 'fwd', '184.6', '66.5', '58.1', '2808', '4', '121', '160', '19', '26', '28150'),
('2', 'saab 9-4X', 'gas', 'turbo', '4', 'fwd', '184.6', '66.5', '58.1', '2847', '6', '121', '160', '19', '26', '28620'),
('2', 'subaru Forester', 'gas', 'std', '2', 'fwd', '186.9', '63.4', '58.7', '2050', '4', '97', '89', '31', '36', '45118'),
('2', 'subaru Forester', 'gas', 'std', '2', 'fwd', '187.9', '63.6', '58.7', '2120', '6', '108', '83', '26', '31', '47053'),
('2', 'subaru XV', 'gas', 'std', '2', 'rwd', '157.3', '63.8', '55.7', '2240', '4', '108', '73', '26', '31', '27603'),
('0', 'subaru Levorg', 'gas', 'std', '4', 'fwd', '172', '65.4', '51.5', '2145', '6', '108', '82', '32', '37', '37126'),
('0', 'subaru Levorg', 'gas', 'std', '4', 'fwd', '172', '65.4', '51.5', '2190', '4', '108', '82', '28', '33', '37775'),
('0', 'subaru WRX', 'gas', 'std', '4', 'fwd', '163', '65.4', '52.5', '2340', '8', '108', '94', '20', '32', '49960'),
('0', 'subaru XV', 'gas', 'std', '4', 'rwd', '172', '65.4', '54.3', '2385', '4', '108', '82', '24', '25', '29233'),
('0', 'subaru WRX', 'gas', 'turbo', '4', 'rwd', '163', '65.4', '52.3', '2510', '4', '108', '111', '20', '31', '41259'),
('0', 'subaru Levorg', 'gas', 'std', '4', 'fwd', '173.5', '65.4', '53', '2290', '4', '108', '82', '28', '32', '31463'),
('0', 'subaru WRX', 'gas', 'std', '4', 'fwd', '163.5', '65.4', '53', '2455', '8', '108', '94', '20', '31', '40198'),
('0', 'subaru XV', 'gas', 'std', '4', 'rwd', '153.6', '65.4', '56.9', '2420', '4', '108', '82', '23', '29', '28013'),
('0', 'subaru WRX', 'gas', 'turbo', '4', 'rwd', '173.6', '65.4', '52.9', '2650', '4', '108', '111', '20', '25', '41694'),
('1', 'toyota AYGO', 'gas', 'std', '2', 'fwd', '156.7', '63.6', '54.5', '1985', '4', '92', '62', '35', '39', '15348'),
('1', 'toyota AYGO', 'gas', 'std', '2', 'fwd', '156.7', '63.6', '54.5', '2040', '4', '92', '62', '31', '38', '16338'),
('1', 'toyota AYGO', 'gas', 'std', '4', 'fwd', '156.7', '63.6', '54.5', '2015', '4', '92', '62', '31', '38', '16488'),
('0', 'toyota AYGO', 'gas', 'std', '4', 'fwd', '155.7', '63.6', '54.1', '2280', '4', '92', '62', '31', '37', '16918'),
('0', 'toyota TRUCK', 'gas', 'std', '4', 'rwd', '174.7', '63.6', '59.1', '2290', '4', '92', '108', '19', '28', '47898'),
('0', 'toyota TRUCK', 'gas', 'std', '4', 'rwd', '174.7', '63.6', '59.1', '3110', '4', '92', '107', '21', '28', '38778'),
('0', 'toyota Yaris', 'gas', 'std', '4', 'fwd', '146.3', '61.4', '53', '2081', '4', '92', '70', '30', '37', '16938'),
('0', 'toyota Yaris', 'gas', 'std', '4', 'fwd', '156.3', '62.4', '52.8', '2109', '4', '90', '70', '30', '37', '17198'),
('0', 'toyota Yaris', 'diesel', 'std', '4', 'fwd', '146.3', '62.4', '53', '2275', '4', '90', '56', '34', '36', '17898'),
('0', 'toyota Yaris', 'diesel', 'std', '4', 'fwd', '156.3', '64.4', '52.8', '2275', '4', '90', '56', '38', '47', '17788'),
('0', 'toyota Yaris', 'gas', 'std', '4', 'fwd', '146.3', '61.4', '53', '2094', '4', '92', '70', '38', '47', '17738'),
('0', 'toyota C-HR', 'gas', 'std', '4', 'fwd', '166.3', '64.4', '53.8', '2122', '4', '95', '70', '28', '34', '33358'),
('0', 'toyota C-HR', 'gas', 'std', '4', 'fwd', '166.3', '64.4', '53.8', '2140', '4', '96', '70', '28', '34', '32258'),
('1', 'toyota C-HR', 'gas', 'std', '4', 'rwd', '168.7', '64', '53.6', '2169', '4', '96', '70', '29', '34', '31058'),
('1', 'toyota C-HR', 'gas', 'std', '4', 'rwd', '168.7', '64', '53.6', '2204', '4', '96', '70', '29', '34', '31238'),
('1', 'toyota C-HR', 'gas', 'std', '4', 'rwd', '168.7', '64', '53.6', '2265', '4', '95', '82', '26', '29', '35298'),
('1', 'toyota C-HR', 'gas', 'std', '4', 'rwd', '168.7', '64', '53.6', '2300', '4', '94', '80', '26', '29', '31538'),
('2', 'toyota RAV-4', 'gas', 'std', '4', 'rwd', '176.2', '65.6', '55', '2540', '4', '104', '100', '24', '30', '38449'),
('2', 'toyota RAV-4', 'gas', 'std', '4', 'rwd', '176.2', '65.6', '56', '2536', '4', '104', '100', '24', '30', '39639'),
('2', 'toyota RAV-4', 'gas', 'std', '4', 'rwd', '176.2', '65.6', '55', '2551', '4', '104', '100', '24', '30', '39989'),
('2', 'toyota RAV-4', 'gas', 'std', '4', 'rwd', '176.2', '65.6', '56', '2679', '4', '104', '100', '24', '30', '34199'),
('2', 'toyota RAV-4', 'gas', 'std', '4', 'rwd', '176.2', '65.6', '55', '2714', '4', '104', '100', '24', '30', '34549'),
('2', 'toyota RAV-4', 'gas', 'std', '4', 'rwd', '176.2', '65.6', '56', '2975', '4', '104', '100', '24', '30', '37669'),
('-1', 'toyota ES', 'gas', 'std', '4', 'fwd', '175.6', '66.5', '54.9', '2326', '4', '102', '100', '24', '34', '58948'),
('-1', 'toyota ES', 'diesel', 'turbo', '4', 'fwd', '175.6', '66.5', '54.9', '2480', '4', '110', '103', '26', '33', '50698'),
('-1', 'toyota IS', 'gas', 'std', '4', 'fwd', '175.6', '66.5', '53.9', '2414', '4', '99', '92', '27', '32', '49889'),
('-1', 'toyota IS', 'gas', 'std', '4', 'fwd', '175.6', '66.5', '54.9', '2414', '4', '98', '92', '27', '32', '40898'),
('-1', 'toyota IS', 'gas', 'std', '4', 'fwd', '175.6', '66.5', '53.9', '2458', '4', '97', '92', '27', '32', '41248'),
('3', 'toyota LEXUS', 'gas', 'std', '4', 'rwd', '183.5', '67.7', '56', '2976', '6', '110', '100', '20', '24', '46558'),
('3', 'toyota LEXUS', 'gas', 'std', '4', 'rwd', '183.5', '67.7', '55', '3016', '6', '110', '100', '19', '24', '45998'),
('-1', 'toyota LEXUS', 'gas', 'std', '4', 'rwd', '187.8', '66.5', '55.1', '3131', '6', '110', '100', '20', '24', '45690'),
('-1', 'toyota LEXUS', 'gas', 'std', '4', 'rwd', '187.8', '66.5', '56.1', '3151', '6', '110', '100', '19', '24', '45750'),
('2', 'volkswagen Polo', 'diesel', 'std', '2', 'fwd', '171.7', '65.5', '55.7', '2261', '4', '97', '52', '27', '30', '17775'),
('2', 'volkswagen Golf', 'gas', 'std', '2', 'fwd', '171.7', '65.5', '55.7', '2209', '4', '109', '85', '22', '27', '27975'),
('2', 'volkswagen Polo', 'diesel', 'std', '4', 'fwd', '171.7', '65.5', '55.7', '2264', '4', '97', '52', '27', '30', '17995'),
('2', 'volkswagen Golf', 'gas', 'std', '4', 'fwd', '171.7', '65.5', '55.7', '2212', '4', '109', '95', '22', '27', '28195'),
('2', 'volkswagen Tiguan', 'gas', 'std', '4', 'fwd', '171.7', '65.5', '59.7', '2275', '4', '109', '100', '27', '34', '38495'),
('2', 'volkswagen Polo', 'diesel', 'turbo', '4', 'fwd', '171.7', '65.5', '55.7', '2319', '4', '97', '68', '27', '30', '19495'),
('2', 'volkswagen Golf', 'gas', 'std', '4', 'fwd', '171.7', '65.5', '55.7', '2300', '4', '109', '100', '22', '27', '29995'),
('3', 'volkswagen Tiguan', 'gas', 'std', '4', 'fwd', '169.3', '64.2', '58.6', '2254', '4', '109', '100', '24', '28', '31595'),
('3', 'volkswagen Tiguan', 'gas', 'std', '4', 'fwd', '169.7', '64', '58.4', '2221', '4', '109', '100', '24', '29', '31980'),
('0', 'volkswagen Passat', 'gas', 'std', '4', 'fwd', '180.2', '66.9', '55.1', '2661', '5', '136', '110', '22', '27', '33295'),
('0', 'volkswagen Passat', 'diesel', 'turbo', '4', 'fwd', '180.2', '66.9', '55.1', '2579', '4', '97', '68', '23', '28', '33845'),
('0', 'volkswagen Passat', 'gas', 'std', '4', 'fwd', '183.1', '66.9', '55.1', '2563', '4', '109', '88', '25', '30', '32290'),
('-2', 'volvo XC40', 'gas', 'std', '4', 'rwd', '188.8', '67.2', '56.2', '2912', '4', '141', '114', '23', '28', '32940'),
('-1', 'volvo XC60', 'gas', 'std', '4', 'rwd', '188.8', '67.2', '57.5', '3034', '4', '141', '114', '23', '28', '35415'),
('-2', 'volvo XC40', 'gas', 'std', '4', 'rwd', '188.8', '67.2', '56.2', '2935', '4', '141', '114', '24', '28', '35985'),
('-1', 'volvo XC60', 'gas', 'std', '4', 'rwd', '188.8', '67.2', '57.5', '3042', '4', '141', '114', '24', '28', '41515'),
('-2', 'volvo XC60', 'gas', 'turbo', '4', 'rwd', '188.8', '67.2', '56.2', '3045', '4', '130', '162', '17', '25', '41515'),
('-1', 'volvo XC40', 'gas', 'turbo', '4', 'rwd', '188.8', '67.2', '57.5', '3157', '4', '130', '162', '17', '25', '32950'),
('-1', 'volvo V60', 'gas', 'std', '4', 'rwd', '190.8', '68.9', '55.5', '2952', '4', '141', '114', '23', '32', '36845'),
('-1', 'volvo V60', 'gas', 'turbo', '4', 'rwd', '190.8', '68.8', '55.5', '3049', '4', '141', '160', '28', '32', '39045'),
('-1', 'volvo V90', 'gas', 'std', '4', 'rwd', '198.8', '68.9', '55.5', '3012', '6', '173', '134', '29', '32', '51485'),
('-1', 'volvo V40', 'diesel', 'turbo', '4', 'rwd', '188.8', '68.9', '55.5', '3217', '6', '145', '106', '25', '30', '22470'),
('-1', 'volvo v40', 'gas', 'turbo', '4', 'rwd', '188.8', '68.9', '55.5', '3062', '4', '141', '114', '25', '30', '22625');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
