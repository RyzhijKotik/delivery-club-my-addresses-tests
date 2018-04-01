from selenium.webdriver.common.action_chains import ActionChains

import page_object.my_addresses as my_addr

import pytest

"""
Tests for delivery-club "My addresses" profile block
"""


def test_myaddr_title(selenium, profile_addresses):
    """"
    check presence of myaddresses title
    """
    myaddr_title_elem = selenium.find_element_by_xpath(my_addr.myaddr_title)
    assert myaddr_title_elem.is_displayed


@pytest.fixture
def test_myaddr_textbox(selenium, profile_addresses):
    """"
    check presence of myaddresses textbox
    """
    myaddr_textbox_elem = selenium.find_element_by_xpath(my_addr.myaddr_textbox)
    assert myaddr_textbox_elem.is_enabled
    return myaddr_textbox_elem


def test_myaddr_map_icon(selenium, profile_addresses):
    """"
    check presence and ready for input of myaddresses map icon
    """
    myaddr_map_icon_elem = selenium.find_element_by_xpath(my_addr.myaddr_map_icon)
    assert myaddr_map_icon_elem.is_displayed


@pytest.fixture
def test_myaddr_submit_address_btn(selenium, profile_addresses):
    """"
    check presence of submit address button
    """
    myaddr_submit_address_elem = selenium.find_element_by_xpath(my_addr.myaddr_submit_address)
    assert myaddr_submit_address_elem.is_enabled
    return myaddr_submit_address_elem


def test_hover_address_field(selenium, profile_addresses):
    """
    action: mouse hover on address field
    result: hint bubble appears  
    """
    hover = ActionChains(selenium).move_to_element(profile_addresses)
    hover.perform()
    myaddr_hover_elem = selenium.find_element_by_xpath(my_addr.myaddr_textbox_hover)
    assert myaddr_hover_elem.is_displayed


def test_hover_map_icon(selenium, profile_addresses):
    """
    action: mouse hover on map icon
    result: hint bubble map appears  
    """
    myaddr_map_icon_elem = selenium.find_element_by_xpath(my_addr.myaddr_map_icon)
    hover = ActionChains(selenium).move_to_element(myaddr_map_icon_elem)
    hover.perform()
    myaddr_hover_elem = selenium.find_element_by_xpath(my_addr.myaddr_map_hover)
    assert myaddr_hover_elem.is_displayed


def test_add_empty_address(selenium, test_myaddr_submit_address_btn):
    """
    action: click submit button without filling textbox
    result: error alert 
    """
    test_myaddr_submit_address_btn.click()
    myaddr_precise_alert_elem = selenium.find_element_by_xpath(my_addr.myaddr_precise_alert)
    assert myaddr_precise_alert_elem.is_displayed


def test_add_incorrect_addresses(selenium, incorrect_addresses, test_myaddr_submit_address_btn, test_myaddr_textbox):
    """
    action: input incorrect symbol(s) into textbox field and click submit button 
    result: error alert 
    """
    test_myaddr_textbox.send_keys(incorrect_addresses)
    test_myaddr_submit_address_btn.click()
    myaddr_precise_alert_elem = selenium.find_element_by_xpath(my_addr.myaddr_precise_alert)
    assert myaddr_precise_alert_elem.is_displayed

"""
ctrl-c ctrl-v в поле (???)
добавить адрес из списка
удалить добавленный адрес 
добавить адрес не из списка -- алерт вдреса нет в списке
Добавить адрес с карты
Открыть-закрыть карту, ничего не добавляя
"""