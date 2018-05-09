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
