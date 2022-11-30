--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 14.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin_black_adminblacksetting; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.admin_black_adminblacksetting (
    id bigint NOT NULL,
    sidebar_background character varying(20) NOT NULL,
    dark_mode smallint NOT NULL,
    created_at timestamp(6) without time zone NOT NULL,
    updated_at timestamp(6) without time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.admin_black_adminblacksetting OWNER TO vtliqlvhugzosr;

--
-- Name: admin_black_adminblacksetting_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.admin_black_adminblacksetting_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.admin_black_adminblacksetting_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: admin_black_adminblacksetting_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.admin_black_adminblacksetting_id_seq OWNED BY public.admin_black_adminblacksetting.id;


--
-- Name: admin_tools_dashboard_preferences; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.admin_tools_dashboard_preferences (
    id bigint NOT NULL,
    data text NOT NULL,
    dashboard_id character varying(100) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.admin_tools_dashboard_preferences OWNER TO vtliqlvhugzosr;

--
-- Name: admin_tools_dashboard_preferences_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.admin_tools_dashboard_preferences_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.admin_tools_dashboard_preferences_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: admin_tools_dashboard_preferences_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.admin_tools_dashboard_preferences_id_seq OWNED BY public.admin_tools_dashboard_preferences.id;


--
-- Name: admin_tools_menu_bookmark; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.admin_tools_menu_bookmark (
    id bigint NOT NULL,
    url character varying(255) NOT NULL,
    title character varying(255) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.admin_tools_menu_bookmark OWNER TO vtliqlvhugzosr;

--
-- Name: admin_tools_menu_bookmark_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.admin_tools_menu_bookmark_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.admin_tools_menu_bookmark_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: admin_tools_menu_bookmark_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.admin_tools_menu_bookmark_id_seq OWNED BY public.admin_tools_menu_bookmark.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO vtliqlvhugzosr;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO vtliqlvhugzosr;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO vtliqlvhugzosr;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp(6) without time zone,
    is_superuser smallint NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff smallint NOT NULL,
    is_active smallint NOT NULL,
    date_joined timestamp(6) without time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO vtliqlvhugzosr;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO vtliqlvhugzosr;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO vtliqlvhugzosr;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: categorias; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.categorias (
    "categoriaID" integer NOT NULL,
    nomecategoria character varying(50)
);


ALTER TABLE public.categorias OWNER TO vtliqlvhugzosr;

--
-- Name: categorias_categoriaID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."categorias_categoriaID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."categorias_categoriaID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: categorias_categoriaID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."categorias_categoriaID_seq" OWNED BY public.categorias."categoriaID";


--
-- Name: clientes; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.clientes (
    "clienteID" integer NOT NULL,
    nomecompleto character varying(50),
    endereco character varying(50),
    complemento character varying(30),
    numero character varying(15),
    cidade character varying(50),
    "estadoID" smallint,
    cep character varying(10),
    ddd character varying(3),
    telefone character varying(10),
    email character varying(50),
    usuario character varying(10),
    senha character varying(10)
);


ALTER TABLE public.clientes OWNER TO vtliqlvhugzosr;

--
-- Name: clientes_clienteID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."clientes_clienteID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."clientes_clienteID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: clientes_clienteID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."clientes_clienteID_seq" OWNED BY public.clientes."clienteID";


--
-- Name: departamentos; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.departamentos (
    "departamentoID" integer NOT NULL,
    nomedepartamento character varying(50)
);


ALTER TABLE public.departamentos OWNER TO vtliqlvhugzosr;

--
-- Name: departamentos_departamentoID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."departamentos_departamentoID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."departamentos_departamentoID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: departamentos_departamentoID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."departamentos_departamentoID_seq" OWNED BY public.departamentos."departamentoID";


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp(6) without time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag integer NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL
);


ALTER TABLE public.django_admin_log OWNER TO vtliqlvhugzosr;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO vtliqlvhugzosr;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp(6) without time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO vtliqlvhugzosr;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp(6) without time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO vtliqlvhugzosr;

--
-- Name: estados; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.estados (
    "estadoID" integer NOT NULL,
    nome character(20) DEFAULT 0,
    sigla character(2)
);


ALTER TABLE public.estados OWNER TO vtliqlvhugzosr;

--
-- Name: estados_estadoID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."estados_estadoID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."estados_estadoID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: estados_estadoID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."estados_estadoID_seq" OWNED BY public.estados."estadoID";


--
-- Name: fornecedores; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.fornecedores (
    "fornecedorID" integer NOT NULL,
    nomefornecedor character varying(50),
    endereco character varying(50),
    cidade character varying(50),
    "estadoID" smallint,
    ddd smallint,
    telefone character varying(14),
    usuario character varying(20),
    senha character varying(20),
    cep character varying(9),
    email character varying(50)
);


ALTER TABLE public.fornecedores OWNER TO vtliqlvhugzosr;

--
-- Name: fornecedores_contatos; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.fornecedores_contatos (
    "contatoID" integer NOT NULL,
    "fornecedorID" integer,
    "departamentoID" integer,
    nome character varying(50),
    telefone character varying(15),
    email character varying(50)
);


ALTER TABLE public.fornecedores_contatos OWNER TO vtliqlvhugzosr;

--
-- Name: fornecedores_contatos_contatoID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."fornecedores_contatos_contatoID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."fornecedores_contatos_contatoID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: fornecedores_contatos_contatoID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."fornecedores_contatos_contatoID_seq" OWNED BY public.fornecedores_contatos."contatoID";


--
-- Name: fornecedores_fornecedorID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."fornecedores_fornecedorID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."fornecedores_fornecedorID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: fornecedores_fornecedorID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."fornecedores_fornecedorID_seq" OWNED BY public.fornecedores."fornecedorID";


--
-- Name: pedidos; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.pedidos (
    "pedidoID" integer NOT NULL,
    "clienteID" integer NOT NULL,
    "transportadoraID" integer,
    data_pedido date NOT NULL,
    data_saida date,
    data_entrega date,
    status_pedido smallint NOT NULL,
    valor_pedido numeric(10,2) NOT NULL,
    conhecimento character varying(20)
);


ALTER TABLE public.pedidos OWNER TO vtliqlvhugzosr;

--
-- Name: pedidos_item; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.pedidos_item (
    "pedidoID" integer,
    "produtoID" integer,
    precounitario numeric(10,2),
    quantidade smallint,
    id bigint NOT NULL
);


ALTER TABLE public.pedidos_item OWNER TO vtliqlvhugzosr;

--
-- Name: pedidos_item_id_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public.pedidos_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pedidos_item_id_seq OWNER TO vtliqlvhugzosr;

--
-- Name: pedidos_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public.pedidos_item_id_seq OWNED BY public.pedidos_item.id;


--
-- Name: pedidos_pedidoID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."pedidos_pedidoID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."pedidos_pedidoID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: pedidos_pedidoID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."pedidos_pedidoID_seq" OWNED BY public.pedidos."pedidoID";


--
-- Name: pedidos_status; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.pedidos_status (
    "statusID" integer NOT NULL,
    nomestatus character varying(50) NOT NULL
);


ALTER TABLE public.pedidos_status OWNER TO vtliqlvhugzosr;

--
-- Name: pedidos_status_statusID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."pedidos_status_statusID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."pedidos_status_statusID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: pedidos_status_statusID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."pedidos_status_statusID_seq" OWNED BY public.pedidos_status."statusID";


--
-- Name: produtos; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.produtos (
    "produtoID" integer NOT NULL,
    nomeproduto character varying(50),
    descricao text,
    codigobarra character varying(15),
    tempoentrega smallint,
    precorevenda numeric(10,2),
    precounitario numeric(10,2),
    estoque integer,
    imagemgrande character varying(100) NOT NULL,
    imagempequena character varying(100) NOT NULL,
    "fornecedorID" smallint,
    "categoriaID" smallint
);


ALTER TABLE public.produtos OWNER TO vtliqlvhugzosr;

--
-- Name: produtos_clientes; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.produtos_clientes (
    "produtoID" integer NOT NULL,
    nomeproduto character varying(50),
    descricao text,
    codigobarra character varying(15),
    tempoentrega smallint,
    precorevenda numeric(10,2),
    precounitario numeric(10,2),
    estoque integer,
    imagemgrande character varying(100) NOT NULL,
    imagempequena character varying(100) NOT NULL,
    descontinuado smallint DEFAULT 0,
    "fornecedorID" smallint,
    "categoriaID" smallint
);


ALTER TABLE public.produtos_clientes OWNER TO vtliqlvhugzosr;

--
-- Name: produtos_clientes_produtoID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."produtos_clientes_produtoID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."produtos_clientes_produtoID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: produtos_clientes_produtoID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."produtos_clientes_produtoID_seq" OWNED BY public.produtos_clientes."produtoID";


--
-- Name: produtos_produtoID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."produtos_produtoID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."produtos_produtoID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: produtos_produtoID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."produtos_produtoID_seq" OWNED BY public.produtos."produtoID";


--
-- Name: produtos_standby; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.produtos_standby (
    "produtoID" integer NOT NULL,
    nomeproduto character varying(50),
    descricao text,
    codigobarra character varying(15),
    tempoentrega smallint,
    precorevenda numeric(10,2),
    precounitario numeric(10,2),
    estoque integer,
    imagemgrande character varying(100) NOT NULL,
    imagempequena character varying(100) NOT NULL,
    "fornecedorID" smallint,
    "categoriaID" smallint
);


ALTER TABLE public.produtos_standby OWNER TO vtliqlvhugzosr;

--
-- Name: transportadoras; Type: TABLE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE TABLE public.transportadoras (
    "transportadoraID" integer NOT NULL,
    nometransportadora character varying(50),
    endereco character varying(50),
    telefone character varying(50),
    cidade character varying(50),
    "estadoID" smallint,
    cep character varying(10),
    cnpj character varying(19)
);


ALTER TABLE public.transportadoras OWNER TO vtliqlvhugzosr;

--
-- Name: transportadoras_transportadoraID_seq; Type: SEQUENCE; Schema: public; Owner: vtliqlvhugzosr
--

CREATE SEQUENCE public."transportadoras_transportadoraID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."transportadoras_transportadoraID_seq" OWNER TO vtliqlvhugzosr;

--
-- Name: transportadoras_transportadoraID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vtliqlvhugzosr
--

ALTER SEQUENCE public."transportadoras_transportadoraID_seq" OWNED BY public.transportadoras."transportadoraID";


--
-- Name: admin_black_adminblacksetting id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_black_adminblacksetting ALTER COLUMN id SET DEFAULT nextval('public.admin_black_adminblacksetting_id_seq'::regclass);


--
-- Name: admin_tools_dashboard_preferences id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_tools_dashboard_preferences ALTER COLUMN id SET DEFAULT nextval('public.admin_tools_dashboard_preferences_id_seq'::regclass);


--
-- Name: admin_tools_menu_bookmark id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_tools_menu_bookmark ALTER COLUMN id SET DEFAULT nextval('public.admin_tools_menu_bookmark_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: categorias categoriaID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.categorias ALTER COLUMN "categoriaID" SET DEFAULT nextval('public."categorias_categoriaID_seq"'::regclass);


--
-- Name: clientes clienteID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.clientes ALTER COLUMN "clienteID" SET DEFAULT nextval('public."clientes_clienteID_seq"'::regclass);


--
-- Name: departamentos departamentoID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.departamentos ALTER COLUMN "departamentoID" SET DEFAULT nextval('public."departamentos_departamentoID_seq"'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: estados estadoID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.estados ALTER COLUMN "estadoID" SET DEFAULT nextval('public."estados_estadoID_seq"'::regclass);


--
-- Name: fornecedores fornecedorID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.fornecedores ALTER COLUMN "fornecedorID" SET DEFAULT nextval('public."fornecedores_fornecedorID_seq"'::regclass);


--
-- Name: fornecedores_contatos contatoID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.fornecedores_contatos ALTER COLUMN "contatoID" SET DEFAULT nextval('public."fornecedores_contatos_contatoID_seq"'::regclass);


--
-- Name: pedidos pedidoID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.pedidos ALTER COLUMN "pedidoID" SET DEFAULT nextval('public."pedidos_pedidoID_seq"'::regclass);


--
-- Name: pedidos_item id; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.pedidos_item ALTER COLUMN id SET DEFAULT nextval('public.pedidos_item_id_seq'::regclass);


--
-- Name: pedidos_status statusID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.pedidos_status ALTER COLUMN "statusID" SET DEFAULT nextval('public."pedidos_status_statusID_seq"'::regclass);


--
-- Name: produtos produtoID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.produtos ALTER COLUMN "produtoID" SET DEFAULT nextval('public."produtos_produtoID_seq"'::regclass);


--
-- Name: produtos_clientes produtoID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.produtos_clientes ALTER COLUMN "produtoID" SET DEFAULT nextval('public."produtos_clientes_produtoID_seq"'::regclass);


--
-- Name: transportadoras transportadoraID; Type: DEFAULT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.transportadoras ALTER COLUMN "transportadoraID" SET DEFAULT nextval('public."transportadoras_transportadoraID_seq"'::regclass);


--
-- Data for Name: admin_black_adminblacksetting; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.admin_black_adminblacksetting (id, sidebar_background, dark_mode, created_at, updated_at, user_id) FROM stdin;
1	blue	0	2021-05-25 14:25:08.877904	2021-05-25 14:29:14.677061	1
\.


--
-- Data for Name: admin_tools_dashboard_preferences; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.admin_tools_dashboard_preferences (id, data, dashboard_id, user_id) FROM stdin;
1	{"positions":["module_2","module_4","module_3","module_5","module_6"],"columns":[2,4],"disabled":{},"collapsed":{}}	dashboard	1
2	{}	autenticacao-e-autorizacao-dashboard	1
\.


--
-- Data for Name: admin_tools_menu_bookmark; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.admin_tools_menu_bookmark (id, url, title, user_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add categorias	7	add_categorias
26	Can change categorias	7	change_categorias
27	Can delete categorias	7	delete_categorias
28	Can view categorias	7	view_categorias
29	Can add clientes	8	add_clientes
30	Can change clientes	8	change_clientes
31	Can delete clientes	8	delete_clientes
32	Can view clientes	8	view_clientes
33	Can add departamentos	9	add_departamentos
34	Can change departamentos	9	change_departamentos
35	Can delete departamentos	9	delete_departamentos
36	Can view departamentos	9	view_departamentos
37	Can add estados	10	add_estados
38	Can change estados	10	change_estados
39	Can delete estados	10	delete_estados
40	Can view estados	10	view_estados
41	Can add fornecedores	11	add_fornecedores
42	Can change fornecedores	11	change_fornecedores
43	Can delete fornecedores	11	delete_fornecedores
44	Can view fornecedores	11	view_fornecedores
45	Can add fornecedores contatos	12	add_fornecedorescontatos
46	Can change fornecedores contatos	12	change_fornecedorescontatos
47	Can delete fornecedores contatos	12	delete_fornecedorescontatos
48	Can view fornecedores contatos	12	view_fornecedorescontatos
49	Can add franquias	13	add_franquias
50	Can change franquias	13	change_franquias
51	Can delete franquias	13	delete_franquias
52	Can view franquias	13	view_franquias
53	Can add produtos	14	add_produtos
54	Can change produtos	14	change_produtos
55	Can delete produtos	14	delete_produtos
56	Can view produtos	14	view_produtos
57	Can add transportadoras	15	add_transportadoras
58	Can change transportadoras	15	change_transportadoras
59	Can delete transportadoras	15	delete_transportadoras
60	Can view transportadoras	15	view_transportadoras
61	Can add pedidos	16	add_pedidos
62	Can change pedidos	16	change_pedidos
63	Can delete pedidos	16	delete_pedidos
64	Can view pedidos	16	view_pedidos
65	Can add pedidos item	17	add_pedidositem
66	Can change pedidos item	17	change_pedidositem
67	Can delete pedidos item	17	delete_pedidositem
68	Can view pedidos item	17	view_pedidositem
69	Can add pedidos status	18	add_pedidosstatus
70	Can change pedidos status	18	change_pedidosstatus
71	Can delete pedidos status	18	delete_pedidosstatus
72	Can view pedidos status	18	view_pedidosstatus
73	Can add document	19	add_document
74	Can change document	19	change_document
75	Can delete document	19	delete_document
76	Can view document	19	view_document
77	Can add pedidos	20	add_pedidos
78	Can change pedidos	20	change_pedidos
79	Can delete pedidos	20	delete_pedidos
80	Can view pedidos	20	view_pedidos
81	Can add pedidos item	21	add_pedidositem
82	Can change pedidos item	21	change_pedidositem
83	Can delete pedidos item	21	delete_pedidositem
84	Can view pedidos item	21	view_pedidositem
85	Can add pedidos status	22	add_pedidosstatus
86	Can change pedidos status	22	change_pedidosstatus
87	Can delete pedidos status	22	delete_pedidosstatus
88	Can view pedidos status	22	view_pedidosstatus
89	Can add categorias	23	add_categorias
90	Can change categorias	23	change_categorias
91	Can delete categorias	23	delete_categorias
92	Can view categorias	23	view_categorias
93	Can add departamentos	24	add_departamentos
94	Can change departamentos	24	change_departamentos
95	Can delete departamentos	24	delete_departamentos
96	Can view departamentos	24	view_departamentos
97	Can add estados	25	add_estados
98	Can change estados	25	change_estados
99	Can delete estados	25	delete_estados
100	Can view estados	25	view_estados
101	Can add clientes	26	add_clientes
102	Can change clientes	26	change_clientes
103	Can delete clientes	26	delete_clientes
104	Can view clientes	26	view_clientes
105	Can add fornecedores	27	add_fornecedores
106	Can change fornecedores	27	change_fornecedores
107	Can delete fornecedores	27	delete_fornecedores
108	Can view fornecedores	27	view_fornecedores
109	Can add fornecedores contatos	28	add_fornecedorescontatos
110	Can change fornecedores contatos	28	change_fornecedorescontatos
111	Can delete fornecedores contatos	28	delete_fornecedorescontatos
112	Can view fornecedores contatos	28	view_fornecedorescontatos
113	Can add dashboard setting	29	add_adminblacksetting
114	Can change dashboard setting	29	change_adminblacksetting
115	Can delete dashboard setting	29	delete_adminblacksetting
116	Can view dashboard setting	29	view_adminblacksetting
117	Can add bookmark	30	add_bookmark
118	Can change bookmark	30	change_bookmark
119	Can delete bookmark	30	delete_bookmark
120	Can view bookmark	30	view_bookmark
121	Can add dashboard preferences	31	add_dashboardpreferences
122	Can change dashboard preferences	31	change_dashboardpreferences
123	Can delete dashboard preferences	31	delete_dashboardpreferences
124	Can view dashboard preferences	31	view_dashboardpreferences
125	Can add Produto do Cliente	32	add_produtosclientes
126	Can change Produto do Cliente	32	change_produtosclientes
127	Can delete Produto do Cliente	32	delete_produtosclientes
128	Can view Produto do Cliente	32	view_produtosclientes
129	Can add Produto em Negociação	33	add_produtosstandby
130	Can change Produto em Negociação	33	change_produtosstandby
131	Can delete Produto em Negociação	33	delete_produtosstandby
132	Can view Produto em Negociação	33	view_produtosstandby
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$260000$bVfQa9nfw4EsJu4LoqbMDw$ybA8OWLsAtKJ0qWKh5xEzuw5/Fdp0V4uqL+odDMjTGw=	2021-06-04 01:35:50.211057	1	projetoSD				1	1	2021-05-24 13:45:30
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	1	11
12	1	12
13	1	13
14	1	14
15	1	15
16	1	16
17	1	17
18	1	18
19	1	19
20	1	20
21	1	21
22	1	22
23	1	23
24	1	24
25	1	25
26	1	26
27	1	27
28	1	28
29	1	29
30	1	30
31	1	31
32	1	32
33	1	33
34	1	34
35	1	35
36	1	36
37	1	37
38	1	38
39	1	39
40	1	40
41	1	41
42	1	42
43	1	43
44	1	44
45	1	45
46	1	46
47	1	47
48	1	48
49	1	49
50	1	50
51	1	51
52	1	52
53	1	53
54	1	54
55	1	55
56	1	56
57	1	57
58	1	58
59	1	59
60	1	60
61	1	61
62	1	62
63	1	63
64	1	64
65	1	65
66	1	66
67	1	67
68	1	68
69	1	69
70	1	70
71	1	71
72	1	72
73	1	73
74	1	74
75	1	75
76	1	76
77	1	77
78	1	78
79	1	79
80	1	80
81	1	81
82	1	82
83	1	83
84	1	84
85	1	85
86	1	86
87	1	87
88	1	88
89	1	89
90	1	90
91	1	91
92	1	92
93	1	93
94	1	94
95	1	95
96	1	96
97	1	97
98	1	98
99	1	99
100	1	100
\.


--
-- Data for Name: categorias; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.categorias ("categoriaID", nomecategoria) FROM stdin;
1	Coffee
2	Food
3	Merchandise
4	Clothing
\.


--
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.clientes ("clienteID", nomecompleto, endereco, complemento, numero, cidade, "estadoID", cep, ddd, telefone, email, usuario, senha) FROM stdin;
7	Bob	Kobe Dr	Suite 31	2929 	São Paulo	27	92123	11	99999-0001	bobrob@dru	bobrob	cheese
8	Lee	Priestly Dr	Suite 30	5927 	Rio de Janeiro	22	92008	21	9999-0101	ldkim@drum	ldkim	drums
9	Jane	Priestly Dr	Suite 01	5924 	Recife	17	92008	81	9999-0202	jstev@fili	zac	zac
33	Mary	Mill Lane	House	22	Rio de Janeiro	22	P0987GH	21	9999-0303	mary@sheep.com	mary	baa
34	Adriaan	Main St.	House	31	Porto Alegre	21	90876	51	9999-0001	joe@blow.net	joe	blow
35	Yeshe	Place des Vosges	House	26 	Recife	17	75003	81	9999-0404	kako@alibert.org	kako	crow
36	Jean-Claude	Rue des Archives	Suite 31	26 	Salvador	5	75003	71	9999-0500	bouquet@paris.com	bouquet	archives
37	Charmian	Biscane Boulevard	Suite 55	21	Fortaleza	6	87543	85	9999-0001	thepet@cows.com	petty	officer
38	Tex	Ocean Dr	Suite 11	32	Fortaleza	6	92107	85	9999-0002	minou@sefton.com	minou	lechat
39	James	Lotus St	Suite 533	33	Belo Horizonte	13	92107	31	9999-0001	jjones@thing.com	jj	magenta
40	Scott	Harley St.	Suite 31	1312 	Curitiba	16	41414	41	9999-4001	scottie@theworks.camvria.com	scooby	doo
41	Mavis	The Lane	Suite 01	774	Florianopolis	28	99999	48	9999-0001	mave@formerly.sisters.org	mkirk	jesus
42	Morton	Kwai	Suite 02	101	João Pessoa	15	71717	83	9999-0001	mgold@brockyard.herrr.org	gold	rng665
43	Monica	Arbor Drive	Suite 01	21 	Belém	14	91111	91	9999-0001	birch@nobodys.fool.com	birch	bsgr%
44	Amos	Framingham Ave	Suite 10	4545 	Manaus	4	31311	92	9999-0001	add@barnham.peoples.com	adur	adur
45	Pietro	Vagam	Suite 01	4010	Goiania	9	dfsf	63	9999-0001	pcard@utica.gegli.it	cardinal	oojj&t
46	Amosa	Conselheiro Av	Suite 15	187	Brasília	7	gfg	61	9999-9991	bosun@navarro.edu	partner	fairies
47	Marvin	Domingos Dr	House	2400	São Luis	10	30303	98	9999-0001	mdekal@megaprod.com	mdekal	uu6654
48	Duncan	Aguamenon Av	Suite 21	3010	Vitória	8	221	27	9999-0001	biggie@brabazon.co.il	brab	plane
49	Brandon	Penny Lane	Suite 22	1212 	Macapá	3	21177	96	9999-0001	bshaft@thegroup.net	shaft	3344510
50	Raul	Farley Ave	Suite 10	444 	Maceió	2	92117	82	9999-0001	rost@aero.mx.com	pilot	brebby
\.


--
-- Data for Name: departamentos; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.departamentos ("departamentoID", nomedepartamento) FROM stdin;
1	financeiro
2	comercial
3	atendimento
4	direção
6	gerência financeira
7	presidencia
8	CPD
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-05-24 18:34:34.06649	1	projetoSD	2	[{"changed": {"fields": ["User permissions"]}}]	4	1
2	2021-05-24 23:33:17.729893	26	Santa Catarina | UF = SC	3		25	1
3	2021-05-25 14:43:20.986206	3	SEDEX | 23.424.243/2456-45	2	[{"changed": {"fields": ["Cnpj"]}}]	15	1
4	2021-05-25 14:43:40.160097	2	Itapemirão | 24.242.432/2111-99	2	[{"changed": {"fields": ["Cnpj"]}}]	15	1
5	2021-05-25 14:43:57.922299	1	Rapidão Estrela | 22.342.342/3456-61	2	[{"changed": {"fields": ["Cnpj"]}}]	15	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
29	admin_black	adminblacksetting
3	auth	group
2	auth	permission
4	auth	user
7	categorias	categorias
8	clientes	clientes
5	contenttypes	contenttype
31	dashboard	dashboardpreferences
9	departamentos	departamentos
10	estados	estados
11	fornecedores	fornecedores
12	fornecedores	fornecedorescontatos
13	franquias	franquias
20	gerenciar_pedidos	pedidos
21	gerenciar_pedidos	pedidositem
22	gerenciar_pedidos	pedidosstatus
23	inicial	categorias
24	inicial	departamentos
25	inicial	estados
19	listar_produtos	document
14	listar_produtos	produtos
32	listar_produtos	produtosclientes
15	listar_transportadoras	transportadoras
26	login	clientes
27	login	fornecedores
28	login	fornecedorescontatos
16	manage_pedidos	pedidos
17	manage_pedidos	pedidositem
18	manage_pedidos	pedidosstatus
30	menu	bookmark
6	sessions	session
33	listar_produtos	produtosstandby
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
58	contenttypes	0001_initial	2021-05-29 18:20:11.755074
59	auth	0001_initial	2021-05-29 18:20:11.766324
60	admin	0001_initial	2021-05-29 18:20:11.776429
61	admin	0002_logentry_remove_auto_add	2021-05-29 18:20:11.786277
62	admin	0003_logentry_add_action_flag_choices	2021-05-29 18:20:11.797452
63	contenttypes	0002_remove_content_type_name	2021-05-30 00:16:47.507885
64	auth	0002_alter_permission_name_max_length	2021-05-30 00:16:48.469701
65	auth	0003_alter_user_email_max_length	2021-05-30 00:16:49.697179
66	auth	0004_alter_user_username_opts	2021-05-30 00:16:50.227275
67	auth	0005_alter_user_last_login_null	2021-05-30 00:16:51.023997
68	auth	0006_require_contenttypes_0002	2021-05-30 00:16:51.639025
69	auth	0007_alter_validators_add_error_messages	2021-05-30 00:16:52.576038
70	auth	0008_alter_user_username_max_length	2021-05-30 00:16:53.480778
71	auth	0009_alter_user_last_name_max_length	2021-05-30 00:16:54.299129
72	auth	0010_alter_group_name_max_length	2021-05-30 00:16:55.322443
73	auth	0011_update_proxy_permissions	2021-05-30 00:16:56.040328
74	auth	0012_alter_user_first_name_max_length	2021-05-30 00:16:56.857968
75	dashboard	0001_initial	2021-05-30 00:18:03.068053
76	dashboard	0002_alter_dashboardpreferences_id	2021-05-30 00:18:04.743199
77	menu	0001_initial	2021-05-30 00:18:05.422099
78	menu	0002_alter_bookmark_id	2021-05-30 00:18:06.854239
79	sessions	0001_initial	2021-05-30 00:18:07.59089
80	gerenciar_pedidos	0001_initial	2021-05-30 23:44:47.550417
81	inicial	0001_initial	2021-05-30 23:44:48.447873
82	listar_produtos	0001_initial	2021-05-30 23:44:49.373972
83	listar_transportadoras	0001_initial	2021-05-30 23:44:49.983514
84	login	0001_initial	2021-05-30 23:44:50.595201
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
0fyp3lcxmj4y2hc7j07ohx8p6pga2ofs	M2I4ZmMyNTVkYTQwZjU3OWM2NDJjMjg1MzJkODBjZjllYmZjYzU4Mjp7ImlkQ2xpZW50ZSI6OSwiaWRGb3JuZWNlZG9yIjoyfQ==	2021-05-28 22:51:06.928249
gypubxbezh43c4ic5mzmh5xbfyrtt771	M2I4ZmMyNTVkYTQwZjU3OWM2NDJjMjg1MzJkODBjZjllYmZjYzU4Mjp7ImlkQ2xpZW50ZSI6OSwiaWRGb3JuZWNlZG9yIjoyfQ==	2021-05-24 18:47:21.655477
qnt6jza83wvzhvbtf6dlbgxcof4mzygd	.eJxVjM0OgjAQhN-lZ9PYHyz1KIk3n4Fsu7tSJW1S4GR8dyFy4TjffDMfkbAbE-WZxFWI0xrvpWaKhKX-SQ_LPPTLRLVPuCJ1ZAHim_JW4Avys8hY8lxTkJsi93aSj4I03nb3cDDANKxrqy7kGm6AjA_aamOVd6FhCB6Zz5pVJEch2tb6YNvYMrFRJqIB5Qxp8f0BgM1Cqw:1llFPc:68Ji_a_9oDMGPV1H3L3JwMewxbL_8M2gaERSRyN9W1A	2021-06-07 18:34:48.645024
r4fhl3m8497dazbf9gyuzh92mohkuy7p	MjU3ZDRiMDc2MzUxNzk4Y2VkNDU1OTQwZTA5ZDY1YzkxMjI4NGFmOTp7ImlkQ2xpZW50ZSI6OX0=	2021-05-26 00:14:11.948288
fnub2u8sfoloro0gb0vnj21wlxhxt23c	.eJxVjMsOwiAURP-FtSHyqJTu1MSd39BwuReLVkhouzL-u8V0ocuZM3NerHfLPPTLRKWPyDom2O63A-cflCrAu0u3zH1Oc4nA64RvdOLXjDSetu2fYHDTsL61OJBpQuNIWZBaKi2sgSY4sBjCXgbhyRB43WoLuvVtoKCE8qicMIrkKo14HiOlmVhnajriM6ZV_UWXXBJ5wlxq8_4AEKhGQg:1ln0ay:MLOLeUjYfoYFjMdDHlteShZVgMSGatTlo3PKyqXXapk	2021-06-12 15:09:48.060544
55w6dz5vaxahs5xkm5cdldbtij59v1oi	eyJpZEZvcm5lY2Vkb3IiOiIiLCJpZENsaWVudGUiOiIiLCJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2MjI5MjcyNzMuNTUxMDczfQ:1lpdWL:QHhY1cCMErE32r4NRA6gE3a8a9lTIUL9YjLf-n3zy_E	2021-06-19 21:07:53.565198
uv0eezswnupcx40blw91c97h5qic8qfb	eyJpZEZvcm5lY2Vkb3IiOiIiLCJpZENsaWVudGUiOiIifQ:1lpdYX:dixbJqwESAAv_UZGbguLKGuAVjjofiYaIzdHeevdA5g	2021-06-19 21:10:09.050557
q3pud8t4rh3yy58mhkvoyw0hj6z4akef	.eJwlyDEKgDAMAMC_ZBahhRraTQS_EcRmCNhU2mzi31Uc7y6QvBzCagwJh1dzLqKQAD6stSnvnGv7hzr3LlVJVIxMCnfbykmQ3OQ9YgjoRh8jTu5-AFhJHNI:1lp03X:09SaMVHzk0cEYToJPlo-PE0hcUPQYw1syFQppAOxnMw	2021-06-18 02:59:31.32399
mjn89hixppwew8yp19b16ratr7hz3c1k	eyJpZENsaWVudGUiOjcsImlkQWRtaW4iOiIiLCJpZEZvcm5lY2Vkb3IiOiIifQ:1loZdn:o9gfyS8qCm47yvcAACvMBEKwgtfUl8jW1yJ2aktPiC0	2021-06-16 22:47:11.012525
4ufsadv6z8157cs4zzwe29z3wmle3v1v	.eJyrVspMcc7JTM0rSVWyUlLSAXIdU3Iz82Act_yivNTk1JT8IpBILQBjqw6y:1lnByt:CT1ct_A9xVB1Aq5DafrZ5via5_jDECsDS7bVf0jsW9g	2021-06-13 03:19:15.417554
fue3j5f8fp0eq35caj40u86bi920hwj3	.eJwlyMEKgCAMANB_2TnCVqh4i6DfkMgdBjlDd4v-vaLjexdwWksV2imVCgG7N-aUWSAAfFgOJlH6GRu1xkUiC2tUztR0y2eEMFhE79C4qffGjjj6-wF87Bz1:1lpPA3:lhs3MckHJdf3UKKadivOu3dq6fOxAIXtw-1DQMZIvJE	2021-06-19 05:47:55.743683
\.


--
-- Data for Name: estados; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.estados ("estadoID", nome, sigla) FROM stdin;
1	Acre                	AC
2	Alagoas             	AL
3	Amapá               	AP
4	Amazonas            	AM
5	Bahia               	BA
6	Ceará               	CE
7	Distrito Federal    	DF
8	Espírito Santo      	ES
9	Goiás               	GO
10	Maranhão            	MA
11	Mato Grosso         	MT
12	Mato Grosso do Sul  	MS
13	Minas Gerais        	MG
14	Pará                	PA
15	Paraíba             	PB
16	Paraná              	PR
17	Pernambuco          	PE
19	Piauí               	PI
20	Rio Grande do Norte 	RN
21	Rio Grande do Sul   	RS
22	Rio de Janeiro      	RJ
24	Rondônia            	RO
25	Roraima             	RA
27	São Paulo           	SP
28	Santa Catarina      	SC
29	Sergipe             	SE
30	Tocantins           	TO
\.


--
-- Data for Name: fornecedores; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.fornecedores ("fornecedorID", nomefornecedor, endereco, cidade, "estadoID", ddd, telefone, usuario, senha, cep, email) FROM stdin;
1	Joe Mugger	Rua Ernesto de Paula Santos, 187	Recife	17	81	949 568 7852	joe	17r	50010-090	contato@joemugger.com
2	Dining Suppliers	Rua 13 de Maio	São Paulo	27	11	56511223	sup	bin	04849-529	contato@dining.com
3	Pacific Merchandise	56 Parkway Plaza	Rio de Janeiro	22	21	310 345 4565	pmerch	356	22030-900	contato@pacific.com
4	Quick Clothing	4598 Main St	Porto Alegre	21	51	858 555 1654	qcloth	1377	91751-440	contato@quickclothing.com
\.


--
-- Data for Name: fornecedores_contatos; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.fornecedores_contatos ("contatoID", "fornecedorID", "departamentoID", nome, telefone, email) FROM stdin;
1	1	1	Joana Piauí	33262836	joana@joemugger.com
2	1	2	Ricardo Prata	33262836	ricardo@joemugger.com
3	2	3	Gustavo Bege	33262836	gustavo@dining.com
4	2	2	Marta Borges	33262836	marta@dining.com
5	3	4	Fernando Maranhão	33262836	fernando@pacific.com
6	3	1	Ronaldo Catarinense	33262836	ronaldo@pacific.com
7	4	2	Alexandre Cisne	33262836	alexandre@quickclothing.com
8	4	1	Paulo José	33262836	paulo@quickclothing.com
9	4	4	Victor Nazário	33262836	victor@quickclothing.com
10	4	4	evellyn sales	3326.2836	aneevellyn@gmail.com
\.


--
-- Data for Name: pedidos; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.pedidos ("pedidoID", "clienteID", "transportadoraID", data_pedido, data_saida, data_entrega, status_pedido, valor_pedido, conhecimento) FROM stdin;
3	8	3	2020-12-06	\N	\N	2	650.00	2342341
10	48	2	2021-01-07	\N	\N	2	2240.00	4345646
11	48	3	2021-01-25	\N	\N	2	1500.00	7628364
14	40	2	2021-02-08	\N	\N	2	380.00	8787999
15	7	1	2021-02-11	\N	\N	2	475.00	2348729
17	50	2	2021-02-19	\N	\N	2	810.00	3234221
18	8	1	2021-02-25	\N	\N	2	445.00	2352329
20	50	1	2021-03-10	\N	\N	2	475.00	7987989
25	7	1	2021-05-27	\N	\N	2	160.00	CCREWV
2	8	2	2020-11-26	2020-11-30	2020-12-04	7	295.00	2342342
4	22	1	2020-12-06	2020-12-09	2020-12-13	7	240.00	2323424
5	33	1	2020-12-15	2020-12-19	2020-12-22	7	600.00	4634633
6	33	2	2020-12-17	2020-12-22	2020-12-27	7	2720.00	5453343
7	35	1	2020-12-23	\N	2020-12-24	3	260.00	5646442
8	40	3	2021-01-04	\N	2021-01-06	4	1840.00	4657574
9	43	1	2021-01-04	2021-01-09	2021-01-14	7	780.00	9837958
12	22	2	2021-01-27	2021-02-03	2021-02-09	7	450.00	6284882
13	35	3	2021-02-06	2021-02-13	2021-02-21	7	800.00	7687688
16	22	3	2021-02-14	2021-02-20	2021-02-25	7	290.00	3253221
19	7	3	2021-03-04	2021-03-15	2021-03-26	7	295.00	7638888
1	7	2	2020-11-19	2020-11-21	2020-11-24	7	480.00	2324324
32	9	1	2021-06-01	2021-06-01	2021-06-01	7	80.00	VONRNQ
\.


--
-- Data for Name: pedidos_item; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.pedidos_item ("pedidoID", "produtoID", precounitario, quantidade, id) FROM stdin;
1	1	20.00	10	1
1	2	9.00	20	2
1	5	20.00	5	3
2	10	5.00	50	4
2	11	9.00	5	5
3	13	14.00	20	6
3	15	14.00	10	7
3	20	12.00	5	8
3	19	12.00	10	9
3	21	5.00	10	10
4	20	12.00	20	11
5	18	12.00	20	12
5	19	12.00	10	13
5	20	12.00	15	14
5	17	12.00	5	15
6	1	20.00	5	16
6	2	9.00	100	17
6	3	3.00	20	18
6	4	3.00	200	19
6	7	14.00	70	20
6	19	12.00	10	21
7	13	14.00	10	22
7	14	9.00	5	23
7	21	5.00	15	24
8	16	12.00	5	25
8	17	12.00	5	26
8	10	12.00	60	27
8	1	20.00	50	28
9	11	12.00	30	29
9	12	21.00	20	30
10	18	12.00	35	31
10	9	5.00	100	32
10	7	7.00	90	33
10	14	9.00	50	34
10	6	14.00	10	35
10	22	2.00	50	36
11	21	5.00	300	37
12	11	12.00	10	38
12	5	21.00	15	39
12	3	3.00	5	40
13	2	14.00	20	41
13	19	12.00	10	42
13	22	2.00	50	43
13	3	3.00	100	44
14	7	7.00	50	45
14	8	3.00	10	46
15	1	20.00	8	47
15	2	9.00	15	48
15	17	12.00	15	49
16	18	12.00	10	50
16	19	12.00	5	51
16	21	5.00	10	52
16	10	12.00	5	53
17	6	14.00	5	54
17	8	3.00	100	55
17	2	9.00	15	56
17	12	21.00	5	57
17	13	14.00	5	58
17	15	14.00	5	59
17	17	12.00	5	60
18	1	20.00	20	61
18	3	3.00	15	62
19	21	5.00	20	63
19	7	7.00	15	64
19	14	9.00	10	65
20	18	12.00	20	66
20	19	12.00	10	67
20	22	2.00	15	68
20	8	3.00	5	69
20	15	14.00	5	70
25	35	4.00	40	71
32	35	4.00	20	78
\.


--
-- Data for Name: pedidos_status; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.pedidos_status ("statusID", nomestatus) FROM stdin;
1	Pagamento Confirmado
2	Pagamento Pendente
3	Cancelado pelo cliente
4	Cancelado pela empresa
5	Aguardando Envio
6	Enviado
7	Entregue
\.


--
-- Data for Name: produtos; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.produtos ("produtoID", nomeproduto, descricao, codigobarra, tempoentrega, precorevenda, precounitario, estoque, imagemgrande, imagempequena, "fornecedorID", "categoriaID") FROM stdin;
1	Biscottis	All-natural bite-sized biscuits.	7891518238009	15	10.00	20.00	100	images/product_images/HoneyBiscotti_Big.jpg	images/product_images/HoneyBiscotti_Smallb.jpg	2	2
2	Organic Earl Grey	Because once in a blue moon you might want something besides coffee. This blend of black and green teas is highly aromatic, rich and flavorful with a hint of light citrus.	789151 823798	8	6.00	9.00	1000	images/product_images/EarlGreyTea_Big.jpg	images/product_images/EarlGreyTea_Smallb.jpg	1	2
3	Sugar	How many spoonfuls do you need? Crystallized from 100% organic sugar cane, and milled within 24 hours of harvest to ensure it's as fresh as our coffee beans.	789151 823797	8	1.00	3.00	500	images/product_images/Sugar_Big.jpg	images/product_images/Sugar_Smallb.jpg	2	2
4	Non-Diary Creamer	If running out of milk or cream for your coffee is tantamount to a state of emergency, we suggest you stock up on these delicious non-dairy creamers just in case.	789151 823796	5	2.00	3.00	500	images/product_images/NonDairyCreamer_Big.jpg	images/product_images/NonDairyCreamer_Smallb.jpg	2	2
5	Steel Mug	Here's one way to make sure your coffee stays warm during a long commute. Made of lightweight metal alloy.	789151 823795	15	15.00	21.00	300	images/product_images/SteelMug_Big.jpg	images/product_images/SteelMug_Smallb.jpg	3	3
6	Ceramic Mug	Handcrafted by Colorado artisans. These generous mugs feature an opaque green satin glaze over classic stoneware.	789151 823799	15	10.00	14.00	80	images/product_images/CeramicMug_Big.jpg	images/product_images/CeramicMug_Smallb.jpg	3	3
7	Plastic Mug	If you're a little klutzy in the morning, we recommend this shatter-proof, durable plastic commuter mug.	789151 823795	8	5.00	7.00	750	images/product_images/PlasticMug_Big.jpg	images/product_images/PlasticMug_Smallb.jpg	3	3
8	Thermometer	Ideal for microwaving your coffee. With a stainless steel stem, large, easy-to-read digital display and case.	789151 823654	30	1.50	3.00	45	images/product_images/Thermometer_Big.jpg	images/product_images/Thermometer_Smallb.jpg	3	3
9	Hype Filters	Never resort to using papers towels when you're out of paper filters. This Gold-Tone filter is always ready.	789151 823655	5	2.80	5.00	50	images/product_images/HypeFilters_Big.jpg	images/product_images/HypeFilters_Smallb.jpg	3	3
10	Brave New World T-Shirt	100% cotton. Available in black, mocha or white.	789151 823765	5	8.00	12.00	60	images/product_images/TShirt_Big.jpg	images/product_images/TShirt_Smallb.jpg	4	4
11	Brave Blend	Grown on some of the highest peaks in Brazil, India, Kenya and Puerto Rico, this blend represents the best arabica beans the world has to offer.	789151 823765	15	8.00	12.00	100	images/product_images/BraveBlend_Group_Big.jpg	images/product_images/BraveBlend_Group_Smallb.jpg	1	1
12	Brave New World Sweatshirt	- Perfect for lazing around on a Sunday morning with the paper and a cup of your favorite blend. Pigment-dyed for lasting color. Ribbed cuff and bottom.	789151 823658	15	8.00	21.00	250	images/product_images/Sweatshirt_Big.jpg	images/product_images/Sweatshirt_Smallb.jpg	4	4
13	Andes Baseball Cap	You're groggy and need coffee right away. This is no time to worry about your hair. Throw on this cap and head to the nearest ANDES. Cotton, adjustable, available in two colors.	789151 823659	5	11.00	14.00	40	images/product_images/Baseballcap_Big.jpg	images/product_images/Baseballcap_Smallb.jpg	4	4
14	Andes Toque	Style comes with a layer of Comfort Max lycra stretch material on the inside and a tasty ANDES logo on the outside.	789151 823564	5	5.00	9.00	80	images/product_images/Toke_Big.jpg	images/product_images/Toke_Smallb.jpg	4	4
15	Audio CD	Our very own coffee house collection, featuring poetry slams, soulful vocals and a generous helping of the blues.	789151 823732	5	11.00	14.00	10	images/product_images/MusicCD_Big.jpg	images/product_images/MusicCD_Smallb.jpg	3	3
16	Year 1999 Blend	Java, Mysore and Sumatra beans offer a mellow flavor to make all the Year 2000 hype more palatable.	789151 823455	5	9.00	12.00	45	images/product_images/Year1999Blend_Group_Big.jpg	images/product_images/Year1999Blend_Group_Smallb.jpg	1	1
17	Border Blend	Columbia, Costa Rica and Estate Java beans offer a mellow flavor to make all the Year 2000 hype more palatable.	782341 823795	5	6.00	12.00	30	images/product_images/BorderBlend_Group_Big.jpg	images/product_images/BorderBlend_Group_Smallb.jpg	1	1
18	Blond Blend	Processed for lower levels of caffeine without reducing the integrity of this rich Costa Rica bean.	734561 823795	5	7.50	12.00	10	images/product_images/BlondBlend_Group_Big.jpg	images/product_images/BlondBlend_Group_Smallb.jpg	1	1
19	Winter Blend	- Columbia and Jamaica beans create a full-bodied, mellow, slightly nutty flavor.	798751 823795	8	7.50	12.00	5	images/product_images/WinterBlend_Group_Big.jpg	images/product_images/WinterBlend_Group_Smallb.jpg	1	1
20	Chocolate Mocha Bars	Very European and very decadent. Drop these milk chocolates into your coffee to release a rich mocha aroma and pool of hot chocolate.	123151 823795	15	9.00	12.00	25	images/product_images/ChocolateMochaBars_Big.jpg	images/product_images/ChocolateMochaBars_Smallb.jpg	2	2
21	Chocolate Covered Coffee Beans	Made for all-nighters, afternoon lulls, and long drives. These are the times when you need a sweet jolt.	784561 823795	30	3.00	5.00	30	images/product_images/ChocolateCoffeBeans_Big.jpg	images/product_images/ChocolateCoffeBeans_Smallb.jpg	2	2
22	Breath Mints	No one need know how many cups of coffee you consume in a day. Hide it well with these powerfully refreshing mints.	7891518823980	30	1.00	2.00	60	images/product_images/BreathMints_Big.jpg	images/product_images/BreathMints_Smallb.jpg	2	2
53	Bala 7Belo	Melhor bala, quem experimenta jamais esquece	7234567897778	5	5.00	4.00	1000	images/product_images/foto_31_05_2021165249_WMTIUKTJQKTUU1.jpg	images/product_images/foto_31_05_2021165249_ZZ0H5GCKW4R0SO.jpg	2	1
35	Teste	Teste de inclusão	1234567891078	5	1.00	4.00	20	images/product_images/foto_12_05_2021224647_3CWBDNEBLV8ESK.jpg	images/product_images/foto_12_05_2021224647_V8RWXU5YXA3THF.png	1	1
\.


--
-- Data for Name: produtos_clientes; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.produtos_clientes ("produtoID", nomeproduto, descricao, codigobarra, tempoentrega, precorevenda, precounitario, estoque, imagemgrande, imagempequena, descontinuado, "fornecedorID", "categoriaID") FROM stdin;
1	Biscottis	All-natural bite-sized biscuits.	789151 823800	15	10.00	20.00	15	images/product_images_clientes/HoneyBiscotti_Big.jpg	images/product_images_clientes/HoneyBiscotti_Smallb.jpg	0	2	2
2	Organic Earl Grey	Because once in a blue moon you might want something besides coffee. This blend of black and green teas is highly aromatic, rich and flavorful with a hint of light citrus.	789151 823798	8	6.00	9.00	140	images/product_images_clientes/EarlGreyTea_Big.jpg	images/product_images_clientes/EarlGreyTea_Smallb.jpg	0	1	2
3	Sugar	How many spoonfuls do you need? Crystallized from 100% organic sugar cane, and milled within 24 hours of harvest to ensure it's as fresh as our coffee beans.	789151 823797	8	1.00	3.00	125	images/product_images_clientes/Sugar_Big.jpg	images/product_images_clientes/Sugar_Smallb.jpg	0	2	2
4	Non-Diary Creamer	If running out of milk or cream for your coffee is tantamount to a state of emergency, we suggest you stock up on these delicious non-dairy creamers just in case.	789151 823796	5	2.00	3.00	200	images/product_images_clientes/NonDairyCreamer_Big.jpg	images/product_images_clientes/NonDairyCreamer_Smallb.jpg	0	2	2
5	Steel Mug	Here's one way to make sure your coffee stays warm during a long commute. Made of lightweight metal alloy.	789151 823795	15	15.00	21.00	20	images/product_images_clientes/SteelMug_Big.jpg	images/product_images_clientes/SteelMug_Smallb.jpg	0	3	3
7	Plastic Mug	If you're a little klutzy in the morning, we recommend this shatter-proof, durable plastic commuter mug.	789151 823795	8	5.00	7.00	85	images/product_images_clientes/PlasticMug_Big.jpg	images/product_images_clientes/PlasticMug_Smallb.jpg	0	3	3
10	Brave New World T-Shirt	100% cotton. Available in black, mocha or white.	789151 823765	5	8.00	12.00	55	images/product_images_clientes/TShirt_Big.jpg	images/product_images_clientes/TShirt_Smallb.jpg	0	4	4
11	Brave Blend	Grown on some of the highest peaks in Brazil, India, Kenya and Puerto Rico, this blend represents the best arabica beans the world has to offer.	789151 823765	15	8.00	12.00	45	images/product_images_clientes/BraveBlend_Group_Big.jpg	images/product_images_clientes/BraveBlend_Group_Smallb.jpg	0	1	1
12	Brave New World Sweatshirt	- Perfect for lazing around on a Sunday morning with the paper and a cup of your favorite blend. Pigment-dyed for lasting color. Ribbed cuff and bottom.	789151 823658	15	8.00	21.00	20	images/product_images_clientes/Sweatshirt_Big.jpg	images/product_images_clientes/Sweatshirt_Smallb.jpg	0	4	4
14	Andes Toque	Style comes with a layer of Comfort Max lycra stretch material on the inside and a tasty ANDES logo on the outside.	789151 823564	5	5.00	9.00	10	images/product_images_clientes/Toke_Big.jpg	images/product_images_clientes/Toke_Smallb.jpg	0	4	4
17	Border Blend	Columbia, Costa Rica and Estate Java beans offer a mellow flavor to make all the Year 2000 hype more palatable.	782341 823795	5	6.00	12.00	5	images/product_images_clientes/BorderBlend_Group_Big.jpg	images/product_images_clientes/BorderBlend_Group_Smallb.jpg	0	1	1
18	Blond Blend	Processed for lower levels of caffeine without reducing the integrity of this rich Costa Rica bean.	734561 823795	5	7.50	12.00	30	images/product_images_clientes/BlondBlend_Group_Big.jpg	images/product_images_clientes/BlondBlend_Group_Smallb.jpg	0	1	1
19	Winter Blend	- Columbia and Jamaica beans create a full-bodied, mellow, slightly nutty flavor.	798751 823795	8	7.50	12.00	35	images/product_images_clientes/WinterBlend_Group_Big.jpg	images/product_images_clientes/WinterBlend_Group_Smallb.jpg	0	1	1
20	Chocolate Mocha Bars	Very European and very decadent. Drop these milk chocolates into your coffee to release a rich mocha aroma and pool of hot chocolate.	123151 823795	15	9.00	12.00	35	images/product_images_clientes/ChocolateMochaBars_Big.jpg	images/product_images_clientes/ChocolateMochaBars_Smallb.jpg	0	2	2
21	Chocolate Covered Coffee Beans	Made for all-nighters, afternoon lulls, and long drives. These are the times when you need a sweet jolt.	784561 823795	30	3.00	5.00	30	images/product_images_clientes/ChocolateCoffeBeans_Big.jpg	images/product_images_clientes/ChocolateCoffeBeans_Smallb.jpg	0	2	2
22	Breath Mints	No one need know how many cups of coffee you consume in a day. Hide it well with these powerfully refreshing mints.	789151 823980	30	1.00	2.00	50	images/product_images_clientes/BreathMints_Big.jpg	images/product_images_clientes/BreathMints_Smallb.jpg	0	2	2
\.


--
-- Data for Name: produtos_standby; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.produtos_standby ("produtoID", nomeproduto, descricao, codigobarra, tempoentrega, precorevenda, precounitario, estoque, imagemgrande, imagempequena, "fornecedorID", "categoriaID") FROM stdin;
1	Biscottis	All-natural bite-sized biscuits.	7891518238009	15	10.00	20.00	28	images/product_images_standby/HoneyBiscotti_Big.jpg	images/product_images_standby/HoneyBiscotti_Smallb.jpg	2	2
2	Organic Earl Grey	Because once in a blue moon you might want something besides coffee. This blend of black and green teas is highly aromatic, rich and flavorful with a hint of light citrus.	789151 823798	8	6.00	9.00	30	images/product_images_standby/EarlGreyTea_Big.jpg	images/product_images_standby/EarlGreyTea_Smallb.jpg	1	2
3	Sugar	How many spoonfuls do you need? Crystallized from 100% organic sugar cane, and milled within 24 hours of harvest to ensure it's as fresh as our coffee beans.	789151 823797	8	1.00	3.00	15	images/product_images_standby/Sugar_Big.jpg	images/product_images_standby/Sugar_Smallb.jpg	2	2
6	Ceramic Mug	Handcrafted by Colorado artisans. These generous mugs feature an opaque green satin glaze over classic stoneware.	789151 823799	15	10.00	14.00	15	images/product_images_standby/CeramicMug_Big.jpg	images/product_images_standby/CeramicMug_Smallb.jpg	3	3
7	Plastic Mug	If you're a little klutzy in the morning, we recommend this shatter-proof, durable plastic commuter mug.	789151 823795	8	5.00	7.00	140	images/product_images_standby/PlasticMug_Big.jpg	images/product_images_standby/PlasticMug_Smallb.jpg	3	3
8	Thermometer	Ideal for microwaving your coffee. With a stainless steel stem, large, easy-to-read digital display and case.	789151 823654	30	1.50	3.00	115	images/product_images_standby/Thermometer_Big.jpg	images/product_images_standby/Thermometer_Smallb.jpg	3	3
9	Hype Filters	Never resort to using papers towels when you're out of paper filters. This Gold-Tone filter is always ready.	789151 823655	5	2.80	5.00	100	images/product_images_standby/HypeFilters_Big.jpg	images/product_images_standby/HypeFilters_Smallb.jpg	3	3
12	Brave New World Sweatshirt	- Perfect for lazing around on a Sunday morning with the paper and a cup of your favorite blend. Pigment-dyed for lasting color. Ribbed cuff and bottom.	789151 823658	15	8.00	21.00	5	images/product_images_standby/Sweatshirt_Big.jpg	images/product_images_standby/Sweatshirt_Smallb.jpg	4	4
14	Andes Toque	Style comes with a layer of Comfort Max lycra stretch material on the inside and a tasty ANDES logo on the outside.	789151 823564	5	5.00	9.00	50	images/product_images_standby/Toke_Big.jpg	images/product_images_standby/Toke_Smallb.jpg	4	4
13	Andes Baseball Cap	You're groggy and need coffee right away. This is no time to worry about your hair. Throw on this cap and head to the nearest ANDES. Cotton, adjustable, available in two colors.	789151 823659	5	11.00	14.00	25	images/product_images_standby/Baseballcap_Big.jpg	images/product_images_standby/Baseballcap_Smallb.jpg	4	4
15	Audio CD	Our very own coffee house collection, featuring poetry slams, soulful vocals and a generous helping of the blues.	789151 823732	5	11.00	14.00	20	images/product_images_standby/MusicCD_Big.jpg	images/product_images_standby/MusicCD_Smallb.jpg	3	3
17	Border Blend	Columbia, Costa Rica and Estate Java beans offer a mellow flavor to make all the Year 2000 hype more palatable.	782341 823795	5	6.00	12.00	20	images/product_images_standby/BorderBlend_Group_Big.jpg	images/product_images_standby/BorderBlend_Group_Smallb.jpg	1	1
18	Blond Blend	Processed for lower levels of caffeine without reducing the integrity of this rich Costa Rica bean.	734561 823795	5	7.50	12.00	55	images/product_images_standby/BlondBlend_Group_Big.jpg	images/product_images_standby/BlondBlend_Group_Smallb.jpg	1	1
19	Winter Blend	- Columbia and Jamaica beans create a full-bodied, mellow, slightly nutty flavor.	798751 823795	8	7.50	12.00	20	images/product_images_standby/WinterBlend_Group_Big.jpg	images/product_images_standby/WinterBlend_Group_Smallb.jpg	1	1
20	Chocolate Mocha Bars	Very European and very decadent. Drop these milk chocolates into your coffee to release a rich mocha aroma and pool of hot chocolate.	123151 823795	15	9.00	12.00	5	images/product_images_standby/ChocolateMochaBars_Big.jpg	images/product_images_standby/ChocolateMochaBars_Smallb.jpg	2	2
21	Chocolate Covered Coffee Beans	Made for all-nighters, afternoon lulls, and long drives. These are the times when you need a sweet jolt.	784561 823795	30	3.00	5.00	310	images/product_images_standby/ChocolateCoffeBeans_Big.jpg	images/product_images_standby/ChocolateCoffeBeans_Smallb.jpg	2	2
22	Breath Mints	No one need know how many cups of coffee you consume in a day. Hide it well with these powerfully refreshing mints.	7891518823980	30	1.00	2.00	65	images/product_images_standby/BreathMints_Big.jpg	images/product_images_standby/BreathMints_Smallb.jpg	2	2
35	Teste	Teste de inclusão	1234567891078	5	1.00	4.00	40	images/product_images_standby/foto_12_05_2021224647_3CWBDNEBLV8ESK.jpg	images/product_images_standby/foto_12_05_2021224647_V8RWXU5YXA3THF.png	1	1
\.


--
-- Data for Name: transportadoras; Type: TABLE DATA; Schema: public; Owner: vtliqlvhugzosr
--

COPY public.transportadoras ("transportadoraID", nometransportadora, endereco, telefone, cidade, "estadoID", cep, cnpj) FROM stdin;
1	Rapidão Estrela	Rua Ernesto de Paula Santos, 187	33262836	Recife	17	51.021-330	22.342.342/3456-61
2	Itapemirão	Rua Visconde de Sabugosa, 11	33262836	São Paulo	27	01.323.123	24.242.432/2111-99
3	SEDEX	Av Ipanema, 22123	33262836	Rio de Janeiro	21	02.320.121	23.424.243/2456-45
6	Vietnã	Rua da Simpatia, 80	+5587988596558	Petrolina	17	56304-440	18.984.560/0003-55
11	Correios	Rua da Simpatia	+5587988596987	Petrolina	17	56304-440	75.315.333/0244-74
\.


--
-- Name: admin_black_adminblacksetting_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.admin_black_adminblacksetting_id_seq', 1, true);


--
-- Name: admin_tools_dashboard_preferences_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.admin_tools_dashboard_preferences_id_seq', 2, true);


--
-- Name: admin_tools_menu_bookmark_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.admin_tools_menu_bookmark_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 161, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 100, true);


--
-- Name: categorias_categoriaID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."categorias_categoriaID_seq"', 4, true);


--
-- Name: clientes_clienteID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."clientes_clienteID_seq"', 52, true);


--
-- Name: departamentos_departamentoID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."departamentos_departamentoID_seq"', 8, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 5, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 65, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 112, true);


--
-- Name: estados_estadoID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."estados_estadoID_seq"', 30, true);


--
-- Name: fornecedores_contatos_contatoID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."fornecedores_contatos_contatoID_seq"', 10, true);


--
-- Name: fornecedores_fornecedorID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."fornecedores_fornecedorID_seq"', 5, true);


--
-- Name: pedidos_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public.pedidos_item_id_seq', 110, true);


--
-- Name: pedidos_pedidoID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."pedidos_pedidoID_seq"', 64, true);


--
-- Name: pedidos_status_statusID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."pedidos_status_statusID_seq"', 7, true);


--
-- Name: produtos_clientes_produtoID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."produtos_clientes_produtoID_seq"', 22, true);


--
-- Name: produtos_produtoID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."produtos_produtoID_seq"', 85, true);


--
-- Name: transportadoras_transportadoraID_seq; Type: SEQUENCE SET; Schema: public; Owner: vtliqlvhugzosr
--

SELECT pg_catalog.setval('public."transportadoras_transportadoraID_seq"', 11, true);


--
-- Name: admin_black_adminblacksetting admin_black_adminblacksetting_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_black_adminblacksetting
    ADD CONSTRAINT admin_black_adminblacksetting_pkey PRIMARY KEY (id);


--
-- Name: admin_tools_dashboard_preferences admin_tools_dashboard_preferences_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_tools_dashboard_preferences
    ADD CONSTRAINT admin_tools_dashboard_preferences_pkey PRIMARY KEY (id);


--
-- Name: admin_tools_menu_bookmark admin_tools_menu_bookmark_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_tools_menu_bookmark
    ADD CONSTRAINT admin_tools_menu_bookmark_pkey PRIMARY KEY (id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: categorias categorias_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_pkey PRIMARY KEY ("categoriaID");


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY ("clienteID");


--
-- Name: departamentos departamentos_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.departamentos
    ADD CONSTRAINT departamentos_pkey PRIMARY KEY ("departamentoID");


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: estados estados_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.estados
    ADD CONSTRAINT estados_pkey PRIMARY KEY ("estadoID");


--
-- Name: fornecedores_contatos fornecedores_contatos_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.fornecedores_contatos
    ADD CONSTRAINT fornecedores_contatos_pkey PRIMARY KEY ("contatoID");


--
-- Name: fornecedores fornecedores_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.fornecedores
    ADD CONSTRAINT fornecedores_pkey PRIMARY KEY ("fornecedorID");


--
-- Name: pedidos_item pedidos_item_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.pedidos_item
    ADD CONSTRAINT pedidos_item_pkey PRIMARY KEY (id);


--
-- Name: pedidos pedidos_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT pedidos_pkey PRIMARY KEY ("pedidoID");


--
-- Name: pedidos_status pedidos_status_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.pedidos_status
    ADD CONSTRAINT pedidos_status_pkey PRIMARY KEY ("statusID");


--
-- Name: produtos_clientes produtos_clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.produtos_clientes
    ADD CONSTRAINT produtos_clientes_pkey PRIMARY KEY ("produtoID");


--
-- Name: produtos produtos_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.produtos
    ADD CONSTRAINT produtos_pkey PRIMARY KEY ("produtoID");


--
-- Name: produtos_standby produtos_standby_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.produtos_standby
    ADD CONSTRAINT produtos_standby_pkey PRIMARY KEY ("produtoID");


--
-- Name: admin_black_adminblacksetting public_admin_black_adminblacksetting_user_id1_idx; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_black_adminblacksetting
    ADD CONSTRAINT public_admin_black_adminblacksetting_user_id1_idx UNIQUE (user_id);


--
-- Name: admin_tools_dashboard_preferences public_admin_tools_dashboard_preferences_user_id1_idx; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_tools_dashboard_preferences
    ADD CONSTRAINT public_admin_tools_dashboard_preferences_user_id1_idx UNIQUE (user_id, dashboard_id);


--
-- Name: auth_group public_auth_group_name1_idx; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT public_auth_group_name1_idx UNIQUE (name);


--
-- Name: auth_group_permissions public_auth_group_permissions_group_id1_idx; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT public_auth_group_permissions_group_id1_idx UNIQUE (group_id, permission_id);


--
-- Name: auth_permission public_auth_permission_content_type_id1_idx; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT public_auth_permission_content_type_id1_idx UNIQUE (content_type_id, codename);


--
-- Name: auth_user_groups public_auth_user_groups_user_id1_idx; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT public_auth_user_groups_user_id1_idx UNIQUE (user_id, group_id);


--
-- Name: auth_user_user_permissions public_auth_user_user_permissions_user_id1_idx; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT public_auth_user_user_permissions_user_id1_idx UNIQUE (user_id, permission_id);


--
-- Name: auth_user public_auth_user_username1_idx; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT public_auth_user_username1_idx UNIQUE (username);


--
-- Name: django_content_type public_django_content_type_app_label1_idx; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT public_django_content_type_app_label1_idx UNIQUE (app_label, model);


--
-- Name: transportadoras transportadoras_pkey; Type: CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.transportadoras
    ADD CONSTRAINT transportadoras_pkey PRIMARY KEY ("transportadoraID");


--
-- Name: public_admin_tools_menu_bookmark_user_id1_idx; Type: INDEX; Schema: public; Owner: vtliqlvhugzosr
--

CREATE INDEX public_admin_tools_menu_bookmark_user_id1_idx ON public.admin_tools_menu_bookmark USING btree (user_id);


--
-- Name: public_auth_group_permissions_permission_id2_idx; Type: INDEX; Schema: public; Owner: vtliqlvhugzosr
--

CREATE INDEX public_auth_group_permissions_permission_id2_idx ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: public_auth_user_groups_group_id2_idx; Type: INDEX; Schema: public; Owner: vtliqlvhugzosr
--

CREATE INDEX public_auth_user_groups_group_id2_idx ON public.auth_user_groups USING btree (group_id);


--
-- Name: public_auth_user_user_permissions_permission_id2_idx; Type: INDEX; Schema: public; Owner: vtliqlvhugzosr
--

CREATE INDEX public_auth_user_user_permissions_permission_id2_idx ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: public_django_admin_log_content_type_id1_idx; Type: INDEX; Schema: public; Owner: vtliqlvhugzosr
--

CREATE INDEX public_django_admin_log_content_type_id1_idx ON public.django_admin_log USING btree (content_type_id);


--
-- Name: public_django_admin_log_user_id2_idx; Type: INDEX; Schema: public; Owner: vtliqlvhugzosr
--

CREATE INDEX public_django_admin_log_user_id2_idx ON public.django_admin_log USING btree (user_id);


--
-- Name: public_django_session_expire_date1_idx; Type: INDEX; Schema: public; Owner: vtliqlvhugzosr
--

CREATE INDEX public_django_session_expire_date1_idx ON public.django_session USING btree (expire_date);


--
-- Name: admin_black_adminblacksetting admin_black_adminblacksetting_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_black_adminblacksetting
    ADD CONSTRAINT admin_black_adminblacksetting_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: admin_tools_dashboard_preferences admin_tools_dashboard_preferences_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_tools_dashboard_preferences
    ADD CONSTRAINT admin_tools_dashboard_preferences_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: admin_tools_menu_bookmark admin_tools_menu_bookmark_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.admin_tools_menu_bookmark
    ADD CONSTRAINT admin_tools_menu_bookmark_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id);


--
-- Name: auth_group_permissions auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id);


--
-- Name: auth_permission auth_permission_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id);


--
-- Name: auth_user_groups auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id);


--
-- Name: auth_user_groups auth_user_groups_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: django_admin_log django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id);


--
-- Name: django_admin_log django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vtliqlvhugzosr
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: tr_vietna
--

GRANT ALL ON SCHEMA public TO vtliqlvhugzosr;


--
-- Name: LANGUAGE plpgsql; Type: ACL; Schema: -; Owner: tr_vietna
--

GRANT ALL ON LANGUAGE plpgsql TO vtliqlvhugzosr;


--
-- PostgreSQL database dump complete
--

