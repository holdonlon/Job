import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ias import do_login, wait_url, open_login, filter_by


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


def test_ias_subject_name(selenium):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/subject/index?regulatorId=61')
    filter_by(selenium, 'SubjectSearch[full_name]', 'ТОВАРИСТВО')