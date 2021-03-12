
--
-- Zrzut danych tabeli auth_user
--

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(1, 'pbkdf2_sha256$150000$NaWaaNLPQRWB$1iGWTr6kjHYUIjTjb11nJ8JNaB8webCnWiqwiBDFSJU=', '2021-03-02 21:55:53.654733', 1, 'arturszwagrzak', '', '', 'artur@szwagrzak.pl', 1, 1, '2020-11-17 23:39:13.323966');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(2, 'pbkdf2_sha256$150000$k4F6Yrb7LtRy$HWTFTH8gpkour3aVKZBUEdXj0+/9gGqYK6QcbQ9SBW0=', '2021-02-15 18:13:10.646931', 1, 'justyna', '', '', 'j@p.ie', 1, 1, '2020-11-21 18:18:49.756756');

--
-- Zrzut danych tabeli blog_blogconfiguration
--

INSERT INTO blog_blogconfiguration (id, main_image, main_image_alt, update_date) VALUES(1, 'images/na_stonę_www_książka_canva_CiAO9ef.png', 'BLOG', '2021-01-29 14:35:54.675128');

--
-- Zrzut danych tabeli blog_blogpost
--

INSERT INTO blog_blogpost (id, photo, photo_alt, description, publication_date, update_date, element_order) VALUES(1, 'images/naslajder_wEIkTCF.jpg', 'Zaczynamy!', 'Witam na moim blogu :-)', '2021-01-29 14:40:20.810041', '2021-01-29 14:40:20.810113', 0);

--
-- Zrzut danych tabeli contact_contact
--

INSERT INTO contact_contact (id, message, email, name, update_date, permission) VALUES(1, 'aaaaa', 'artur.szwagrzak@gmail.com', 'Artur Szwagrzak', '2021-01-13 16:54:49.703696', 1);
INSERT INTO contact_contact (id, message, email, name, update_date, permission) VALUES(3, 'dfasdfasdf', 'artur.szwagrzak@gmail.com', 'Artur Szwagrzaksdafasdf', '2021-03-04 15:45:33.936015', 1);
INSERT INTO contact_contact (id, message, email, name, update_date, permission) VALUES(4, 'fdsfasdf', 'artur.szwagrzak@gmail.com', 'Artur Szwagrzak', '2021-03-04 15:46:08.184521', 1);
INSERT INTO contact_contact (id, message, email, name, update_date, permission) VALUES(5, 'asdfasdf', 'artur.szwagrzak@gmail.com', 'Artur Szwagrzak', '2021-03-04 15:48:50.382008', 1);
INSERT INTO contact_contact (id, message, email, name, update_date, permission) VALUES(6, 'dsfa', 'artur.szwagrzak@gmail.com', 'Artur Szwagrzak', '2021-03-04 15:49:05.905619', 1);
INSERT INTO contact_contact (id, message, email, name, update_date, permission) VALUES(7, 'asfdsf', 'artur.szwagrzak@gmail.com', 'Artur Szwagrzak', '2021-03-04 15:49:51.429146', 1);
INSERT INTO contact_contact (id, message, email, name, update_date, permission) VALUES(8, 'fasdf', 'artur.szwagrzak@gmail.comfff', 'Artur Szwagrzakff', '2021-03-04 15:49:58.106540', 1);

--
-- Zrzut danych tabeli contact_contactconfiguration
--

INSERT INTO contact_contactconfiguration (id, map_url, phone_number, email, on_site_client_info, have_questions, working_hours, facebook, twitter, linkedin, instagram, snapchat, youtube, google_map, update_date) VALUES(1, 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2548.5237834465074!2d18.6868682158951!3d50.300816706016164!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4711314a54981b81%3A0x497cea66083f4e7e!2sMobilne%20Centrum%20Masa%C5%BCu%20Relaksownia!5e0!3m2!1spl!2spl!4v1603059899120!5m2!1spl!2spl', '+48608557617', 'kontakt@relaksownia.org.pl', '<p>Dojazd do klienta na terenie całego wojew&oacute;dztwa śląskiego, w Gliwicach dojazd gratis</p>', '<p>Masz do mnie pytania albo sugestie, napisz, chętnie odpowiem. Podziel się swoją opinią, ulepszaj z nami nasze usługi.</p>', '<p>&nbsp;</p><table>	<tbody>		<tr>			<td>			<p>poniedziałek</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>wtorek</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>środa</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>czwartek</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>piątek</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>sobota</p>			</td>			<td>			<p>zadzwoń - jeśli nie jestem w g&oacute;rach,&nbsp;</p>			<p>możemy się um&oacute;wić :)</p>			</td>		</tr>	</tbody></table>', 'https://www.facebook.com/relaksownia.masaz', '', 'https://www.linkedin.com/in/justyna-pietraszek-781385144/', 'https://www.instagram.com/justyna_pietraszek1', '', '', 'https://g.page/Relaksownia_Masaz_Gliwice?share', '2021-02-15 18:15:26.782786');

--
-- Zrzut danych tabeli django_content_type
--

