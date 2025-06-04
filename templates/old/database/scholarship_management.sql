-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 17, 2021 at 09:29 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `scholarship_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_government_scheme`
--

CREATE TABLE `add_government_scheme` (
  `id` int(11) NOT NULL,
  `category` varchar(200) NOT NULL,
  `scheme_name` varchar(200) NOT NULL,
  `scheme_period` varchar(200) NOT NULL,
  `conditions` varchar(200) NOT NULL,
  `required_doc` varchar(200) NOT NULL,
  `rdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `add_government_scheme`
--

INSERT INTO `add_government_scheme` (`id`, `category`, `scheme_name`, `scheme_period`, `conditions`, `required_doc`, `rdate`) VALUES
(2, 'cate', 'schemes', '2 months', 'all eligibil', 'photo,aadhar,voter id', '16-04-21');

-- --------------------------------------------------------

--
-- Table structure for table `add_rural_head`
--

CREATE TABLE `add_rural_head` (
  `id` int(11) NOT NULL,
  `officer_name` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `college` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `rdate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `add_rural_head`
--

INSERT INTO `add_rural_head` (`id`, `officer_name`, `category`, `college`, `contact`, `email`, `address`, `uname`, `pass`, `rdate`) VALUES
(1, 'Cherry', 'health', 'SJT', '9887546598', 'mickey@gmail.com', 'thillai nagar, trichy', 'cherry', '1234', '09-02-21'),
(2, 'Mickey', 'cate', 'BHC', '9876543210', 'mickey@gmail.com', 'thillai nagar, trichy', 'mickey', '1234', '16-04-21');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `user_apply`
--

CREATE TABLE `user_apply` (
  `id` int(11) NOT NULL,
  `app_no` varchar(50) NOT NULL,
  `username` varchar(200) NOT NULL,
  `contact` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `deparment` varchar(200) NOT NULL,
  `scheme_name` varchar(200) NOT NULL,
  `scheme_period` varchar(200) NOT NULL,
  `ac_certi` varchar(200) NOT NULL,
  `instu_id` varchar(200) NOT NULL,
  `aadhar_card1` varchar(200) NOT NULL,
  `aadhar_card2` varchar(100) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `report` varchar(200) NOT NULL,
  `rdate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_apply`
--

INSERT INTO `user_apply` (`id`, `app_no`, `username`, `contact`, `email`, `deparment`, `scheme_name`, `scheme_period`, `ac_certi`, `instu_id`, `aadhar_card1`, `aadhar_card2`, `photo`, `status`, `report`, `rdate`) VALUES
(4, 'APP_NO-5387', 'cherry', '9876543210', 'cherry@gmail.com', 'cate', 'schemes', '2 months', 'big_portfolio_item_5.jpg', 'big_portfolio_item_2.jpg', 'big_portfolio_item_4.jpg', 'big_portfolio_item_7.jpg', 'big_portfolio_item_1.jpg', '0', '0', '16-04-21'),
(5, 'APP_NO-5184', 'cherry', '9876543210', 'cherry@gmail.com', 'health', 'aa', 'bbb', 'g1.jpg', 'g7.jpg', 'g4.jpg', 'g9.jpg', 'client1.jpg', '1', '0', '16-04-21');

-- --------------------------------------------------------

--
-- Table structure for table `user_register`
--

CREATE TABLE `user_register` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  `rdate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_register`
--

INSERT INTO `user_register` (`id`, `name`, `address`, `contact`, `email`, `uname`, `pass`, `status`, `rdate`) VALUES
(1, 'cherry', 'thillai nagar, trichy', '9876543210', 'cherry@gmail.com', 'cherry', '1234', '', '09-02-21');
