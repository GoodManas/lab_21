-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 20 2025 г., 20:17
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `Ali_21`
--

DELIMITER $$
--
-- Процедуры
--
CREATE DEFINER=`root`@`%` PROCEDURE `AppointmentDetails` (IN `patient_id` INT, IN `appointment_date` DATETIME)   BEGIN
    SELECT
        s.ServiceName,
        s.Price,
        a.Prescription,
        a.Diagnosis
    FROM
        Appointments a
    JOIN
        AppointmentServices aps ON a.AppointmentID = aps.AppointmentID
    JOIN
        Services s ON aps.ServiceID = s.ServiceID
    WHERE
        a.PatientID = patient_id AND a.AppointmentDate = appointment_date;
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `PatientAppointmentSummary` (IN `patient_id` INT)   BEGIN
    SELECT
        p.Photo,
        p.LastName,
        p.FirstName,
        p.Email,
        p.BirthDate,
        a.AppointmentDate,
        COUNT(DISTINCT aps.ServiceID) AS NumberOfServices,  
        SUM(s.Price) AS TotalServiceCost
    FROM
        Patients p
    JOIN
        Appointments a ON p.PatientID = a.PatientID
    LEFT JOIN  
        AppointmentServices aps ON a.AppointmentID = aps.AppointmentID
    LEFT JOIN
        Services s ON aps.ServiceID = s.ServiceID
    WHERE
        p.PatientID = patient_id  
    GROUP BY
        p.PatientID, a.AppointmentID   
    ORDER BY
        a.AppointmentDate;  
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `Appointments`
--

CREATE TABLE `Appointments` (
  `AppointmentID` int NOT NULL,
  `AppointmentDate` datetime NOT NULL,
  `PatientID` int NOT NULL,
  `Diagnosis` varchar(25) DEFAULT NULL,
  `Prescription` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Appointments`
--

INSERT INTO `Appointments` (`AppointmentID`, `AppointmentDate`, `PatientID`, `Diagnosis`, `Prescription`) VALUES
(1, '2023-11-15 10:00:00', 1, 'ОРВИ', 'Антибиотики'),
(2, '2023-11-15 11:30:00', 2, 'Гастрит', 'Омепразол'),
(3, '2023-11-16 09:00:00', 3, 'Мигрень', 'Ибупрофен'),
(4, '2023-11-16 14:00:00', 1, 'Повышенное давление', 'Каптоприл');

-- --------------------------------------------------------

--
-- Структура таблицы `AppointmentServices`
--

CREATE TABLE `AppointmentServices` (
  `AppointmentServiceID` int NOT NULL,
  `AppointmentID` int DEFAULT NULL,
  `ServiceID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `AppointmentServices`
--

INSERT INTO `AppointmentServices` (`AppointmentServiceID`, `AppointmentID`, `ServiceID`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(4, 2, 3),
(5, 3, 1),
(6, 3, 4),
(7, 4, 1),
(8, 4, 2);

-- --------------------------------------------------------

--
-- Структура таблицы `Patients`
--

CREATE TABLE `Patients` (
  `PatientID` int NOT NULL,
  `LastName` varchar(25) DEFAULT NULL,
  `FirstName` varchar(25) DEFAULT NULL,
  `Email` varchar(25) DEFAULT NULL,
  `Login` varchar(25) DEFAULT NULL,
  `Password` varchar(25) DEFAULT NULL,
  `BirthDate` date DEFAULT NULL,
  `Photo` longblob
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Patients`
--

INSERT INTO `Patients` (`PatientID`, `LastName`, `FirstName`, `Email`, `Login`, `Password`, `BirthDate`, `Photo`) VALUES
(1, 'Иванов', 'Иван', 'ivanov@example.com', '1', '1', '1990-05-15', NULL),
(2, 'Петрова', 'Елена', 'petrova@example.com', 'alisher', 'alisher', '1985-10-20', NULL),
(3, 'Сидоров', 'Алексей', 'sidorov@example.com', 'ali', 'ali', '1992-03-01', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `Services`
--

CREATE TABLE `Services` (
  `ServiceID` int NOT NULL,
  `ServiceName` varchar(25) NOT NULL,
  `Price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Services`
--

INSERT INTO `Services` (`ServiceID`, `ServiceName`, `Price`) VALUES
(1, 'Консультация терапевта', 1500),
(2, 'Анализ крови', 800),
(3, 'УЗИ брюшной полости', 2000),
(4, 'ЭКГ', 1000);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Appointments`
--
ALTER TABLE `Appointments`
  ADD PRIMARY KEY (`AppointmentID`),
  ADD KEY `PatientID` (`PatientID`);

--
-- Индексы таблицы `AppointmentServices`
--
ALTER TABLE `AppointmentServices`
  ADD PRIMARY KEY (`AppointmentServiceID`),
  ADD KEY `AppointmentID` (`AppointmentID`),
  ADD KEY `ServiceID` (`ServiceID`);

--
-- Индексы таблицы `Patients`
--
ALTER TABLE `Patients`
  ADD PRIMARY KEY (`PatientID`);

--
-- Индексы таблицы `Services`
--
ALTER TABLE `Services`
  ADD PRIMARY KEY (`ServiceID`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `Appointments`
--
ALTER TABLE `Appointments`
  MODIFY `AppointmentID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `AppointmentServices`
--
ALTER TABLE `AppointmentServices`
  MODIFY `AppointmentServiceID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `Patients`
--
ALTER TABLE `Patients`
  MODIFY `PatientID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `Services`
--
ALTER TABLE `Services`
  MODIFY `ServiceID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `Appointments`
--
ALTER TABLE `Appointments`
  ADD CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `Patients` (`PatientID`);

--
-- Ограничения внешнего ключа таблицы `AppointmentServices`
--
ALTER TABLE `AppointmentServices`
  ADD CONSTRAINT `appointmentservices_ibfk_1` FOREIGN KEY (`AppointmentID`) REFERENCES `Appointments` (`AppointmentID`),
  ADD CONSTRAINT `appointmentservices_ibfk_2` FOREIGN KEY (`ServiceID`) REFERENCES `Services` (`ServiceID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