INSERT INTO django_content_type (id, app_label, model) VALUES(17, 'admin', 'logentry');
INSERT INTO django_content_type (id, app_label, model) VALUES(18, 'auth', 'group');
INSERT INTO django_content_type (id, app_label, model) VALUES(20, 'auth', 'permission');
INSERT INTO django_content_type (id, app_label, model) VALUES(19, 'auth', 'user');
INSERT INTO django_content_type (id, app_label, model) VALUES(14, 'blog', 'blogconfiguration');
INSERT INTO django_content_type (id, app_label, model) VALUES(13, 'blog', 'blogpost');
INSERT INTO django_content_type (id, app_label, model) VALUES(8, 'contact', 'contact');
INSERT INTO django_content_type (id, app_label, model) VALUES(7, 'contact', 'contactconfiguration');
INSERT INTO django_content_type (id, app_label, model) VALUES(21, 'contenttypes', 'contenttype');
INSERT INTO django_content_type (id, app_label, model) VALUES(6, 'faq', 'faqconfiguration');
INSERT INTO django_content_type (id, app_label, model) VALUES(5, 'faq', 'faqitem');
INSERT INTO django_content_type (id, app_label, model) VALUES(23, 'info', 'certitem');
INSERT INTO django_content_type (id, app_label, model) VALUES(12, 'info', 'info');
INSERT INTO django_content_type (id, app_label, model) VALUES(2, 'main', 'mainboxitem');
INSERT INTO django_content_type (id, app_label, model) VALUES(3, 'main', 'mainconfiguration');
INSERT INTO django_content_type (id, app_label, model) VALUES(1, 'main', 'mainsliderconfiguration');
INSERT INTO django_content_type (id, app_label, model) VALUES(4, 'main', 'mainslideritem');
INSERT INTO django_content_type (id, app_label, model) VALUES(16, 'newsletter', 'newsletter');
INSERT INTO django_content_type (id, app_label, model) VALUES(15, 'offer', 'offeritem');
INSERT INTO django_content_type (id, app_label, model) VALUES(9, 'opinions', 'opinionitem');
INSERT INTO django_content_type (id, app_label, model) VALUES(11, 'opinions', 'opinionsconfiguration');
INSERT INTO django_content_type (id, app_label, model) VALUES(10, 'opinions', 'opiniontreeitem');
INSERT INTO django_content_type (id, app_label, model) VALUES(24, 'policy', 'policyconfiguration');
INSERT INTO django_content_type (id, app_label, model) VALUES(26, 'promo', 'promoclient');
INSERT INTO django_content_type (id, app_label, model) VALUES(28, 'promo', 'promoconfiguration');
INSERT INTO django_content_type (id, app_label, model) VALUES(29, 'promo', 'promoemailconfiguration');
INSERT INTO django_content_type (id, app_label, model) VALUES(25, 'promo', 'promoitem');
INSERT INTO django_content_type (id, app_label, model) VALUES(27, 'promo', 'promopagecomponent');
INSERT INTO django_content_type (id, app_label, model) VALUES(22, 'sessions', 'session');

--
-- Zrzut danych tabeli faq_faqconfiguration
--

INSERT INTO faq_faqconfiguration (id, main_image, main_image_alt, update_date) VALUES(1, 'images/pytania_cQenBz2.jpg', 'Pytania', '2020-11-21 19:01:49.099106');

--
-- Zrzut danych tabeli faq_faqitem
--

INSERT INTO faq_faqitem (id, question_text, answer_text, update_date, element_order) VALUES(1, '<p>Jakie są koszty masaż&oacute;w?&nbsp;</p>', '<p>Cennik masaży jest dostępny na podstronie: <a href=\"/offer\"> OFERTA </a></p>', '2020-11-12 03:46:46.710000', 0);
INSERT INTO faq_faqitem (id, question_text, answer_text, update_date, element_order) VALUES(2, '<p>Jakie są nasze godziny otwarcia i obszar działania ?</p>', '<p>Obszarem naszego działania są Gliwice i okolice.</p>', '2020-11-12 03:41:40.822000', 0);
INSERT INTO faq_faqitem (id, question_text, answer_text, update_date, element_order) VALUES(3, '<p>Jakie masaże są dostępne?</p>', '<p>W naszej ofercie mamy masaże:&nbsp;</p><p>- masaż bańką chińską</p><p>- masaż klasyczny</p><p>- masaż relaksacyjny</p><p>- drenaż limfatyczny</p><p>- kosmetyczny masaż szyi, twarzy i dekoltu</p>', '2020-11-12 03:40:38.618000', 0);

--
-- Zrzut danych tabeli info_certitem
--

INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(1, 'images/aromaterapia.jpg', 'aromaterapia', 13);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(2, 'images/banka-chinska.jpg', 'bańka chińska', 11);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(3, 'images/dyplom.jpg', 'dyplom', 2);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(4, 'images/gorące-kamienie.jpg', 'gorące kamienie', 12);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(5, 'images/kinesio.jpg', 'kinesio', 9);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(6, 'images/kursaroma.jpg', 'kurs aroma', 7);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(7, 'images/kursbanka.jpg', 'kurs bańka', 5);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(8, 'images/kurskamienie.jpg', 'kurs kamienie', 6);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(9, 'images/kurskinesio.jpg', 'kurs kinesio', 8);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(10, 'images/suplement-ang.jpg', 'suplement ang', 10);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(11, 'images/suplement-dyplom.jpg', 'suplement dyplomu', 4);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(12, 'images/swiadectwo-kwalifikacje.jpg', 'świadectwo kwalifikacyjne', 1);
INSERT INTO info_certitem (id, image, image_alt, element_order) VALUES(13, 'images/zaswiadczenie-szkola.jpg', 'zaświadczenie szkoła', 3);

