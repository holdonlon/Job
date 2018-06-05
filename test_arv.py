import os

LOGIN_FORM = (
    ('LoginForm[username]','ayzhana'),
    ('LoginForm[password]', 'JXjUsV44'),
)

def fill_form(selenium, form):
    for name, texts in form:
        texts = texts if isinstance(texts, list) else [texts]

        for element, text in zip(selenium.find_elements_by_name(name), texts):
            if text is True:
                element.click()
            elif text is False:
                pass
            if element.tag_name == 'select':
                element.find_element_by_css_selector('option[value="{}"]'.format(text)).click()
            else:
                element.send_keys(text)

def do_login(selenium):
    selenium.get('https://dev.brdo.com.ua/site/login')
    fill_form(selenium, LOGIN_FORM)
    
    element = selenium.find_element_by_name('login-button')
    element.click()

ARV_FORM = (
    ('otvet[a1]', 'Здоровий спосіб життя – це одна з найактуальніших проблем сьогоднішнього дня. Кожна держава чекає майбутнього від свого нового покоління, яке буде здоровим, здатним працювати, захищати Батьківщину, жити у відповідності з моральними вимогами суспільства, нормативними настановами держави і своєю індивідуальністю.'),
    ('otvet[a2][]', [
        'Розпочатий процес утворення об\'єднаних територіальних громад',
        'dva',
        'tri'
    ]),
    ('otvet[a3]', 'Залучення об\'єднаних територіальних громад та громадських організацій фізкультурно-спортивної спрямованості до системного моніторингу стану розвитку сфери фізичної культури та спорту.'),
    ('otvet[a4][0][kr]', 'об\'єднані територіальні громади та громадські організації фізкультурно-спортивної спрямованості '),
    ('otvet[a4][0][ed]', 'одиниця'),
    ('otvet[a4][0][pk]', '834'),
    ('otvet[a4][0][djerelo]', 'нормативно-правові акти'),
    ('otvet[a4][0][link]', 'Інститут економіки і миру, Сідней (Австралія)  http://visionofhumanity.org/app/uploads/2017/06/GPI-2017-Report-1.pdf'),
    ('otvet[a4][1][kr]', 'об\'єднані територіальні громади та громадські організації фізкультурно-спортивної спрямованості '),
    ('otvet[a4][1][ed]', 'одиниця'),
    ('otvet[a4][1][pk]', '835'),
    ('otvet[a4][1][djerelo]', 'нормативно-правові акти'),
    ('otvet[a4][1][link]', 'Інститут економіки і миру, Сідней (Австралія)  http://visionofhumanity.org/app/uploads/2017/06/GPI-2017-Report-1.pdf'),
    ('otvet[a5][]', [True, False, False, True]),
    ('otvet[a6]', 'Зазначена проблема не може бути розв’язана за допомогою ринкових механізмів, оскільки питання, що порушуються у ній, не стосуються механізмів стихійного регулювання ціни, темпів і пропорцій суспільного виробництва.'),
    ('otvet[a7]', 'Проблема не може бути розв’язана за допомогою діючих регуляторних актів, оскільки вони не охоплюють всіх суб\'єктів сфери фізичної культури і спорту.'),
    ('otvet[a8][]', 'Основною ціллю проекту регуляторного акта є приведення системи статистичної звітності ')
)


