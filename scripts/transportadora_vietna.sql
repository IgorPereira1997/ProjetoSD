-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 19/05/2021 às 19:01
-- Versão do servidor: 8.0.25-0ubuntu0.20.04.1
-- Versão do PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `transportadora_vietna`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estrutura para tabela `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estrutura para tabela `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add categorias', 7, 'add_categorias'),
(26, 'Can change categorias', 7, 'change_categorias'),
(27, 'Can delete categorias', 7, 'delete_categorias'),
(28, 'Can view categorias', 7, 'view_categorias'),
(29, 'Can add clientes', 8, 'add_clientes'),
(30, 'Can change clientes', 8, 'change_clientes'),
(31, 'Can delete clientes', 8, 'delete_clientes'),
(32, 'Can view clientes', 8, 'view_clientes'),
(33, 'Can add departamentos', 9, 'add_departamentos'),
(34, 'Can change departamentos', 9, 'change_departamentos'),
(35, 'Can delete departamentos', 9, 'delete_departamentos'),
(36, 'Can view departamentos', 9, 'view_departamentos'),
(37, 'Can add estados', 10, 'add_estados'),
(38, 'Can change estados', 10, 'change_estados'),
(39, 'Can delete estados', 10, 'delete_estados'),
(40, 'Can view estados', 10, 'view_estados'),
(41, 'Can add fornecedores', 11, 'add_fornecedores'),
(42, 'Can change fornecedores', 11, 'change_fornecedores'),
(43, 'Can delete fornecedores', 11, 'delete_fornecedores'),
(44, 'Can view fornecedores', 11, 'view_fornecedores'),
(45, 'Can add fornecedores contatos', 12, 'add_fornecedorescontatos'),
(46, 'Can change fornecedores contatos', 12, 'change_fornecedorescontatos'),
(47, 'Can delete fornecedores contatos', 12, 'delete_fornecedorescontatos'),
(48, 'Can view fornecedores contatos', 12, 'view_fornecedorescontatos'),
(49, 'Can add franquias', 13, 'add_franquias'),
(50, 'Can change franquias', 13, 'change_franquias'),
(51, 'Can delete franquias', 13, 'delete_franquias'),
(52, 'Can view franquias', 13, 'view_franquias'),
(53, 'Can add produtos', 14, 'add_produtos'),
(54, 'Can change produtos', 14, 'change_produtos'),
(55, 'Can delete produtos', 14, 'delete_produtos'),
(56, 'Can view produtos', 14, 'view_produtos'),
(57, 'Can add transportadoras', 15, 'add_transportadoras'),
(58, 'Can change transportadoras', 15, 'change_transportadoras'),
(59, 'Can delete transportadoras', 15, 'delete_transportadoras'),
(60, 'Can view transportadoras', 15, 'view_transportadoras'),
(61, 'Can add pedidos', 16, 'add_pedidos'),
(62, 'Can change pedidos', 16, 'change_pedidos'),
(63, 'Can delete pedidos', 16, 'delete_pedidos'),
(64, 'Can view pedidos', 16, 'view_pedidos'),
(65, 'Can add pedidos item', 17, 'add_pedidositem'),
(66, 'Can change pedidos item', 17, 'change_pedidositem'),
(67, 'Can delete pedidos item', 17, 'delete_pedidositem'),
(68, 'Can view pedidos item', 17, 'view_pedidositem'),
(69, 'Can add pedidos status', 18, 'add_pedidosstatus'),
(70, 'Can change pedidos status', 18, 'change_pedidosstatus'),
(71, 'Can delete pedidos status', 18, 'delete_pedidosstatus'),
(72, 'Can view pedidos status', 18, 'view_pedidosstatus'),
(73, 'Can add document', 19, 'add_document'),
(74, 'Can change document', 19, 'change_document'),
(75, 'Can delete document', 19, 'delete_document'),
(76, 'Can view document', 19, 'view_document');

-- --------------------------------------------------------

