-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 15, 2026 at 12:23 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`id`, `message`) VALUES
(1, 'Gram Sabha meeting on the first Saturday of every month at 10 AM.'),
(2, 'Water supply will be off on Sunday for tank cleaning.'),
(3, 'Last date to pay the property tax without a fine is 31 December.');

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `id` int(11) NOT NULL,
  `user` varchar(100) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `pdo_details`
--

INSERT INTO `pdo_details` (`id`, `pdo_name`, `contact`, `email`, `address`, `gender`, `username`, `password`, `status`, `report`) VALUES
(1, 'suresh', '1234567882', 'suresh@gmail.com', 'dcvbn mjkhuyt6r54e', 'Male', 'suresh', '12345678', '0', '0');

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `scheme_details`
--

INSERT INTO `scheme_details` (`id`, `scheme_name`, `scheme_eligibility_criteria`, `age`, `description`, `govenment`, `status`, `report`) VALUES
(1, 'free educational ', 'who scores above 80 percent in 10th', '15', 'should be the first graduate, family income should be less than 5 lakhs ', 'State', '0', '0');

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `suggestions`
--

CREATE TABLE `suggestions` (
  `id` int(11) NOT NULL,
  `user` varchar(100) DEFAULT NULL,
  `village` varchar(100) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `status` int(11) NOT NULL DEFAULT 0,
  `viewed_date` varchar(20) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `user_apply_scheme`
--

INSERT INTO `user_apply_scheme` (`id`, `uname`, `scheme_id`, `status`, `report`, `area`) VALUES
(1, 'ram', '1', '0', '2026-11-15', 'adbjxvkcbikhnbv v');

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`id`, `name`, `email`, `address`, `gender`, `contact`, `username`, `password`, `status`, `report`) VALUES
(1, 'ram', 'ram@gmail.com', 'adbjxvkcbikhnbv v', 'Male', '1235467891', 'ram', '123456', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `voting_candidates`
--

CREATE TABLE `voting_candidates` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `age` varchar(10) DEFAULT NULL,
  `position` varchar(100) DEFAULT NULL,
  `votes` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `voting_candidates`
--

INSERT INTO `voting_candidates` (`id`, `name`, `age`, `position`, `votes`) VALUES
(1, 'palani', '50', 'ward councilor ', 0);

-- --------------------------------------------------------

--
-- Table structure for table `voting_status`
--

CREATE TABLE `voting_status` (
  `status` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `voting_status`
--

INSERT INTO `voting_status` (`status`) VALUES
(1);

-- --------------------------------------------------------

--
-- Table structure for table `voting_votes`
--

CREATE TABLE `voting_votes` (
  `id` int(11) NOT NULL,
  `user_aadhaar` varchar(20) NOT NULL,
  `candidate_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `suggestions`
--
ALTER TABLE `suggestions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `voting_candidates`
--
ALTER TABLE `voting_candidates`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `voting_votes`
--
ALTER TABLE `voting_votes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `voting_votes`
--
ALTER TABLE `voting_votes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