--
-- Zrzut danych tabeli info_info
--

INSERT INTO info_info (id, photo, photo_alt, description, update_date) VALUES(1, 'images/Jysty_kato-29.jpg', 'Justyna', '<h2><u>NAZYWAM SIĘ JUSTYNA PIETRASZEK</h2></u><p>Jestem dyplomowaną masażystką i świadczę mobilne usługi masażu, z dojazdem na terenie Gliwic i okolic (wojew&oacute;dztwo śląskie). Uczyłam się w dwuletniej szkole medycznej na kierunku &quot;Technik masażysta z elementami fizjoterapii&quot;, ukończyłam specjalistyczne kursy masażu, między innymi:&nbsp;bańką chińską, gorącymi kamieniami, masaż aromaterapeutyczny, kinesio taping, a także jestem instruktorem fitness - nowoczesne formy gimnastyki.&nbsp;</p><p>Masaż to m&oacute;j zaw&oacute;d, ale przede wszystkim pasja! Każdego dnia robię to, co po prostu kocham - spotykam się z ludźmi i pomagam im w rozwiązywaniu problem&oacute;w z b&oacute;lem, napięciem i stresem. Uwielbiam te kontakty, rozmowy i niezwykłą atmosferę, kt&oacute;ra się tworzy podczas naszych sesji. Najbardziej zaś cieszą mnie efekty pracy, gdy po masażu Klienci czują wyraźną poprawę.</p><p>Poza pracą interesuję się zdrowym trybem życia i preferuję ruch w każdej postaci - najczęściej jeżdżę na rowerze, chodzę po g&oacute;rach, spaceruję, ćwiczę na siłowni, przez kilka lat trenowałam sztuki walki, a niedawno rozpoczęłam przygodę z morsowaniem :) Moje wartości to zdrowie, ciągły rozw&oacute;j osobisty i dbanie o dobre o relacje. M&oacute;j cel to Twoje lepsze ZDROWIE, a moja misja &ndash; przekazywanie POZYTYWNEJ ENERGII i sprawienie, abyś po spotkaniu ze mną czuł się lepiej, nie tylko fizycznie :)</p>', '2020-12-19 09:14:11.200305');

--
-- Zrzut danych tabeli main_mainboxitem
--

INSERT INTO main_mainboxitem (id, header_text, image, image_alt, description, visible, update_date, element_order) VALUES(1, 'twój komfort - dojazd do domu', 'images/autonastrone_Qchww0R.jpg', 'masaz', '<ul>	<li>Bez stania w korkach</li>	<li>Bez stresu związanego z szukaniem parkingu</li>	<li>Nie marzniesz czekając na przystanku a&nbsp;po masażu nie wychodzisz z ciepłego domu</li>	<li>Oszczędność czasu - świetne rozwiązanie dla zapracowanych - nie musisz nigdzie jechać, bo to ja&nbsp;przyjadę do Ciebie</li>	<li>Masaż bez wychodzenia z domu to idealna opcja&nbsp;- po skończonym masażu zostajesz u siebie i delektujesz się jego dobroczynnym dzialaniem.</li></ul>', 1, '2021-01-23 12:29:13.548884', 1);
INSERT INTO main_mainboxitem (id, header_text, image, image_alt, description, visible, update_date, element_order) VALUES(2, 'głęboki relaks i redukcja stresu', 'images/relaksnastrone_8mRXwzw.jpg', 'auto', '<p>Masaż to zabieg holistyczny, działa leczniczo nie tylko na ciało, ale i na ducha. Wydzielająca się podczas masażu serotonina i dopamina sprzyja odprężeniu i eliminacji negatywnych emocji. Podczas masażu zostajesz wprowadzony w stan głębokiego relaksu, uspokajasz się i napełniasz pozytywną energią życiową.</p>', 1, '2020-12-30 14:28:22.723156', 3);
INSERT INTO main_mainboxitem (id, header_text, image, image_alt, description, visible, update_date, element_order) VALUES(3, 'ukojenie bólu, likwidacja napięć', 'images/box_środkowy.jpg', 'masaz', '<p>In malesuada quam eget egestas fringilla. Proin maximus porttitor dui. In maximus blandit fermentum. Vivamus rhoncus iaculis turpis id euismod.&nbsp;</p>', 1, '2020-12-30 15:07:19.349978', 2);

--
-- Zrzut danych tabeli main_mainconfiguration
--

INSERT INTO main_mainconfiguration (id, is_modal_visible, newsletter_info, main_text, update_date) VALUES(1, 1, '<p>Zapisz się na bezpłatny newsletter i bądź z nami&nbsp;na bieżąco :-)</p>', '<h3>&nbsp;</h3><h2>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CIESZĘ SIĘ, ŻE TU JESTEŚ!</h2><h3>Masaż w RELAKSOWNI to najlepszy wyb&oacute;r, sprawdź dlaczego :)</h3>', '2020-12-19 11:38:39.804988');

--
-- Zrzut danych tabeli main_mainsliderconfiguration
--

INSERT INTO main_mainsliderconfiguration (id, change_image_time_ms, update_date) VALUES(1, 10000, '2020-12-12 09:52:09.477876');

