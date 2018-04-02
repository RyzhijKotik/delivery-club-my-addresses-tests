import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import page_object.main_page as main_page
import page_object.login_popup as login_popup
import page_object.my_addresses as my_addr
import page_object.main_page_logged_in as mp_loggedin

import common_data


"""
Preparations for testing addresses block: open main page, sign in, go to profile page
"""


@pytest.fixture()
def open_page(selenium):
    selenium.get('https://www.delivery-club.ru/')
    assert main_page.mp_title in selenium.title
    return selenium


@pytest.fixture
def login_button(selenium, open_page):
    login_btn = selenium.find_element_by_xpath(main_page.mp_login_button)
    assert login_btn.is_displayed
    return login_btn


@pytest.fixture
def login_textbox(selenium, login_button):
    login_button.click()
    login_input_textbox = selenium.find_element_by_xpath(login_popup.popup_login_input)
    assert login_input_textbox.is_displayed
    return login_input_textbox


@pytest.fixture
def password_textbox(selenium, login_textbox):
    login_textbox.send_keys(common_data.email)
    password_input_textbox = selenium.find_element_by_xpath(login_popup.popup_password_input)
    assert password_input_textbox.is_displayed
    return password_input_textbox


@pytest.fixture
def submit_button(selenium, password_textbox):
    password_textbox.send_keys(common_data.password)
    submit_btn = selenium.find_element_by_xpath(login_popup.popup_submit_btn)
    assert submit_btn.is_displayed
    return submit_btn


@pytest.fixture
def logged_in(selenium, submit_button):
    submit_button.click()
    logged_in_name = WebDriverWait(selenium, 10).\
        until(EC.presence_of_element_located((By.ID, mp_loggedin.mp_logged_in_id)))
    assert logged_in_name.is_displayed
    return logged_in_name


@pytest.fixture
def profile_options(selenium, logged_in):
    logged_in.click()
    profile_menu_option = selenium.find_element_by_xpath(mp_loggedin.mp_profile_option)
    assert profile_menu_option.is_displayed
    return profile_menu_option


@pytest.fixture
def profile_addresses(selenium, profile_options):
    profile_options.click()
    my_addresses = selenium.find_element_by_xpath(my_addr.myaddr_profile_block)
    assert my_addresses.is_displayed
    return my_addresses


@pytest.fixture(params=common_data.incorrect_addresses_list)
def incorrect_addresses(request):
    """
    forming a list for incorrect addresses; yielding 1 address per test 
    """
    incorrect_address = request.param
    yield incorrect_address


@pytest.fixture(params=common_data.correct_addresses_list)
def correct_addresses(request):
    """
    forming a list for correct addresses; yielding 1 address per test 
    """
    correct_address = request.param
    yield correct_address


@pytest.fixture(params=common_data.housenumber_list)
def housenumber(request):
    """
    forming a list for house numbers; yielding 1 number per test 
    """
    house_number = request.param
    yield house_number


@pytest.fixture(params=common_data.unknown_addr_list)
def unknown_addresses(request):
    """
    forming a list for unkonown addresses; yielding 1 addr per test 
    """
    unknown_addr = request.param
    yield unknown_addr