--
-- Estrutura para tabela `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estrutura para tabela `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estrutura para tabela `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estrutura para tabela `categorias`
--

CREATE TABLE `categorias` (
  `categoriaID` int NOT NULL,
  `nomecategoria` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `categorias`
--

INSERT INTO `categorias` (`categoriaID`, `nomecategoria`) VALUES
(1, 'Coffee'),
(2, 'Food'),
(3, 'Merchandise'),
(4, 'Clothing');

-- --------------------------------------------------------

--
-- Estrutura para tabela `clientes`
--

CREATE TABLE `clientes` (
  `clienteID` int NOT NULL,
  `nomecompleto` varchar(50) DEFAULT NULL,
  `endereco` varchar(50) DEFAULT NULL,
  `complemento` varchar(30) DEFAULT NULL,
  `numero` varchar(15) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `estadoID` tinyint DEFAULT NULL,
  `cep` varchar(10) DEFAULT NULL,
  `ddd` varchar(3) DEFAULT NULL,
  `telefone` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `usuario` varchar(10) DEFAULT NULL,
  `senha` varchar(10) DEFAULT NULL,
  `nivel` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `clientes`
--

INSERT INTO `clientes` (`clienteID`, `nomecompleto`, `endereco`, `complemento`, `numero`, `cidade`, `estadoID`, `cep`, `ddd`, `telefone`, `email`, `usuario`, `senha`, `nivel`) VALUES
(7, 'Bob', 'Kobe Dr', 'Suite 31', '2929 ', 'São Paulo', 27, '92123', '11', '99999-0001', 'bobrob@dru', 'bobrob', 'cheese', 'admin'),
(8, 'Lee', 'Priestly Dr', 'Suite 30', '5927 ', 'Rio de Janeiro', 22, '92008', '21', '9999-0101', 'ldkim@drum', 'ldkim', 'drums', 'admin'),
(9, 'Jane', 'Priestly Dr', 'Suite 01', '5924 ', 'Recife', 17, '92008', '81', '9999-0202', 'jstev@fili', 'zac', 'zac', 'admin'),
(33, 'Mary', 'Mill Lane', 'House', '22', 'Rio de Janeiro', 22, 'P0987GH', '21', '9999-0303', 'mary@sheep.com', 'mary', 'baa', 'user'),
(34, 'Adriaan', 'Main St.', 'House', '31', 'Porto Alegre', 21, '90876', '51', '9999-0001', 'joe@blow.net', 'joe', 'blow', 'user'),
(35, 'Yeshe', 'Place des Vosges', 'House', '26 ', 'Recife', 17, '75003', '81', '9999-0404', 'kako@alibert.org', 'kako', 'crow', 'user'),
(36, 'Jean-Claude', 'Rue des Archives', 'Suite 31', '26 ', 'Salvador', 5, '75003', '71', '9999-0500', 'bouquet@paris.com', 'bouquet', 'archives', 'foreign'),
(37, 'Charmian', 'Biscane Boulevard', 'Suite 55', '21', 'Fortaleza', 6, '87543', '85', '9999-0001', 'thepet@cows.com', 'petty', 'officer', 'admin'),
(38, 'Tex', 'Ocean Dr', 'Suite 11', '32', 'Fortaleza', 6, '92107', '85', '9999-0002', 'minou@sefton.com', 'minou', 'lechat', 'user'),
(39, 'James', 'Lotus St', 'Suite 533', '33', 'Belo Horizonte', 13, '92107', '31', '9999-0001', 'jjones@thing.com', 'jj', 'magenta', 'user'),
(40, 'Scott', 'Harley St.', 'Suite 31', '1312 ', 'Curitiba', 16, '41414', '41', '9999-4001', 'scottie@theworks.camvria.com', 'scooby', 'doo', 'user'),
(41, 'Mavis', 'The Lane', 'Suite 01', '774', 'Florianopolis', 28, '99999', '48', '9999-0001', 'mave@formerly.sisters.org', 'mkirk', 'jesus', 'user'),
(42, 'Morton', 'Kwai', 'Suite 02', '101', 'João Pessoa', 15, '71717', '83', '9999-0001', 'mgold@brockyard.herrr.org', 'gold', 'rng665', 'user'),
(43, 'Monica', 'Arbor Drive', 'Suite 01', '21 ', 'Belém', 14, '91111', '91', '9999-0001', 'birch@nobodys.fool.com', 'birch', 'bsgr%', 'admin'),
(44, 'Amos', 'Framingham Ave', 'Suite 10', '4545 ', 'Manaus', 4, '31311', '92', '9999-0001', 'add@barnham.peoples.com', 'adur', 'adur', 'user'),
(45, 'Pietro', 'Vagam', 'Suite 01', '4010', 'Goiania', 9, 'dfsf', '63', '9999-0001', 'pcard@utica.gegli.it', 'cardinal', 'oojj&t', 'foreign'),
(46, 'Amosa', 'Conselheiro Av', 'Suite 15', '187', 'Brasília', 7, 'gfg', '61', '9999-9991', 'bosun@navarro.edu', 'partner', 'fairies', 'user'),
(47, 'Marvin', 'Domingos Dr', 'House', '2400', 'São Luis', 10, '30303', '98', '9999-0001', 'mdekal@megaprod.com', 'mdekal', 'uu6654', 'user'),
(48, 'Duncan', 'Aguamenon Av', 'Suite 21', '3010', 'Vitória', 8, '221', '27', '9999-0001', 'biggie@brabazon.co.il', 'brab', 'plane', 'foreign'),
(49, 'Brandon', 'Penny Lane', 'Suite 22', '1212 ', 'Macapá', 3, '21177', '96', '9999-0001', 'bshaft@thegroup.net', 'shaft', '3344510', 'user'),
(50, 'Raul', 'Farley Ave', 'Suite 10', '444 ', 'Maceió', 2, '92117', '82', '9999-0001', 'rost@aero.mx.com', 'pilot', 'brebby', 'user');

-- --------------------------------------------------------

--
-- Estrutura para tabela `departamentos`
--

CREATE TABLE `departamentos` (
  `departamentoID` int NOT NULL,
  `nomedepartamento` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `departamentos`
--

INSERT INTO `departamentos` (`departamentoID`, `nomedepartamento`) VALUES
(1, 'financeiro'),
(2, 'comercial'),
(3, 'atendimento'),
(4, 'direção'),
(6, 'gerência financeira'),
(7, 'presidencia'),
(8, 'CPD');

-- --------------------------------------------------------

--
-- Estrutura para tabela `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estrutura para tabela `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'categorias', 'categorias'),
(8, 'clientes', 'clientes'),
(5, 'contenttypes', 'contenttype'),
(9, 'departamentos', 'departamentos'),
(10, 'estados', 'estados'),
(11, 'fornecedores', 'fornecedores'),
(12, 'fornecedores', 'fornecedorescontatos'),
(13, 'franquias', 'franquias'),
(19, 'listar_produtos', 'document'),
(14, 'listar_produtos', 'produtos'),
(15, 'listar_transportadoras', 'transportadoras'),
(16, 'manage_pedidos', 'pedidos'),
(17, 'manage_pedidos', 'pedidositem'),
(18, 'manage_pedidos', 'pedidosstatus'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estrutura para tabela `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-05-05 15:12:58.889387'),
(2, 'auth', '0001_initial', '2021-05-05 15:12:59.097251'),
(3, 'admin', '0001_initial', '2021-05-05 15:12:59.701914'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-05-05 15:12:59.892224'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-05-05 15:12:59.922088'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-05-05 15:13:00.088903'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-05-05 15:13:00.176318'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-05-05 15:13:00.280741'),
(9, 'auth', '0004_alter_user_username_opts', '2021-05-05 15:13:00.307218'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-05-05 15:13:00.400044'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-05-05 15:13:00.407042'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-05-05 15:13:00.442075'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-05-05 15:13:00.552689'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-05-05 15:13:00.653593'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-05-05 15:13:00.737117'),
(16, 'auth', '0011_update_proxy_permissions', '2021-05-05 15:13:00.763010'),
(17, 'categorias', '0001_initial', '2021-05-05 15:13:00.801472'),
(18, 'categorias', '0002_auto_20210503_0047', '2021-05-05 15:13:00.812511'),
(19, 'clientes', '0001_initial', '2021-05-05 15:13:00.890452'),
(20, 'departamentos', '0001_initial', '2021-05-05 15:13:00.900981'),
(21, 'departamentos', '0002_auto_20210505_1512', '2021-05-05 15:13:00.912085'),
(22, 'estados', '0001_initial', '2021-05-05 15:13:00.923853'),
(23, 'estados', '0002_auto_20210505_1512', '2021-05-05 15:13:00.936006'),
(24, 'fornecedores', '0001_initial', '2021-05-05 15:13:00.991695'),
(25, 'fornecedores', '0002_auto_20210505_1512', '2021-05-05 15:13:01.004173'),
(26, 'franquias', '0001_initial', '2021-05-05 15:13:01.066818'),
(27, 'listar_produtos', '0001_initial', '2021-05-05 15:13:01.141694'),
(28, 'listar_transportadoras', '0001_initial', '2021-05-05 15:13:01.204840'),
(29, 'manage_pedidos', '0001_initial', '2021-05-05 15:13:01.326912'),
(30, 'manage_pedidos', '0002_auto_20210503_0047', '2021-05-05 15:13:01.339352'),
(31, 'sessions', '0001_initial', '2021-05-05 15:13:01.384705'),
(32, 'categorias', '0003_auto_20210507_1440', '2021-05-07 14:40:46.115496'),
(33, 'listar_produtos', '0002_auto_20210512_0226', '2021-05-12 02:26:22.044698'),
(34, 'listar_produtos', '0003_delete_document', '2021-05-12 18:23:05.594550');

-- --------------------------------------------------------

--
-- Estrutura para tabela `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0fyp3lcxmj4y2hc7j07ohx8p6pga2ofs', 'M2I4ZmMyNTVkYTQwZjU3OWM2NDJjMjg1MzJkODBjZjllYmZjYzU4Mjp7ImlkQ2xpZW50ZSI6OSwiaWRGb3JuZWNlZG9yIjoyfQ==', '2021-05-28 22:51:06.928249'),
('gypubxbezh43c4ic5mzmh5xbfyrtt771', 'M2I4ZmMyNTVkYTQwZjU3OWM2NDJjMjg1MzJkODBjZjllYmZjYzU4Mjp7ImlkQ2xpZW50ZSI6OSwiaWRGb3JuZWNlZG9yIjoyfQ==', '2021-05-24 18:47:21.655477'),
('r4fhl3m8497dazbf9gyuzh92mohkuy7p', 'MjU3ZDRiMDc2MzUxNzk4Y2VkNDU1OTQwZTA5ZDY1YzkxMjI4NGFmOTp7ImlkQ2xpZW50ZSI6OX0=', '2021-05-26 00:14:11.948288');

-- --------------------------------------------------------

--
-- Estrutura para tabela `estados`
--

CREATE TABLE `estados` (
  `estadoID` tinyint UNSIGNED NOT NULL,
  `nome` char(20) DEFAULT '0',
  `sigla` char(2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `estados`
--

INSERT INTO `estados` (`estadoID`, `nome`, `sigla`) VALUES
(1, 'Acre', 'AC'),
(2, 'Alagoas', 'AL'),
(3, 'Amapá', 'AP'),
(4, 'Amazonas', 'AM'),
(5, 'Bahia', 'BA'),
(6, 'Ceará', 'CE'),
(7, 'Distrito Federal', 'DF'),
(8, 'Espírito Santo', 'ES'),
(9, 'Goiás', 'GO'),
(10, 'Maranhão', 'MA'),
(11, 'Mato Grosso', 'MT'),
(12, 'Mato Grosso do Sul', 'MS'),
(13, 'Minas Gerais', 'MG'),
(14, 'Pará', 'PA'),
(15, 'Paraíba', 'PB'),
(16, 'Paraná', 'PR'),
(17, 'Pernambuco', 'PE'),
(19, 'Piauí', 'PI'),
(20, 'Rio Grande do Norte', 'RN'),
(21, 'Rio Grande do Sul', 'RS'),
(22, 'Rio de Janeiro', 'RJ'),
(24, 'Rondônia', 'RO'),
(25, 'Roraima', 'RA'),
(26, 'Santa Catarina', 'SC'),
(27, 'São Paulo', 'SP'),
(28, 'Santa Catarina', 'SC'),
(29, 'Sergipe', 'SE'),
(30, 'Tocantins', 'TO');

-- --------------------------------------------------------

--
-- Estrutura para tabela `fornecedores`
--

CREATE TABLE `fornecedores` (
  `fornecedorID` int NOT NULL,
  `nomefornecedor` varchar(50) DEFAULT NULL,
  `endereco` varchar(50) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `estadoID` tinyint DEFAULT NULL,
  `ddd` tinyint DEFAULT NULL,
  `telefone` varchar(14) DEFAULT NULL,
  `usuario` varchar(20) DEFAULT NULL,
  `senha` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `fornecedores`
--

INSERT INTO `fornecedores` (`fornecedorID`, `nomefornecedor`, `endereco`, `cidade`, `estadoID`, `ddd`, `telefone`, `usuario`, `senha`) VALUES
(1, 'Joe Mugger', 'Rua Ernesto de Paula Santos, 187', 'Recife', 17, 81, '949 568 7852', 'joe', '17r'),
(2, 'Dining Suppliers', '5 Hometown Dr.', 'São Paulo', 27, 11, '565 123 1223', 'sup', 'bin'),
(3, 'Pacific Merchandise', '56 Parkway Plaza', 'Rio de Janeiro', 22, 21, '310 345 4565', 'pmerch', '356'),
(4, 'Quick Clothing', '4598 Main St', 'Porto Alegre', 21, 51, '858 555 1654', 'qcloth', '1377');

-- --------------------------------------------------------

--
-- Estrutura para tabela `fornecedores_contatos`
--

CREATE TABLE `fornecedores_contatos` (
  `contatoID` int NOT NULL,
  `fornecedorID` int DEFAULT NULL,
  `departamentoID` int DEFAULT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `fornecedores_contatos`
--

INSERT INTO `fornecedores_contatos` (`contatoID`, `fornecedorID`, `departamentoID`, `nome`, `telefone`, `email`) VALUES
(1, 1, 1, 'Joana Piauí', '33262836', 'joana@joemugger.com'),
(2, 1, 2, 'Ricardo Prata', '33262836', 'ricardo@joemugger.com'),
(3, 2, 3, 'Gustavo Bege', '33262836', 'gustavo@dining.com'),
(4, 2, 2, 'Marta Borges', '33262836', 'marta@dining.com'),
(5, 3, 4, 'Fernando Maranhão', '33262836', 'fernando@pacific.com'),
(6, 3, 1, 'Ronaldo Catarinense', '33262836', 'ronaldo@pacific.com'),
(7, 4, 2, 'Alexandre Cisne', '33262836', 'alexandre@quickclothing.com'),
(8, 4, 1, 'Paulo José', '33262836', 'paulo@quickclothing.com'),
(9, 4, 4, 'Victor Nazário', '33262836', 'victor@quickclothing.com'),
(10, 4, 4, 'evellyn sales', '3326.2836', 'aneevellyn@gmail.com');

-- --------------------------------------------------------

--
-- Estrutura para tabela `franquias`
--

CREATE TABLE `franquias` (
  `franquiaID` int NOT NULL,
  `nomegerente` varchar(50) NOT NULL,
  `endereco` varchar(50) NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `estadoID` tinyint(1) NOT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  `dataabertura` date NOT NULL,
  `faturamento` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `franquias`
--

INSERT INTO `franquias` (`franquiaID`, `nomegerente`, `endereco`, `cidade`, `estadoID`, `telefone`, `dataabertura`, `faturamento`) VALUES
(1, 'Fabiana Albuquerque', 'Rua Jose Lourenço, 870 Sala 210', 'Fortaleza', 6, '085-2615554', '2006-05-18', '200000.00'),
(2, 'Neto Leal', 'Rua Ernesto de Paula Santos, 187 Sala 505', 'Recife', 17, '081.3326.2836', '2006-11-01', '300000.00'),
(3, 'Roberto Rabelo', 'Av. Antonio Carlos Magalhaes, 188', 'Salvador', 5, '071.3580705', '2006-12-16', '450000.00'),
(4, 'Victor Alves', 'Av. Barão de Studart, 101', 'Fortaleza', 6, '085.2480500', '2007-01-02', '150000.00'),
(5, 'Anne Sampaio', 'Av. Senhor do Bonfim', 'Salvador', 5, '417 625 6005', '2007-03-08', '280000.00'),
(6, 'Vinicius Samico', 'Av. Agamenon Magalhaes', 'Recife', 17, '081.33222233', '2007-05-01', '120000.00'),
(7, 'Paula Sanguinetti', 'Av. Presidente Prudente', 'Recife', 1, '081.3326.2938', '2007-10-11', '150000.00'),
(8, 'Michelle Alves', 'Av. Getúlio Vargas', 'Porto Alegre', 21, '051.3030302', '2007-11-20', '320000.00'),
(9, 'Saulo Brito', 'Av. São João, 10', 'São Paulo', 27, '011.3223-2232', '2008-04-02', '323221.00'),
(10, 'Davi Sampaio', 'Av. Copacabana, 101', 'Rio de Janeiro', 22, '021.3223-1010', '2008-05-01', '223421.00');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedidos`
--

CREATE TABLE `pedidos` (
  `pedidoID` int NOT NULL,
  `clienteID` int NOT NULL,
  `transportadoraID` int DEFAULT NULL,
  `data_pedido` date NOT NULL,
  `data_saida` date DEFAULT NULL,
  `data_entrega` date DEFAULT NULL,
  `status_pedido` tinyint NOT NULL,
  `valor_pedido` decimal(10,2) NOT NULL,
  `conhecimento` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `pedidos`
--

INSERT INTO `pedidos` (`pedidoID`, `clienteID`, `transportadoraID`, `data_pedido`, `data_saida`, `data_entrega`, `status_pedido`, `valor_pedido`, `conhecimento`) VALUES
(1, 7, 2, '2006-11-19', '2006-11-19', '2006-11-24', 1, '480.00', '2324324'),
(2, 8, 2, '2006-11-19', '2006-11-24', '2006-11-29', 1, '295.00', '2342342'),
(3, 8, 3, '2006-12-20', '2006-12-20', '2006-12-25', 2, '650.00', '2342341'),
(4, 22, 1, '2007-12-22', '2007-12-23', '2007-12-29', 1, '240.00', '2323424'),
(5, 33, 1, '2007-01-21', '2007-01-22', '2007-01-28', 1, '600.00', '4634633'),
(6, 33, 2, '2007-01-21', '2007-01-22', '2007-01-27', 1, '2720.00', '5453343'),
(7, 35, 1, '2007-01-24', '2007-01-25', '2007-01-28', 3, '260.00', '5646442'),
(8, 40, 3, '2007-01-27', '2007-01-29', '2007-01-31', 4, '1840.00', '4657574'),
(9, 43, 1, '2007-02-01', '2007-02-01', '2007-02-01', 1, '780.00', '9837958'),
(10, 48, 2, '2007-02-01', '2007-02-01', '2007-02-01', 2, '2240.00', '4345646'),
(11, 48, 3, '2007-02-03', '2007-02-03', '2007-02-08', 2, '1500.00', '7628364'),
(12, 22, 2, '2007-02-03', '2007-02-03', '2007-02-09', 1, '450.00', '6284882'),
(13, 35, 3, '2007-03-18', '2007-03-26', '2007-03-30', 1, '800.00', '7687688'),
(14, 40, 2, '2007-03-25', '2007-03-25', '2007-03-26', 2, '380.00', '8787999'),
(15, 7, 1, '2007-04-02', '2007-04-05', '2007-04-09', 2, '475.00', '2348729'),
(16, 22, 3, '2007-04-05', '2007-04-05', '2007-04-11', 1, '290.00', '3253221'),
(17, 50, 2, '2007-04-19', '2007-04-19', '2007-04-19', 2, '810.00', '3234221'),
(18, 8, 1, '2007-05-01', '2007-02-12', '2007-02-17', 2, '445.00', '2352329'),
(19, 7, 3, '2007-05-04', '2007-05-05', '2007-05-07', 1, '295.00', '7638888'),
(20, 50, 1, '2007-06-10', '2007-06-10', '2007-06-11', 2, '475.00', '7987989');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedidos_item`
--

CREATE TABLE `pedidos_item` (
  `pedidoID` int DEFAULT NULL,
  `produtoID` int DEFAULT NULL,
  `precounitario` decimal(10,2) DEFAULT NULL,
  `quantidade` smallint DEFAULT NULL,
  `id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `pedidos_item`
--

INSERT INTO `pedidos_item` (`pedidoID`, `produtoID`, `precounitario`, `quantidade`, `id`) VALUES
(1, 1, '20.00', 10, 1),
(1, 2, '9.00', 20, 2),
(1, 5, '20.00', 5, 3),
(2, 10, '5.00', 50, 4),
(2, 11, '9.00', 5, 5),
(3, 13, '14.00', 20, 6),
(3, 15, '14.00', 10, 7),
(3, 20, '12.00', 5, 8),
(3, 19, '12.00', 10, 9),
(3, 21, '5.00', 10, 10),
(4, 20, '12.00', 20, 11),
(5, 18, '12.00', 20, 12),
(5, 19, '12.00', 10, 13),
(5, 20, '12.00', 15, 14),
(5, 17, '12.00', 5, 15),
(6, 1, '20.00', 5, 16),
(6, 2, '9.00', 100, 17),
(6, 3, '3.00', 20, 18),
(6, 4, '3.00', 200, 19),
(6, 7, '14.00', 70, 20),
(6, 19, '12.00', 10, 21),
(7, 13, '14.00', 10, 22),
(7, 14, '9.00', 5, 23),
(7, 21, '5.00', 15, 24),
(8, 16, '12.00', 5, 25),
(8, 17, '12.00', 5, 26),
(8, 10, '12.00', 60, 27),
(8, 1, '20.00', 50, 28),
(9, 11, '12.00', 30, 29),
(9, 12, '21.00', 20, 30),
(10, 18, '12.00', 35, 31),
(10, 9, '5.00', 100, 32),
(10, 7, '7.00', 90, 33),
(10, 14, '9.00', 50, 34),
(10, 6, '14.00', 10, 35),
(10, 22, '2.00', 50, 36),
(11, 21, '5.00', 300, 37),
(12, 11, '12.00', 10, 38),
(12, 5, '21.00', 15, 39),
(12, 3, '3.00', 5, 40),
(13, 2, '14.00', 20, 41),
(13, 19, '12.00', 10, 42),
(13, 22, '2.00', 50, 43),
(13, 3, '3.00', 100, 44),
(14, 7, '7.00', 50, 45),
(14, 8, '3.00', 10, 46),
(15, 1, '20.00', 8, 47),
(15, 2, '9.00', 15, 48),
(15, 17, '12.00', 15, 49),
(16, 18, '12.00', 10, 50),
(16, 19, '12.00', 5, 51),
(16, 21, '5.00', 10, 52),
(16, 10, '12.00', 5, 53),
(17, 6, '14.00', 5, 54),
(17, 8, '3.00', 100, 55),
(17, 2, '9.00', 15, 56),
(17, 12, '21.00', 5, 57),
(17, 13, '14.00', 5, 58),
(17, 15, '14.00', 5, 59),
(17, 17, '12.00', 5, 60),
(18, 1, '20.00', 20, 61),
(18, 3, '3.00', 15, 62),
(19, 21, '5.00', 20, 63),
(19, 7, '7.00', 15, 64),
(19, 14, '9.00', 10, 65),
(20, 18, '12.00', 20, 66),
(20, 19, '12.00', 10, 67),
(20, 22, '2.00', 15, 68),
(20, 8, '3.00', 5, 69),
(20, 15, '14.00', 5, 70);

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedidos_status`
--

CREATE TABLE `pedidos_status` (
  `statusID` int NOT NULL,
  `nomestatus` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `pedidos_status`
--

INSERT INTO `pedidos_status` (`statusID`, `nomestatus`) VALUES
(1, 'Pagamento Confirmado'),
(2, 'Pagamento Pendente'),
(3, 'Cancelado pelo cliente'),
(4, 'Cancelado pela empresa');

-- --------------------------------------------------------

--
-- Estrutura para tabela `produtos`
--

CREATE TABLE `produtos` (
  `produtoID` int NOT NULL,
  `nomeproduto` varchar(50) DEFAULT NULL,
  `descricao` longtext,
  `codigobarra` varchar(15) DEFAULT NULL,
  `tempoentrega` tinyint DEFAULT NULL,
  `precorevenda` decimal(10,2) DEFAULT NULL,
  `precounitario` decimal(10,2) DEFAULT NULL,
  `estoque` mediumint DEFAULT NULL,
  `imagemgrande` varchar(100) NOT NULL,
  `imagempequena` varchar(100) NOT NULL,
  `descontinuado` tinyint(1) DEFAULT '0',
  `fornecedorID` tinyint DEFAULT NULL,
  `categoriaID` tinyint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `produtos`
--

INSERT INTO `produtos` (`produtoID`, `nomeproduto`, `descricao`, `codigobarra`, `tempoentrega`, `precorevenda`, `precounitario`, `estoque`, `imagemgrande`, `imagempequena`, `descontinuado`, `fornecedorID`, `categoriaID`) VALUES
(1, 'Biscottis', 'All-natural bite-sized biscuits.', '789151 823800', 15, '10.00', '20.00', 100, 'images/product_images/HoneyBiscotti_Big.jpg', 'images/product_images/HoneyBiscotti_Smallb.jpg', 0, 2, 2),
(2, 'Organic Earl Grey', 'Because once in a blue moon you might want something besides coffee. This blend of black and green teas is highly aromatic, rich and flavorful with a hint of light citrus.', '789151 823798', 8, '6.00', '9.00', 1000, 'images/product_images/EarlGreyTea_Big.jpg', 'images/product_images/EarlGreyTea_Smallb.jpg', 0, 1, 2),
(3, 'Sugar', 'How many spoonfuls do you need? Crystallized from 100% organic sugar cane, and milled within 24 hours of harvest to ensure it\'s as fresh as our coffee beans.', '789151 823797', 8, '1.00', '3.00', 500, 'images/product_images/Sugar_Big.jpg', 'images/product_images/Sugar_Smallb.jpg', 0, 2, 2),
(4, 'Non-Diary Creamer', 'If running out of milk or cream for your coffee is tantamount to a state of emergency, we suggest you stock up on these delicious non-dairy creamers just in case.', '789151 823796', 5, '2.00', '3.00', 500, 'images/product_images/NonDairyCreamer_Big.jpg', 'images/product_images/NonDairyCreamer_Smallb.jpg', 0, 2, 2),
(5, 'Steel Mug', 'Here\'s one way to make sure your coffee stays warm during a long commute. Made of lightweight metal alloy.', '789151 823795', 15, '15.00', '21.00', 300, 'images/product_images/SteelMug_Big.jpg', 'images/product_images/SteelMug_Smallb.jpg', 0, 3, 3),
(6, 'Ceramic Mug', 'Handcrafted by Colorado artisans. These generous mugs feature an opaque green satin glaze over classic stoneware.', '789151 823799', 15, '10.00', '14.00', 80, 'images/product_images/CeramicMug_Big.jpg', 'images/product_images/CeramicMug_Smallb.jpg', 0, 3, 3),
(7, 'Plastic Mug', 'If you\'re a little klutzy in the morning, we recommend this shatter-proof, durable plastic commuter mug.', '789151 823795', 8, '5.00', '7.00', 750, 'images/product_images/PlasticMug_Big.jpg', 'images/product_images/PlasticMug_Smallb.jpg', 0, 3, 3),
(8, 'Thermometer', 'Ideal for microwaving your coffee. With a stainless steel stem, large, easy-to-read digital display and case.', '789151 823654', 30, '1.50', '3.00', 45, 'images/product_images/Thermometer_Big.jpg', 'images/product_images/Thermometer_Smallb.jpg', 0, 3, 3),
(9, 'Hype Filters', 'Never resort to using papers towels when you\'re out of paper filters. This Gold-Tone filter is always ready.', '789151 823655', 5, '2.80', '5.00', 50, 'images/product_images/HypeFilters_Big.jpg', 'images/product_images/HypeFilters_Smallb.jpg', 0, 3, 3),
(10, 'Brave New World T-Shirt', '100% cotton. Available in black, mocha or white.', '789151 823765', 5, '8.00', '12.00', 60, 'images/product_images/TShirt_Big.jpg', 'images/product_images/TShirt_Smallb.jpg', 0, 4, 4),
(11, 'Brave Blend', 'Grown on some of the highest peaks in Brazil, India, Kenya and Puerto Rico, this blend represents the best arabica beans the world has to offer.', '789151 823765', 15, '8.00', '12.00', 100, 'images/product_images/BraveBlend_Group_Big.jpg', 'images/product_images/BraveBlend_Group_Smallb.jpg', 0, 1, 1),
(12, 'Brave New World Sweatshirt', '- Perfect for lazing around on a Sunday morning with the paper and a cup of your favorite blend. Pigment-dyed for lasting color. Ribbed cuff and bottom.', '789151 823658', 15, '8.00', '21.00', 250, 'images/product_images/Sweatshirt_Big.jpg', 'images/product_images/Sweatshirt_Smallb.jpg', 0, 4, 4),
(13, 'Andes Baseball Cap', 'You\'re groggy and need coffee right away. This is no time to worry about your hair. Throw on this cap and head to the nearest ANDES. Cotton, adjustable, available in two colors.', '789151 823659', 5, '11.00', '14.00', 40, 'images/product_images/Baseballcap_Big.jpg', 'images/product_images/Baseballcap_Smallb.jpg', 0, 4, 4),
(14, 'Andes Toque', 'Style comes with a layer of Comfort Max lycra stretch material on the inside and a tasty ANDES logo on the outside.', '789151 823564', 5, '5.00', '9.00', 80, 'images/product_images/Toke_Big.jpg', 'images/product_images/Toke_Smallb.jpg', 0, 4, 4),
(15, 'Audio CD', 'Our very own coffee house collection, featuring poetry slams, soulful vocals and a generous helping of the blues.', '789151 823732', 5, '11.00', '14.00', 10, 'images/product_images/MusicCD_Big.jpg', 'images/product_images/MusicCD_Smallb.jpg', 0, 3, 3),
(16, 'Year 1999 Blend', 'Java, Mysore and Sumatra beans offer a mellow flavor to make all the Year 2000 hype more palatable.', '789151 823455', 5, '9.00', '12.00', 45, 'images/product_images/Year1999Blend_Group_Big.jpg', 'images/product_images/Year1999Blend_Group_Smallb.jpg', 0, 1, 1),
(17, 'Border Blend', 'Columbia, Costa Rica and Estate Java beans offer a mellow flavor to make all the Year 2000 hype more palatable.', '782341 823795', 5, '6.00', '12.00', 30, 'images/product_images/BorderBlend_Group_Big.jpg', 'images/product_images/BorderBlend_Group_Smallb.jpg', 0, 1, 1),
(18, 'Blond Blend', 'Processed for lower levels of caffeine without reducing the integrity of this rich Costa Rica bean.', '734561 823795', 5, '7.50', '12.00', 10, 'images/product_images/BlondBlend_Group_Big.jpg', 'images/product_images/BlondBlend_Group_Smallb.jpg', 0, 1, 1),
(19, 'Winter Blend', '- Columbia and Jamaica beans create a full-bodied, mellow, slightly nutty flavor.', '798751 823795', 8, '7.50', '12.00', 5, 'images/product_images/WinterBlend_Group_Big.jpg', 'images/product_images/WinterBlend_Group_Smallb.jpg', 0, 1, 1),
(20, 'Chocolate Mocha Bars', 'Very European and very decadent. Drop these milk chocolates into your coffee to release a rich mocha aroma and pool of hot chocolate.', '123151 823795', 15, '9.00', '12.00', 25, 'images/product_images/ChocolateMochaBars_Big.jpg', 'images/product_images/ChocolateMochaBars_Smallb.jpg', 0, 2, 2),
(21, 'Chocolate Covered Coffee Beans', 'Made for all-nighters, afternoon lulls, and long drives. These are the times when you need a sweet jolt.', '784561 823795', 30, '3.00', '5.00', 30, 'images/product_images/ChocolateCoffeBeans_Big.jpg', 'images/product_images/ChocolateCoffeBeans_Smallb.jpg', 0, 2, 2),
(22, 'Breath Mints', 'No one need know how many cups of coffee you consume in a day. Hide it well with these powerfully refreshing mints.', '789151 823980', 30, '1.00', '2.00', 60, 'images/product_images/BreathMints_Big.jpg', 'images/product_images/BreathMints_Smallb.jpg', 0, 2, 2),
(35, 'Teste', 'Teste de inclusão', '1234567891078', 5, '1.00', '4.00', 40, 'images/product_images/foto_12_05_2021224647_3CWBDNEBLV8ESK.jpg', 'images/product_images/foto_12_05_2021224647_V8RWXU5YXA3THF.png', NULL, 1, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `transportadoras`
--

CREATE TABLE `transportadoras` (
  `transportadoraID` int NOT NULL,
  `nometransportadora` varchar(50) DEFAULT NULL,
  `endereco` varchar(50) DEFAULT NULL,
  `telefone` varchar(50) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `estadoID` tinyint DEFAULT NULL,
  `cep` varchar(10) DEFAULT NULL,
  `cnpj` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Despejando dados para a tabela `transportadoras`
--

INSERT INTO `transportadoras` (`transportadoraID`, `nometransportadora`, `endereco`, `telefone`, `cidade`, `estadoID`, `cep`, `cnpj`) VALUES
(1, 'Rapidão Estrela', 'Rua Ernesto de Paula Santos, 187', '33262836', 'Recife', 17, '51.021-330', '2234234234'),
(2, 'Itapemirão', 'Rua Visconde de Sabugosa, 11', '33262836', 'São Paulo', 27, '01.323.123', '2424243221'),
(3, 'SEDEX', 'Av Ipanema, 22123', '33262836', 'Rio de Janeiro', 21, '02.320.121', '2342424324'),
(6, 'Vietnã', 'Rua da Simpatia, 80', '+5587988596558', 'Petrolina', 17, '56304-440', '18.984.560/0003-55');

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Índices de tabela `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Índices de tabela `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Índices de tabela `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Índices de tabela `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Índices de tabela `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Índices de tabela `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`categoriaID`);

--
-- Índices de tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`clienteID`);

--
-- Índices de tabela `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`departamentoID`);

--
-- Índices de tabela `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Índices de tabela `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Índices de tabela `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Índices de tabela `estados`
--
ALTER TABLE `estados`
  ADD PRIMARY KEY (`estadoID`);

--
-- Índices de tabela `fornecedores`
--
ALTER TABLE `fornecedores`
  ADD PRIMARY KEY (`fornecedorID`);

--
-- Índices de tabela `fornecedores_contatos`
--
ALTER TABLE `fornecedores_contatos`
  ADD PRIMARY KEY (`contatoID`);

--
-- Índices de tabela `franquias`
--
ALTER TABLE `franquias`
  ADD PRIMARY KEY (`franquiaID`);

--
-- Índices de tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`pedidoID`);

--
-- Índices de tabela `pedidos_item`
--
ALTER TABLE `pedidos_item`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `pedidos_status`
--
ALTER TABLE `pedidos_status`
  ADD PRIMARY KEY (`statusID`);

--
-- Índices de tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`produtoID`);

--
-- Índices de tabela `transportadoras`
--
ALTER TABLE `transportadoras`
  ADD PRIMARY KEY (`transportadoraID`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT de tabela `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `categorias`
--
ALTER TABLE `categorias`
  MODIFY `categoriaID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `clienteID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT de tabela `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `departamentoID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de tabela `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT de tabela `estados`
--
ALTER TABLE `estados`
  MODIFY `estadoID` tinyint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de tabela `fornecedores`
--
ALTER TABLE `fornecedores`
  MODIFY `fornecedorID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `fornecedores_contatos`
--
ALTER TABLE `fornecedores_contatos`
  MODIFY `contatoID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `franquias`
--
ALTER TABLE `franquias`
  MODIFY `franquiaID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `pedidoID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de tabela `pedidos_item`
--
ALTER TABLE `pedidos_item`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT de tabela `pedidos_status`
--
ALTER TABLE `pedidos_status`
  MODIFY `statusID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `produtoID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de tabela `transportadoras`
--
ALTER TABLE `transportadoras`
  MODIFY `transportadoraID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Restrições para tabelas `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Restrições para tabelas `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Restrições para tabelas `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Restrições para tabelas `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
