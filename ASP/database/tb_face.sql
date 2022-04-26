-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 26, 2022 at 11:05 AM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 7.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `asp_base`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_face`
--

CREATE TABLE `tb_face` (
  `f_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Surname` varchar(30) NOT NULL,
  `st_Id` varchar(10) CHARACTER SET utf8mb4 DEFAULT NULL,
  `t_Id` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_face`
--
ALTER TABLE `tb_face`
  ADD PRIMARY KEY (`f_Id`),
  ADD KEY `st_Id` (`st_Id`),
  ADD KEY `t_Id` (`t_Id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_face`
--
ALTER TABLE `tb_face`
  ADD CONSTRAINT `tb_face_ibfk_1` FOREIGN KEY (`st_Id`) REFERENCES `tb_student` (`st_Id`),
  ADD CONSTRAINT `tb_face_ibfk_2` FOREIGN KEY (`t_Id`) REFERENCES `tb_teacher` (`t_Id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