--
-- Zrzut danych tabeli main_mainslideritem
--

INSERT INTO main_mainslideritem (id, image, image_alt, visible, update_date, element_order) VALUES(4, 'images/masaż_mężczyzna_na_slider.jpg', 'mężczyzna', 1, '2020-11-25 19:23:44.237255', 0);
INSERT INTO main_mainslideritem (id, image, image_alt, visible, update_date, element_order) VALUES(5, 'images/naslajder_2qso2Vs.jpg', 'kobieta', 1, '2021-01-29 14:37:29.968274', 0);

--
-- Zrzut danych tabeli newsletter_newsletter
--

INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(1, 'test@test.pl', 'Yolo', 1, '2020-12-27 01:51:04.997921');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(2, 'aaa@dadasdasda.pl', 'Yolo', 1, '2021-01-09 10:08:55.505945');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(3, 'aaa@dadasdasda.pl', 'Yolo', 1, '2021-01-09 10:09:04.014643');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(4, 'artur.szwagrzak@gmail.com', 'demosite', 1, '2021-01-13 16:54:39.467317');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(5, 'artur.szwagrzak@gmail.com', 'demosite', 1, '2021-01-13 16:55:29.195760');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(6, 'artur.szwagrzak@gmail.com', 'demosite', 1, '2021-01-13 16:55:37.703960');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(7, 'dasdas@dadasd.ss', 'sss', 1, '2021-03-04 15:42:05.030224');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(8, 'dasdas@dadasd.ss', 'sss', 1, '2021-03-04 15:42:09.836723');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(9, 'kontakt@relaksownia.org.pl', 'fdsafsdf', 1, '2021-03-04 15:50:05.682914');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(10, 'kontakt@relaksownia.org.pl', 'fdsafsdf', 1, '2021-03-04 15:51:20.076386');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(11, 'kontakt@relaksownia.org.pl', 'fdsafsdf', 1, '2021-03-04 15:51:24.082409');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(12, 'kontakt@relaksownia.org.pl', 'fdsafsdf', 1, '2021-03-04 15:51:26.155832');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(13, 'kontakt@relaksownia.org.pldd', 'fdsafsdf', 1, '2021-03-04 15:51:29.482231');

--
-- Zrzut danych tabeli offer_offeritem
--

INSERT INTO offer_offeritem (id, title, text, image, image_alt, update_date, element_order) VALUES(1, 'MASAŻ LECZNICZY/ KLASYCZNY', '<p>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot; od 20 minut - 40 zł do 60 minut - 120 zł</p><p>Najbardziej znany i popularny masaż na świecie. Łagodzi dolegliwości b&oacute;lowe, rozluźnia mięśnie i poprawia samopoczucie. Działa przeciwb&oacute;lowo, poprawia ukrwienie, odżywia tkanki, ujędrnia mięśnie i uelastycznia sk&oacute;rę. Może dotyczyć całego ciała lub poszczeg&oacute;lnych jego części. Jest dobry dla os&oacute;b w każdym wieku.</p><p>&nbsp;</p>', 'images/paniola_Mybjhsl.jpg', 'klasyczny', '2020-12-30 08:29:51.906694', 1);
INSERT INTO offer_offeritem (id, title, text, image, image_alt, update_date, element_order) VALUES(2, 'MASAŻ RELAKSACYJNY', '<p>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot; 60 minut - 100 zł, 90 minut&nbsp;150 zł</p><p>Masaż relaksacyjny/aromaterapeutyczny całego ciała na bazie naturalnych, ciepłych olejk&oacute;w. Delikatniejszy i mniej intensywny od masażu klasycznego, zmniejsza napięcie mięśni i oddziałuje na układ nerwowy. Skutecznie redukuje stres, regeneruje siły witalne, odpręża ciało, umysł i duszę. Wprowadza w stan głębokiego relaksu.</p>', 'images/ola.jpg', 'relaks', '2020-12-30 08:30:37.158167', 2);
INSERT INTO offer_offeritem (id, title, text, image, image_alt, update_date, element_order) VALUES(3, 'MASAŻ BAŃKĄ CHIŃSKĄ', '<p>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot;&nbsp;20 minut - 50 zł</p><p>Wykorzystuje metodę pr&oacute;żniowego zasysania sk&oacute;ry i znajdujących się pod nią tkanek, doskonale poprawiając ich ukrwienie. Pobudza procesy przemiany materii i usuwa toksyny z organizmu, rozbija tkankę tłuszczową, wspomaga walkę z cellulitem i wyraźnie wygładza sk&oacute;rę.</p>', 'images/bańka_chińska.jpg', 'bańka', '2020-12-30 15:10:24.814895', 3);
INSERT INTO offer_offeritem (id, title, text, image, image_alt, update_date, element_order) VALUES(4, 'KOSMETYCZNY MASAŻ TWARZY, SZYI I DEKOLTU', '<p>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot;&nbsp;30 minut 60 zł</p><p>Jest świetną formą relaksu, szczeg&oacute;lnie dedykowaną kobietom. Delikatne techniki masażu w połączeniu z odpowiednimi kosmetykami wprowadzają w stan rozluźnienia, doskonale dotleniają, uelastyczniają i ujędrniają sk&oacute;rę. Regularnie stosowany zapobiega utrwalaniu zmarszczek i wyraźnie odmładza sk&oacute;rę.</p>', 'images/masaż_twarzybox.jpg', 'twarz', '2020-12-30 15:12:34.683158', 4);
INSERT INTO offer_offeritem (id, title, text, image, image_alt, update_date, element_order) VALUES(5, 'DRENAŻ LIMFATYCZNY', '<p>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot;&nbsp;50 minut 100 zł</p><p>Jest zabiegiem usprawniającym przepływ limfy w organizmie poprzez mechaniczne jej przepchnięcie i udrożnienie węzł&oacute;w chłonnych. Zalecany w przypadku widocznej opuchlizny i tzw. obrzęk&oacute;w zastoinowych kończyn, wspomaga leczenie kobiet po mastektomii. Skutecznie niweluje b&oacute;l, redukuje obrzęki, usuwa toksyny z organizmu i pomaga w walce z cellulitem</p>', 'images/drenaż_box_DSvAgz9.jpg', 'drenaż', '2020-12-30 15:38:33.160238', 5);
INSERT INTO offer_offeritem (id, title, text, image, image_alt, update_date, element_order) VALUES(6, 'MASAŻ W PLENERZE', '<p>Czas trwania jest zr&oacute;żnicowany&nbsp;&middot;&nbsp;60 minut 120 zł, 90 minut 150 zł</p><p>Masaż wykonany na łonie natury, w blasku słońca i przy akompaniamencie spiewu ptak&oacute;w. Działa na zmysły, wspaniale rozluźnia i relaksuje. To idealna opcja na ciepłe, słoneczne dni. Jeśli dysponujesz ogrodem lub&nbsp;działką, takie naturalne SPA będzie idealnym wyborem.</p>', 'images/dzialeczka.jpg', 'plener', '2020-12-30 08:31:16.854387', 6);

