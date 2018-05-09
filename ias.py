import urllib.parse
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
        WebDriverWait(selenium, 10).until(EC.url_to_be(url)))
    assert selenium.current_url == url


def open_login(selenium, url):
    selenium.get(url)
    do_login(selenium)
    # IAS-123 wait_url(selenium, url)
    selenium.get(url)


def filter_by(selenium, input_name, value):
    table_element = selenium.find_element_by_css_selector('.table-bordered')
    element = selenium.find_element_by_name(input_name)
    element.send_keys(value)
    table_element.click()
    WebDriverWait(selenium, 4).until(EC.staleness_of(table_element))
    assert urllib.parse.urlencode({input_name: value}).replace('+', '%20') in selenium.current_url