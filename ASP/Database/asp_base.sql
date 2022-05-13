-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2022 at 03:22 AM
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
CREATE DATABASE IF NOT EXISTS `asp_base` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `asp_base`;

-- --------------------------------------------------------

--
-- Table structure for table `tb_attandance`
--

CREATE TABLE `tb_attandance` (
  `a_Id` int(10) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Surname` varchar(30) NOT NULL,
  `d_Name` varchar(30) NOT NULL,
  `s_Name` varchar(50) NOT NULL,
  `r_Name` varchar(30) NOT NULL,
  `cl_Name` varchar(30) NOT NULL,
  `sc_Period` varchar(30) NOT NULL,
  `sc_Year` varchar(30) NOT NULL,
  `time_In` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_attandance`
--

INSERT INTO `tb_attandance` (`a_Id`, `Name`, `Surname`, `d_Name`, `s_Name`, `r_Name`, `cl_Name`, `sc_Period`, `sc_Year`, `time_In`) VALUES
(1, '2', 'athid', '', '', '', 'vilaisak', '', '', '2022-04-28 06:38:07'),
(2, 'athid', 'vilaisak', '', '', '', 'FCS-AM-135', '', '', '2022-04-28 06:42:19'),
(3, 'athid', 'vilaisuk', '', '', '', 'FCS-AM-135', '', '', '2022-04-28 06:53:13'),
(4, 'phimon', 'soutthipapha', '', '', '', 'FCS-AM-135', '', '', '2022-04-28 06:54:16'),
(5, 'phimon', 'stpp', '', '', '', 'FCS-AM-1359-19', '', '', '2022-05-10 05:58:10'),
(7, 'Souliya', 'Thammavong', 'Monday', 'Python Programing', '309', 'CS6B', 'ເຊົ້າ', '2021-2022', '2022-05-12 17:03:43'),
(8, 'Souliya', 'Thammavong', 'Monday', 'Python Programing', '309', 'CS6B', 'ເຊົ້າ', '2021-2022', '2022-05-13 01:12:07'),
(9, 'Souliya', 'Thammavong', 'Monday', 'Python Programing', '309', 'CS6B', 'ເຊົ້າ', '2021-2022', '2022-05-13 01:14:57');

-- --------------------------------------------------------

--
-- Table structure for table `tb_class`
--

CREATE TABLE `tb_class` (
  `cl_Id` varchar(25) NOT NULL,
  `cl_Name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_class`
--

INSERT INTO `tb_class` (`cl_Id`, `cl_Name`) VALUES
('cl_CS6A', 'CS6A'),
('cl_CS6B', 'CS6B');

-- --------------------------------------------------------

--
-- Table structure for table `tb_day`
--

CREATE TABLE `tb_day` (
  `d_Id` varchar(25) NOT NULL,
  `d_Name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_day`
--

INSERT INTO `tb_day` (`d_Id`, `d_Name`) VALUES
('d_Monday', 'Monday'),
('d_Tuesday', 'Tuesday');

-- --------------------------------------------------------

--
-- Table structure for table `tb_face`
--

CREATE TABLE `tb_face` (
  `f_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Surname` varchar(30) NOT NULL,
  `st_Id` varchar(25) DEFAULT NULL,
  `t_Id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_face`
--

INSERT INTO `tb_face` (`f_Id`, `Name`, `Surname`, `st_Id`, `t_Id`) VALUES
(1, 'dump', 'dump', 'st001', 't001'),
(2, 'Souliya', 'Thammavong', 'st_002', NULL),
(3, 'dummy', 'dummy', NULL, NULL),
(4, 'obama', 'obama', 'st_001', 'None');

-- --------------------------------------------------------

--
-- Table structure for table `tb_room`
--

CREATE TABLE `tb_room` (
  `r_Id` varchar(25) NOT NULL,
  `r_Name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_room`
--

INSERT INTO `tb_room` (`r_Id`, `r_Name`) VALUES
('r_309', '309'),
('r_401', '401');

-- --------------------------------------------------------

--
-- Table structure for table `tb_schedule`
--

CREATE TABLE `tb_schedule` (
  `sc_Id` int(11) NOT NULL,
  `d_Id` varchar(25) NOT NULL,
  `sc_Period` varchar(30) NOT NULL,
  `sc_Year` varchar(30) NOT NULL,
  `r_Id` varchar(25) NOT NULL,
  `s_Id` varchar(50) NOT NULL,
  `cl_Id` varchar(25) NOT NULL,
  `t_Id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_schedule`
--

INSERT INTO `tb_schedule` (`sc_Id`, `d_Id`, `sc_Period`, `sc_Year`, `r_Id`, `s_Id`, `cl_Id`, `t_Id`) VALUES
(0, 'd_Monday', 'ເຊົ້າ', '2021-2022', 'r_309', 's_Python Programing', 'cl_CS6B', 't001'),
(1, 'd_Tuesday', 'ເຊົ້າ', '2021-2022', 'r_401', 's_Java', 'cl_CS6A', 't001');

-- --------------------------------------------------------

--
-- Table structure for table `tb_student`
--

CREATE TABLE `tb_student` (
  `st_Id` varchar(25) NOT NULL,
  `st_Name` varchar(50) NOT NULL,
  `st_Surname` varchar(50) DEFAULT NULL,
  `st_Gender` varchar(10) DEFAULT NULL,
  `cl_Id` varchar(25) DEFAULT NULL,
  `st_DOB` date DEFAULT NULL,
  `st_Tel` int(15) DEFAULT NULL,
  `st_village` varchar(100) DEFAULT NULL,
  `st_district` varchar(100) DEFAULT NULL,
  `st_province` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_student`
--

INSERT INTO `tb_student` (`st_Id`, `st_Name`, `st_Surname`, `st_Gender`, `cl_Id`, `st_DOB`, `st_Tel`, `st_village`, `st_district`, `st_province`) VALUES
('st001', 'nexsiz', 'nexsiz', 'ຍິງ', 'cl_CS6B', '2000-01-01', 2012345687, 'aaaa', 'bbbb', 'cccc'),
('st_001', 'dummy', 'dummy', 'ຊາຍ', 'cl_CS6A', '2001-04-28', 2012345678, 'dummy', 'dummy', 'dummy'),
('st_002', 'Souliya', 'Thammavong', 'ຊາຍ', 'cl_CS6B', '2001-04-28', 2012345678, 'Huaysangao', 'Vangvieng', 'Vientiane');

-- --------------------------------------------------------

--
-- Table structure for table `tb_subject`
--

CREATE TABLE `tb_subject` (
  `s_Id` varchar(50) NOT NULL,
  `s_Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_subject`
--

INSERT INTO `tb_subject` (`s_Id`, `s_Name`) VALUES
('s_Java', 'Java'),
('s_Python Programing', 'Python Programing');

-- --------------------------------------------------------

--
-- Table structure for table `tb_teacher`
--

CREATE TABLE `tb_teacher` (
  `t_Id` varchar(10) NOT NULL,
  `t_Name` varchar(50) NOT NULL,
  `t_Surname` varchar(50) NOT NULL,
  `t_Gender` varchar(10) NOT NULL,
  `t_Village` varchar(50) NOT NULL,
  `t_District` varchar(50) NOT NULL,
  `t_Province` varchar(50) NOT NULL,
  `t_Tel` int(15) NOT NULL,
  `t_Email` varchar(50) NOT NULL,
  `t_Degree` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_teacher`
--

INSERT INTO `tb_teacher` (`t_Id`, `t_Name`, `t_Surname`, `t_Gender`, `t_Village`, `t_District`, `t_Province`, `t_Tel`, `t_Email`, `t_Degree`) VALUES
('t001', 'aaa', 'bbbb', 'ຊາຍ', 'aaaa', 'aaaa', 'aaaa', 204444222, 'ggggg@gmail.com', 'aadsfgs');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_attandance`
--
ALTER TABLE `tb_attandance`
  ADD PRIMARY KEY (`a_Id`);

--
-- Indexes for table `tb_class`
--
ALTER TABLE `tb_class`
  ADD PRIMARY KEY (`cl_Id`);

--
-- Indexes for table `tb_day`
--
ALTER TABLE `tb_day`
  ADD PRIMARY KEY (`d_Id`);

--
-- Indexes for table `tb_face`
--
ALTER TABLE `tb_face`
  ADD PRIMARY KEY (`f_Id`),
  ADD KEY `st_Id` (`st_Id`),
  ADD KEY `t_Id` (`t_Id`);

--
-- Indexes for table `tb_room`
--
ALTER TABLE `tb_room`
  ADD PRIMARY KEY (`r_Id`);

--
-- Indexes for table `tb_schedule`
--
ALTER TABLE `tb_schedule`
  ADD PRIMARY KEY (`sc_Id`),
  ADD KEY `r_Id` (`r_Id`),
  ADD KEY `d_Id` (`d_Id`),
  ADD KEY `t_Id` (`t_Id`),
  ADD KEY `cl_Id` (`cl_Id`),
  ADD KEY `s_Id` (`s_Id`);

--
-- Indexes for table `tb_student`
--
ALTER TABLE `tb_student`
  ADD PRIMARY KEY (`st_Id`),
  ADD KEY `cl_Id` (`cl_Id`);

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

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_attandance`
--
ALTER TABLE `tb_attandance`
  MODIFY `a_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_face`
--
ALTER TABLE `tb_face`
  ADD CONSTRAINT `tb_face_ibfk_1` FOREIGN KEY (`st_Id`) REFERENCES `tb_student` (`st_Id`),
  ADD CONSTRAINT `tb_face_ibfk_2` FOREIGN KEY (`t_Id`) REFERENCES `tb_teacher` (`t_Id`);

--
-- Constraints for table `tb_schedule`
--
ALTER TABLE `tb_schedule`
  ADD CONSTRAINT `tb_schedule_ibfk_1` FOREIGN KEY (`r_Id`) REFERENCES `tb_room` (`r_Id`),
  ADD CONSTRAINT `tb_schedule_ibfk_3` FOREIGN KEY (`d_Id`) REFERENCES `tb_day` (`d_Id`),
  ADD CONSTRAINT `tb_schedule_ibfk_5` FOREIGN KEY (`t_Id`) REFERENCES `tb_teacher` (`t_Id`),
  ADD CONSTRAINT `tb_schedule_ibfk_6` FOREIGN KEY (`cl_Id`) REFERENCES `tb_class` (`cl_Id`),
  ADD CONSTRAINT `tb_schedule_ibfk_7` FOREIGN KEY (`s_Id`) REFERENCES `tb_subject` (`s_Id`);

--
-- Constraints for table `tb_student`
--
ALTER TABLE `tb_student`
  ADD CONSTRAINT `tb_student_ibfk_1` FOREIGN KEY (`cl_Id`) REFERENCES `tb_class` (`cl_Id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
