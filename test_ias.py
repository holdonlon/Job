import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ias import do_login, wait_url, open_login, filter_by

EDR_LABEL = 'Ідентифікаційний код юридичної особи або реєстраційний номер облікової картки платника податків фізичної особи - підприємця (серія (за наявності) та номер паспорта*)'

def read_table(elements):
    table = {}
    for row in elements:
        title_element = row.find_element_by_css_selector('td:nth-child(1)')
        value_element = row.find_element_by_css_selector('td:nth-child(2)')
        table[title_element.text] = value_element.text

    return table

def test_ias_login(selenium):
    selenium.get('http://inspections.staging.brdo.com.ua/site/login')
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/')

@pytest.mark.skip(reason='ticket IAS-123')
def test_ias_login_redirect(selenium):
    selenium.get('http://inspections.staging.brdo.com.ua/inspection/planned')
    do_login(selenium)
    wait_url(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')

SELECTED_EDR = [
    '31979894',
    '13318525',
    '00691470',
]
    

@pytest.mark.parametrize("edr_code", SELECTED_EDR)
def test_ias_plan_filter_code(selenium, edr_code):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')
    WebDriverWait(selenium, 4).until(
        EC.presence_of_element_located(('css selector', '.table-responsive tbody tr'))
    )
    elements = selenium.find_elements_by_css_selector('.table-responsive tbody tr')
    assert len(elements) > 1

    filter_by(selenium, 'AnnualInspectionPlanned[code]', edr_code)

    elements = selenium.find_elements_by_css_selector('.table-responsive tbody tr')
    assert len(elements) == 1

    element = elements[0].find_element_by_css_selector('td:nth-child(3) span')
    assert element.text == edr_code


@pytest.mark.parametrize("edr_code", SELECTED_EDR)
def test_ias_plan_card_view(selenium, edr_code):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')
    filter_by(selenium, 'AnnualInspectionPlanned[code]', edr_code)
    element = selenium.find_element_by_css_selector('.table_action_btn.icon-details')
    element.click()
    assert selenium.current_url.startswith('http://inspections.staging.brdo.com.ua/inspection/view?id=')
    table = read_table(selenium.find_elements_by_css_selector('.result_table_mobile_panel tr'))

    assert table[EDR_LABEL] == edr_code


@pytest.mark.parametrize("edr_code", SELECTED_EDR)
def test_ias_plan_card_edit(selenium, edr_code):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')
    filter_by(selenium, 'AnnualInspectionPlanned[code]', edr_code)
    element = selenium.find_element_by_css_selector('.table_action_btn.icon-pencil')
    element.click()
    assert selenium.current_url.startswith('http://inspections.staging.brdo.com.ua/inspection/parts?id=')
    element = selenium.find_element_by_css_selector('.page_title')
    assert 'Оновлення інформації про перевірку' in element.text

@pytest.mark.skip(reason="removed after update")
def test_ias_plan_pdf(selenium):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')
    element = selenium.find_element_by_link_text('pdf')
    element.click()
    assert selenium.current_url.startswith('https://cdn.inspections.gov.ua/')
    assert selenium.current_url.endswith('.pdf')

@pytest.mark.skip(reason="removed after update")
def test_ias_plan_xls(selenium):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned') 
    element = selenium.find_element_by_link_text('xlsx')  
    element.click()

@pytest.mark.skip(reason="removed after update")
def test_ias_differences(selenium):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned') 
    element = selenium.find_element_by_link_text('xlsx') 
    element.click()


@pytest.mark.parametrize("error_code,error_link,error_reason", [
    ('subject_close', 'Суб\'єкт в стадії припинення або припинив діяльність', 'Суб\'єкт господарювання знаходиться в стані припинення діяльності або припинив свою діяльність'),
])
def test_ias_plan_error(selenium, error_code, error_link, error_reason):
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')
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
    open_login(selenium, 'http://inspections.staging.brdo.com.ua/inspection/planned')    
    element = selenium.find_element_by_css_selector('button[data-id="annualinspectionplanned-step"]')
    element.click()
    element = selenium.find_element_by_css_selector('.open .dropdown-menu.open li:nth-child({})'.format(child))
    element.click()
    assert 'AnnualInspectionPlanned%5Bstep%5D={}'.format(step) in selenium.current_url
    for element in selenium.find_elements_by_css_selector('.table-responsive tbody tr td:nth-child(9)'):
       assert text in element.text
"""
def test_ias_in_progress(selenium):
    open_login(selenium, 'https://inspections.gov.ua/inspection/planned')
    element = selenium.find_element_by_link_text('.nav-link, Суб\'єкт в стадії припинення або припинив діяльність')
    element.click()
""" 
"""
def test_ias_complex_plan(selenium):
    element = selenium.get('http://inspections.staging.brdo.com.ua/complex-plan-change/index')  
    do_login(selenium)
    wait_url('http://inspections.staging.brdo.com.ua/complex-plan-change/index')  
    element = selenium.find_element_by_css_selector('.icon-doc li')
    element.click()
"""