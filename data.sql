--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-10-08 01:07:26

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
-- TOC entry 207 (class 1259 OID 16721)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16719)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- TOC entry 3306 (class 0 OID 0)
-- Dependencies: 206
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- TOC entry 209 (class 1259 OID 16731)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16729)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 3307 (class 0 OID 0)
-- Dependencies: 208
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- TOC entry 205 (class 1259 OID 16713)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16711)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- TOC entry 3308 (class 0 OID 0)
-- Dependencies: 204
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- TOC entry 211 (class 1259 OID 16739)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16749)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16747)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- TOC entry 3309 (class 0 OID 0)
-- Dependencies: 212
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- TOC entry 210 (class 1259 OID 16737)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- TOC entry 3310 (class 0 OID 0)
-- Dependencies: 210
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- TOC entry 215 (class 1259 OID 16757)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16755)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 3311 (class 0 OID 0)
-- Dependencies: 214
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- TOC entry 219 (class 1259 OID 16850)
-- Name: blog_blogconfiguration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blog_blogconfiguration (
    id integer NOT NULL,
    main_image character varying(100) NOT NULL,
    main_image_alt character varying(400) NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.blog_blogconfiguration OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16848)
-- Name: blog_blogconfiguration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.blog_blogconfiguration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_blogconfiguration_id_seq OWNER TO postgres;

--
-- TOC entry 3312 (class 0 OID 0)
-- Dependencies: 218
-- Name: blog_blogconfiguration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.blog_blogconfiguration_id_seq OWNED BY public.blog_blogconfiguration.id;


--
-- TOC entry 221 (class 1259 OID 16861)
-- Name: blog_blogpost; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blog_blogpost (
    id integer NOT NULL,
    photo character varying(100) NOT NULL,
    photo_alt character varying(400) NOT NULL,
    description text NOT NULL,
    publication_date timestamp with time zone NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.blog_blogpost OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16859)
-- Name: blog_blogpost_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.blog_blogpost_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_blogpost_id_seq OWNER TO postgres;

--
-- TOC entry 3313 (class 0 OID 0)
-- Dependencies: 220
-- Name: blog_blogpost_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.blog_blogpost_id_seq OWNED BY public.blog_blogpost.id;


--
-- TOC entry 223 (class 1259 OID 16872)
-- Name: contact_contact; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contact_contact (
    id integer NOT NULL,
    message text NOT NULL,
    email character varying(300) NOT NULL,
    phone character varying(400) NOT NULL,
    name character varying(400) NOT NULL,
    attachment_img character varying(400) NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.contact_contact OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16870)
-- Name: contact_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contact_contact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contact_contact_id_seq OWNER TO postgres;

--
-- TOC entry 3314 (class 0 OID 0)
-- Dependencies: 222
-- Name: contact_contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contact_contact_id_seq OWNED BY public.contact_contact.id;


--
-- TOC entry 225 (class 1259 OID 16883)
-- Name: contact_contactconfiguration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contact_contactconfiguration (
    id integer NOT NULL,
    map_url character varying(400) NOT NULL,
    phone_number character varying(128) NOT NULL,
    email character varying(254) NOT NULL,
    on_site_client_info text NOT NULL,
    working_hours text NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.contact_contactconfiguration OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16881)
-- Name: contact_contactconfiguration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contact_contactconfiguration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contact_contactconfiguration_id_seq OWNER TO postgres;

--
-- TOC entry 3315 (class 0 OID 0)
-- Dependencies: 224
-- Name: contact_contactconfiguration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contact_contactconfiguration_id_seq OWNED BY public.contact_contactconfiguration.id;


--
-- TOC entry 217 (class 1259 OID 16817)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16815)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- TOC entry 3316 (class 0 OID 0)
-- Dependencies: 216
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- TOC entry 203 (class 1259 OID 16703)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16701)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- TOC entry 3317 (class 0 OID 0)
-- Dependencies: 202
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- TOC entry 201 (class 1259 OID 16692)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16690)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- TOC entry 3318 (class 0 OID 0)
-- Dependencies: 200
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- TOC entry 248 (class 1259 OID 17011)
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16894)
-- Name: faq_faqconfiguration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faq_faqconfiguration (
    id integer NOT NULL,
    main_image character varying(100) NOT NULL,
    main_image_alt character varying(400) NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.faq_faqconfiguration OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16892)
-- Name: faq_faqconfiguration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faq_faqconfiguration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faq_faqconfiguration_id_seq OWNER TO postgres;

--
-- TOC entry 3319 (class 0 OID 0)
-- Dependencies: 226
-- Name: faq_faqconfiguration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.faq_faqconfiguration_id_seq OWNED BY public.faq_faqconfiguration.id;


--
-- TOC entry 229 (class 1259 OID 16905)
-- Name: faq_faqitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faq_faqitem (
    id integer NOT NULL,
    question_text text NOT NULL,
    answer_text text NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.faq_faqitem OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16903)
-- Name: faq_faqitem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faq_faqitem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faq_faqitem_id_seq OWNER TO postgres;

--
-- TOC entry 3320 (class 0 OID 0)
-- Dependencies: 228
-- Name: faq_faqitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.faq_faqitem_id_seq OWNED BY public.faq_faqitem.id;


--
-- TOC entry 231 (class 1259 OID 16916)
-- Name: info_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.info_info (
    id integer NOT NULL,
    photo character varying(100) NOT NULL,
    photo_alt character varying(400) NOT NULL,
    description text NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.info_info OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16914)
