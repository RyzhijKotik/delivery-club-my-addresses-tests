from selenium.webdriver.common.action_chains import ActionChains

import page_object.my_addresses as my_addr


"""
Tests for delivery-club "My addresses" profile block
"""


def test_myaddr_title(selenium, profile_addresses):
    """"
    check presence of myaddresses title
    """
    myaddr_title_elem = selenium.find_element_by_xpath(my_addr.myaddr_title)
    assert myaddr_title_elem.is_displayed


def test_myaddr_textbox(selenium, profile_addresses):
    """"
    check presence of myaddresses textbox
    """
    myaddr_textbox_elem = selenium.find_element_by_xpath(my_addr.myaddr_textbox)
    assert myaddr_textbox_elem.is_enabled


def test_myaddr_map_icon(selenium, profile_addresses):
    """"
    check presence and ready for input of myaddresses map icon
    """
    myaddr_map_icon_elem = selenium.find_element_by_xpath(my_addr.myaddr_map_icon)
    assert myaddr_map_icon_elem.is_displayed


def test_myaddr_submit_address_btn(selenium, profile_addresses):
    """"
    check presence of submit address button
    """
    myaddr_submit_address_elem = selenium.find_element_by_xpath(my_addr.myaddr_submit_address)
    assert myaddr_submit_address_elem.is_enabled


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