ARV_FORM2 = (
    ('otvet[b1][0]', 'На сьогодні діє наказ Міністерства молоді та спорту України від 14.12.2015 № 4611 "Про затвердження форми звітності № 2-ФК (річна) "Звіт з фізичної культури і спорту" '),
    ('otvet[b1][1]', 'Відсутні'),
    ('otvet[b1][2]', 'Втрати для Державного та місцевих бюджетів України через неотримання податків  та інших обов\'язкових платежів суб’єктів господарювання'),
    ('otvet[b1][3]', 'Відсутні.'),
    ('otvet[b1][4]', 'Часові та фінансові  витрати, пов\'язані з перетином лінії зіткнення задля державної реєстрації для суб\'єктів першої групи єдиного податку'),
    ('otvet[b1][5]', 'Відсутні'),
    ('otvet[b1][6]', 'Для державної реєстрації потенційні суб\'єкти господарювання повинні повинні перетинати лінію зіткнення, у зв\'язку з чим зазнавати часові та фінансові  витрати.'),
    ('otvet[b1][7][1][sviy]', '10'),
    ('otvet[b1][7][2][sviy]', '20'),
    ('otvet[b1][7][3][sviy]', '30'),
    ('otvet[b1][7][4][sviy]', '40'),
    ('otvet[b1][13][]','123'),
    ('otvet[b1][14]', 'У держави немає контролю над економікою та суб\'єктами господарювання на тимчасово неконтрольованій території УкраїниДля суб’єктів господарювання, що мають намір здійснювати господарську діяльність на тимчасово неконтрольованій території України відповідно до законодавства України, залишаються   фінансові  та часові витрати, пов\'язані з перетином лінії зіткнення задля реєстрації. Це призводить до того, що такі суб\'єти господарювання фізично мають більш зручний доступ до здійснення діяльності за режимом так окупуційної влади АРК та окремих районів Донецької та Луганської областейЗалишення цієї проблеми без змін тягне за собою подальші втрати для Державного та місцевих бюджетів України та економіки країни в цілому.'),
    ('otvet[b1][14a]','123'),
    ('otvet[b1][20]', 'З урахуванням існуючої ситуації, через невідому кількість суб\'єктів малого та середнього підприємництв на некотрольованій території  України обчислення витрат є неможливим'),
    ('otvet[b1][21]', 'З урахуванням існуючої ситуації, через втрату конролю та тимчасову окупацію частини території України,  обчислення витрат є неможливим.'),
    ('otvet[b1][23]', 'З урахуванням існуючої ситуації, через невідому кількість суб\'єктів малого та середнього підприємництв на некотрольованій території  України обчислення витрат є неможливим'),
    ('otvet[b1][24]','З урахуванням існуючої ситуації, через втрату конролю та тимчасову окупацію частини території України,  обчислення витрат є неможливим.'),
    ('otvet[b1][10]', True),
    ('otvet[b2][10]', True),
    ('otvet[b3][10]', True),
    ('otvet[b1][11]','Така альтернатива досягнення цілей державного регулювання  не врегульовує суспільні відносини, пов\'язані з контролем держави відповідно до чинного законодавства України за здійсненням суб\'єктами господарювання господарської дяльності на неконтрольованій території України, порядком їх реєстрації'),
    ('otvet[b2][0]', 'Внесення змін до Господарського кодексу та Закону України «Про державну реєстрацію юридичних осіб, фізичних осіб'),
    ('otvet[b2][1]', 'Підвищення економічного розвитку України.'),
    ('otvet[b2][2]','Втрати для Державного та місцевих бюджетів України у вигляді податків  та інших обов\'язкових платежів суб\'єктів через ухилення від сплати з урахуванням відстутності обов\'язковості приписів щодо реєстраціїЗловживання застосуванням порядку спрощеної процедури реєстрації з боку суб’єктів великого і середнього підприємництва, що створить перешкоди для розвитку малого бізнесу; неможливість здійснення такої процедури для юридичних осіб'),
    ('otvet[b2][3]', 'Ситуативні, надають певну  можливість, але не гарантують в розумні строки та в повному обсязі долучення до правового простору України'),
    ('otvet[b2][4]', 'Через відсутність обов\'язкових до виконання приписів для суб\'єктів господарювання, які здійснюють господарювання над неконтрольваній території України, є значна ймовірність для громадян Україна зилишитись у невизначеному та неправомірному  режимі, що тимчасово має місце на тимчасово неконтрольованій території України'),
    ('otvet[b2][5]', 'Можливість для суб\'єктів господарювання здійснювати господарську  діяльність на неконтрольованій території України та діяти відповідно та в межах правового простору України.'),
    ('otvet[b2][6]', 'Через відсутність обов\'язкових до виконання приписів для суб\'єктів господарювання, які мають намір здійснити або здійснюють господарювання над неконтрольваній території України, такі суб\'єкти можуть зилишитись у невизначеному та неправомірному  режимі, що начебто діє на тимчасово неконтрольованій території України.'),
    ('otvet[b2][7][1][sviy]', '10'),
    ('otvet[b2][7][2][sviy]', '20'),
    ('otvet[b2][7][3][sviy]', '30'),
    ('otvet[b2][7][4][sviy]', '40'),
    ('otvet[b2][14]', '135'),
    ('otvet[b2][14a]','http://rada.gov.ua/'),
    ('otvet[b2][17]', 'З урахуванням існуючої ситуації, через невідому кількість суб\'єктів малого та середнього підприємництва на некотрольованій території  України, обчислення витрат є неможливим'),
    ('otvet[b2][18]', 'З урахуванням існуючої ситуації, через втрату конролю та тимчасову окупацію частини території України,  обчислення витрат є неможливим'),
    ('otvet[b2][20]', 'З урахуванням існуючої ситуації, через невідому кількість суб\'єктів малого та середнього підприємництва на некотрольованій території  України, обчислення витрат є неможливим'),
    ('otvet[b2][21]', 'З урахуванням існуючої ситуації, через втрату конролю та тимчасову окупацію частини території України,  обчислення витрат є неможливим'),
    ('otvet[b2][23]', 'З урахуванням існуючої ситуації, через невідому кількість суб\'єктів малого та середнього підприємництва на некотрольованій території  України, обчислення витрат є неможливим'),
    ('otvet[b2][24]', 'З урахуванням існуючої ситуації, через втрату конролю та тимчасову окупацію частини території України,  обчислення витрат є неможливим'),
    ('otvet[b2][11]', 'Цілі регулювання можуть бути досягнуті частково, проблеми деякою мірою зменшаться, але  основні важливі та критичні аспекти проблем залишаться невирішеними, оскільки можливість контролю державою над неконтрольованою територією України та суб\'єктами господарювання, які здійснюють на ній господарювання,  зросте, але такий контроль буде неефективним, нестабільним та незабезпеченним'),
    ('otvet[b3][0]','Відсутня'),
    ('otvet[b3][1]', 'Відсутні'),
    ('otvet[b3][2]', 'Відсутні'),
    ('otvet[b3][3]', 'Відсутні'),
    ('otvet[b3][4]', 'Відсутні'),
    ('otvet[b3][5]', 'Відсутні'),
    ('otvet[b3][6]', 'Відсутні'),
    ('otvet[b3][7][1][sviy]', '10'),
    ('otvet[b3][7][2][sviy]', '20'),
    ('otvet[b3][7][3][sviy]', '30'),
    ('otvet[b3][7][4][sviy]', '40'),
    ('otvet[b3][12][]', '102'),
    ('otvet[b3][14]', '345'),
    ('otvet[b3][14a]', 'http://rada.gov.ua/'),
    ('otvet[b3][17]', 'З урахуванням існуючої ситуації, через невідому кількість суб\'єктів малого та середнього підприємництва на некотрольованій території  України, обчислення витрат є неможливим'),
    ('otvet[b3][18]', 'З урахуванням існуючої ситуації, через втрату конролю та тимчасову окупацію частини території України,  обчислення витрат є неможливим'),
    ('otvet[b3][20]', 'З урахуванням існуючої ситуації, через невідому кількість суб\'єктів малого та середнього підприємництва на некотрольованій території  України, обчислення витрат є неможливим'),
    ('otvet[b3][21]', 'З урахуванням існуючої ситуації, через втрату конролю та тимчасову окупацію частини території України,  обчислення витрат є неможливим'),
    ('otvet[b3][23]', 'З урахуванням існуючої ситуації, через невідому кількість суб\'єктів малого та середнього підприємництва на некотрольованій території  України, обчислення витрат є неможливим'),
    ('otvet[b3][24]', 'З урахуванням існуючої ситуації, через втрату конролю та тимчасову окупацію частини території України,  обчислення витрат є неможливим'),
    ('otvet[b3][8]', '555'),
    ('otvet_b3_9', os.getcwd() + '/doc.txt'),
    ('otvet[b3][11]', 'Цілі регулювання можуть бути досягнуті частково, проблеми деякою мірою зменшаться, але  основні важливі та критичні аспекти проблем залишаться невирішеними, оскільки можливість контролю державою над неконтрольованою територією України та суб\'єктами господарювання, які здійснюють на ній господарювання,  зросте, але такий контроль буде неефективним, нестабільним та незабезпеченним. Спрощена процедура для всіх суб\'єктів господарювання, в тому числі для суб\’єктів великого і середнього підприємництва, створюють загрозу зловживання таким порядком та створять перешкоди для розвитку малого бізнесу та підвищення економічного розвитку держави в цілому')
)