--
-- Zrzut danych tabeli opinions_opinionitem
--

INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(1, '<p>Polecam. Miła i profesjonalna obsługa.</p><p>Masaż w domu jest świetnym rozwiązaniem dla os&oacute;b z deficytem czasu!</p>', 'Agata', '2021-03-07 22:59:02.607826', 0);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(2, '<p>Serdecznie polecam! Wykonany masaż pom&oacute;gł przy dolegliwościach b&oacute;lowych plec&oacute;w i dał możliwość odcięcia się od stresu. Jestem bardzo zadowolona i mile zaskoczona profesjonalizmem.</p>', 'Malwina', '2021-03-07 22:59:02.610225', 3);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(3, '<p>Przesympatyczna Pani Justynka doskonale potrafi rozluźnić mięśnie i wyeliminować dolegliwości b&oacute;lowe kręgosłupa. Lepsze samopoczucie już po pierwszym masażu <img alt=\"????\" src=\"https://static.xx.fbcdn.net/images/emoji.php/v9/t4c/1/16/1f642.png\" style=\"height:16px; width:16px\" />Jestem bardzo zadowolona z opcji masażu bez wychodzenia z domu i z bardzo elastycznych termin&oacute;w.</p>', 'Beata', '2021-03-07 22:59:02.611766', 4);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(4, '<p>Przemiła, subtelna i profesjonalna Pani Justyna. Potrafi zadbać o m&oacute;j zmęczony kręgosłup i poprawić samopoczucie. Gorąco polecam!</p>', 'Ela', '2021-03-07 22:59:02.613161', 4);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(5, '<p>bardzo profesjonalna miła obsługa, zadowolenie relaks muzyka, um&oacute;wienie bez problemu z dojazdem, dobra usluga, dobra cena, dobre ręce, polecam</p>', 'Dorota', '2021-03-07 22:59:02.614476', 5);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(6, '<p>Relaksujący i za każdym razem skuteczny masaż w wykonaniu pani Justyny. Niesamowite wyczucie i profesjonalizm, świetny kontakt z pacjentem. Jestem stałą klientką i polecam każdemu</p>', 'Tala', '2021-03-07 22:59:02.615889', 5);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(7, '<p>Świetna jakoś usług, profesjonalizm, odpowiednie podejście do klienta. Nie mogłam lepiej trafić.</p>', 'Sylwia', '2021-03-07 22:59:02.617238', 6);

--
-- Zrzut danych tabeli opinions_opinionsconfiguration
--

INSERT INTO opinions_opinionsconfiguration (id, main_image, main_image_alt, update_date, tree_img) VALUES(1, 'images/opinie.jpg', 'Opinie', '2020-12-05 12:09:46.181500', 'images/juzotwarte.jpg');

--
-- Zrzut danych tabeli opinions_opiniontreeitem
--

INSERT INTO opinions_opiniontreeitem (id, text, img, element_order) VALUES(2, '<p>Odpoczynek dla ciała i umysłu</p>', 'images/massage1_lbMY1WI.png', 0);
INSERT INTO opinions_opiniontreeitem (id, text, img, element_order) VALUES(3, '<p>Pozwól sobie na relaks i odprężenie</p>', 'images/massage_SD9F0yL.png', 0);
INSERT INTO opinions_opiniontreeitem (id, text, img, element_order) VALUES(4, '<p>Różnorodność masażów</p>', 'images/relaks.png', 0);
INSERT INTO opinions_opiniontreeitem (id, text, img, element_order) VALUES(5, '<p>Pełem profesjonalizm to nasza domena, cechuje nas indywidualne podejście do każdego klienta</p>', 'images/massage.png', 0);
INSERT INTO opinions_opiniontreeitem (id, text, img, element_order) VALUES(6, '<p>Wysoki poziom zadowolenia klient&oacute;w jest naszą wizyt&oacute;wką</p>', 'images/massage1.png', 0);
INSERT INTO opinions_opiniontreeitem (id, text, img, element_order) VALUES(7, '<p>Masaże są idealnym rozwiązaniem dla osób zapracowanych i aktywnych</p>', 'images/massage_Irq1EMs.png', 0);

