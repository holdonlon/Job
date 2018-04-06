from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_brdo_search_smoke(selenium):
	selenium.get('https://regulation.gov.ua')
	element = selenium.find_element_by_css_selector('#searchform-term')
	element.send_keys('закон')
	element.send_keys(Keys.ENTER)

	WebDriverWait(selenium, 2).until(EC.url_changes('https://regulation.gov.ua/search/закон'))
	WebDriverWait(selenium, 10).until(EC.presence_of_element_located(('css selector', '.pjax-preload')))

	elements = selenium.find_elements_by_css_selector('.search-container-result small')
	assert elements
	for element in elements:
		assert 'закон' in element.text.lower()

def test_brdo_search_link_sector_smoke(selenium):
    selenium.get('https://regulation.gov.ua/search/закон')	
    search_element = selenium.find_element_by_css_selector('.nav-search')
    element = search_element.find_element_by_partial_link_text('Сектори')	
    element.click()
    WebDriverWait(selenium, 2).until(EC.url_changes('https://regulation.gov.ua/search/закон/sector_dialogue'))

def test_brdo_search_tab_smoke(selenium):
	selenium.get('https://regulation.gov.ua/search/закон')
	search_element = selenium.find_element_by_css_selector('.nav-search.procedure')
	element.click()
	WebDriverWait(selenium, 2).until(EC.url_changes('https://regulation.gov.ua/search/закон/sector_dialogue'))

def test_brdo_search_event_smoke(selenium):
    selenium.get('https://regulation.gov.ua/search/закон')	
    search_element = selenium.find_element_by_css_selector('.event')
    element.click()
    WebDriverWait(selenium,2).until(EC.url_changes('https://regulation.gov.ua/search/закон/sector_dialogue'))



