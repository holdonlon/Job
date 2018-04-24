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
		WebDriverWait(selenium, 5).until(EC.url_to_be(url)))
	print('ur', selenium.current_url, url)
	assert selenium.current_url == url