ARV_FORM3 = (
    ('otvet[c1][0]', '1'),
    ('otvet[c1][1]', 'Альтернатива не вирішує існуючих проблем, наразі у держави відсутній контроль над економікою та суб\'єктами господарювання на тимчасово неконтрольованій території України.'),
    ('otvet[c1][2]', 'Для суб’єктів господарювання, що мають намір здійснювати господарську діяльність на тимчасово неконтрольованій території України відповідно до законодавства України, залишаються   фінансові  та часові витрати, пов\'язані з перетином лінії зіткнення задля реєстрації.'),
    ('otvet[c1][3]', 'Ризик зовнішніх факторів є значним з урахуванням втрати контрою владою України та тимчасовою окупацією частини території України і, як наслідок, прямого впливу на суспільні відносини з боку влади Російської Федерації та злочинної влади так званих "ДНР" та "ЛНР".'),
    ('otvet[c2][0]', '2'),
    ('otvet[c2][1]', 'Внесення змін до Господарського кодексу та Закону України «Про державну реєстрацію юридичних осіб, фізичних осіб - підприємців та громадських формувань" з метою врегулювання суспільних відносини, пов\'язаних зі здійсненням суб\'єктами господарювання господарської дяльності на неконтрольованій території України відповідно до чинного законодавства України, обов\'язковим повідомленням про здійснення такої діяльності,  встановлення державного контролю за діяльністю таких суб\'єктів господарювання, спощення  порядку державної реєстрації є найбільш прийнятним'),
    ('otvet[c2][2]', 'Перевагами обраної альтернативи є встановлення державою контролю за суб\'єктами господарювання, що здійснюють господарську діяльність на тимчасово неконтрольованій території України, фінансові надходження для Державного та місцевих бюджетів України у вигляді податків  та інших обов\'язкових платежів суб’єктів господарювання, в тому числі й від застосування санкцій.'),
    ('otvet[c2][3]', 'Залишається певний ризик впливу зовнішніх факторів з урахуванням втрати контролю та тимчасовою окупацією частини території України і, як наслідок, прямого впливу на суспільні відносини з боку влади Російської Федерації та злочинної влади так званих "ДНР" та "ЛНР", але з урахуванням запропонованих механізмів цей ризик знижується.'),
    ('otvet[c3][0]', '3'),
    ('otvet[c3][1]', 'Необов\'язкова (добровільна) реєстрація для суб\'єктів господарювання, які здійснюють господарювання над неконтрольваній території України та запровадження процедури спрощеної процедури для всіх суб\'єктів господарювання, які здійснюють господарювання над неконтрольваній території України через необов\'язковість приписів не забезпечує належний контроль держави щодо суб\'єктів господарювання, які здійснюють свою діяльність на тимчасово неконтрольованій території України.'),
    ('otvet[c3][2]', 'Така альтернатива містить певні переваги, але її недоліки переважають, враховуючи той факт, що такий порядок недостатньої мірою регулює суспільні відносини, які потребують такого врегулювання у зв\'язку з відсутністю обов\'язковості механізмів реалізації.'),
    ('otvet[c3][3]', 'Ризик зовнішніх факторів є доволі значним з урахуванням відсутності обов\'язкових механізмів реалізації такої альтернативи, а також в умовах тимчасової втрати контрою владою України, залишається велика ймовірність прямого впливу на суспільні відносини з боку влади Російської Федерації та злочинної влади так званих "ДНР" та "ЛНР".'),
)

