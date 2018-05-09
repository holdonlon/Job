import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ias import do_login, wait_url, open_login

def enter_code(selenium, edr_code):
    url = selenium.current_url
    element = selenium.find_element_by_name('AnnualInspectionUnplanned[code]')
    element.send_keys(edr_code)
    element = selenium.find_element_by_name('AnnualInspectionUnplanned[activity_type]')
    element.click()
    WebDriverWait(selenium, 20).until(EC.url_changes(url))

@pytest.mark.skip
@pytest.mark.parametrize("edr_code", [
    '25304474',
    '00377785',
    '40227200',
    '13996024',
])
def test_ias_unplanned(selenium, edr_code):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/unplanned')
    
    element = selenium.find_element_by_name('AnnualInspectionUnplanned[code]')
    element = send_keys(edr_code)
    element = selenium.find_element_by_name('AnnualInspectionUnplanned[activity_type]')
    element.click()


def test_ias_unplanned_create(selenium):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/unplanned')
    element = selenium.find_element_by_link_text('Створити позапланову перевірку')
    element.click()
    assert selenium.current_url == 'http://inspections.staging.brdo.com.ua/inspection/create'  

def test_ias_unplanned_card_edit(selenium, edr_code='2140703638'):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/unplanned')
    enter_code(selenium, edr_code)
    assert 'AnnualInspectionUnplanned%5Bcode%5D=2140703638' in selenium.current_url
    element = selenium.find_element_by_css_selector('.table_action_btn.icon-pencil')
    element.click()
    assert selenium.current_url.startswith('http://inspections.staging.brdo.com.ua/inspection/update?id=')
    element = selenium.find_element_by_css_selector('.page_title')
    assert 'Оновити дані про перевірку' in element.text