-- Name: info_info_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.info_info_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.info_info_id_seq OWNER TO postgres;

--
-- TOC entry 3321 (class 0 OID 0)
-- Dependencies: 230
-- Name: info_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.info_info_id_seq OWNED BY public.info_info.id;


--
-- TOC entry 233 (class 1259 OID 16927)
-- Name: main_mainboxitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.main_mainboxitem (
    id integer NOT NULL,
    header_text character varying(400) NOT NULL,
    image character varying(100) NOT NULL,
    image_alt character varying(400) NOT NULL,
    description text NOT NULL,
    visible boolean NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.main_mainboxitem OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 16925)
-- Name: main_mainboxitem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.main_mainboxitem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_mainboxitem_id_seq OWNER TO postgres;

--
-- TOC entry 3322 (class 0 OID 0)
-- Dependencies: 232
-- Name: main_mainboxitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.main_mainboxitem_id_seq OWNED BY public.main_mainboxitem.id;


--
-- TOC entry 235 (class 1259 OID 16938)
-- Name: main_mainconfiguration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.main_mainconfiguration (
    id integer NOT NULL,
    is_modal_visible boolean NOT NULL,
    newsletter_info text NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.main_mainconfiguration OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 16936)
-- Name: main_mainconfiguration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.main_mainconfiguration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_mainconfiguration_id_seq OWNER TO postgres;

--
-- TOC entry 3323 (class 0 OID 0)
-- Dependencies: 234
-- Name: main_mainconfiguration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.main_mainconfiguration_id_seq OWNED BY public.main_mainconfiguration.id;


--
-- TOC entry 237 (class 1259 OID 16949)
-- Name: main_mainsliderconfiguration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.main_mainsliderconfiguration (
    id integer NOT NULL,
    change_image_time_ms integer NOT NULL,
    update_date timestamp with time zone NOT NULL,
    CONSTRAINT main_mainsliderconfiguration_change_image_time_ms_check CHECK ((change_image_time_ms >= 0))
);


ALTER TABLE public.main_mainsliderconfiguration OWNER TO postgres;

--
-- TOC entry 236 (class 1259 OID 16947)
-- Name: main_mainsliderconfiguration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.main_mainsliderconfiguration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_mainsliderconfiguration_id_seq OWNER TO postgres;

--
-- TOC entry 3324 (class 0 OID 0)
-- Dependencies: 236
-- Name: main_mainsliderconfiguration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.main_mainsliderconfiguration_id_seq OWNED BY public.main_mainsliderconfiguration.id;