ARV_FORM4 = (
    ('otvet[d1][]','затвердити форму повідомлення про здійснення або намір здійснення господарської діяльності на тимчасово неконтрольованій території; налагодити ефективну взаємодію щодо обміну інформацією між суб\'єктами господарювання про порушення вимог регуляторного акту '),
    ('otvet[d2][]', 'затвердити форму повідомлення про здійснення або намір здійснення господарської діяльності на тимчасово неконтрольованій території; налагодити ефективну взаємодію щодо обміну інформацією між суб\'єктами господарювання про порушення вимог регуляторного акту '),
    ('otvet[d2a][]','ознайомитись з вимогами регуляторного акта; здійснити передбачені у ньому дії щодо обов\'язкової реєстрації відповідно до чинного законодавства України та повідомлення про намір здійснення господарської діяльності на тимчасово неконтрольованій території МТОТ.'),
    ('otvet_d3', os.getcwd() + '/doc.txt'),  
)
 
ARV_FORM5 = (
    ('otvet[e1]','0'),
    ('otvet[e2]', 'носить перманентний характер'),
    ('otvet[e3][1][0]','30'),
    ('otvet[e3][1][1]', '60'),
    ('otvet[e3][1][2]', '180'),
    ('otvet[e3][2][0]', '20'),
    ('otvet[e3][2][1]','20'),
    ('otvet[e3][2][2]', '20'),
    ('otvet[e3][3][0]', '30'),
    ('otvet[e3][3][1]', '30'),
    ('otvet[e3][3][2]', '30'),
    ('otvet[e3][4][0]', '40'),
    ('otvet[e3][4][1]', '40'),
    ('otvet[e3][4][2]', '40'),
    ('otvet[e3][5][0]', '50'),
    ('otvet[e3][5][1]', '50'),
    ('otvet[e3][5][2]', '50'),
    ('otvet[e3][6][0]', '75'),
    ('otvet[e3][6][1]', '85'),
    ('otvet[e3][6][2]', '95'),
    ('otvet[e3][7][0]', '15'),
    ('otvet[e3][7][1]', '10'),
    ('otvet[e3][7][2]', '5'),
    ('otvet[e4][ni0][0]', '15'),
    ('otvet[e4][ni0][1]', '10'),
    ('otvet[e4][ni0][2]', '5'),
    ('otvet[e4][][0]','1'),
    ('otvet[e4][][1]', '2'),
    ('otvet[e4][][2]', '3'),
    #('otvet[e4][9][0]', ''),
    #('otvet[e4][9][1]', ''),
    #('otvet[e4][9][2]', ''),
    ('otvet[e5][0]', 'Через півроку після набрання чинності актом'),
    ('otvet[e6][0]', 'Через рік після набрання чинності актом'),
    ('otvet[e7]', True),
    ('otvet[e8]', True),
    ('otvet[e9]', 'Через півроку після набрання чинності актом'),
    ('otvet[e10]', 'Через півроку після набрання чинності актом')
)

