import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ias import do_login, wait_url, open_login, filter_by


def table_size(selenium):
    element = selenium.find_element_by_css_selector('.grid-view b:nth-child(2)')
    return int(element.text.replace(' ', ''))


@pytest.mark.parametrize("edr_code", [
    '37580028',
    '38135005',
    '34939236',
    '25503630',
    '40644484',
])

def test_ias_subject_edr_code(selenium, edr_code):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/subject/index?regulatorId=61')
    elements = selenium.find_elements_by_css_selector('.table-bordered tbody tr')
    assert len(elements) > 1
    
    filter_by(selenium, 'SubjectSearch[code]', edr_code)

    elements = selenium.find_elements_by_css_selector('.table-bordered tbody tr')
    assert len(elements) == 1

    element = elements[0].find_element_by_css_selector('td:nth-child(3)')
    assert element.text == edr_code


@pytest.mark.parametrize("name", [
    'МЕНДЕЛЄЄВ ЛАБ',
    'ОДЕСАКОМУНЕКОЛОГІЯ',
    'ОБОДІВКА - АГРО',
    'ТЕРНОПІЛЬОБЛЕНЕРГО',
])
def test_ias_subject_name_uniq(selenium, name):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/subject/index?regulatorId=61')
    elements = selenium.find_elements_by_css_selector('.table-bordered tbody tr')
    assert len(elements) > 1
    assert table_size(selenium) > 1
    filter_by(selenium, 'SubjectSearch[full_name]', name)
    elements = selenium.find_elements_by_css_selector('.table-bordered tbody tr')
    assert len(elements) == 1
    assert table_size(selenium) == 1
    element = elements[0].find_element_by_css_selector('td:nth-child(2)')
    assert name in element.text


@pytest.mark.parametrize("name", [
    'ПРИВАТНЕ АКЦІОНЕРНЕ ТОВАРИСТВО',
])
def test_ias_subject_name_many(selenium, name):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/subject/index?regulatorId=61')
    len_before = table_size(selenium)
    assert len_before > 1

    elements = selenium.find_elements_by_css_selector('.table-bordered tbody tr')
    assert len(elements) > 1

    filter_by(selenium, 'SubjectSearch[full_name]', name)

    elements = selenium.find_elements_by_css_selector('.table-bordered tbody tr')
    assert len(elements) > 1
    assert 1 < table_size(selenium) < len_before

    for row_element in elements:
        element = row_element.find_element_by_css_selector('td:nth-child(2)')
        assert name in element.text


@pytest.mark.parametrize("subject", [
    {
        'Subject[code]': '37580028',
        'Subject[full_name]': 'КОМУНАЛЬНА УСТАНОВА "МОГИЛІВ-ПОДІЛЬСЬКИЙ РАЙОННИЙ МЕДИЧНИЙ ЦЕНТР ПЕРВИННОЇ МЕДИКО-САНІТАРНОЇ ДОПОМОГИ"',
        'Subject[short_name]': 'КУ "МОГИЛІВ-ПОДІЛЬСЬКИЙ РМЦПМСД"',
        'Subject[location]': '24000, Вінницька обл., місто Могилів-Подільський, ВУЛИЦЯ ПОЛТАВСЬКА, будинок 89, корпус 2',
        'Subject[ceo_name]': 'Цибульчак Євдокія Артемівна',
        'Subject[status]': 'в стані припинення',

    }
])
def test_ias_subject_add(selenium, subject):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/subject/index?regulatorId=61')
    element = selenium.find_element_by_link_text('Додати суб\'єкт господарювання')
    element.click()
    assert selenium.current_url == 'http://inspections.staging.brdo.com.ua/subject/add'
    element = selenium.find_element_by_css_selector('h1.page_title')
    assert element.text == 'Додати суб’єкт господарювання'
    assert selenium.title == 'Додати суб\'єкт господарювання'
    element = selenium.find_element_by_name('SubjectAdd[code]')
    element.send_keys(subject['Subject[code]'])
    element = selenium.find_element_by_css_selector('.create_doc_btn')
    element.click()

    for name, value in subject.items():
        element = selenium.find_element_by_name(name)
        assert element.get_attribute('value') == value

def test_ias_subject_add_error(selenium):   
    open_login(selenium,'http://inspections.staging.brdo.com.ua/subject/add')
    element = selenium.find_element_by_name('SubjectAdd[code]')
    element.send_keys('3758002')
    element = selenium.find_element_by_css_selector('.create_doc_btn')
    element.click()
    element = selenium.find_element_by_css_selector('.field-subjectadd-code')
    assert 'has-error' in element.get_attribute('class')
    element = element.find_element_by_css_selector('.help-block')
    assert element.text == 'Значення "Код суб\'єкту господарювання" повинно містити мінімум 8 символів.'

