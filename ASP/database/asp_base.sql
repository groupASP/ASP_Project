-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 05, 2022 at 11:50 AM
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
-- Table structure for table `tb_attandance`
--

CREATE TABLE `tb_attandance` (
  `a_Id` int(10) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Surname` varchar(30) NOT NULL,
  `st_Id` varchar(30) NOT NULL,
  `time_In` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_attandance`
--

INSERT INTO `tb_attandance` (`a_Id`, `Name`, `Surname`, `st_Id`, `time_In`) VALUES
(1, '2', 'athid', 'vilaisak', '2022-04-28 06:38:07'),
(2, 'athid', 'vilaisak', 'FCS-AM-135', '2022-04-28 06:42:19'),
(3, 'athid', 'vilaisuk', 'FCS-AM-135', '2022-04-28 06:53:13'),
(4, 'phimon', 'soutthipapha', 'FCS-AM-135', '2022-04-28 06:54:16');

-- --------------------------------------------------------

--
-- Table structure for table `tb_class`
--

CREATE TABLE `tb_class` (
  `cl_Id` int(11) NOT NULL,
  `cl_Name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_class`
--

INSERT INTO `tb_class` (`cl_Id`, `cl_Name`) VALUES
(1, 'CS6B');

-- --------------------------------------------------------

--
-- Table structure for table `tb_face`
--

CREATE TABLE `tb_face` (
  `f_Id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Surname` varchar(30) NOT NULL,
  `st_Id` varchar(30) CHARACTER SET utf8mb4 DEFAULT NULL,
  `t_Id` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_face`
--

INSERT INTO `tb_face` (`f_Id`, `Name`, `Surname`, `st_Id`, `t_Id`) VALUES
(1, '0', '0', 'st001', 't001'),
(2, 'phimon', 'stpp', 'FCS-AM-1359-19', '0'),
(3, 'athid', 'vilaisak', 'FCS-AM-1351-19', '0'),
(4, 'souliya', 'thammavong', 'FCS-AM-1332-19', '0');

-- --------------------------------------------------------

--
-- Table structure for table `tb_room`
--

CREATE TABLE `tb_room` (
  `r_Id` int(10) NOT NULL,
  `r_Name` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tb_room`
--

INSERT INTO `tb_room` (`r_Id`, `r_Name`) VALUES
(1, '309');

-- --------------------------------------------------------

--
-- Table structure for table `tb_schedule`
--

CREATE TABLE `tb_schedule` (
  `sc_Id` int(11) NOT NULL,
  `sc_Day` varchar(30) NOT NULL,
  `sc_Period` varchar(30) NOT NULL,
  `sc_Year` varchar(30) NOT NULL,
  `r_Id` int(10) NOT NULL,
  `s_Id` int(10) NOT NULL,
  `st_Id` varchar(25) NOT NULL,
  `t_Id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `tb_student`
--

CREATE TABLE `tb_student` (
  `st_Id` varchar(25) NOT NULL,
  `st_Name` varchar(50) NOT NULL,
  `st_Surname` varchar(50) DEFAULT NULL,
  `st_Gender` varchar(10) DEFAULT NULL,
  `cl_Id` int(10) DEFAULT NULL,
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
('st001', 'Souliya', 'Thammavong', 'Male', 1, '2001-04-28', 2052013931, 'Huaysangao', 'Vangvieng', 'Vientiane');

-- --------------------------------------------------------

--
-- Table structure for table `tb_subject`
--

CREATE TABLE `tb_subject` (
  `s_Id` int(10) NOT NULL,
  `s_Name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tb_subject`
--

INSERT INTO `tb_subject` (`s_Id`, `s_Name`) VALUES
(1, 'Python programing');

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
-- Indexes for table `tb_face`
--
ALTER TABLE `tb_face`
  ADD PRIMARY KEY (`f_Id`);

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
  ADD KEY `s_Id` (`s_Id`),
  ADD KEY `st_Id` (`st_Id`),
  ADD KEY `t_Id` (`t_Id`);

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
  MODIFY `a_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `tb_class`
--
ALTER TABLE `tb_class`
  MODIFY `cl_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `tb_room`
--
ALTER TABLE `tb_room`
  MODIFY `r_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `tb_schedule`
--
ALTER TABLE `tb_schedule`
  MODIFY `sc_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `tb_subject`
--
ALTER TABLE `tb_subject`
  MODIFY `s_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_schedule`
--
ALTER TABLE `tb_schedule`
  ADD CONSTRAINT `tb_schedule_ibfk_1` FOREIGN KEY (`r_Id`) REFERENCES `tb_room` (`r_Id`),
  ADD CONSTRAINT `tb_schedule_ibfk_2` FOREIGN KEY (`s_Id`) REFERENCES `tb_subject` (`s_Id`),
  ADD CONSTRAINT `tb_schedule_ibfk_3` FOREIGN KEY (`st_Id`) REFERENCES `tb_student` (`st_Id`),
  ADD CONSTRAINT `tb_schedule_ibfk_4` FOREIGN KEY (`t_Id`) REFERENCES `tb_teacher` (`t_Id`);

--
-- Constraints for table `tb_student`
--
ALTER TABLE `tb_student`
  ADD CONSTRAINT `tb_student_ibfk_1` FOREIGN KEY (`cl_Id`) REFERENCES `tb_class` (`cl_Id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
