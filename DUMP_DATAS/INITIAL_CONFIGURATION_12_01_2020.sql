--
-- Zrzut danych tabeli auth_user
--

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(1, 'pbkdf2_sha256$150000$NaWaaNLPQRWB$1iGWTr6kjHYUIjTjb11nJ8JNaB8webCnWiqwiBDFSJU=', '2020-12-30 10:10:13.404671', true,'arturszwagrzak', '', '', 'artur@szwagrzak.pl', true, true, '2020-11-17 23:39:13.323966');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES(2, 'pbkdf2_sha256$150000$k4F6Yrb7LtRy$HWTFTH8gpkour3aVKZBUEdXj0+/9gGqYK6QcbQ9SBW0=', '2021-01-09 07:46:49.811531', true,'justyna', '', '', 'j@p.ie', true, true, '2020-11-21 18:18:49.756756');

--
-- Zrzut danych tabeli blog_blogconfiguration
--

INSERT INTO blog_blogconfiguration (id, main_image, main_image_alt, update_date) VALUES(1, 'images/people_RPAst5s.jpg', 'BLOG', '2020-12-13 03:55:55.806152');

--
-- Zrzut danych tabeli contact_contactconfiguration
--

INSERT INTO contact_contactconfiguration (id, map_url, phone_number, email, on_site_client_info, have_questions, working_hours, facebook, twitter, linkedin, instagram, snapchat, youtube, google_plus, update_date) VALUES(1, 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2548.5237834465074!2d18.6868682158951!3d50.300816706016164!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4711314a54981b81%3A0x497cea66083f4e7e!2sMobilne%20Centrum%20Masa%C5%BCu%20Relaksownia!5e0!3m2!1spl!2spl!4v1603059899120!5m2!1spl!2spl', '+48608557617', 'kontakt@relaksownia.org.pl', '<p>Dojazd do klienta na terenie całego wojew&oacute;dztwa śląskiego, w Gliwicach dojazd gratis</p>', '<p>Masz do mnie pytania albo sugestie, napisz, chętnie odpowiem. Podziel się swoją opinią, ulepszaj z nami nasze usługi.</p>', '<p>&nbsp;</p><table>	<tbody>		<tr>			<td>			<p>poniedziałek</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>wtorek</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>środa</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>czwartek</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>piątek</p>			</td>			<td>			<p>08:00&ndash;21:00</p>			</td>		</tr>		<tr>			<td>			<p>sobota</p>			</td>			<td>			<p>zadzwoń - jeśli nie jestem w g&oacute;rach,&nbsp;</p>			<p>możemy się um&oacute;wić :)</p>			</td>		</tr>	</tbody></table>', 'https://www.facebook.com/relaksownia.masaz', '', '', '', '', '', 'https://g.page/Relaksownia_Masaz_Gliwice?share', '2020-12-12 09:38:23.779709');

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

INSERT INTO main_mainboxitem (id, header_text, image, image_alt, description, visible, update_date, element_order) VALUES(1, 'twój komfort - dojazd do domu', 'images/autonastrone.jpg', 'masaz', '<ul>	<li>Bez stania w korkach</li>	<li>Bez stresu związanego z szukaniem parkingu</li>	<li>Nie marzniesz czekając na przystanku a&nbsp;po masażu nie wychodzisz z ciepłego domu</li>	<li>Oszczędność czasu - świetne rozwiązanie dla zapracowanych - nie musisz nigdzie jechać, bo to ja&nbsp;przyjadę do Ciebie</li>	<li>Masaż bez wychodzenia z domu to idealna opcja&nbsp;- po skończonym masażu zostajesz u siebie i delektujesz się jego dobroczynnym dzialaniem.</li></ul>', true,'2020-12-30 14:24:24.694312', 1);
INSERT INTO main_mainboxitem (id, header_text, image, image_alt, description, visible, update_date, element_order) VALUES(2, 'głęboki relaks i redukcja stresu', 'images/relaksnastrone_8mRXwzw.jpg', 'auto', '<p>Masaż to zabieg holistyczny, działa leczniczo nie tylko na ciało, ale i na ducha. Wydzielająca się podczas masażu serotonina i dopamina sprzyja odprężeniu i eliminacji negatywnych emocji. Podczas masażu zostajesz wprowadzony w stan głębokiego relaksu, uspokajasz się i napełniasz pozytywną energią życiową.</p>', true,'2020-12-30 14:28:22.723156', 3);
INSERT INTO main_mainboxitem (id, header_text, image, image_alt, description, visible, update_date, element_order) VALUES(3, 'ukojenie bólu, likwidacja napięć', 'images/box_środkowy.jpg', 'masaz', '<p>In malesuada quam eget egestas fringilla. Proin maximus porttitor dui. In maximus blandit fermentum. Vivamus rhoncus iaculis turpis id euismod.&nbsp;</p>', true,'2020-12-30 15:07:19.349978', 2);