--
-- TOC entry 239 (class 1259 OID 16958)
-- Name: main_mainslideritem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.main_mainslideritem (
    id integer NOT NULL,
    image character varying(100) NOT NULL,
    image_alt character varying(400) NOT NULL,
    visible boolean NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.main_mainslideritem OWNER TO postgres;

--
-- TOC entry 238 (class 1259 OID 16956)
-- Name: main_mainslideritem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.main_mainslideritem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_mainslideritem_id_seq OWNER TO postgres;

--
-- TOC entry 3325 (class 0 OID 0)
-- Dependencies: 238
-- Name: main_mainslideritem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.main_mainslideritem_id_seq OWNED BY public.main_mainslideritem.id;


--
-- TOC entry 241 (class 1259 OID 16969)
-- Name: offer_offerconfiguration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.offer_offerconfiguration (
    id integer NOT NULL,
    main_image character varying(100) NOT NULL,
    main_image_alt character varying(400) NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.offer_offerconfiguration OWNER TO postgres;

--
-- TOC entry 240 (class 1259 OID 16967)
-- Name: offer_offerconfiguration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.offer_offerconfiguration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.offer_offerconfiguration_id_seq OWNER TO postgres;

--
-- TOC entry 3326 (class 0 OID 0)
-- Dependencies: 240
-- Name: offer_offerconfiguration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.offer_offerconfiguration_id_seq OWNED BY public.offer_offerconfiguration.id;


--
-- TOC entry 243 (class 1259 OID 16980)
-- Name: offer_offeritem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.offer_offeritem (
    id integer NOT NULL,
    title text NOT NULL,
    text text NOT NULL,
    image character varying(100) NOT NULL,
    image_alt text NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.offer_offeritem OWNER TO postgres;

--
-- TOC entry 242 (class 1259 OID 16978)
-- Name: offer_offeritem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.offer_offeritem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.offer_offeritem_id_seq OWNER TO postgres;

--
-- TOC entry 3327 (class 0 OID 0)
-- Dependencies: 242
-- Name: offer_offeritem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.offer_offeritem_id_seq OWNED BY public.offer_offeritem.id;


--
-- TOC entry 245 (class 1259 OID 16991)
-- Name: opinions_opinionitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.opinions_opinionitem (
    id integer NOT NULL,
    opinion_text text NOT NULL,
    customer_name character varying(400) NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.opinions_opinionitem OWNER TO postgres;

--
-- TOC entry 244 (class 1259 OID 16989)
-- Name: opinions_opinionitem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.opinions_opinionitem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.opinions_opinionitem_id_seq OWNER TO postgres;

--
-- TOC entry 3328 (class 0 OID 0)
-- Dependencies: 244
-- Name: opinions_opinionitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.opinions_opinionitem_id_seq OWNED BY public.opinions_opinionitem.id;


--
-- TOC entry 247 (class 1259 OID 17002)
-- Name: opinions_opinionsconfiguration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.opinions_opinionsconfiguration (
    id integer NOT NULL,
    main_image character varying(100) NOT NULL,
    main_image_alt character varying(400) NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.opinions_opinionsconfiguration OWNER TO postgres;

--
-- TOC entry 246 (class 1259 OID 17000)
-- Name: opinions_opinionsconfiguration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.opinions_opinionsconfiguration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.opinions_opinionsconfiguration_id_seq OWNER TO postgres;

--
-- TOC entry 3329 (class 0 OID 0)
-- Dependencies: 246
-- Name: opinions_opinionsconfiguration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.opinions_opinionsconfiguration_id_seq OWNED BY public.opinions_opinionsconfiguration.id;


--
-- TOC entry 3013 (class 2604 OID 16724)
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- TOC entry 3014 (class 2604 OID 16734)
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 3012 (class 2604 OID 16716)
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- TOC entry 3015 (class 2604 OID 16742)
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- TOC entry 3016 (class 2604 OID 16752)
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- TOC entry 3017 (class 2604 OID 16760)
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 3020 (class 2604 OID 16853)
-- Name: blog_blogconfiguration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_blogconfiguration ALTER COLUMN id SET DEFAULT nextval('public.blog_blogconfiguration_id_seq'::regclass);


--
-- TOC entry 3021 (class 2604 OID 16864)
-- Name: blog_blogpost id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_blogpost ALTER COLUMN id SET DEFAULT nextval('public.blog_blogpost_id_seq'::regclass);


--
-- TOC entry 3022 (class 2604 OID 16875)
-- Name: contact_contact id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact_contact ALTER COLUMN id SET DEFAULT nextval('public.contact_contact_id_seq'::regclass);


--
-- TOC entry 3023 (class 2604 OID 16886)
-- Name: contact_contactconfiguration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact_contactconfiguration ALTER COLUMN id SET DEFAULT nextval('public.contact_contactconfiguration_id_seq'::regclass);


--
-- TOC entry 3018 (class 2604 OID 16820)
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- TOC entry 3011 (class 2604 OID 16706)
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- TOC entry 3010 (class 2604 OID 16695)
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- TOC entry 3024 (class 2604 OID 16897)
-- Name: faq_faqconfiguration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faq_faqconfiguration ALTER COLUMN id SET DEFAULT nextval('public.faq_faqconfiguration_id_seq'::regclass);


--
-- TOC entry 3025 (class 2604 OID 16908)
-- Name: faq_faqitem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faq_faqitem ALTER COLUMN id SET DEFAULT nextval('public.faq_faqitem_id_seq'::regclass);


--
-- TOC entry 3026 (class 2604 OID 16919)
-- Name: info_info id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.info_info ALTER COLUMN id SET DEFAULT nextval('public.info_info_id_seq'::regclass);


--
-- TOC entry 3027 (class 2604 OID 16930)
-- Name: main_mainboxitem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_mainboxitem ALTER COLUMN id SET DEFAULT nextval('public.main_mainboxitem_id_seq'::regclass);


--
-- TOC entry 3028 (class 2604 OID 16941)
-- Name: main_mainconfiguration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_mainconfiguration ALTER COLUMN id SET DEFAULT nextval('public.main_mainconfiguration_id_seq'::regclass);


--
-- TOC entry 3029 (class 2604 OID 16952)
-- Name: main_mainsliderconfiguration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_mainsliderconfiguration ALTER COLUMN id SET DEFAULT nextval('public.main_mainsliderconfiguration_id_seq'::regclass);


--
-- TOC entry 3031 (class 2604 OID 16961)
-- Name: main_mainslideritem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_mainslideritem ALTER COLUMN id SET DEFAULT nextval('public.main_mainslideritem_id_seq'::regclass);


--
-- TOC entry 3032 (class 2604 OID 16972)
-- Name: offer_offerconfiguration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.offer_offerconfiguration ALTER COLUMN id SET DEFAULT nextval('public.offer_offerconfiguration_id_seq'::regclass);


--
-- TOC entry 3033 (class 2604 OID 16983)
-- Name: offer_offeritem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.offer_offeritem ALTER COLUMN id SET DEFAULT nextval('public.offer_offeritem_id_seq'::regclass);


--
-- TOC entry 3034 (class 2604 OID 16994)
-- Name: opinions_opinionitem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opinions_opinionitem ALTER COLUMN id SET DEFAULT nextval('public.opinions_opinionitem_id_seq'::regclass);


--
-- TOC entry 3035 (class 2604 OID 17005)
-- Name: opinions_opinionsconfiguration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opinions_opinionsconfiguration ALTER COLUMN id SET DEFAULT nextval('public.opinions_opinionsconfiguration_id_seq'::regclass);


--
-- TOC entry 3259 (class 0 OID 16721)
-- Dependencies: 207
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- TOC entry 3261 (class 0 OID 16731)
-- Dependencies: 209
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- TOC entry 3257 (class 0 OID 16713)
-- Dependencies: 205
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add main box item	1	add_mainboxitem
2	Can change main box item	1	change_mainboxitem
3	Can delete main box item	1	delete_mainboxitem
4	Can view main box item	1	view_mainboxitem
5	Can add main configuration	2	add_mainconfiguration
6	Can change main configuration	2	change_mainconfiguration
7	Can delete main configuration	2	delete_mainconfiguration
8	Can view main configuration	2	view_mainconfiguration
9	Can add main slider configuration	3	add_mainsliderconfiguration
10	Can change main slider configuration	3	change_mainsliderconfiguration
11	Can delete main slider configuration	3	delete_mainsliderconfiguration
12	Can view main slider configuration	3	view_mainsliderconfiguration
13	Can add main slider item	4	add_mainslideritem
14	Can change main slider item	4	change_mainslideritem
15	Can delete main slider item	4	delete_mainslideritem
16	Can view main slider item	4	view_mainslideritem
17	Can add faq configuration	5	add_faqconfiguration
18	Can change faq configuration	5	change_faqconfiguration
19	Can delete faq configuration	5	delete_faqconfiguration
20	Can view faq configuration	5	view_faqconfiguration
21	Can add faq item	6	add_faqitem
22	Can change faq item	6	change_faqitem
23	Can delete faq item	6	delete_faqitem
24	Can view faq item	6	view_faqitem
25	Can add contact	7	add_contact
26	Can change contact	7	change_contact
27	Can delete contact	7	delete_contact
28	Can view contact	7	view_contact
29	Can add contact configuration	8	add_contactconfiguration
30	Can change contact configuration	8	change_contactconfiguration
31	Can delete contact configuration	8	delete_contactconfiguration
32	Can view contact configuration	8	view_contactconfiguration
33	Can add opinion item	9	add_opinionitem
34	Can change opinion item	9	change_opinionitem
35	Can delete opinion item	9	delete_opinionitem
36	Can view opinion item	9	view_opinionitem
37	Can add opinions configuration	10	add_opinionsconfiguration
38	Can change opinions configuration	10	change_opinionsconfiguration
39	Can delete opinions configuration	10	delete_opinionsconfiguration
40	Can view opinions configuration	10	view_opinionsconfiguration
41	Can add info	11	add_info
42	Can change info	11	change_info
43	Can delete info	11	delete_info
44	Can view info	11	view_info
45	Can add blog configuration	12	add_blogconfiguration
46	Can change blog configuration	12	change_blogconfiguration
47	Can delete blog configuration	12	delete_blogconfiguration
48	Can view blog configuration	12	view_blogconfiguration
49	Can add blog post	13	add_blogpost
50	Can change blog post	13	change_blogpost
51	Can delete blog post	13	delete_blogpost
52	Can view blog post	13	view_blogpost
53	Can add offer configuration	14	add_offerconfiguration
54	Can change offer configuration	14	change_offerconfiguration
55	Can delete offer configuration	14	delete_offerconfiguration
56	Can view offer configuration	14	view_offerconfiguration
57	Can add offer item	15	add_offeritem
58	Can change offer item	15	change_offeritem
59	Can delete offer item	15	delete_offeritem
60	Can view offer item	15	view_offeritem
61	Can add log entry	16	add_logentry
62	Can change log entry	16	change_logentry
63	Can delete log entry	16	delete_logentry
64	Can view log entry	16	view_logentry
65	Can add permission	17	add_permission
66	Can change permission	17	change_permission
67	Can delete permission	17	delete_permission
68	Can view permission	17	view_permission
69	Can add group	18	add_group
70	Can change group	18	change_group
71	Can delete group	18	delete_group
72	Can view group	18	view_group
73	Can add user	19	add_user
74	Can change user	19	change_user
75	Can delete user	19	delete_user
76	Can view user	19	view_user
77	Can add content type	20	add_contenttype
78	Can change content type	20	change_contenttype
79	Can delete content type	20	delete_contenttype
80	Can view content type	20	view_contenttype
81	Can add session	21	add_session
82	Can change session	21	change_session
83	Can delete session	21	delete_session
84	Can view session	21	view_session
\.


--
-- TOC entry 3263 (class 0 OID 16739)
-- Dependencies: 211
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$216000$NdXmgJb3sQE5$q6pdYhtHqqUxnVSnaJNcr9UQdiojyTWEB30hBKXR5Do=	2020-10-08 00:27:30.767187+02	t	admin			artur@szwagrzak.pl	t	t	2020-10-08 00:27:26.533897+02
\.


--
-- TOC entry 3265 (class 0 OID 16749)
-- Dependencies: 213
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 3267 (class 0 OID 16757)
-- Dependencies: 215
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 3271 (class 0 OID 16850)
-- Dependencies: 219
-- Data for Name: blog_blogconfiguration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blog_blogconfiguration (id, main_image, main_image_alt, update_date) FROM stdin;
\.


--
-- TOC entry 3273 (class 0 OID 16861)
-- Dependencies: 221
-- Data for Name: blog_blogpost; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blog_blogpost (id, photo, photo_alt, description, publication_date, update_date) FROM stdin;
\.


--
-- TOC entry 3275 (class 0 OID 16872)
-- Dependencies: 223
-- Data for Name: contact_contact; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contact_contact (id, message, email, phone, name, attachment_img, update_date) FROM stdin;
\.


--
-- TOC entry 3277 (class 0 OID 16883)
-- Dependencies: 225
-- Data for Name: contact_contactconfiguration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contact_contactconfiguration (id, map_url, phone_number, email, on_site_client_info, working_hours, update_date) FROM stdin;
\.


--
-- TOC entry 3269 (class 0 OID 16817)
-- Dependencies: 217
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-10-08 00:41:59.225106+02	1	Main page slider configuration	1	[{"added": {}}]	3	1
2	2020-10-08 00:42:45.335457+02	1	Main page configuration	1	[{"added": {}}]	2	1
3	2020-10-08 00:43:24.83272+02	1	masaz	1	[{"added": {}}]	4	1
4	2020-10-08 00:43:41.167171+02	2	masaz 2	1	[{"added": {}}]	4	1
5	2020-10-08 00:46:18.781772+02	1	Profesjonalizm	1	[{"added": {}}]	1	1
6	2020-10-08 00:47:10.761238+02	2	Dojazd do domu	1	[{"added": {}}]	1	1
7	2020-10-08 00:47:35.120052+02	2	Dojazd do domu	2	[{"changed": {"fields": ["Image alt"]}}]	1	1
8	2020-10-08 00:48:29.731358+02	3	Dobra cena	1	[{"added": {}}]	1	1
9	2020-10-08 00:49:14.114049+02	1	Offers page configuration	1	[{"added": {}}]	14	1
10	2020-10-08 00:52:31.298095+02	1	MASAŻ KLASYCZNY	1	[{"added": {}}]	15	1
11	2020-10-08 00:53:07.398346+02	2	Masaz relaksacyjny	1	[{"added": {}}]	15	1
12	2020-10-08 00:54:06.035902+02	3	MASAŻ BAŃKĄ CHIŃSKĄ	1	[{"added": {}}]	15	1
13	2020-10-08 00:55:21.26142+02	4	Masaz lorem ipsum	1	[{"added": {}}]	15	1
14	2020-10-08 00:55:39.978195+02	5	Masaz lorem ipsum 2	1	[{"added": {}}]	15	1
\.


--
-- TOC entry 3255 (class 0 OID 16703)
-- Dependencies: 203
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	main	mainboxitem
2	main	mainconfiguration
3	main	mainsliderconfiguration
4	main	mainslideritem
5	faq	faqconfiguration
6	faq	faqitem
7	contact	contact
8	contact	contactconfiguration
9	opinions	opinionitem
10	opinions	opinionsconfiguration
11	info	info
12	blog	blogconfiguration
13	blog	blogpost
14	offer	offerconfiguration
15	offer	offeritem
16	admin	logentry
17	auth	permission
18	auth	group
19	auth	user
20	contenttypes	contenttype
21	sessions	session
\.


--
-- TOC entry 3253 (class 0 OID 16692)
-- Dependencies: 201
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-10-08 00:25:00.419824+02
2	auth	0001_initial	2020-10-08 00:25:00.569455+02
3	admin	0001_initial	2020-10-08 00:25:00.743554+02
4	admin	0002_logentry_remove_auto_add	2020-10-08 00:25:00.805286+02
5	admin	0003_logentry_add_action_flag_choices	2020-10-08 00:25:00.834479+02
6	contenttypes	0002_remove_content_type_name	2020-10-08 00:25:00.903888+02
7	auth	0002_alter_permission_name_max_length	2020-10-08 00:25:00.940786+02
8	auth	0003_alter_user_email_max_length	2020-10-08 00:25:00.974694+02
9	auth	0004_alter_user_username_opts	2020-10-08 00:25:01.014586+02
10	auth	0005_alter_user_last_login_null	2020-10-08 00:25:01.051488+02
11	auth	0006_require_contenttypes_0002	2020-10-08 00:25:01.059468+02
12	auth	0007_alter_validators_add_error_messages	2020-10-08 00:25:01.098437+02
13	auth	0008_alter_user_username_max_length	2020-10-08 00:25:01.168036+02
14	auth	0009_alter_user_last_name_max_length	2020-10-08 00:25:01.20094+02
15	auth	0010_alter_group_name_max_length	2020-10-08 00:25:01.243828+02
16	auth	0011_update_proxy_permissions	2020-10-08 00:25:01.275738+02
17	auth	0012_alter_user_first_name_max_length	2020-10-08 00:25:01.305656+02
18	blog	0001_initial	2020-10-08 00:25:01.371481+02
19	contact	0001_initial	2020-10-08 00:25:01.432083+02
20	faq	0001_initial	2020-10-08 00:25:01.49392+02
21	info	0001_initial	2020-10-08 00:25:01.530818+02
22	main	0001_initial	2020-10-08 00:25:01.649506+02
23	offer	0001_initial	2020-10-08 00:25:01.708821+02
24	opinions	0001_initial	2020-10-08 00:25:01.771646+02
25	sessions	0001_initial	2020-10-08 00:25:01.803562+02
\.


--
-- TOC entry 3300 (class 0 OID 17011)
-- Dependencies: 248
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
x0f5v0hny4iyarwxerj9is0gscnxn1zi	.eJxVjMEOwiAQRP-FsyGQBQoevfsNZFkWqRqalPbU-O-2SQ96m8x7M5uIuC41rp3nOGZxFVpcfruE9OJ2gPzE9pgkTW2ZxyQPRZ60y_uU-X073b-Dir3ua8tkg9Wc_LDHElRghV5lA6gdhUIGnFOJi9F5AHDAmlyARAY1GevF5wvpfzfY:1kQHuE:6nTnbZnqjpemVjRlQp0RAPdPoD3_TTFM59uobi6RY44	2020-10-22 00:27:30.77317+02
\.


--
-- TOC entry 3279 (class 0 OID 16894)
-- Dependencies: 227
-- Data for Name: faq_faqconfiguration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faq_faqconfiguration (id, main_image, main_image_alt, update_date) FROM stdin;
\.


--
-- TOC entry 3281 (class 0 OID 16905)
-- Dependencies: 229
-- Data for Name: faq_faqitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faq_faqitem (id, question_text, answer_text, update_date) FROM stdin;
\.


--
-- TOC entry 3283 (class 0 OID 16916)
-- Dependencies: 231
-- Data for Name: info_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.info_info (id, photo, photo_alt, description, update_date) FROM stdin;
\.


--
-- TOC entry 3285 (class 0 OID 16927)
-- Dependencies: 233
-- Data for Name: main_mainboxitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.main_mainboxitem (id, header_text, image, image_alt, description, visible, update_date) FROM stdin;
1	Profesjonalizm	images/light.jpg	Profesjonalizm	<p><strong>Lorem ipsum dolor sit amet</strong>, consectetur adipiscing elit. Donec tempor laoreet interdum. Pellentesque ut odio venenatis, tristique nulla eu, pharetra sem. Praesent ullamcorper urna pharetra neque rutrum fringilla.&nbsp;</p>	t	2020-10-08 00:46:18.776791+02
2	Dojazd do domu	images/dojazd_YtcrS1k.jpg	Dojazd do domu	<p><strong>Morbi sed convallis diam</strong>. Vestibulum tincidunt, sapien suscipit scelerisque egestas, nisl ante ultricies urna, sit amet tempor augue elit sit amet nisl. Duis eget ullamcorper&nbsp;</p>	t	2020-10-08 00:47:35.115065+02
3	Dobra cena	images/masaz_NYcInk5.jpg	Dobra cena	<p><strong>Vestibulum tincidunt, sapien suscipit scelerisque egestas,</strong> nisl ante ultricies urna, sit amet tempor augue elit sit amet nisl. Duis eget ullamcorper ex, vel malesuada tortor. Donec sit amet ornare nisi. Fusce interdum enim et augue egestas egestas. Quisque quis velit et urna lobortis blandit.</p>	t	2020-10-08 00:48:29.727375+02
\.


--
-- TOC entry 3287 (class 0 OID 16938)
-- Dependencies: 235
-- Data for Name: main_mainconfiguration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.main_mainconfiguration (id, is_modal_visible, newsletter_info, update_date) FROM stdin;
1	f	<p>Chcesz byc na biezaco z naszymi ofertami? Zapisz sie na newsletter!</p>	2020-10-08 00:42:45.329473+02
\.


--
-- TOC entry 3289 (class 0 OID 16949)
-- Dependencies: 237
-- Data for Name: main_mainsliderconfiguration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.main_mainsliderconfiguration (id, change_image_time_ms, update_date) FROM stdin;
1	500	2020-10-08 00:41:59.218096+02
\.


--
-- TOC entry 3291 (class 0 OID 16958)
-- Dependencies: 239
-- Data for Name: main_mainslideritem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.main_mainslideritem (id, image, image_alt, visible, update_date) FROM stdin;
1	images/relax_XuZ3tNb.jpg	masaz	t	2020-10-08 00:43:24.827733+02
2	images/masaz2.jpg	masaz 2	t	2020-10-08 00:43:41.163185+02
\.


--
-- TOC entry 3293 (class 0 OID 16969)
-- Dependencies: 241
-- Data for Name: offer_offerconfiguration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.offer_offerconfiguration (id, main_image, main_image_alt, update_date) FROM stdin;
1	images/relax_ouer20A.jpg	Nasze oferty	2020-10-08 00:49:14.109063+02
\.


--
-- TOC entry 3295 (class 0 OID 16980)
-- Dependencies: 243
-- Data for Name: offer_offeritem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.offer_offeritem (id, title, text, image, image_alt, update_date) FROM stdin;
1	MASAŻ KLASYCZNY	<p><strong>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot;&nbsp;Od 40 zł do 120 zł</strong></p>\r\n\r\n<p>Najbardziej znany i popularny masaż na świecie. Łagodzi dolegliwości b&oacute;lowe, rozluźnia mięśnie i poprawia samopoczucie. Działa przeciwb&oacute;lowo, poprawia ukrwienie, odżywia tkanki, ujędrnia mięśnie i uelastycznia sk&oacute;rę. Może dotyczyć całego ciała lub poszczeg&oacute;lnych jego części. Jest dobry dla os&oacute;b w każdym wieku.</p>	masaz2.jpg	Masaz klasyczny	2020-10-08 00:52:31.292111+02
2	Masaz relaksacyjny	<p><strong>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot;&nbsp;Od 100 zł do 150 zł</strong></p>\r\n\r\n<p>Masaż aromaterapeutyczny całego ciała na bazie naturalnych, ciepłych olejk&oacute;w. Delikatniejszy i mniej intensywny od masażu klasycznego, zmniejsza napięcie mięśni i oddziałuje na układ nerwowy. Skutecznie redukuje stres, regeneruje siły witalne, odpręża ciało, umysł i duszę. Wprowadza w stan głębokiego relaksu.</p>	masaz_TY9WeB6.jpg	Masaz relaksacyjny	2020-10-08 00:53:07.393358+02
3	MASAŻ BAŃKĄ CHIŃSKĄ	<p><strong>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot;&nbsp;20 minut 50 zł</strong></p>\r\n\r\n<p>Wykorzystuje metodę pr&oacute;żniowego zasysania sk&oacute;ry i znajdujących się pod nią tkanek, doskonale poprawiając ich ukrwienie. Pobudza procesy przemiany materii i usuwa toksyny z organizmu, rozbija tkankę tłuszczową, wspomaga walkę z cellulitem i wyraźnie wygładza sk&oacute;rę.</p>	relax_fNSgOlH.jpg	MASAŻ BAŃKĄ CHIŃSKĄ	2020-10-08 00:54:06.029509+02
4	Masaz lorem ipsum	<p><strong>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot;&nbsp;Od 36383 zł do 345345 zł</strong></p>\r\n\r\n<p>Lorem ipsum&nbsp;Mauris in scelerisque dolor, sit amet interdum mi. Integer in ante maximus, sodales velit nec, pretium lectus. Quisque non mauris eget justo tempus malesuada in a urna. Fusce sagittis dui sit amet magna iaculis porta. Pellentesque posuere enim eros, at fermentum est fringilla a. Nullam molestie vitae urna ac luctus. Mauris malesuada semper ante, non molestie sem posuere quis. Sed hendrerit sit amet ante eu pulvinar. Ut et porta mauris.</p>	light.jpg	Masaz lorem ipsum	2020-10-08 00:55:21.257434+02
5	Masaz lorem ipsum 2	<p><strong>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot;&nbsp;Od 36383 zł do 345345 zł</strong></p>\r\n\r\n<p>Lorem ipsum&nbsp;Mauris in scelerisque dolor, sit amet interdum mi. Integer in ante maximus, sodales velit nec, pretium lectus. Quisque non mauris eget justo tempus malesuada in a urna. Fusce sagittis dui sit amet magna iaculis porta. Pellentesque posuere enim eros, at fermentum est fringilla a. Nullam molestie vitae urna ac luctus. Mauris malesuada semper ante, non molestie sem posuere quis. Sed hendrerit sit amet ante eu pulvinar. Ut et porta mauris.</p>	masaz2_3tbAQZC.jpg	Masaz lorem ipsum 2	2020-10-08 00:55:39.974158+02
\.


--
-- TOC entry 3297 (class 0 OID 16991)
-- Dependencies: 245
-- Data for Name: opinions_opinionitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.opinions_opinionitem (id, opinion_text, customer_name, update_date) FROM stdin;
\.


--
-- TOC entry 3299 (class 0 OID 17002)
-- Dependencies: 247
-- Data for Name: opinions_opinionsconfiguration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.opinions_opinionsconfiguration (id, main_image, main_image_alt, update_date) FROM stdin;
\.


--
-- TOC entry 3330 (class 0 OID 0)
-- Dependencies: 206
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- TOC entry 3331 (class 0 OID 0)
-- Dependencies: 208
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 3332 (class 0 OID 0)
-- Dependencies: 204
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 84, true);


--
-- TOC entry 3333 (class 0 OID 0)
-- Dependencies: 212
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- TOC entry 3334 (class 0 OID 0)
-- Dependencies: 210
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- TOC entry 3335 (class 0 OID 0)
-- Dependencies: 214
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 3336 (class 0 OID 0)
-- Dependencies: 218
-- Name: blog_blogconfiguration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_blogconfiguration_id_seq', 1, false);


--
-- TOC entry 3337 (class 0 OID 0)
-- Dependencies: 220
-- Name: blog_blogpost_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_blogpost_id_seq', 1, false);


--
-- TOC entry 3338 (class 0 OID 0)
-- Dependencies: 222
-- Name: contact_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contact_contact_id_seq', 1, false);


--
-- TOC entry 3339 (class 0 OID 0)
-- Dependencies: 224
-- Name: contact_contactconfiguration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contact_contactconfiguration_id_seq', 1, false);


--
-- TOC entry 3340 (class 0 OID 0)
-- Dependencies: 216
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 14, true);


--
-- TOC entry 3341 (class 0 OID 0)
-- Dependencies: 202
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 21, true);


--
-- TOC entry 3342 (class 0 OID 0)
-- Dependencies: 200
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 25, true);


--
-- TOC entry 3343 (class 0 OID 0)
-- Dependencies: 226
-- Name: faq_faqconfiguration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.faq_faqconfiguration_id_seq', 1, false);


--
-- TOC entry 3344 (class 0 OID 0)
-- Dependencies: 228
-- Name: faq_faqitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.faq_faqitem_id_seq', 1, false);


--
-- TOC entry 3345 (class 0 OID 0)
-- Dependencies: 230
-- Name: info_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.info_info_id_seq', 1, false);


--
-- TOC entry 3346 (class 0 OID 0)
-- Dependencies: 232
-- Name: main_mainboxitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.main_mainboxitem_id_seq', 3, true);


--
-- TOC entry 3347 (class 0 OID 0)
-- Dependencies: 234
-- Name: main_mainconfiguration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.main_mainconfiguration_id_seq', 1, true);


--
-- TOC entry 3348 (class 0 OID 0)
-- Dependencies: 236
-- Name: main_mainsliderconfiguration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.main_mainsliderconfiguration_id_seq', 1, true);


--
-- TOC entry 3349 (class 0 OID 0)
-- Dependencies: 238
-- Name: main_mainslideritem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.main_mainslideritem_id_seq', 2, true);


--
-- TOC entry 3350 (class 0 OID 0)
-- Dependencies: 240
-- Name: offer_offerconfiguration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.offer_offerconfiguration_id_seq', 1, true);


--
-- TOC entry 3351 (class 0 OID 0)
-- Dependencies: 242
-- Name: offer_offeritem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.offer_offeritem_id_seq', 5, true);


--
-- TOC entry 3352 (class 0 OID 0)
-- Dependencies: 244
-- Name: opinions_opinionitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.opinions_opinionitem_id_seq', 1, false);


--
-- TOC entry 3353 (class 0 OID 0)
-- Dependencies: 246
-- Name: opinions_opinionsconfiguration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.opinions_opinionsconfiguration_id_seq', 1, false);


--
-- TOC entry 3049 (class 2606 OID 16846)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 3054 (class 2606 OID 16773)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 3057 (class 2606 OID 16736)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3051 (class 2606 OID 16726)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 3044 (class 2606 OID 16764)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 3046 (class 2606 OID 16718)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 3065 (class 2606 OID 16754)
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3068 (class 2606 OID 16788)
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- TOC entry 3059 (class 2606 OID 16744)
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 3071 (class 2606 OID 16762)
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3074 (class 2606 OID 16802)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- TOC entry 3062 (class 2606 OID 16840)
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 3080 (class 2606 OID 16858)
-- Name: blog_blogconfiguration blog_blogconfiguration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_blogconfiguration
    ADD CONSTRAINT blog_blogconfiguration_pkey PRIMARY KEY (id);


--
-- TOC entry 3082 (class 2606 OID 16869)
-- Name: blog_blogpost blog_blogpost_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_blogpost
    ADD CONSTRAINT blog_blogpost_pkey PRIMARY KEY (id);


--
-- TOC entry 3084 (class 2606 OID 16880)
-- Name: contact_contact contact_contact_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact_contact
    ADD CONSTRAINT contact_contact_pkey PRIMARY KEY (id);


--
-- TOC entry 3086 (class 2606 OID 16891)
-- Name: contact_contactconfiguration contact_contactconfiguration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact_contactconfiguration
    ADD CONSTRAINT contact_contactconfiguration_pkey PRIMARY KEY (id);


--
-- TOC entry 3077 (class 2606 OID 16826)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 3039 (class 2606 OID 16710)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 3041 (class 2606 OID 16708)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 3037 (class 2606 OID 16700)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 3111 (class 2606 OID 17018)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 3088 (class 2606 OID 16902)
-- Name: faq_faqconfiguration faq_faqconfiguration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faq_faqconfiguration
    ADD CONSTRAINT faq_faqconfiguration_pkey PRIMARY KEY (id);


--
-- TOC entry 3090 (class 2606 OID 16913)
-- Name: faq_faqitem faq_faqitem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faq_faqitem
    ADD CONSTRAINT faq_faqitem_pkey PRIMARY KEY (id);


--
-- TOC entry 3092 (class 2606 OID 16924)
-- Name: info_info info_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.info_info
    ADD CONSTRAINT info_info_pkey PRIMARY KEY (id);


--
-- TOC entry 3094 (class 2606 OID 16935)
-- Name: main_mainboxitem main_mainboxitem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_mainboxitem
    ADD CONSTRAINT main_mainboxitem_pkey PRIMARY KEY (id);


--
-- TOC entry 3096 (class 2606 OID 16946)
-- Name: main_mainconfiguration main_mainconfiguration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_mainconfiguration
    ADD CONSTRAINT main_mainconfiguration_pkey PRIMARY KEY (id);


--
-- TOC entry 3098 (class 2606 OID 16955)
-- Name: main_mainsliderconfiguration main_mainsliderconfiguration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_mainsliderconfiguration
    ADD CONSTRAINT main_mainsliderconfiguration_pkey PRIMARY KEY (id);


--
-- TOC entry 3100 (class 2606 OID 16966)
-- Name: main_mainslideritem main_mainslideritem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_mainslideritem
    ADD CONSTRAINT main_mainslideritem_pkey PRIMARY KEY (id);


--
-- TOC entry 3102 (class 2606 OID 16977)
-- Name: offer_offerconfiguration offer_offerconfiguration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.offer_offerconfiguration
    ADD CONSTRAINT offer_offerconfiguration_pkey PRIMARY KEY (id);


--
-- TOC entry 3104 (class 2606 OID 16988)
-- Name: offer_offeritem offer_offeritem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.offer_offeritem
    ADD CONSTRAINT offer_offeritem_pkey PRIMARY KEY (id);


--
-- TOC entry 3106 (class 2606 OID 16999)
-- Name: opinions_opinionitem opinions_opinionitem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opinions_opinionitem
    ADD CONSTRAINT opinions_opinionitem_pkey PRIMARY KEY (id);


--
-- TOC entry 3108 (class 2606 OID 17010)
-- Name: opinions_opinionsconfiguration opinions_opinionsconfiguration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opinions_opinionsconfiguration
    ADD CONSTRAINT opinions_opinionsconfiguration_pkey PRIMARY KEY (id);


--
-- TOC entry 3047 (class 1259 OID 16847)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 3052 (class 1259 OID 16784)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 3055 (class 1259 OID 16785)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 3042 (class 1259 OID 16770)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 3063 (class 1259 OID 16800)
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- TOC entry 3066 (class 1259 OID 16799)
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- TOC entry 3069 (class 1259 OID 16814)
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 3072 (class 1259 OID 16813)
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 3060 (class 1259 OID 16841)
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 3075 (class 1259 OID 16837)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 3078 (class 1259 OID 16838)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 3109 (class 1259 OID 17020)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 3112 (class 1259 OID 17019)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 3115 (class 2606 OID 16779)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3114 (class 2606 OID 16774)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3113 (class 2606 OID 16765)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3117 (class 2606 OID 16794)
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3116 (class 2606 OID 16789)
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3119 (class 2606 OID 16808)
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3118 (class 2606 OID 16803)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3120 (class 2606 OID 16827)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3121 (class 2606 OID 16832)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2020-10-08 01:07:27

--
-- PostgreSQL database dump complete
--

