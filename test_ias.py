import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def do_login(selenium):
    element = selenium.find_element_by_name('LoginForm[username]')
    element.send_keys('support')
    element = selenium.find_element_by_name('LoginForm[password]')
    element.send_keys('supportbrdo')
    element = selenium.find_element_by_name('login-button')
    element.click()


def wait_url(selenium, url):
	assert (selenium.current_url == url or
		WebDriverWait(selenium, 2).until(EC.url_changes(url)))
	assert selenium.current_url == url


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
def test_ias_plan_card(selenium, edr_code):
    selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned')
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')	
    enter_code(selenium, edr_code)
    element = selenium.find_element_by_css_selector('.table_action_btn.icon-details')
    element.click()
    assert selenium.current_url.startswith('http://inspections.staging.brdo.com.ua/inspection/view?id=')
    element = selenium.find_element_by_css_selector('.result_table_mobile_panel tr:nth-child(3) td:nth-child(2)')
    assert element.text == edr_code
    
