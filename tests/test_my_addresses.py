from selenium.webdriver.common.action_chains import ActionChains

import page_object.my_addresses as my_addr


"""
Tests for delivery-club "My addresses" profile block
"""


def test_hover_address_field(selenium, profile_addresses):
    """
    action: mouse hover on address field
    result: hint bubble appears  
    """
    hover = ActionChains(selenium).move_to_element(profile_addresses)
    hover.perform()
    myaddr_hover_elem = selenium.find_element_by_xpath(my_addr.myaddr_textbox_hover)
    assert myaddr_hover_elem.is_displayed




