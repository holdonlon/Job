import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ias import do_login, wait_url


def test_ias_login(selenium):
    selenium.get('http://inspections.staging.brdo.com.ua/site/login')
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/')


def enter_code(selenium, edr_code):
	element = selenium.find_element_by_name('AnnualInspectionPlanned[code]')
	element.send_keys(edr_code)
	element = selenium.find_element_by_name('AnnualInspectionPlanned[activity_type]')
	element.click()

    

@pytest.mark.parametrize("edr_code", [
	'33231317',
	'34004453',
	'13318525',
	'00691748',
	'40511902',
])
def test_ias_plan_filter_code(selenium, edr_code):
	selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned')
	do_login(selenium)
	wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')

	elements = selenium.find_elements_by_css_selector('.table-responsive tbody tr')
	assert len(elements) > 1

	enter_code(selenium, edr_code)

	elements = selenium.find_elements_by_css_selector('.table-responsive tbody tr')

	element = elements[0].find_element_by_css_selector('td:nth-child(3) span')
	assert element.text == edr_code

@pytest.mark.parametrize("edr_code", [
	'33231317',
	'34004453',
	'13318525',
	'00691748',
	'40511902',
])
def test_ias_plan_card_view(selenium, edr_code):
    selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned')
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')	
    enter_code(selenium, edr_code)
    element = selenium.find_element_by_css_selector('.table_action_btn.icon-details')
    element.click()
    assert selenium.current_url.startswith('http://inspections.staging.brdo.com.ua/inspection/view?id=')
    element = selenium.find_element_by_css_selector('.result_table_mobile_panel tr:nth-child(3) td:nth-child(2)')
    assert element.text == edr_code
 
def test_ias_plan_card_edit(selenium, edr_code='33231317'):
	selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned')
	do_login(selenium)
	wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')
	enter_code(selenium, edr_code)
	element = selenium.find_element_by_css_selector('.table_action_btn.icon-pencil')
	element.click()
	assert selenium.current_url.startswith('http://inspections.staging.brdo.com.ua/inspection/update-all?id=')
	element = selenium.find_element_by_css_selector('.page_title')
	assert 'Оновити дані про перевірку' in element.text

def test_ias_plan_pdf(selenium):
    selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned')
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')
    element = selenium.find_element_by_link_text('pdf')
    element.click()
    assert selenium.current_url.startswith('https://cdn.inspections.gov.ua/')
    assert selenium.current_url.endswith('.pdf')

def test_ias_plan_xls(selenium):
    selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned') 
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')
    element = selenium.find_element_by_link_text('xlsx')  
    element.click()

def test_ias_differences(selenium):
    selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned') 
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')
    element = selenium.find_element_by_link_text('xlsx') 
    element.click()


@pytest.mark.parametrize("error_code,error_link,error_reason", [
	('subject_close', 'Суб\'єкт в стадії припинення або припинив діяльність', 'Суб\'єкт господарювання знаходиться в стані припинення діяльності або припинив свою діяльність'),
])
def test_ias_plan_error(selenium, error_code, error_link, error_reason):
    selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned')
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')	
    element = selenium.find_element_by_link_text(error_link)
    element.click()
    assert selenium.current_url == 'http://inspections.staging.brdo.com.ua/inspection/planned?AnnualInspectionPlanned%5Berror%5D=' + error_code
    elements = selenium.find_elements_by_css_selector('.table-responsive tbody tr')
    assert elements
    for element in elements:
    	allert_element = element.find_element_by_css_selector('.icon-alert')
    	assert allert_element.get_attribute('data-add-tr') == error_reason
    	assert allert_element.get_attribute('data-original-title') == 'Помилка'

@pytest.mark.parametrize('child,text,step', [
	(2, 'Наказ','reason'),
	(3, 'Результати','results'),
])
def test_ias_step(selenium, child, text, step):
    selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned')    
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')	
    element = selenium.find_element_by_css_selector('button[data-id="annualinspectionplanned-step"]')
    element.click()
    element = selenium.find_element_by_css_selector('.open .dropdown-menu.open li:nth-child({})'.format(child))
    element.click()
    assert 'AnnualInspectionPlanned%5Bstep%5D={}'.format(step) in selenium.current_url
    for element in selenium.find_elements_by_css_selector('.table-responsive tbody tr td:nth-child(9)'):
       assert text in element.text