--
-- Zrzut danych tabeli policy_policyconfiguration
--

INSERT INTO policy_policyconfiguration (id, privacy_text, order_rules, update_date) VALUES(1, '<h1>POLITYKA PRYWATNOŚCI&nbsp;</h1><p><strong>POSTANOWIENIA OG&Oacute;LNE</strong></p><p>1. Administratorem danych osobowych, zbieranych za pośrednictwem strony internetowej www.relaksownia.org.pl, jest Justyna Pietraszek, wykonujący jednoosobową działalność gospodarczą pod nazwą Justyna Pietraszek Mobilne Centrum Masażu Relaksownia, miejsce wykonywania działalności: 44-100 Gliwice, ul. Świętej Bronisławy 13/5, NIP: 9691217183, REGON: 383441026, adres e-mail: kontakt@relaksownia.org.pl, zwany dalej &ldquo;Administratorem&rdquo;.</p><p>2. Dane osobowe zbierane przez Administratora za pośrednictwem strony internetowej są przetwarzane zgodnie z Rozporządzeniem Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony os&oacute;b fizycznych w związku z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE (og&oacute;lne rozporządzenie o ochronie danych), zwane dalej RODO oraz ustawą o ochronie danych osobowych z dnia 10 maja 2018 r.</p><p>3. Administrator przetwarza dane osobowe za pośrednictwem strony www.relaksownia.org.pl w przypadku &nbsp;skorzystania przez użytkownika z formularza kontaktowego, zapisu na newsletter oraz zakupu książki. W przypadku newslettera i formularza kontaktowego dane, kt&oacute;re są zbierane i przetwarzane to imię oraz email. Użytkownik w każdej chwili może zrezygnować z subskrypcji newslettera klikając w link anulujący subskrypcję, znajdujący się w stopce newslettera. W przypadku zakupu książki niezbędne jest podanie danych, takich jak: imię i nazwisko, adres zamieszkania, telefon, adres email &ndash; w celu realizacji zam&oacute;wienia.&nbsp; Twoje dane osobowe przechowujemy nie dłużej, niż to jest konieczne. W szczeg&oacute;lności dane te przechowujemy przez czas niezbędny do prawidłowej realizacji usług, a po tym okresie nie dłużej, niż do upływu okresu przedawnienia roszczeń, jakie mogą zostać podniesione w związku z realizacją tych usług.&nbsp;</p><p>4. Podczas korzystania ze strony internetowej mogą być pobierane dodatkowe informacje, w szczeg&oacute;lności: adres IP przypisany do komputera użytkownika lub zewnętrzny adres IP dostawcy Internetu, nazwa domeny, rodzaj przeglądarki, czas dostępu, typ systemu operacyjnego.</p><p>5. Mogą być także gromadzone dane nawigacyjne użytkownik&oacute;w, w tym informacje o linkach i odnośnikach, w kt&oacute;re zdecydują się kliknąć lub innych czynnościach, podejmowanych na stronie internetowej. Podstawą prawną tego rodzaju czynności jest prawnie uzasadniony interes Administratora (art. 6 ust. 1 lit. f RODO), polegający na ułatwieniu korzystania z usług świadczonych drogą elektroniczną oraz na poprawie funkcjonalności tych usług.</p><p>6. Podanie danych osobowych, a także zgoda na ich przetwarzanie są całkowicie dobrowolne, lecz niezbędne w celu wykonania usługi. Wszelkie przekazane dane osobowe są przetwarzane wyłącznie w zakresie i celu, na jaki została wyrażona zgoda.&nbsp;</p><p>7. Dane osobowe będą przetwarzane także w spos&oacute;b zautomatyzowany w formie prolowania, o ile użytkownik wyrazi na to zgodę na podstawie art. 6 ust. 1 lit. a) RODO. Konsekwencją prolowania będzie przypisanie danej osobie prolu w celu podejmowania dotyczących jej decyzji bądź analizy lub przewidywania jej preferencji, zachowań i postaw.</p><p>8. Administrator dokłada szczeg&oacute;lnej staranności w celu ochrony interes&oacute;w os&oacute;b, kt&oacute;rych dane dotyczą, a w szczeg&oacute;lności zapewnia, że zbierane przez niego dane są: przetwarzane zgodnie z prawem, zbierane dla oznaczonych, zgodnych z prawem cel&oacute;w i niepoddawane dalszemu przetwarzaniu niezgodnemu z tymi celami, merytorycznie poprawne i adekwatne w stosunku do cel&oacute;w, w jakich są przetwarzane oraz przechowywane w postaci umożliwiającej identyfikację os&oacute;b, kt&oacute;rych dotyczą, nie dłużej niż jest to niezbędne do osiągnięcia celu przetwarzania.</p><p>9. Dane osobowe użytkownik&oacute;w przekazywane są dostawcom usług, z kt&oacute;rych korzysta Administrator przy prowadzeniu strony internetowej. Dostawcy usług, kt&oacute;rym przekazywane są dane osobowe, w zależności od uzgodnień umownych i okoliczności, albo podlegają poleceniom Administratora co do cel&oacute;w i sposob&oacute;w przetwarzania tych danych (podmioty przetwarzające) albo samodzielnie określają cele i sposoby ich przetwarzania (administratorzy). Dane osobowe użytkownik&oacute;w są przechowywane wyłącznie na terenie Europejskiego Obszaru Gospodarczego (EOG).</p><p>10. Osoba, kt&oacute;rej dane dotyczą, ma prawo dostępu do treści swoich danych osobowych oraz prawo ich sprostowania, usunięcia, ograniczenia przetwarzania, prawo do przenoszenia danych, prawo wniesienia sprzeciwu, prawo do cofnięcia zgody w dowolnym momencie bez wpływu na zgodność z prawem przetwarzania, kt&oacute;rego dokonano na podstawie zgody przed jej cofnięciem. W celu realizacji tych uprawnień, można wysłać stosowną wiadomość e-mail na adres: kontakt@relaksownia.org.pl.&nbsp;</p><p><strong>PLIKI &ldquo;COOKIES&rdquo;</strong></p><p>1. Strona Administratora używa plik&oacute;w &bdquo;cookies&rdquo;.</p><p>2. Instalacja plik&oacute;w &bdquo;cookies&rdquo; jest konieczna do prawidłowego świadczenia usług na stronie internetowej. W plikach &bdquo;cookies&rdquo; znajdują się informacje niezbędne do prawidłowego funkcjonowania strony, a także dają one także możliwość opracowywania og&oacute;lnych statystyk odwiedzin strony internetowej.</p><p>3. W ramach strony stosowane są rodzaje plik&oacute;w &ldquo;cookies&rdquo;: sesyjne i stałe. &bdquo;Cookies&rdquo; &bdquo;sesyjne&rdquo; są plikami tymczasowymi, kt&oacute;re przechowywane są w urządzeniu końcowym użytkownika do czasu wylogowania (opuszczenia strony). &bdquo;Stałe&rdquo; pliki &bdquo;cookies&rdquo; przechowywane są w urządzeniu końcowym użytkownika przez czas określony w parametrach plik&oacute;w &bdquo;cookies&rdquo; lub do czasu ich usunięcia przez użytkownika.</p><p>4. Administrator wykorzystuje własne pliki cookies w celu lepszego poznania sposobu interakcji użytkownika w zakresie zawartości strony. Pliki gromadzą informacje o sposobie korzystania ze strony internetowej przez użytkownika, typie strony, z jakiej użytkownik został przekierowany oraz liczbie odwiedzin i czasie wizyty użytkownika na stronie internetowej. Informacje te nie rejestrują konkretnych danych osobowych użytkownika, lecz służą do opracowania statystyk korzystania ze strony.</p><p>5. Użytkownik ma prawo zadecydowania w zakresie dostępu plik&oacute;w &bdquo;cookies&rdquo; do swojego komputera poprzez ich uprzedni wyb&oacute;r w oknie swojej przeglądarki. Szczeg&oacute;łowe informacje o możliwości i sposobach obsługi plik&oacute;w &bdquo;cookies&rdquo; dostępne są w ustawieniach oprogramowania (przeglądarki internetowej).</p><p><strong>POSTANOWIENIA KOŃCOWE</strong></p><p>1. Administrator stosuje środki techniczne i organizacyjne zapewniające ochronę przetwarzanych danych osobowych odpowiednią do zagrożeń oraz kategorii danych objętych ochroną, a w szczeg&oacute;lności zabezpiecza dane przed ich udostępnieniem osobom nieupoważnionym, zabraniem przez osobę nieuprawnioną, przetwarzaniem z naruszeniem obowiązujących przepis&oacute;w oraz zmianą, utratą, uszkodzeniem lub zniszczeniem.</p><p>2. Administrator udostępnia odpowiednie środki techniczne zapobiegające pozyskiwaniu i modyfikowaniu przez osoby nieuprawnione, danych osobowych przesyłanych drogą elektroniczną.</p><p>3. W sprawach nieuregulowanych niniejszą Polityką prywatności stosuje się odpowiednio przepisy RODO oraz inne właściwe przepisy prawa polskiego.</p>', '', '2021-01-28 12:56:54.869809');

