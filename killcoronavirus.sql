-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-07-2024 a las 07:07:12
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `killcoronavirus`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidad`
--

CREATE TABLE `especialidad` (
  `ID_Especialidad` int(11) NOT NULL,
  `Nombre_Especialidad` varchar(100) NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `especialidad`
--

INSERT INTO `especialidad` (`ID_Especialidad`, `Nombre_Especialidad`, `activo`) VALUES
(1, 'Neumología', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `examen`
--

CREATE TABLE `examen` (
  `ID_Examen` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Descripcion` text DEFAULT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `examen`
--

INSERT INTO `examen` (`ID_Examen`, `Nombre`, `Descripcion`, `activo`) VALUES
(1, 'Radiografía de tórax', 'Imagen radiográfica del tórax para evaluar estructuras pulmonares y cardíacas.', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fichamedica`
--

CREATE TABLE `fichamedica` (
  `ID_FichaMedica` int(11) NOT NULL,
  `Diagnostico` text DEFAULT NULL,
  `Fecha_Atencion` date DEFAULT NULL,
  `Anamnesis` text DEFAULT NULL,
  `ID_Paciente` int(11) DEFAULT NULL,
  `ID_Profesional` int(11) DEFAULT NULL,
  `ID_Medicamento` int(11) DEFAULT NULL,
  `ID_Examen` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `fichamedica`
--

INSERT INTO `fichamedica` (`ID_FichaMedica`, `Diagnostico`, `Fecha_Atencion`, `Anamnesis`, `ID_Paciente`, `ID_Profesional`, `ID_Medicamento`, `ID_Examen`) VALUES
(1, 'Neumonía bilateral', '2024-07-11', 'Paciente de 45 años con antecedente de tos persistente y fiebre alta desde hace una semana.', 1, 1, 1, 1),
(2, 'Fractura de tobillo izquierdo', '2024-07-11', 'Paciente de 30 años con antecedente de caída desde una altura, dolor intenso en el tobillo izquierdo y dificultad para apoyar el pie.', 2, 1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login`
--

CREATE TABLE `login` (
  `ID_Login` int(11) NOT NULL,
  `Usuario` varchar(100) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `ID_TipoUsuario` int(11) NOT NULL,
  `ID_Profesional` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `login`
--

INSERT INTO `login` (`ID_Login`, `Usuario`, `Password`, `ID_TipoUsuario`, `ID_Profesional`) VALUES
(1, 'Admin', 'admin1234', 1, NULL),
(2, 'Marcos', 'Rojo', 2, NULL),
(3, 'Matias', 'Pardo', 3, NULL),
(4, 'Ana', 'Maldonado', 3, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicamento`
--

CREATE TABLE `medicamento` (
  `ID_Medicamento` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Descripcion` text DEFAULT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medicamento`
--

INSERT INTO `medicamento` (`ID_Medicamento`, `Nombre`, `Descripcion`, `activo`) VALUES
(1, 'Antibiótico Amoxicilina', 'Antibiótico de amplio espectro para tratar infecciones bacterianas.', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `ID_Paciente` int(11) NOT NULL,
  `RUT` varchar(20) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Apellido` varchar(100) NOT NULL,
  `Fecha_Nac` date DEFAULT NULL,
  `Telefono` varchar(15) DEFAULT NULL,
  `ID_TipoUsuario` int(11) NOT NULL DEFAULT 3,
  `Usuario` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`ID_Paciente`, `RUT`, `Nombre`, `Apellido`, `Fecha_Nac`, `Telefono`, `ID_TipoUsuario`, `Usuario`) VALUES
(1, '213400691', 'Matias', 'Pardo', '2003-10-07', '991591931', 3, 'Matias'),
(2, '215238539', 'Ana', 'Maldonado', '2004-05-03', '912345678', 3, 'Ana');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesional`
--

CREATE TABLE `profesional` (
  `ID_Profesional` int(11) NOT NULL,
  `RUT` varchar(20) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Apellido` varchar(100) NOT NULL,
  `Telefono` varchar(15) DEFAULT NULL,
  `ID_Especialidad` int(11) DEFAULT NULL,
  `ID_TipoUsuario` int(11) DEFAULT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesional`
--

INSERT INTO `profesional` (`ID_Profesional`, `RUT`, `Nombre`, `Apellido`, `Telefono`, `ID_Especialidad`, `ID_TipoUsuario`, `activo`) VALUES
(1, '141638386', 'Marcos', 'Rojo', '978906543', NULL, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesional_especialidad`
--

CREATE TABLE `profesional_especialidad` (
  `ID` int(11) NOT NULL,
  `ID_Profesional` int(11) DEFAULT NULL,
  `ID_Especialidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesional_especialidad`
--

INSERT INTO `profesional_especialidad` (`ID`, `ID_Profesional`, `ID_Especialidad`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipousuario`
--

CREATE TABLE `tipousuario` (
  `ID_TipoUsuario` int(11) NOT NULL,
  `Nombre_Usuario` varchar(100) NOT NULL,
  `Descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipousuario`
--

INSERT INTO `tipousuario` (`ID_TipoUsuario`, `Nombre_Usuario`, `Descripcion`) VALUES
(1, 'Administrador', 'Es el Administrador del sistema'),
(2, 'Medico', 'Es el Medico del sistema.'),
(3, 'Paciente', 'Es el Paciente del sistema.');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `especialidad`
--
ALTER TABLE `especialidad`
  ADD PRIMARY KEY (`ID_Especialidad`);

--
-- Indices de la tabla `examen`
--
ALTER TABLE `examen`
  ADD PRIMARY KEY (`ID_Examen`);

--
-- Indices de la tabla `fichamedica`
--
ALTER TABLE `fichamedica`
  ADD PRIMARY KEY (`ID_FichaMedica`),
  ADD KEY `ID_Paciente` (`ID_Paciente`),
  ADD KEY `ID_Profesional` (`ID_Profesional`),
  ADD KEY `ID_Medicamento` (`ID_Medicamento`,`ID_Examen`);

--
-- Indices de la tabla `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`ID_Login`),
  ADD KEY `ID_TipoUsuario` (`ID_TipoUsuario`),
  ADD KEY `fk_login_profesional` (`ID_Profesional`);

--
-- Indices de la tabla `medicamento`
--
ALTER TABLE `medicamento`
  ADD PRIMARY KEY (`ID_Medicamento`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`ID_Paciente`);

--
-- Indices de la tabla `profesional`
--
ALTER TABLE `profesional`
  ADD PRIMARY KEY (`ID_Profesional`),
  ADD KEY `ID_Especialidad` (`ID_Especialidad`),
  ADD KEY `ID_TipoUsuario` (`ID_TipoUsuario`);

--
-- Indices de la tabla `profesional_especialidad`
--
ALTER TABLE `profesional_especialidad`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Profesional` (`ID_Profesional`),
  ADD KEY `ID_Especialidad` (`ID_Especialidad`);

--
-- Indices de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  ADD PRIMARY KEY (`ID_TipoUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `especialidad`
--
ALTER TABLE `especialidad`
  MODIFY `ID_Especialidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `examen`
--
ALTER TABLE `examen`
  MODIFY `ID_Examen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `fichamedica`
--
ALTER TABLE `fichamedica`
  MODIFY `ID_FichaMedica` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `login`
--
ALTER TABLE `login`
  MODIFY `ID_Login` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `medicamento`
--
ALTER TABLE `medicamento`
  MODIFY `ID_Medicamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `ID_Paciente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `profesional`
--
ALTER TABLE `profesional`
  MODIFY `ID_Profesional` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `profesional_especialidad`
--
ALTER TABLE `profesional_especialidad`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  MODIFY `ID_TipoUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `fichamedica`
--
ALTER TABLE `fichamedica`
  ADD CONSTRAINT `fichamedica_ibfk_1` FOREIGN KEY (`ID_Paciente`) REFERENCES `paciente` (`ID_Paciente`),
  ADD CONSTRAINT `fichamedica_ibfk_2` FOREIGN KEY (`ID_Profesional`) REFERENCES `profesional` (`ID_Profesional`),
  ADD CONSTRAINT `fk_fichamedica_profesional` FOREIGN KEY (`ID_Profesional`) REFERENCES `profesional` (`ID_Profesional`),
  ADD CONSTRAINT `fk_profesional` FOREIGN KEY (`ID_Profesional`) REFERENCES `profesional` (`ID_Profesional`);

--
-- Filtros para la tabla `login`
--
ALTER TABLE `login`
  ADD CONSTRAINT `fk_login_profesional` FOREIGN KEY (`ID_Profesional`) REFERENCES `profesional` (`ID_Profesional`),
  ADD CONSTRAINT `login_ibfk_1` FOREIGN KEY (`ID_TipoUsuario`) REFERENCES `tipousuario` (`ID_TipoUsuario`);

--
-- Filtros para la tabla `profesional`
--
ALTER TABLE `profesional`
  ADD CONSTRAINT `profesional_ibfk_1` FOREIGN KEY (`ID_Especialidad`) REFERENCES `especialidad` (`ID_Especialidad`);

--
-- Filtros para la tabla `profesional_especialidad`
--
ALTER TABLE `profesional_especialidad`
  ADD CONSTRAINT `profesional_especialidad_ibfk_1` FOREIGN KEY (`ID_Profesional`) REFERENCES `profesional` (`ID_Profesional`),
  ADD CONSTRAINT `profesional_especialidad_ibfk_2` FOREIGN KEY (`ID_Especialidad`) REFERENCES `especialidad` (`ID_Especialidad`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
