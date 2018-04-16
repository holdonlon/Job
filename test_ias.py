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
    

def test_ias_plan_filter_code(selenium):
	selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned')
	do_login(selenium)
	wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')

	elements = selenium.find_elements_by_css_selector('.table-responsive tbody tr')
	assert len(elements) > 1

	element = selenium.find_element_by_name('AnnualInspectionPlanned[code]')
	element.send_keys('33231317')
	element = selenium.find_element_by_name('AnnualInspectionPlanned[activity_type]')
	element.click()

	elements = selenium.find_elements_by_css_selector('.table-responsive tbody tr')

	element = elements[0].find_element_by_css_selector('td:nth-child(3) span')
	assert element.text == '33231317'