--
-- Zrzut danych tabeli promo_promoclient
--

INSERT INTO promo_promoclient (id, contact_name, email, phone, delivery_kind, street, postcode, city, inpost_code, delivery_place, is_vat, company_name, nip, permission) VALUES(1, 'Artur Szwagrzak', 'artur.szwagrzak@gmail.com', '534260238', 'KURIER', 'Warszawska', '44-102', 'Gliwice', '', '', 1, 'Wizytoowka.pl', '97632782438726383483', 1);
INSERT INTO promo_promoclient (id, contact_name, email, phone, delivery_kind, street, postcode, city, inpost_code, delivery_place, is_vat, company_name, nip, permission) VALUES(14, 'AAAA', 'artur.szwagrzak@gmail.com', '534260238', 'KURIER', 'Warszawska', '44-102', 'Gliwice', '', '', 1, 'LOLO', '9763278243872638348322', 1);
INSERT INTO promo_promoclient (id, contact_name, email, phone, delivery_kind, street, postcode, city, inpost_code, delivery_place, is_vat, company_name, nip, permission) VALUES(15, 'Artur Szwagrzak', 'artur.szwagrzak@gmail.com', '534260238', 'KURIER', 'Warszawska', '44-102', 'Gliwice', '', '', 1, 'Wizytoowka.pl', '97632782438726383483', 1);