--
-- Zrzut danych tabeli main_mainconfiguration
--

INSERT INTO main_mainconfiguration (id, is_modal_visible, newsletter_info, main_text, update_date) VALUES(1, true,'<p>Zapisz się na bezpłatny newsletter i bądź z nami&nbsp;na bieżąco :-)</p>', '<h3>&nbsp;</h3><h2>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CIESZĘ SIĘ, ŻE TU JESTEŚ!</h2><h3>Masaż w RELAKSOWNI to najlepszy wyb&oacute;r, sprawdź dlaczego :)</h3>', '2020-12-19 11:38:39.804988');

--
-- Zrzut danych tabeli main_mainsliderconfiguration
--

INSERT INTO main_mainsliderconfiguration (id, change_image_time_ms, update_date) VALUES(1, 10000, '2020-12-12 09:52:09.477876');

--
-- Zrzut danych tabeli main_mainslideritem
--

INSERT INTO main_mainslideritem (id, image, image_alt, visible, update_date, element_order) VALUES(4, 'images/masaż_mężczyzna_na_slider.jpg', 'mężczyzna', true,'2020-11-25 19:23:44.237255', 0);
INSERT INTO main_mainslideritem (id, image, image_alt, visible, update_date, element_order) VALUES(5, 'images/naslajder_7c6zMbX.jpg', 'kobieta', true,'2020-11-25 19:22:57.802723', 0);

--
-- Zrzut danych tabeli newsletter_newsletter
--

INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(1, 'test@test.pl', 'Yolo', true,'2020-12-27 01:51:04.997921');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(2, 'aaa@dadasdasda.pl', 'Yolo', true,'2021-01-09 10:08:55.505945');
INSERT INTO newsletter_newsletter (id, email, name, permission, update_date) VALUES(3, 'aaa@dadasdasda.pl', 'Yolo', true,'2021-01-09 10:09:04.014643');

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

INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(1, '<p>Polecam. Miła i profesjonalna obsługa.</p><p>Masaż w domu jest świetnym rozwiązaniem dla os&oacute;b z deficytem czasu!</p>', 'Agata', '2020-11-12 03:17:02.315000', 0);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(2, '<p>Serdecznie polecam! Wykonany masaż pom&oacute;gł przy dolegliwościach b&oacute;lowych plec&oacute;w i dał możliwość odcięcia się od stresu. Jestem bardzo zadowolona i mile zaskoczona profesjonalizmem.</p>', 'Malwina', '2020-11-12 03:18:37.927000', 0);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(3, '<p>Przesympatyczna Pani Justynka doskonale potrafi rozluźnić mięśnie i wyeliminować dolegliwości b&oacute;lowe kręgosłupa. Lepsze samopoczucie już po pierwszym masażu <img alt=\"????\" src=\"https://static.xx.fbcdn.net/images/emoji.php/v9/t4c/1/16/1f642.png\" style=\"height:16px; width:16px\" />Jestem bardzo zadowolona z opcji masażu bez wychodzenia z domu i z bardzo elastycznych termin&oacute;w.</p>', 'Beata', '2020-11-12 03:20:27.911000', 0);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(4, '<p>Przemiła, subtelna i profesjonalna Pani Justyna. Potrafi zadbać o m&oacute;j zmęczony kręgosłup i poprawić samopoczucie. Gorąco polecam!</p>', 'Ela', '2020-11-12 03:15:43.605000', 0);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(5, '<p>bardzo profesjonalna miła obsługa, zadowolenie relaks muzyka, um&oacute;wienie bez problemu z dojazdem, dobra usluga, dobra cena, dobre ręce, polecam</p>', 'Dorota', '2020-11-12 03:15:29.333000', 0);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(6, '<p>Relaksujący i za każdym razem skuteczny masaż w wykonaniu pani Justyny. Niesamowite wyczucie i profesjonalizm, świetny kontakt z pacjentem. Jestem stałą klientką i polecam każdemu</p>', 'Tala', '2020-11-12 03:15:06.240000', 0);
INSERT INTO opinions_opinionitem (id, opinion_text, customer_name, update_date, element_order) VALUES(7, '<p>Świetna jakoś usług, profesjonalizm, odpowiednie podejście do klienta. Nie mogłam lepiej trafić.</p>', 'Sylwia', '2020-11-12 03:14:41.720000', 0);

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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
