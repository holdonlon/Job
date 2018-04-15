from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def assert_text_found(selenium, text):
	elements = selenium.find_elements_by_css_selector('.search-container-result small')
	assert elements
	for element in elements:
		assert text in element.text.lower()



def test_brdo_search_smoke(selenium):
	selenium.get('https://regulation.gov.ua')
	element = selenium.find_element_by_css_selector('#searchform-term')
	element.send_keys('закон')
	element.send_keys(Keys.ENTER)

	WebDriverWait(selenium, 2).until(EC.url_changes('https://regulation.gov.ua/search/закон'))
	WebDriverWait(selenium, 10).until(EC.presence_of_element_located(('css selector', '.pjax-preload')))

	assert_text_found(selenium, 'закон')

def test_brdo_search_link_sector_smoke(selenium):
    selenium.get('https://regulation.gov.ua/search/закон')	
    search_element = selenium.find_element_by_css_selector('.nav-search')
    element = search_element.find_element_by_partial_link_text('Сектори')	
    element.click()
    WebDriverWait(selenium, 2).until(EC.url_changes('https://regulation.gov.ua/search/закон/sector_dialogue'))

def test_brdo_search_tab_procedure(selenium):
	selenium.get('https://regulation.gov.ua/search/закон')
	element = selenium.find_element_by_css_selector('ul.nav-search li.procedure a')
	element.click()
	WebDriverWait(selenium, 2).until(EC.url_changes('https://regulation.gov.ua/search/закон/procedure'))
	assert_text_found(selenium, 'закон')

def test_brdo_search_dialogue(selenium):
    selenium.get('https://regulation.gov.ua/search/закон')	
    search_element = selenium.find_element_by_css_selector('li.sector_dialogue')
    WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/sector_dialogue'))
    assert_text_found(selenium, 'закон')
 
def test_brdo_search_department(selenium):
    selenium.get('https://regulation.gov.ua/search/закон') 
    element = selenium.find_element_by_css_selector('li.department a')
    WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/department'))
    assert_text_found(selenium, 'закон')

def test_brdo_search_permit(selenium):
    selenium.get('https://regulation.gov.ua/search/закон')   
    element = selenium.find_element_by_css_selector('li.permit a')
    WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/permit'))
    assert_text_found(selenium, 'закон')

def test_brdo_search_event(selenium):
    selenium.get('https://regulation.gov.ua/search/закон') 
    element = selenium.find_element_by_css_selector('li.event a')
    WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/event'))  
    assert_text_found(selenium, 'закон')

def test_brdo_search_regulator(selenium):
    selenium.get('https://regulation.gov.ua/search/закон') 
    element = selenium.find_element_by_css_selector('li.regulator a')   
    WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/regulator'))
    assert_text_found(selenium, 'закон')

def test_brdo_search_library(selenium):
    selenium.get('https://regulation.gov.ua/search/закон') 
    element = selenium.find_element_by_css_selector('li.library a')   
    WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/library'))
    assert_text_found(selenium, 'закон')

def test_brdo_search_function(selenium):
    selenium.get('https://regulation.gov.ua/search/закон')   
    element = selenium.find_element_by_css_selector('li.function a') 
    WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/function'))
    assert_text_found(selenium, 'закон')

def test_brdo_search_department_function(selenium):
	selenium.get('https://regulation.gov.ua/search/закон')
	element = selenium.find_element_by_css_selector('li.department_function a')
	WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/department_function'))
	assert_text_found(selenium, 'закон')

def test_brdo_search_index_item(selenium):
	selenium.get('https://regulation.gov.ua/search/закон')
	element = selenium.find_element_by_css_selector('li.index_item a')
	WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/index_item'))
	assert_text_found(selenium, 'закон')