-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 13-Dez-2020 às 03:49
-- Versão do servidor: 10.4.11-MariaDB
-- versão do PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `petshop`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `agendamento`
--

CREATE TABLE `agendamento` (
  `id_agendamento` int(11) NOT NULL,
  `nomepet` varchar(25) DEFAULT NULL,
  `especie` varchar(1) DEFAULT NULL,
  `porte` varchar(1) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `datas` varchar(10) DEFAULT NULL,
  `horario` varchar(5) DEFAULT NULL,
  `valorservico` varchar(7) DEFAULT NULL,
  `nomeprofissional` varchar(25) DEFAULT NULL,
  `procedimento` varchar(25) DEFAULT NULL,
  `realizado` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `agendamento`
--

INSERT INTO `agendamento` (`id_agendamento`, `nomepet`, `especie`, `porte`, `peso`, `datas`, `horario`, `valorservico`, `nomeprofissional`, `procedimento`, `realizado`) VALUES
(37, 'AMELIA', 'G', 'P', 3, '14/01/2021', '00:00', '25.00', 'BELANA', 'CIRURGIA', 'SIM'),
(38, 'BETE', 'C', 'P', 12, '15/01/2021', '11:00', '2000.00', 'BELANA', 'CIRURGIA GERAL', 'NAO'),
(39, 'CAKI', 'G', 'P', 20, '15/12/2021', '15:00', '200.00', 'LUCIO MARLON', 'BANHO', 'SIM'),
(40, 'CANEÇA', 'C', 'P', 15, '15/01/2021', '09:00', '35.00', 'LUCIO MARLON', 'BANHO', 'SIM'),
(44, 'CANELA', 'C', 'P', 15, '01/01/2021', '15:00', '25.00', 'ZILDA CLARA VIANA', 'TOSA', 'SIM'),
(50, 'CARACA', 'G', 'P', 20, '12/01/2021', '11:00', '35.00', 'VINICIUS', 'BANHO', 'SIM'),
(56, 'CLIC', 'G', 'P', 10, '01/12/2021', '11:00', '50.00', 'SIMONE', 'BANHO', 'SIM'),
(61, 'KIKA', 'G', 'P', 0, '01/01/2020', '00:00', '35.00', 'SIMONE', 'BANHO', 'SIM'),
(62, 'LITOCA', 'G', 'P', 2, '01/01/2021', '10:00', '200.00', 'BELANA', 'TOSA', 'NAO'),
(63, 'MILUCA', 'G', 'M', 2, '12/01/2021', '09:00', '35.00', 'BELANA', 'BANHO', 'SIM'),
(64, 'PAÇOCA', 'G', 'M', 9, '15/01/2021', '10:00', '25.00', 'SIMONE', 'CIRURGIA GERAL', 'NAO'),
(65, 'YOURI', 'G', 'P', 2, '01/01/2020', '00:00', '120.00', 'LUCIO MARLON', 'BANHO', 'SIM');

-- --------------------------------------------------------

--
-- Estrutura da tabela `categoriapet`
--

CREATE TABLE `categoriapet` (
  `id_categoriapet` int(11) NOT NULL,
  `raca` varchar(25) DEFAULT NULL,
  `lixo` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `categoriapet`
--

INSERT INTO `categoriapet` (`id_categoriapet`, `raca`, `lixo`) VALUES
(10, 'VIRA-LATA', ''),
(11, 'DALMATA', ''),
(12, 'MAINE COON', ''),
(13, 'BULDOG', ''),
(14, 'HOTWEILLER', ''),
(15, 'PUG', ''),
(16, 'PERSA', ''),
(17, 'SIAMES', ''),
(18, 'FILA', ''),
(19, 'DOG ALEMÃO', ''),
(20, 'GOLDEN', ''),
(21, 'AKITA', '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `rg` varchar(12) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `celular` varchar(13) DEFAULT NULL,
  `telefone` varchar(12) DEFAULT NULL,
  `logradouro` varchar(45) DEFAULT NULL,
  `cep` varchar(9) DEFAULT NULL,
  `bairro` varchar(30) DEFAULT NULL,
  `cidade` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `nome`, `rg`, `cpf`, `celular`, `telefone`, `logradouro`, `cep`, `bairro`, `cidade`) VALUES
(50, 'ANTONIA PEREIRA CASTRO', '32156788979', '23265467877', '11-98551-1111', '11-5555-4444', 'RUA GALAXIA', '06846-063', 'JD CORSEGA', 'SÃO PAULO'),
(54, 'CARLOS LACERDA', '152555448787', '24321137468', '11-95999-9999', '11-4550-0000', 'RUA BARÃO DE IGUAPE', '06850-000', 'VILA VINTEM', 'SÃO PAULO'),
(57, 'CAROLINA DANTES AZEVEDO', '237984635431', '12356486745', '11-85222-2222', '11-6541-2222', 'AV. PAULISTA', '05684-622', 'BELA VISTA', 'SÃO PAULO'),
(61, 'CÉSAR MEGALE', '251234168768', '25874633214', '11-98755-5000', '11-5225-4478', 'RUA BARÃO DE IGUAPE', '06843-500', 'ENGENHO VELHO', 'EMBU DAS ARTES'),
(63, 'ROGERIO DA SILVA BRITO', '253231544454', '12364568764', '11-89554-0004', '11-5212-5552', 'RUA ANGLO', '06850-522', 'DA GALAXIA', 'SAO PAULO'),
(68, 'XERXES MICAEL SOUSA', '32154877744', '32515747782', '11-98551-1111', '11-33551-111', 'RUA ALMEIDA', '06846-111', 'MILHARAL', 'SANTOS'),
(70, 'ANDREA DA COSTA MENDES', '321466876454', '25667498764', '11-89999-9999', '11-5444-4444', 'R. BELA CINTRA', '05433-333', 'BELA VISTA', 'SÃO PAULO'),
(71, 'CAROLINA SOARES', '321354544411', '12348678435', '11-85555-5555', '11-6555-5555', 'AV. VERGUEIRO', '02500-000', 'PARAISO', 'SAO PAULO');

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `id_funcionario` int(11) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `cargo` varchar(25) DEFAULT NULL,
  `rg` varchar(12) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `datadeNascimento` varchar(10) DEFAULT NULL,
  `telefone` varchar(12) DEFAULT NULL,
  `celular` varchar(13) DEFAULT NULL,
  `logradouro` varchar(45) DEFAULT NULL,
  `cidade` varchar(25) DEFAULT NULL,
  `cep` varchar(9) DEFAULT NULL,
  `salario` varchar(7) DEFAULT NULL,
  `horaentrar` varchar(5) DEFAULT NULL,
  `horasaida` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `funcionario`
--

INSERT INTO `funcionario` (`id_funcionario`, `nome`, `cargo`, `rg`, `cpf`, `datadeNascimento`, `telefone`, `celular`, `logradouro`, `cidade`, `cep`, `salario`, `horaentrar`, `horasaida`) VALUES
(25, 'ANTONIO VIEIRA SILVA', 'MEDICO', '132456987', '25512212144', '01/12/2021', '11-4567-4564', '11-98552-1234', 'RUA DUMOND VILARES', 'EMBU DAS ARTES', 'EMBU DAS ', '6500.00', '08:00', '17:00'),
(26, 'LUCIO MARLON', 'AUX. VET', '291141323555', '23356844654', '01/02/1998', '11-4444-4444', '11-99999-9999', 'RUA DUMOND VILARES', 'EMBU DAS ARTES', '06844-000', '4500.00', '08:00', '17:00'),
(28, 'VINICIUS ALMEIDA PRADO', 'ANALISTA', '2512477441', '12345649874', '01/12/2020', '11-4561-4040', '11-95000-5151', 'RUA DA MATA', 'TABOAO DA SERRA', '06845-122', '6500.00', '07:30', '16:30'),
(29, 'ZILA SOARES ALMEIRA', 'MEDICO', '321548776545', '13734431313', '31/03/1999', '11-4455-1234', '11-98555-5555', 'RUA DA MATA', 'TABOAO DA SERRA', '06845-122', '6500.00', '08:00', '17:00'),
(30, 'ZILDA CLARA VIANA', 'AUX. VET', '216464313213', '21746431232', '05/11/1975', '11-5555-5555', '11-54465-4132', 'RUA BARAO DE IGUAPE', 'TABOAO DA SERRA', '05688-855', '4500.00', '08:00', '16:30'),
(32, 'LUCIMARA MENEZES', 'AUX. DE ENFERMAGEM', '321546874546', '25655221122', '01/12/1980', '11-5521-2131', '11-92134-3411', 'RUA ANGELICA', 'SÃO PAULO', '02154-441', '4500.00', '08:00', '17:00'),
(33, 'LUZIA MENEZES COSTA', 'MEDICA', '123468744441', '23138738431', '08/06/1975', '11-2252-2144', '11-95222-1244', 'RUA BARAO', 'SÃO PAULO', '02154-441', '7000.00', '08:00', '18:00'),
(34, 'MONICA MARIA', 'MEDICA', '328413323131', '74687434353', '31/12/1970', '11-5422-1122', '11-98845-6411', 'RUA ANGELICA', 'SÃO PAULO', '02154-441', '7000.00', '08:00', '18:00');

-- --------------------------------------------------------

--
-- Estrutura da tabela `login`
--

CREATE TABLE `login` (
  `id_login` int(11) NOT NULL,
  `usuario` varchar(25) DEFAULT NULL,
  `senha` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `loginfacessatabelafuncionario`
--

CREATE TABLE `loginfacessatabelafuncionario` (
  `id_logintabelafuncionario` int(11) NOT NULL,
  `usuario` varchar(25) DEFAULT NULL,
  `senha` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pet`
--

CREATE TABLE `pet` (
  `id_pet` int(11) NOT NULL,
  `nomepet` varchar(45) NOT NULL,
  `idade` int(2) NOT NULL,
  `especie` varchar(1) DEFAULT NULL,
  `porte` varchar(1) DEFAULT NULL,
  `raca` varchar(20) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `pet_cliente` int(11) DEFAULT NULL,
  `cpfcliente` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `pet`
--

INSERT INTO `pet` (`id_pet`, `nomepet`, `idade`, `especie`, `porte`, `raca`, `peso`, `pet_cliente`, `cpfcliente`) VALUES
(146, 'ACRILA', 5, 'C', 'G', 'FILA', 10, NULL, '12345678943'),
(147, 'ADRI', 1, 'G', 'M', 'DALMATA', 2, NULL, '32154644655'),
(152, 'MILUCA', 12, 'G', 'P', 'VIRA-LATA', 5, NULL, '28485544741'),
(156, 'SIÇA', 15, 'C', 'M', 'VIRA-LATA', 12, NULL, '25456412313'),
(161, 'ABILIA', 12, 'C', 'M', 'VIRA-LATA', 11.2, NULL, '2587419630'),
(162, 'ZEZE', 10, 'G', 'G', 'MAINE COON', 5, NULL, '25621325443'),
(164, 'ZICA', 2, 'G', 'P', 'VIRA-LATA', 2.5, NULL, '12412432423'),
(165, 'CRICA', 2, 'C', 'G', 'VIRA-LATA', 25, NULL, '13654878745'),
(166, 'IURY', 2, 'G', 'G', 'MAINE COON', 5, NULL, '33574445445'),
(167, 'ZERO', 2, 'C', 'G', 'VIRA-LATA', 20, NULL, '21111111111');

-- --------------------------------------------------------

--
-- Estrutura da tabela `servicos`
--

CREATE TABLE `servicos` (
  `id_servicos` int(11) NOT NULL,
  `servico` varchar(25) DEFAULT NULL,
  `lixo` varchar(1) DEFAULT NULL,
  `categoria_servicos` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `servicos`
--

INSERT INTO `servicos` (`id_servicos`, `servico`, `lixo`, `categoria_servicos`) VALUES
(10, 'BANHO', '', NULL),
(11, 'PEQUENAS CIRURGIAS', '', NULL),
(12, 'TOSA', '', NULL),
(13, 'HOTEL', '', NULL),
(14, 'ANÁLLISE CLÍNICA', '', NULL),
(15, 'HOSPEDAGEM', '', NULL),
(16, 'ADESTRAMENTO', '', NULL),
(17, 'EMERGENCIA', '', NULL);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `agendamento`
--
ALTER TABLE `agendamento`
  ADD PRIMARY KEY (`id_agendamento`);

--
-- Índices para tabela `categoriapet`
--
ALTER TABLE `categoriapet`
  ADD PRIMARY KEY (`id_categoriapet`);

--
-- Índices para tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Índices para tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`id_funcionario`);

--
-- Índices para tabela `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id_login`);

--
-- Índices para tabela `loginfacessatabelafuncionario`
--
ALTER TABLE `loginfacessatabelafuncionario`
  ADD PRIMARY KEY (`id_logintabelafuncionario`);

--
-- Índices para tabela `pet`
--
ALTER TABLE `pet`
  ADD PRIMARY KEY (`id_pet`),
  ADD KEY `fk_id_pet` (`pet_cliente`);

--
-- Índices para tabela `servicos`
--
ALTER TABLE `servicos`
  ADD PRIMARY KEY (`id_servicos`),
  ADD KEY `fk_id_servicos` (`categoria_servicos`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `agendamento`
--
ALTER TABLE `agendamento`
  MODIFY `id_agendamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT de tabela `categoriapet`
--
ALTER TABLE `categoriapet`
  MODIFY `id_categoriapet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `id_funcionario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT de tabela `login`
--
ALTER TABLE `login`
  MODIFY `id_login` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `loginfacessatabelafuncionario`
--
ALTER TABLE `loginfacessatabelafuncionario`
  MODIFY `id_logintabelafuncionario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `pet`
--
ALTER TABLE `pet`
  MODIFY `id_pet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=168;

--
-- AUTO_INCREMENT de tabela `servicos`
--
ALTER TABLE `servicos`
  MODIFY `id_servicos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `pet`
--
ALTER TABLE `pet`
  ADD CONSTRAINT `fk_id_pet` FOREIGN KEY (`pet_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Limitadores para a tabela `servicos`
--
ALTER TABLE `servicos`
  ADD CONSTRAINT `fk_id_servicos` FOREIGN KEY (`categoria_servicos`) REFERENCES `pet` (`id_pet`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
