import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_new_tab(selenium):
	WebDriverWait(selenium, 10).until(EC.new_window_is_opened(selenium.window_handles))
	selenium.close()
	selenium.switch_to_window(selenium.window_handles[0])


def random_element(elements):
	return random.sample(elements, 1)[0]


def test_startup_open_smoke(selenium):
	selenium.get('https://regulation.gov.ua')
	element = selenium.find_element_by_link_text('Спробуй вже зараз!')
	element.click()
	wait_new_tab(selenium)

	assert (selenium.current_url == 'https://regulation.gov.ua/startup' or
		WebDriverWait(selenium, 2).until(EC.url_changes('https://regulation.gov.ua/startup')))


def test_startup_quiz_start_smoke(selenium):
	selenium.get('https://regulation.gov.ua/startup')
	element = random_element(selenium.find_elements_by_css_selector('.dialogue-container'))
	element.click()
	assert selenium.current_url.startswith('https://regulation.gov.ua/startup/id')


def test_startup_quiz_end_smoke(selenium):
	selenium.get('https://regulation.gov.ua/startup')
	element = random_element(selenium.find_elements_by_css_selector('.dialogue-container'))
	element.click()

	while selenium.find_elements_by_css_selector('.question-container button'):
		element = random_element(selenium.find_elements_by_css_selector('.question-container button'))
		element.click()
		WebDriverWait(selenium, 2).until(EC.staleness_of(element))

	element = WebDriverWait(selenium, 4).until(
		EC.presence_of_element_located(('css selector', 'a.toggle-startup'))
	)
	assert element.text == 'Загальний опис'

def test_startup_quiz_back(selenium):
	selenium.get('https://regulation.gov.ua/startup/id17/city-all')
	element = selenium.find_element_by_css_selector('.container-change-answer')
	assert 'opacity-0' in element.get_attribute("class")
	button_element = selenium.find_element_by_css_selector('.question-container button')
	button_element.click()
	WebDriverWait(selenium, 2).until(EC.staleness_of(button_element))
	assert 'opacity-0' not in element.get_attribute("class")

def test_startup_quiz_index(selenium):
    selenium.get('https://regulation.gov.ua/startup')
    element = selenium.find_element_by_link_text('Спробуй вже зараз!')
    element.click()
    wait_new_tab(selenium)


