-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: studentregister
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hackathon_answers`
--

DROP TABLE IF EXISTS `hackathon_answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hackathon_answers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_email` varchar(100) DEFAULT NULL,
  `question_id` int DEFAULT NULL,
  `answer` text,
  `time_taken` float DEFAULT NULL,
  `attempt_done` tinyint(1) DEFAULT '0',
  `question` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=244 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hackathon_answers`
--

LOCK TABLES `hackathon_answers` WRITE;
/*!40000 ALTER TABLE `hackathon_answers` DISABLE KEYS */;
INSERT INTO `hackathon_answers` VALUES (241,'aarav@gmail.com',NULL,'hh',19.3785,1,'Explain OOP concept'),(242,'aarav@gmail.com',NULL,'n',19.3785,1,'What is DBMS?'),(243,'aarav@gmail.com',NULL,'h',19.3785,1,'What is Python?');
/*!40000 ALTER TABLE `hackathon_answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hackathon_attempts`
--

DROP TABLE IF EXISTS `hackathon_attempts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hackathon_attempts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `question_id` int DEFAULT NULL,
  `answer` text,
  `score` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hackathon_attempts`
--

LOCK TABLES `hackathon_attempts` WRITE;
/*!40000 ALTER TABLE `hackathon_attempts` DISABLE KEYS */;
/*!40000 ALTER TABLE `hackathon_attempts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hackathon_questions`
--

DROP TABLE IF EXISTS `hackathon_questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hackathon_questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hackathon_questions`
--

LOCK TABLES `hackathon_questions` WRITE;
/*!40000 ALTER TABLE `hackathon_questions` DISABLE KEYS */;
INSERT INTO `hackathon_questions` VALUES (1,'Explain the difference between multithreading and multiprocessing'),(2,'What is the time complexity of binary search'),(3,'Explain stack vs queue'),(4,'What is database normalization'),(5,'Difference between REST and SOAP API'),(6,'Explain Git branching'),(7,'Difference between deep copy and shallow copy'),(8,'Explain SQL joins'),(9,'What is overfitting in machine learning'),(10,'Explain hash table'),(11,'What is a deadlock in operating systems'),(12,'Difference between process and thread'),(13,'Explain BFS vs DFS'),(14,'What is caching'),(15,'Explain load balancing'),(16,'What is an index in database'),(17,'Explain API rate limiting'),(18,'Difference between HTTP and HTTPS'),(19,'Explain MVC architecture'),(20,'What is a primary key'),(21,'What is foreign key'),(22,'Explain containerization'),(23,'Difference between AI and ML'),(24,'Explain cloud computing'),(25,'What is data structure'),(26,'Explain recursion'),(27,'What is a linked list'),(28,'Difference between array and list'),(29,'Explain authentication vs authorization'),(30,'What is a transaction in database');
/*!40000 ALTER TABLE `hackathon_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hackathon_results`
--

DROP TABLE IF EXISTS `hackathon_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hackathon_results` (
  `student_email` varchar(100) DEFAULT NULL,
  `score` int DEFAULT NULL,
  `time_taken` float DEFAULT NULL,
  `plagiarism` tinyint(1) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hackathon_results`
--

LOCK TABLES `hackathon_results` WRITE;
/*!40000 ALTER TABLE `hackathon_results` DISABLE KEYS */;
INSERT INTO `hackathon_results` VALUES ('rishikjariwala54@gmail.com',0,19.0826,0,'Rejected'),('rishikjariwala689@gmail.com',0,10.6297,0,'Rejected'),('rishikjariwala689@gmail.com',0,11.0004,0,'Rejected'),('rishikjariwala689@gmail.com',0,9.48439,0,'Rejected'),('rishikjariwala689@gmail.com',0,9.72125,0,'Rejected'),('ramesh@gmail.com',0,22.9127,0,'Rejected');
/*!40000 ALTER TABLE `hackathon_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_name` varchar(100) DEFAULT NULL,
  `job_role` varchar(100) DEFAULT NULL,
  `description` text,
  `posted_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` VALUES (1,'Hello','MERN','MERN STACK DEVELOPER','2026-03-15 05:21:33');
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_auth`
--

DROP TABLE IF EXISTS `main_auth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_auth` (
  `password` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_auth`
--

LOCK TABLES `main_auth` WRITE;
/*!40000 ALTER TABLE `main_auth` DISABLE KEYS */;
INSERT INTO `main_auth` VALUES ('internfadmin@123');
/*!40000 ALTER TABLE `main_auth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruiter_register`
--

DROP TABLE IF EXISTS `recruiter_register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recruiter_register` (
  `id` int NOT NULL AUTO_INCREMENT,
  `recruiter_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter_register`
--

LOCK TABLES `recruiter_register` WRITE;
/*!40000 ALTER TABLE `recruiter_register` DISABLE KEYS */;
INSERT INTO `recruiter_register` VALUES (1,'Rishi','rishi@gmail.com','1234','ABC Company');
/*!40000 ALTER TABLE `recruiter_register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruiter_requests`
--

DROP TABLE IF EXISTS `recruiter_requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recruiter_requests` (
  `id` int NOT NULL AUTO_INCREMENT,
  `compnay_name` varchar(100) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  `students_required` int DEFAULT NULL,
  `invite_count` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter_requests`
--

LOCK TABLES `recruiter_requests` WRITE;
/*!40000 ALTER TABLE `recruiter_requests` DISABLE KEYS */;
INSERT INTO `recruiter_requests` VALUES (1,'rt','rt',10,50,'recruiter@email.com','pending'),(2,'Flipkart','Software Developer',10,50,'recruiter@email.com','pending'),(3,'Flipkart','Software Developer',10,50,'recruiter@email.com','pending'),(4,'Flipkart','Software Developer',10,50,'recruiter@email.com','pending'),(5,'Flipkart','Software Developer',10,50,'recruiter@email.com','pending'),(6,'Flipkart','Software Developer',10,50,'recruiter@email.com','pending'),(7,'Microsoft','MERN',10,50,'recruiter@email.com','pending'),(8,'Microsoft','MERN',10,50,'recruiter@email.com','pending'),(9,'Amazon','AI/ML',10,50,'recruiter@email.com','pending'),(10,'GOOGLE','PERN',10,50,'recruiter@email.com','pending'),(11,'GOOGLE','PERN',10,50,'recruiter@email.com','pending'),(12,'GOOGLE','PERN',10,50,'recruiter@email.com','pending'),(13,'GOOGLE','PERN',10,50,'recruiter@email.com','pending'),(14,'GOOGLE','PERN',10,50,'recruiter@email.com','pending');
/*!40000 ALTER TABLE `recruiter_requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruiter_requirements`
--

DROP TABLE IF EXISTS `recruiter_requirements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recruiter_requirements` (
  `id` int NOT NULL AUTO_INCREMENT,
  `recruiter_name` varchar(100) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `job_role` varchar(100) DEFAULT NULL,
  `primary_skill` varchar(100) DEFAULT NULL,
  `skill_level` varchar(50) DEFAULT NULL,
  `min_cgpa` decimal(3,2) DEFAULT NULL,
  `degree` varchar(100) DEFAULT NULL,
  `branch` varchar(100) DEFAULT NULL,
  `passing_year` decimal(4,0) DEFAULT NULL,
  `salary` varchar(20) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `job_type` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `recruiter_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_recruiter` (`recruiter_id`),
  CONSTRAINT `fk_recruiter` FOREIGN KEY (`recruiter_id`) REFERENCES `recruiter_register` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruiter_requirements`
--

LOCK TABLES `recruiter_requirements` WRITE;
/*!40000 ALTER TABLE `recruiter_requirements` DISABLE KEYS */;
INSERT INTO `recruiter_requirements` VALUES (1,'Ramesh','Amazon','App developer','Android',NULL,8.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 06:04:07',1),(2,'f','f','MERN','MERN',NULL,9.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 06:29:34',1),(3,'rr','r','r','r',NULL,9.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 06:30:57',1),(4,'rt','rt','rt','rt',NULL,9.00,NULL,'rt',NULL,NULL,NULL,NULL,'2026-03-22 06:54:17',1),(5,'Rakesh Shah','Flipkart','Software Developer','Software',NULL,8.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 07:00:42',1),(6,'Rakesh Shah','Flipkart','Software Developer','Software',NULL,8.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 07:02:33',1),(7,'Rakesh Shah','Flipkart','Software Developer','Software',NULL,8.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 07:02:45',1),(8,'Rakesh Shah','Flipkart','Software Developer','Software',NULL,8.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 07:41:38',1),(9,'Rakesh Shah','Flipkart','Software Developer','Software',NULL,8.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 07:42:36',1),(10,'aarav','Microsoft','MERN','MERN',NULL,8.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 13:27:55',1),(11,'aarav','Microsoft','MERN','MERN',NULL,8.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 13:28:09',1),(12,'Akruti','Amazon','AI/ML','AI/ML',NULL,9.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 16:02:03',1),(13,'FAHRUCK','GOOGLE','PERN','PERN',NULL,9.00,NULL,'CSE',NULL,NULL,NULL,NULL,'2026-03-22 16:25:02',1),(14,'FAHRUCK','GOOGLE','PERN','PERN',NULL,9.00,NULL,'CSE',NULL,NULL,NULL,NULL,'2026-03-22 16:27:13',1),(15,'FAHRUCK','GOOGLE','PERN','PERN',NULL,9.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 16:27:31',1),(16,'FAHRUCK','GOOGLE','PERN','PERN',NULL,9.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 16:27:39',1),(17,'FAHRUCK','GOOGLE','PERN','PERN',NULL,9.00,NULL,'IT',NULL,NULL,NULL,NULL,'2026-03-22 16:35:16',1);
/*!40000 ALTER TABLE `recruiter_requirements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shortlisted_students`
--

DROP TABLE IF EXISTS `shortlisted_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shortlisted_students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `request_id` int DEFAULT NULL,
  `score` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shortlisted_students`
--

LOCK TABLES `shortlisted_students` WRITE;
/*!40000 ALTER TABLE `shortlisted_students` DISABLE KEYS */;
/*!40000 ALTER TABLE `shortlisted_students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(10) DEFAULT NULL,
  `password` varchar(15) NOT NULL,
  `college_name` varchar(100) DEFAULT NULL,
  `branch` varchar(30) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `CGPA` decimal(3,2) DEFAULT NULL,
  `skills` varchar(50) DEFAULT NULL,
  `primary_skill` varchar(50) DEFAULT NULL,
  `skill_level` varchar(20) DEFAULT NULL,
  `degree` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('aarav','aarav@gmail.com','1234567890','aarav@123','SBMP','IT',3,9.00,'PERN','PERN','Intermediate','Diploma'),('Aarush','aarush@gmail.com','8374659746','aarush@12345','DJ','IT',3,8.00,'AI/ML','AI/ML','intermediate','Degree'),('Ramesh','ramesh@gmail.com','7364528371','ramesh@12345','DJ Sanghvi','CSE',3,8.00,'IT','MERN','intermediate','Diploma'),('Rishik Jariwala','rishikjariwala54@gmail.com','9136091620','rishik@12345','SBMP','IT',3,8.00,'Software','Software','intermediate','Diploma');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uploadresume`
--

DROP TABLE IF EXISTS `uploadresume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uploadresume` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `file_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uploadresume`
--

LOCK TABLES `uploadresume` WRITE;
/*!40000 ALTER TABLE `uploadresume` DISABLE KEYS */;
INSERT INTO `uploadresume` VALUES (1,'2','2','C:/Users/Abcom/Downloads/Week4_QEC.pdf'),(2,'2','2','C:/Users/Abcom/Downloads/Doc2 (3) (1).docx'),(3,'r','r','C:/Users/Abcom/Downloads/BlackBox_Debugging_Practice_Set.docx'),(4,'eew','ee','C:/Users/Abcom/Downloads/Doc1 (1) (3) (2).docx'),(5,'a','a','C:/Users/Abcom/Downloads/Doc1 (1) (3) (2).docx'),(6,'b','b','C:/Users/Abcom/Downloads/Doc1 (1) (3) (2).docx'),(7,'Rishik','rishikjariwala54@gmail.com','C:/Users/Abcom/Downloads/Doc1 (1) (3) (2).docx'),(8,'Ram','ram@gmail.com','C:/Users/Abcom/Downloads/Doc1 (1) (3) (2).docx'),(9,'Rishik','rishikjariwala54@gmail.com','C:/Users/Abcom/Downloads/a2d13424-f742-426d-a585-5b1a9d9ac140.pdf'),(10,'Suresh','suresh@gmail.com','C:/Users/Abcom/Downloads/RESEARCH PAPPER 3.pdf'),(11,'Rishik JARIWALA','rishikjariwala54@gmail.com','C:/Users/Abcom/Downloads/Junaid Sikander Resume.pdf'),(12,'Rishik','rishikjariwala54@gmail.com','C:/Users/Abcom/Downloads/Junaid Sikander Resume.pdf'),(13,'Rishik','rishikjariwala54@gmail.com','C:/Users/Abcom/Downloads/Junaid Sikander Resume.pdf'),(14,'Rishik','rishikjariwala54@gmail.com','C:/Users/Abcom/Downloads/Junaid Sikander Resume.pdf'),(15,'Ramesh','rishikjariwala689@gmail.com','C:/Users/Abcom/Downloads/Junaid Sikander Resume.pdf'),(16,'Rameesh','ramesh@gmail.com','C:/Users/Abcom/Downloads/Jillani Resume.pdf'),(17,'Rishik','rishikjariwala54@gmail.com','C:/Users/Abcom/Downloads/Junaid Sikander Resume.pdf'),(18,'Rishik Jariwala','rishikjariwala54@gmail.com','C:/Users/Abcom/Downloads/vertopal.com_EXPERIMENT8 KNN ALGORTIHM.pdf'),(19,'Ramesh','ramesh@gmail.com','C:/Users/Abcom/Downloads/Rishik Jariwala resume (1).pdf'),(20,'Ramesh','ramesh@gmail.com','C:/Users/Abcom/Downloads/Rishik Jariwala resume (1).pdf'),(21,'Aarush','aarush@gmail.com','C:/Users/Abcom/Downloads/Rishik Jariwala resume (1).pdf'),(22,'aarav','aarav@gmail.com','C:/Users/Abcom/Downloads/Rishik Jariwala resume (1).pdf'),(23,'aarav','aarav@gmail.com','C:/Users/Abcom/Downloads/Rishik Jariwala resume (1).pdf'),(24,'aarav','aarav@gmail.com','C:/Users/Abcom/Downloads/Rishik Jariwala resume (1).pdf');
/*!40000 ALTER TABLE `uploadresume` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-22 23:18:27
