-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 02, 2024 at 02:07 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python_digital_gram_panchayat`
--

-- --------------------------------------------------------

--
-- Table structure for table `death_birth_details`
--

CREATE TABLE `death_birth_details` (
  `id` int(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `person_name` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL,
  `cdate` varchar(100) NOT NULL,
  `area` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `death_birth_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `family_members_details`
--

CREATE TABLE `family_members_details` (
  `id` int(100) NOT NULL,
  `family_head_name` varchar(100) NOT NULL,
  `family_head_aadhar_no` varchar(100) NOT NULL,
  `ration_card_no` varchar(100) NOT NULL,
  `family_member_count` varchar(100) NOT NULL,
  `family_members_name` varchar(100) NOT NULL,
  `door_no` varchar(100) NOT NULL,
  `street` varchar(100) NOT NULL,
  `area` varchar(100) NOT NULL,
  `village` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `taluk` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL,
  `area1` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `family_members_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `fine_details`
--

CREATE TABLE `fine_details` (
  `id` int(100) NOT NULL,
  `family_head_name` varchar(100) NOT NULL,
  `fine_regarding` varchar(100) NOT NULL,
  `fine_amount` varchar(100) NOT NULL,
  `fine_date` varchar(100) NOT NULL,
  `pdo` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fine_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `pdo_details`
--

CREATE TABLE `pdo_details` (
  `id` int(100) NOT NULL,
  `pdo_name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pdo_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `scheme_details`
--

CREATE TABLE `scheme_details` (
  `id` int(100) NOT NULL,
  `scheme_name` varchar(100) NOT NULL,
  `scheme_eligibility_criteria` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `govenment` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `scheme_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `service_details`
--

CREATE TABLE `service_details` (
  `id` int(100) NOT NULL,
  `service_name` varchar(100) NOT NULL,
  `service_date` varchar(100) NOT NULL,
  `pdo` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `service_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `user_apply_scheme`
--

CREATE TABLE `user_apply_scheme` (
  `id` int(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `scheme_id` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL,
  `area` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_apply_scheme`
--


-- --------------------------------------------------------

--
-- Table structure for table `user_complaint_details`
--

CREATE TABLE `user_complaint_details` (
  `id` int(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `complaint_description` varchar(100) NOT NULL,
  `complaint_on` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `area` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_complaint_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

