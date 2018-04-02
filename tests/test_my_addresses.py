from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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


@pytest.fixture
def test_myaddr_map_icon(selenium, profile_addresses):
    """"
    check presence and ready for input of myaddresses map icon
    """
    myaddr_map_icon_elem = selenium.find_element_by_xpath(my_addr.myaddr_map_icon)
    assert myaddr_map_icon_elem.is_displayed
    return myaddr_map_icon_elem


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
    result: error alert -- address to precise
    """
    test_myaddr_textbox.send_keys(incorrect_addresses)
    test_myaddr_submit_address_btn.click()
    myaddr_precise_alert_elem = selenium.find_element_by_xpath(my_addr.myaddr_precise_alert)
    assert myaddr_precise_alert_elem.is_displayed


@pytest.fixture
def test_choose_address_from_list(selenium, test_myaddr_textbox, correct_addresses):
    """
    action: fill some correct letters into textbox and chhose address from list 
    result: address filled into textbox
    """
    myaddr_delete_addr_btn_elem = selenium.find_element_by_xpath(my_addr.myaddr_delete_addr_btn)
    myaddr_delete_addr_btn_elem.click()
    selenium.switch_to_alert().accept()
    test_myaddr_textbox.send_keys(correct_addresses)
    myaddr_second_item_elem = WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, my_addr.myaddr_second_address_in_list)))
    assert myaddr_second_item_elem.is_displayed
    return myaddr_second_item_elem


@pytest.fixture
def test_add_address_from_list(selenium, test_choose_address_from_list):
    """
    action: choose address from list 
    result: textbox filled with the chosen address
    """
    test_choose_address_from_list.click()
    myaddr_from_list_filled_elem = selenium.find_element_by_xpath(my_addr.myaddr_second_addr_filled )
    assert myaddr_from_list_filled_elem.is_displayed
    return myaddr_from_list_filled_elem


def test_submit_unprecise_address_from_list(selenium, test_add_address_from_list, test_myaddr_submit_address_btn):
    """
    !!! Этот тест будет падать. 
    При наличии уже добавленного адреса я не могу добавить ещё один, 
    если он начинается на те же буквы, что и добавленный.
    Представим, что список адресов у нас изначально пустой.
    1) Вводим в поле адреса "заг"
    2) Добавляем любой адрес из списка на "заг": например Санкт-Петербург, Загребский проезд, 9
    3) Снова вводим в поле адреса "заг"
    Результат: список адресов на "заг" мне больше не выдаётся
    """
    test_myaddr_submit_address_btn.click()
    myaddr_precise_alert_elem = selenium.find_element_by_xpath(my_addr.myaddr_precise_alert)
    assert myaddr_precise_alert_elem.is_displayed


#it fails
def test_add_and_delete_address(selenium, housenumber, test_myaddr_textbox, test_add_address_from_list,
                                test_myaddr_submit_address_btn, test_choose_address_from_list):
    """
    !!!! Этот тест будет падать, потому что добавленный адрес не удаляется. 
    1) добавляем любой адрес, который добавится (с номером дома)
    2) жмем конпку удалить 
    3) жмем f5 
    результат: адрес остался на месте 
    """
    test_myaddr_textbox.send_keys(housenumber)
    test_myaddr_submit_address_btn.click()
    myaddr_delete_addr_btn_elem = selenium.find_element_by_xpath(my_addr.myaddr_delete_addr_btn)
    myaddr_delete_addr_btn_elem.click()
    selenium.switch_to_alert().accept()
    assert test_choose_address_from_list.is_displayed


def test_unknown_address(selenium, test_myaddr_textbox, unknown_addresses):
    """
    action: put unknown address into textbox
    result: alert about unknown address
    """
    test_myaddr_textbox.send_keys(unknown_addresses)
    myaddr_unknown_elem = WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, my_addr.myaddr_unknown)))
    assert myaddr_unknown_elem.is_displayed


@pytest.fixture
def test_open_map(selenium, test_myaddr_map_icon):
    """
    action: click open map button 
    result: check if map is opened
    """
    test_myaddr_map_icon.click()
    myaddr_map_close_btn_elem = WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, my_addr.myaddr_map_close_btn)))
    assert myaddr_map_close_btn_elem.is_enabled
    return myaddr_map_close_btn_elem


def test_open_and_close_map(selenium, test_open_map, test_myaddr_map_icon):
    """
    action: click close button 
    result: map closed
    """
    test_open_map.click()
    assert test_myaddr_map_icon.is_enabled


def test_add_default_address_from_map(selenium, test_open_map):
    """
    action: add default address from map
    result: address added
    """
    myaddr_map_confirm_addr_elem = WebDriverWait(selenium, 30). \
        until(EC.visibility_of_element_located((By.XPATH, my_addr.myaddr_map_confirm_addr)))
    myaddr_map_confirm_addr_elem.click()
    myaddr_delete_addr_btn_elem = selenium.find_element_by_xpath(my_addr.myaddr_delete_addr_btn)
    assert myaddr_delete_addr_btn_elem.is_enabled