--
-- Zrzut danych tabeli promo_promoconfiguration
--

INSERT INTO promo_promoconfiguration (id, permission_text, delivery_info, bank_account_number, inpost_code_search_info) VALUES(1, 'Oświadczam, że wyrażam zgodę na przetwarzanie i wykorzystanie moich danych osobowych w celu realizacji zam&oacute;wienia przez Justyna Pietraszek Mobilne Centrum Masażu Relaksownia, ul. Świętej Bronisławy 13/5, 44-100 Gliwice, NIP: 9691217183, REGON: 383441026, kt&oacute;ry jest administratorem danych osobowych zgodnie z przepisami Rozporządzenia Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony os&oacute;b fizycznych w związku z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE i ustawy o ochronie danych osobowych z dnia 10 maja 2018 r. (Dz.U. 2018 poz. 1000)', '<p>Książka będzie wysłana i doręczona za pomocą paczkomatu lub kuriera Inpost. W przypadku wyboru paczkomatu do ceny trzeba doliczyć 13 zł, w przypadku kuriera 16,50 zł. Wysyłka zam&oacute;wienia będzie realizowana tylko na terenie Polski</p>', '00000000000000000000000000', 'https://inpost.pl/znajdz-paczkomat');

--
-- Zrzut danych tabeli promo_promoemailconfiguration
--

INSERT INTO promo_promoemailconfiguration (id, subject, message, from_email) VALUES(1, 'Twoje zamówienie zostało przyjęte.', '<p>Dziękuję za zainteresowanie książką Doskonale Niedoskonali i złożenie zam&oacute;wienia. Twoje zam&oacute;wienie zostało przyjęte i zostanie realizowane jak tylko płatność zostanie potwierdzona. W dniu wysyłki zostaniesz o tym poinformowany drogą mailową i otrzymasz informacje zawierające:</p><ul>	<li>numer listu przewozowego</li>	<li>link do strony firmy kurierskiej umożliwiający monitorowanie przesyłki</li>	<li>instrukcję postępowania podczas odbioru przesyłki od kuriera</li></ul><p>Serdecznie pozdrawiam, Justyna</p>', 'zamowienia@relaksownia.org.pl');

--
-- Zrzut danych tabeli promo_promopagecomponent
--

INSERT INTO promo_promopagecomponent (id, photo, photo_alt, photo_responsive1, photo_responsive1_alt, photo_responsive2, photo_responsive2_alt, text, text_position, update_date, element_order, photo_responsive3, photo_responsive3_alt, photo_responsive4, photo_responsive4_alt) VALUES(1, 'images/2_hTMFV1T.png', 'Część 2', 'images/respons_2.1..PNG', 'Promocja', 'images/JESZCZE_RAZ_2.2..PNG', 'Promocja', '', 1, '2021-02-01 15:08:09.160982', 2, 'images/CZARNE_TŁO_2.5..PNG', '', '', '');
INSERT INTO promo_promopagecomponent (id, photo, photo_alt, photo_responsive1, photo_responsive1_alt, photo_responsive2, photo_responsive2_alt, text, text_position, update_date, element_order, photo_responsive3, photo_responsive3_alt, photo_responsive4, photo_responsive4_alt) VALUES(2, 'images/1_7Xvkr0Q.png', 'Część 1', 'images/pocięty_1.1..PNG', 'Promocja', 'images/pocięty_1.2..PNG', 'Promocja', '', 1, '2021-02-01 14:54:17.086833', 1, '', '', '', '');
INSERT INTO promo_promopagecomponent (id, photo, photo_alt, photo_responsive1, photo_responsive1_alt, photo_responsive2, photo_responsive2_alt, text, text_position, update_date, element_order, photo_responsive3, photo_responsive3_alt, photo_responsive4, photo_responsive4_alt) VALUES(3, 'images/3_dkuzV1W.png', 'Część 3', 'images/POCIĘTY_3.1..PNG', 'Promocja', 'images/POCIĘTY_3.2..PNG', 'Promocja', '', 1, '2021-02-01 15:11:00.916070', 3, 'images/napisautorzy_9BdvP2B.png', '', '', '');
INSERT INTO promo_promopagecomponent (id, photo, photo_alt, photo_responsive1, photo_responsive1_alt, photo_responsive2, photo_responsive2_alt, text, text_position, update_date, element_order, photo_responsive3, photo_responsive3_alt, photo_responsive4, photo_responsive4_alt) VALUES(4, 'images/4_iK0IaBw_QcM8KYl.png', 'część 4', 'images/1_XVozZDB.png', 'promocja', 'images/2_xAa5k68.png', 'promo', '', 1, '2021-02-01 15:12:01.148012', 4, 'images/3_bTChCKI.png', 'promo', 'images/Agata_i_Ewa.PNG', 'promo');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
