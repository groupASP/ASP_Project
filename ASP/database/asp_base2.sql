-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2022 at 01:19 PM
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
-- Table structure for table `attandance`
--

CREATE TABLE `attandance` (
  `ID` int(11) NOT NULL,
  `ENROLLMENT` int(11) NOT NULL,
  `NAME` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Subject` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_class`
--

CREATE TABLE `tb_class` (
  `cl_Id` varchar(10) NOT NULL,
  `cl_Name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_class`
--

INSERT INTO `tb_class` (`cl_Id`, `cl_Name`) VALUES
('aaaa', 'aaaa'),
('cl001', 'CS6B-AM'),
('cl002', 'CS2B-AM');

-- --------------------------------------------------------

--
-- Table structure for table `tb_face`
--

CREATE TABLE `tb_face` (
  `F_ID` int(10) NOT NULL,
  `Name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Surname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `S_ID` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_room`
--

CREATE TABLE `tb_room` (
  `r_Id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `r_Name` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_student`
--

CREATE TABLE `tb_student` (
  `st_Id` varchar(25) NOT NULL,
  `st_Name` varchar(50) NOT NULL,
  `st_Surname` varchar(50) DEFAULT NULL,
  `st_Gender` varchar(10) DEFAULT NULL,
  `st_DOB` date DEFAULT NULL,
  `st_Tel` int(15) DEFAULT NULL,
  `st_village` varchar(100) DEFAULT NULL,
  `st_district` varchar(100) DEFAULT NULL,
  `st_province` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_student`
--

INSERT INTO `tb_student` (`st_Id`, `st_Name`, `st_Surname`, `st_Gender`, `st_DOB`, `st_Tel`, `st_village`, `st_district`, `st_province`) VALUES
('st001', 'ພິມົນ', 'ສຸດທິປະພາ', 'ຍິງ', '2001-08-02', 56626362, 'ໄຮ່', 'ປາກງື່ມ', 'ນະຄອນຫຼວງ'),
('st002', 'ສຸ​ລິ​ຍາ', 'ທຳ​ມະ​ວົງ', 'ຊາຍ', '2001-04-28', 98546712, 'ຫ້ວຍ​ສະ​ເຫງົ້າ', 'ວັງ​ວຽງ', 'ວຽງ​ຈັນ'),
('st003', 'ອາ​ທິດ', 'ວິ​ໄລ​ສັກ', 'ຊາຍ', '1999-11-11', 95647812, 'ແປກ', 'ນ້ຳ​ບາກ', 'ໄຊ​ຍະ​ບູ​ລີ');

-- --------------------------------------------------------

--
-- Table structure for table `tb_subject`
--

CREATE TABLE `tb_subject` (
  `s_Id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `s_Name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_teacher`
--

CREATE TABLE `tb_teacher` (
  `t_Id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `t_Name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `t_Surname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `t_Gender` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `t_Village` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `t_District` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `t_Province` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `t_Tel` int(15) NOT NULL,
  `t_Email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `t_Degree` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attandance`
--
ALTER TABLE `attandance`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `tb_class`
--
ALTER TABLE `tb_class`
  ADD PRIMARY KEY (`cl_Id`);

--
-- Indexes for table `tb_face`
--
ALTER TABLE `tb_face`
  ADD PRIMARY KEY (`F_ID`);

--
-- Indexes for table `tb_room`
--
ALTER TABLE `tb_room`
  ADD PRIMARY KEY (`r_Id`);

--
-- Indexes for table `tb_student`
--
ALTER TABLE `tb_student`
  ADD PRIMARY KEY (`st_Id`);

--
-- Indexes for table `tb_subject`
--
ALTER TABLE `tb_subject`
  ADD PRIMARY KEY (`s_Id`);

--
-- Indexes for table `tb_teacher`
--
ALTER TABLE `tb_teacher`
  ADD PRIMARY KEY (`t_Id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
