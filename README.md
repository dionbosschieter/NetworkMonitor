NetworkMonitor
==============

NetworkMonitor for Unix Network Programming in Python


This is a network monitor which is developed with Python3.

The agent can run on every computer with python3 installed. For example we've tested it on a Raspberry Pi. 

The agent captures all the packets on eth0. You can edit the network interface. All the packet data is putted in a mysql database. 

The client can also run on every computer with python3 installed. It connect's to the mysql database and reads the packets. 

We've used the following libaries:

Cursus: To make the client user interface
PyMySQL: Mysql client for python
PyLibPcap-0.6.4: To sniff the packets

It's a school project so don't expect many changes;)


Example DB sql code, before you run this, create new database with name: networkmonitor

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `networkmonitor`
--

-- --------------------------------------------------------

--
-- Structure for table `packets`
--

CREATE TABLE IF NOT EXISTS `packets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `version` int(255) NOT NULL,
  `header_len` int(255) NOT NULL,
  `tos` int(255) NOT NULL,
  `total_len` int(255) NOT NULL,
  `ttl` int(255) NOT NULL,
  `protocol` varchar(255) NOT NULL,
  `src_port` int(255) NOT NULL,
  `dst_port` int(255) NOT NULL,
  `src_ip` varchar(255) NOT NULL,
  `dst_ip` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