ARV_FORM6 = (
    ('otvet[f2]', 'Закону України "Про внесення змін до Господарського кодексу України та Закону України «Про державну реєстрацію юридичних осіб, фізичних осіб - підприємців та громадських формувань»'),
    ('otvet_f3', os.getcwd() + '/doc.txt'),
)

def test_arv(selenium):
    do_login(selenium)
    selenium.get('https://dev.brdo.com.ua/arv/new')
    element = selenium.find_element_by_css_selector('#arvform .form-group:nth-child(3) button')
    element.click()
    element.click()
    element = selenium.find_element_by_css_selector('#arvform .form-group:nth-child(5) button')
    element.click()
    fill_form(selenium, ARV_FORM)
    element = selenium.find_element_by_css_selector('.btn-success')
    element.click()

    # Form 2
    assert selenium.current_url.startswith('https://dev.brdo.com.ua/arv/step2?id=')
    element = selenium.find_element_by_css_selector('#arvform .form-group:nth-child(3) button')
    element.click()
    fill_form(selenium,ARV_FORM2)
    element = selenium.find_element_by_css_selector('.btn-success')
    element.click()

    # Form 3
    assert selenium.current_url.startswith('https://dev.brdo.com.ua/arv/step3?id=')
    fill_form(selenium,ARV_FORM3)
    element = selenium.find_element_by_css_selector('.btn-success')
    element.click()

    # Form 4
    assert selenium.current_url.startswith('https://dev.brdo.com.ua/arv/step4?id=')  
    fill_form(selenium,ARV_FORM4)
    element = selenium.find_element_by_css_selector('.btn-success')
    element.click()

    # Form 5
    assert selenium.current_url.startswith('https://dev.brdo.com.ua/arv/step5?id=') 
    fill_form(selenium,ARV_FORM5) 
    element = selenium.find_element_by_css_selector('.btn-success.btn-social')
    element.click()

    # Form 6
    assert selenium.current_url.startswith('https://dev.brdo.com.ua/arv/step6?id=') 
    fill_form(selenium,ARV_FORM6)
    element = selenium.find_element_by_css_selector('.btn-success')
    element.click()